import os
from dotenv import load_dotenv
import google.generativeai as genai
from git import Repo

def gerar_mensagem_commit():
    load_dotenv()  # carrega variáveis do .env

    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("A variável GEMINI_API_KEY não está definida.")

    # Configure a chave da API
    genai.configure(api_key=key)

    # Acesse o modelo diretamente
    model = genai.GenerativeModel("gemini-2.0-flash")

    repo = Repo(os.getcwd())
    diff = repo.git.diff()

    response = model.generate_content(
        contents=[{"role": "user", "parts": [f"Você pode escrever uma mensagem sucinta e técnica com uma breve explicação das mudanças que foram feitas de commit, para o seguinte diff:\n{diff}\nnão é necessário explicar a mensagem em si, apenas apresenta-la"]}]
    )
    return response.text