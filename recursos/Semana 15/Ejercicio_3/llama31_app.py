from flask import Flask, render_template, request, jsonify
import os
import time
import google.generativeai as genai

app = Flask(__name__)

# Configuración de la API de Google (alternativa a modelos locales como Llama)
# Necesitas obtener una API key de Google AI Studio: https://makersuite.google.com/app/apikey
API_KEY = "AIzaSyDF-EE_XEE8Y0BUveW4RiYAp_hY7ehbnHY"  # Reemplaza con tu API key
genai.configure(api_key=API_KEY)

# Configurar el modelo con Gemini 2.0 Flash (alternativa más potente a Llama 3B)
model = genai.GenerativeModel('models/gemini-2.0-flash')  # Modelo avanzado de Google

print("Usando modelo Gemini 2.0 Flash de Google (alternativa a Llama)")
print("Este modelo se ejecuta en la nube y no requiere recursos locales")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    
    try:
        print(f"Prompt: {prompt}")
        print("Generando respuesta con IA avanzada...")
        
        # Medir tiempo de generación
        start_time = time.time()
        
        # Generar respuesta con Gemini
        response = model.generate_content(prompt)
        
        # Extraer el texto de la respuesta
        response_text = response.text
        
        # Calcular tiempo
        elapsed = time.time() - start_time
        print(f"Respuesta generada en {elapsed:.2f} segundos")
        print(f"Respuesta: {response_text}")
        
        return jsonify({"response": response_text})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"response": f"Error al generar respuesta: {str(e)}"})

if __name__ == "__main__":
    if not API_KEY or API_KEY == "TU_API_KEY_AQUI":
        print("\n" + "=" * 80)
        print("INSTRUCCIONES PARA USAR GEMINI DE GOOGLE:")
        print("=" * 80)
        print("1. Ve a https://makersuite.google.com/app/apikey")
        print("2. Crea una cuenta de Google AI Studio (es gratis)")
        print("3. Genera una API key")
        print("4. Reemplaza 'TU_API_KEY_AQUI' en este archivo con tu API key")
        print("5. Instala la biblioteca: pip install google-generativeai")
        print("6. Ejecuta este script nuevamente")
        print("=" * 80 + "\n")
    else:
        print("Iniciando servidor Flask con modelo de IA avanzada en http://127.0.0.1:5000")
        app.run(debug=True)