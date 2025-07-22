from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

app = Flask(__name__)

# Usar Falcon-RW-1B-Instruct-OpenOrca (1B parámetros)
model_id = "LenguajeNaturalAI/leniachat-gemma-2b-v0"  # Modelo de 1B parámetros

print(f"Cargando modelo {model_id}...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
# Configurar el tokenizer para LenhuajeNaturalAI
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto" if torch.cuda.is_available() else None,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
print("Modelo cargado correctamente")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    # Formato para LenhuajeNaturalAI
    formatted_prompt = f"User: {prompt}\nAssistant:"
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7
        )
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Extraer solo la respuesta del asistente
    if "Assistant:" in response:
        response = response.split("Assistant:", 1)[1].strip()
    else:
        # Si no encuentra el formato esperado, eliminar el prompt
        response = response.replace(formatted_prompt, "").strip()
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
