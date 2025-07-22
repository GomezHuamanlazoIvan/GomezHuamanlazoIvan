from flask import Flask, render_template, request, jsonify
import os
import time
import sys

app = Flask(__name__)

# Directorio para guardar el modelo - usando ruta absoluta
model_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models"))
model_path = os.path.join(model_dir, "Meta-Llama-3.1-8B-Instruct-Q4_K_L.gguf")

# Imprimir la ruta completa para verificación
print(f"Buscando modelo en: {model_path}")
print(f"El archivo existe: {os.path.exists(model_path)}")
if os.path.exists(model_path):
    print(f"Tamaño del archivo: {os.path.getsize(model_path) / (1024*1024*1024):.2f} GB")

# Intentar cargar el modelo con llama-cpp-python
try:
    from llama_cpp import Llama
    print("Usando llama-cpp-python para cargar el modelo...")
    
    # Cargar el modelo
    llm = Llama(
        model_path=model_path,
        n_ctx=2048,         # Contexto
        n_batch=512,        # Tamaño de lote
        n_threads=4,        # Hilos (ajustar según CPU)
        n_gpu_layers=0      # Capas en GPU (0 para solo CPU)
    )
    print("Modelo Llama 3.1 cargado correctamente con llama-cpp-python")
    model_loaded = True
    
except ImportError:
    print("\nNo se pudo importar llama-cpp-python. Intenta instalarlo con:")
    print("pip install llama-cpp-python")
    print("O para usar GPU (si tienes CUDA):")
    print("pip install llama-cpp-python --prefer-binary --extra-index-url https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2/cu118")
    llm = None
    model_loaded = False
    
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    llm = None
    model_loaded = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    
    # Verificar si el modelo está cargado
    if not model_loaded or llm is None:
        return jsonify({
            "response": f"El modelo no está cargado correctamente. Ruta del modelo: {model_path}. Existe: {os.path.exists(model_path)}. Por favor revisa los logs del servidor."
        })
    
    try:
        # Formato para Llama 3.1
        formatted_prompt = f"<s>[INST] {prompt} [/INST]"
        
        # Medir tiempo de generación
        start_time = time.time()
        
        # Generar respuesta con llama-cpp-python
        output = llm(formatted_prompt, max_tokens=128, temperature=0.7, stop=["</s>", "[INST]"])
        response = output["choices"][0]["text"].strip()
        
        # Calcular tiempo
        elapsed = time.time() - start_time
        print(f"Prompt: {prompt}")
        print(f"Respuesta generada en {elapsed:.2f} segundos")
        
        return jsonify({"response": response})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"response": f"Error al generar respuesta: {str(e)}"})

if __name__ == "__main__":
    if not model_loaded:
        print("\n" + "=" * 80)
        print("ERROR: No se pudo cargar el modelo.")
        print("=" * 80)
        print("Intenta instalar llama-cpp-python:")
        print("pip install llama-cpp-python")
        print("=" * 80 + "\n")
    
    print("Iniciando servidor Flask en http://127.0.0.1:5000")
    app.run(debug=True)