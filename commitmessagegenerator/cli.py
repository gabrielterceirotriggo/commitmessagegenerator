import argparse
import subprocess
from .generator import gerar_mensagem_commit
from .configure import api_key
import sys
import getpass

def main():
    parser = argparse.ArgumentParser(description="Gerador de mensagens de commit com IA")
    parser.add_argument("-c", "--commit", action="store_true", help="Commits with the generated message")
    parser.add_argument("-cp", "--commitpush",  action="store_true", help="Commits and pushes with the generated message")
    parser.add_argument("-cf", "--configure", action="store_true", help="Configures the GEMINI_API_KEY environment variable")
    args = parser.parse_args()

    if not args.configure:
        mensagem = gerar_mensagem_commit()

        if "No changes detected" in mensagem:
            print(mensagem)
            return

        print("\nGenerated commit message:\n" + mensagem)

    if args.commit or args.commitpush:
        print("\nCommitting changes...")
        subprocess.run(["git", "commit", "-m", mensagem])

    if args.commitpush:
        print("\nPushing changes...")
        subprocess.run(["git", "push"])
    
    if args.configure:
        print("\nPlease input your API KEY\nThis is directly set in the .env file")
        key = getpass.getpass()
        api_key(key)
        print("\nAPI KEY saved in .env file\n")
    
    if len(sys.argv) == 1:
        print("\nRemoving staged changes (git reset)...")
        subprocess.run(["git", "reset"])
