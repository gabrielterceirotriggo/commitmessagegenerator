import argparse
import subprocess
from .generator import gerar_mensagem_commit

def main():
    parser = argparse.ArgumentParser(description="Gerador de mensagens de commit com IA")
    parser.add_argument("-c", action="store_true", help="Commits with the generated message")
    parser.add_argument("-cp", action="store_true", help="Commits and pushes with the generated message")
    args = parser.parse_args()

    mensagem = gerar_mensagem_commit()

    if "No changes detected" in mensagem:
        print(mensagem)
        return

    print("\nGenerated commit message:\n" + mensagem)

    if args.c or args.cp:
        print("\nCommitting changes...")
        subprocess.run(["git", "commit", "-m", mensagem])

    if args.cp:
        print("\nPushing changes...")
        subprocess.run(["git", "push"])
    
    elif not args.c or not args.cp:
        print("\nRemoving staged changes (git reset)...")
        subprocess.run(["git", "reset"])
