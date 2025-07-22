from flask import Flask, render_template, request, jsonify
import torch
import time

app = Flask(__name__)

# Usar GPT-2 que no requiere SentencePiece
print("Cargando modelo GPT-2...")

try:
    # Importar las bibliotecas necesarias
    from transformers import GPT2Tokenizer, GPT2LMHeadModel
    
    # Cargar tokenizer y modelo
    model_id = "gpt2"  # Modelo pequeño de OpenAI (no requiere SentencePiece)
    tokenizer = GPT2Tokenizer.from_pretrained(model_id)
    model = GPT2LMHeadModel.from_pretrained(model_id)
    
    # Configurar el tokenizer
    tokenizer.pad_token = tokenizer.eos_token
    
    # Mover a GPU si está disponible
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    print(f"Modelo {model_id} cargado correctamente")
    print(f"Usando dispositivo: {device}")
    model_loaded = True
    
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    model_loaded = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    if not model_loaded:
        return jsonify({"response": "El modelo no está cargado correctamente. Por favor revisa los logs del servidor."})
    
    prompt = request.json.get("prompt", "")
    
    try:
        print(f"Prompt: {prompt}")
        print("Generando respuesta...")
        
        # Medir tiempo de generación
        start_time = time.time()
        
        # Codificar el prompt
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        # Generar respuesta
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id
        )
        
        # Decodificar respuesta
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Eliminar el prompt de la respuesta
        if response.startswith(prompt):
            response = response[len(prompt):].strip()
        
        # Calcular tiempo
        elapsed = time.time() - start_time
        print(f"Respuesta generada en {elapsed:.2f} segundos")
        print(f"Respuesta: {response}")
        
        return jsonify({"response": response})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"response": f"Error al generar respuesta: {str(e)}"})

if __name__ == "__main__":
    print("Iniciando servidor Flask en http://127.0.0.1:5000")
    app.run(debug=True)