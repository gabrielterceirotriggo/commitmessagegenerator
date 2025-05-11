import os
from dotenv import load_dotenv
import google.generativeai as genai
from git import Repo

def gerar_mensagem_commit():
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("The GEMINI_API_KEY environment variable is not set.")

    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    repo = Repo(os.getcwd())

    # Inclui arquivos staged (adicionados ou modificados)
    repo.git.add(all=True)
    diff = repo.git.diff("--cached")

    if not diff.strip():
        return "No changes detected in staged files (git diff --cached). No commit message generated."

    prompt = (
        f'''
        Generate a technical and concise Git commit message in plain text format.

        The message should follow the standard convention:
        - A single subject line (50 characters max) in the imperative mood, summarizing the change.
        - An optional blank line followed by a body explaining the *what* and *why* of the change (72 characters per line max).

        Provide *only* the commit message text, ready for direct insertion into a commit. Do not include any conversational text or additional formatting.

        Based on the following changes: {diff}
        '''
    )

    response = model.generate_content(
        contents=[{"role": "user", "parts": [prompt]}]
    )
    return response.text.strip()
