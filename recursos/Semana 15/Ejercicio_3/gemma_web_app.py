import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configuración de la API de Google 
API_KEY = "AIzaSyDF-EE_XEE8Y0BUveW4RiYAp_hY7ehbnHY"  # 
genai.configure(api_key=API_KEY)

# Configurar el modelo con Gemini 2.0 Flash (alternativa más potente a Llama 3B)
model = genai.GenerativeModel('models/gemini-2.0-flash')  # Modelo avanzado de Google

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    
    try:
        print(f"Prompt: {prompt}")
        print("Generando respuesta con IA avanzada...")
        
        # Generar respuesta con Gemini
        response = model.generate_content(prompt)
        
        # Extraer el texto de la respuesta
        response_text = response.text
        
        print(f"Respuesta: {response_text}")
        return jsonify({"response": response_text})
        
    except Exception as e:
        print(f"Error al generar respuesta: {e}")
        error_msg = f"Error al generar respuesta: {str(e)}"
        return jsonify({"response": error_msg})

if __name__ == "__main__":
    if not API_KEY or API_KEY == "TU_API_KEY_AQUI":
        print("\n" + "=" * 80)
    else:
        print("Iniciando servidor Flask con modelo de IA avanzada en http://127.0.0.1:5000")
        app.run(debug=True)