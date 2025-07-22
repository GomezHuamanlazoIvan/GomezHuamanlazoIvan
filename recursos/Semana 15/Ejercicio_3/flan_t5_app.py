from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import time
import os

app = Flask(__name__)

# Configuración del modelo
model_id = "google/flan-t5-xl"
print(f"Cargando modelo {model_id}...")
print("Este modelo se descargará la primera vez que ejecutes la aplicación.")

# Cargar el modelo y tokenizer
try:
    # Configurar la caché de Hugging Face para guardar el modelo en la carpeta del proyecto
    os.environ["TRANSFORMERS_CACHE"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
    
    # Cargar tokenizer y modelo
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"  # Usar GPU si está disponible
    )
    
    print(f"Modelo {model_id} cargado correctamente")
    print(f"Usando GPU: {torch.cuda.is_available()}")
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
        
        # Preparar entrada para el modelo
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        # Generar respuesta
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.95
        )
        
        # Decodificar respuesta
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
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