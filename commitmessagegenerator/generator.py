import os
from dotenv import load_dotenv
import google.generativeai as genai
from git import Repo

def gerar_mensagem_commit():
    load_dotenv()  # carrega variáveis do .env

    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("The GEMINI_API_KEY variable is not defined.")

    # Configure a chave da API
    genai.configure(api_key=key)

    # Acesse o modelo diretamente
    model = genai.GenerativeModel("gemini-2.0-flash")

    repo = Repo(os.getcwd())
    diff = repo.git.diff()

    response = model.generate_content(
        contents=[{"role": "user", "parts": [f"Can you write a concise and technical message with a brief explanation of the changes made in the commit for the following diff:\n{diff}\nThere is no need to explain the message itself, just present it."]}]
    )
    return response.text