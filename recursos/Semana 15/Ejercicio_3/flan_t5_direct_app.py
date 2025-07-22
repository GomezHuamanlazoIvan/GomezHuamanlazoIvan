from flask import Flask, render_template, request, jsonify
import os
import time
import requests
import zipfile
import io
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = Flask(__name__)

# Directorio para guardar el modelo
model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "flan-t5-xl")
os.makedirs(model_dir, exist_ok=True)

# Función para descargar el modelo directamente desde Google Cloud Storage
def download_model():
    print("Descargando modelo flan-t5-xl directamente desde Google Cloud Storage...")
    
    # URLs para los archivos del modelo (estos son ejemplos, los URLs reales pueden ser diferentes)
    model_files = {
        "config.json": "https://storage.googleapis.com/t5-data/pretrained_models/flan_t5/xl/config.json",
        "pytorch_model.bin": "https://storage.googleapis.com/t5-data/pretrained_models/flan_t5/xl/pytorch_model.bin",
        "tokenizer.json": "https://storage.googleapis.com/t5-data/pretrained_models/flan_t5/xl/tokenizer.json",
        "vocab.txt": "https://storage.googleapis.com/t5-data/pretrained_models/flan_t5/xl/vocab.txt"
    }
    
    # Verificar si el modelo ya está descargado
    if os.path.exists(os.path.join(model_dir, "config.json")) and \
       os.path.exists(os.path.join(model_dir, "pytorch_model.bin")):
        print("El modelo ya está descargado.")
        return True
    
    try:
        # Descargar cada archivo
        for filename, url in model_files.items():
            print(f"Descargando {filename}...")
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(os.path.join(model_dir, filename), 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            else:
                print(f"Error al descargar {filename}: {response.status_code}")
                return False
        
        print("Modelo descargado correctamente.")
        return True
    except Exception as e:
        print(f"Error al descargar el modelo: {e}")
        return False

# Intentar descargar el modelo
model_downloaded = download_model()

# Cargar el modelo
if model_downloaded:
    try:
        print("Cargando modelo flan-t5-xl...")
        tokenizer = T5Tokenizer.from_pretrained(model_dir)
        model = T5ForConditionalGeneration.from_pretrained(
            model_dir,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"  # Usar GPU si está disponible
        )
        print("Modelo cargado correctamente.")
        model_loaded = True
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        model_loaded = False
else:
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
    if not model_loaded:
        print("\n" + "=" * 80)
        print("ERROR: No se pudo cargar el modelo flan-t5-xl.")
        print("=" * 80)
        print("Intenta descargar el modelo manualmente desde:")
        print("https://console.cloud.google.com/storage/browser/t5-data/pretrained_models/flan_t5/xl")
        print("Y colócalo en la carpeta:", model_dir)
        print("=" * 80 + "\n")
    
    print("Iniciando servidor Flask en http://127.0.0.1:5000")
    app.run(debug=True)