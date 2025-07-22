from flask import Flask, render_template, request, jsonify
import os
from ctransformers import AutoModelForCausalLM

app = Flask(__name__)

# Directorio para guardar el modelo
model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
os.makedirs(model_dir, exist_ok=True)

# Ruta al modelo GGUF (necesitarás descargarlo)
model_path = os.path.join(model_dir, "llama-3-8b-instruct.Q4_K_M.gguf")

# Mensaje si el modelo no está descargado
if not os.path.exists(model_path):
    print(f"\nEl modelo no se encuentra en {model_path}")
    print("Descarga el modelo desde: https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF")
    print("Archivo recomendado: llama-3-8b-instruct.Q4_K_M.gguf (aproximadamente 2.9GB)")
    print(f"Colócalo en: {model_dir}\n")
    llm = None
else:
    # Cargar el modelo con ctransformers (más eficiente que transformers)
    llm = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="llama",
        max_new_tokens=128,
        context_length=2048,
        gpu_layers=0,  # Cambiar a un número mayor si tienes GPU
        threads=8      # Ajustar según tu CPU
    )
    print(f"Modelo Llama 3 cargado correctamente")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    
    if llm is None:
        return jsonify({
            "response": "El modelo no está cargado. Por favor, descarga el modelo Llama 3 primero."
        })
    
    try:
        # Formato para Llama 3
        formatted_prompt = f"<s>[INST] {prompt} [/INST]"
        
        # Generar respuesta
        start_time = os.times()
        response = llm(
            formatted_prompt,
            max_new_tokens=128,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1
        )
        end_time = os.times()
        
        # Calcular tiempo de generación
        generation_time = end_time.user - start_time.user
        print(f"Respuesta generada en {generation_time:.2f} segundos")
        
        return jsonify({"response": response})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"response": f"Error al generar respuesta: {str(e)}"})

if __name__ == "__main__":
    if llm is None:
        print("\n" + "=" * 80)
        print("INSTRUCCIONES PARA USAR LLAMA 3:")
        print("=" * 80)
        print("1. Instala ctransformers: pip install ctransformers")
        print("2. Descarga el modelo desde: https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF")
        print("3. Archivo recomendado: llama-3-8b-instruct.Q4_K_M.gguf (2.9GB)")
        print(f"4. Colócalo en: {model_dir}")
        print("5. Reinicia esta aplicación")
        print("=" * 80 + "\n")
    
    print("Iniciando servidor Flask en http://127.0.0.1:5000")
    app.run(debug=True)