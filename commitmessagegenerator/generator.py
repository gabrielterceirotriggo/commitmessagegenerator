import os
from dotenv import load_dotenv
from google import genai
from git import Repo

def gerar_mensagem_commit():
    load_dotenv()  # carrega variáveis do .env

    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("A variável GEMINI_API_KEY não está definida.")

    repo = Repo(os.getcwd())
    diff = repo.git.diff()

    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Você pode escrever uma mensagem sucinta e técnica com uma breve explicação das mudanças que foram feitas de commit, para o seguinte diff:\n"
                 + diff +
                 "não é necessário explicar a mensagem em si, apenas apresenta-la",
    )
    return response.text
