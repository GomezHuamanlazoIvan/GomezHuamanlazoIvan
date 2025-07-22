# 🤖 Sistema Inteligente de Análisis de Datos con IA

## 📋 Descripción del Proyecto

Este proyecto es una **aplicación web completa** que implementa técnicas avanzadas de **Inteligencia Artificial** para el análisis de datos, específicamente replicando la metodología científica del paper **"DeepLearning_Based_MissingData_Imputation (DMDI)"** para la gestión de datos faltantes.

## 🏗️ Estructura del Proyecto

```
📁 Proyecto/
├── 📁 backend/                 # Servidor Flask + API REST
│   ├── app.py                  # Aplicación principal
│   ├── config_new.py           # Configuración
│   ├── text_analysis.py        # Análisis de sentimientos
│   ├── save_model.py           # Entrenamiento de modelos
│   ├── requirements.txt        # Dependencias Python
│   └── 📁 data/               # Datos del proyecto
│       ├── Data.csv           # Dataset (76 características)
│       ├── Label.csv          # Etiquetas de clasificación
│       └── schema.sql         # Esquema de base de datos
├── 📁 frontend/               # Aplicación React
│   ├── package.json           # Dependencias Node.js
│   ├── 📁 src/               # Código fuente React
│   └── 📁 public/            # Archivos públicos
├── 📁 models/                 # Modelos entrenados de IA
│   ├── autoencoder.pth        # Red neuronal (PyTorch)
│   ├── classifier.pkl         # Random Forest
│   └── scaler.pkl            # Normalizador de datos
└── 📁 docs/                   # Documentación completa
    └── README.md              # Documentación detallada
```

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone <tu-repositorio>
cd Proyecto
```

### 2. Configurar el Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Configurar la Base de Datos
```bash
# Crear base de datos MySQL (desde la carpeta backend)
cd backend
mysql -u root -p < data/schema.sql
```

### 4. Entrenar los Modelos
```bash
# Desde la carpeta backend
cd backend
python save_model.py
```

### 5. Configurar el Frontend
```bash
cd frontend
npm install
```

## 🎮 Ejecutar la Aplicación

### Backend (Puerto 5000)
```bash
cd backend
python app.py
```

### Frontend (Puerto 3000)
```bash
cd frontend
npm start
```

## 🧠 Funcionalidades de IA

1. **📊 Análisis de Datos**: Reconstrucción de datos faltantes con Autoencoder
2. **💖 Análisis de Sentimientos**: Procesamiento de lenguaje natural
3. **✍️ Generación de Texto**: Integración con Google Gemini API

## 📚 Documentación Completa

Para documentación detallada, consulta: [`docs/README.md`](docs/README.md)

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask, PyTorch, scikit-learn, TextBlob
- **Frontend**: React, Bootstrap, Axios
- **Base de Datos**: MySQL
- **IA**: Autoencoder, Random Forest, Google Gemini

## 👥 Contribución

Este proyecto está diseñado para fines educativos y de investigación en el campo de la Inteligencia Artificial aplicada al análisis de datos.

---
**Desarrollado con ❤️ para demostrar el poder de la IA en el análisis de datos**