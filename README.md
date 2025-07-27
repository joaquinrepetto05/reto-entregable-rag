# ¿Qué dijo el Filósofo?

Este proyecto implementa un sistema de Recuperación Aumentada con Generación (RAG) utilizando ChromaDB como base vectorial y Gemini como modelo de lenguaje.
El programa recibe una frase de un usuario, busca citas filosóficas similares en la base de datos y genera una respuesta estilo "sabio antiguo" utilizando esas citas como contexto.

## Instalación de dependencias

1. Clonar el proyecto desde GitHub.
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar una API Key de Gemini en un nuevo archivo .env localizado en la carpeta raiz del proyecto de la siguiente manera:
   ```bash
   GOOGLE_API_KEY=tu_api_key
   ```
> [!WARNING]
> Es importante que la API Key quede bien configurada para la correcta ejecución del código

## Ejecución del proyecto

El proyecto puede ejecutarse utilizando el comando:
```bash
python main.py
```

Una vez ejecutado el comando, seguir las instrucciones de la consola.
