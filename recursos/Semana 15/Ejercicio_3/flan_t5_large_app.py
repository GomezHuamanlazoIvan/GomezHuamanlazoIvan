from flask import Flask, render_template, request, jsonify
import torch
import time
import sys
import os

app = Flask(__name__)

# Verificar si SentencePiece está instalado
try:
    import sentencepiece
    print("SentencePiece está instalado correctamente.")
except ImportError:
    print("\n" + "=" * 80)
    print("ERROR: SentencePiece no está instalado.")
    print("=" * 80)
    print("Instala SentencePiece con el siguiente comando:")
    print("pip install sentencepiece")
    print("Después de instalar, reinicia la aplicación.")
    print("=" * 80 + "\n")
    sys.exit(1)

# Importar transformers después de verificar SentencePiece
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Usar el modelo google/flan-t5-large que es más potente
model_id = "google/flan-t5-large"
print(f"Cargando modelo {model_id}...")
print("Este modelo es más potente y sofisticado, pero sigue siendo libre.")

try:
    # Cargar tokenizer y modelo
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    
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
        
        # Para flan-t5-large no necesitamos un formato especial
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
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