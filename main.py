import os
import json
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection(name="filosofia")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def indexar_frases():
    count = collection.count()
    if count == 0:
        with open("data/frases.json", "r", encoding="utf-8") as f:
            frases = json.load(f)
        for idx, item in enumerate(frases):
            collection.add(
                documents=[item["frase"]],
                metadatas=[{"autor": item["autor"]}],
                ids=[f"frase_{idx}"]
            )
        print(f"{len(frases)} frases indexadas en ChromaDB")
    else:
        print(f"La base de datos ya tiene {count} frases, no es necesario reindexar.")

def buscar_citas(frase_usuario, k=3):
    result = collection.query(
        query_texts=[frase_usuario],
        n_results=k
    )
    citas = result["documents"][0]
    autores = [meta["autor"] for meta in result["metadatas"][0]]
    return citas, autores

def generar_prompt(frase_usuario, citas, autores):
    citas_texto = "\n".join([f"- \"{c}\" ({a})" for c, a in zip(citas, autores)])
    prompt = f"""
Eres un sabio antiguo. Una persona te dice: "{frase_usuario}".
Respóndele usando estas citas como contexto, mencionando a los autores:

{citas_texto}

Da una respuesta coherente y profunda, como si fueras un filósofo.
"""
    return prompt

def responder_sabio(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    indexar_frases()

    frase_usuario = input("Escribe una frase para consultar al sabio: ")

    citas, autores = buscar_citas(frase_usuario)
    prompt = generar_prompt(frase_usuario, citas, autores)
    respuesta = responder_sabio(prompt)

    print("\n=== Resultado ===")
    print(f"Frase del usuario: {frase_usuario}")
    print(f"Autores referenciados: {', '.join(set(autores))}")
    print(f"Respuesta del sabio:\n{respuesta}")
