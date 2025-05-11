import argparse
import subprocess
from .generator import gerar_mensagem_commit

def main():
    parser = argparse.ArgumentParser(description="Gerador de mensagens de commit com IA")
    parser.add_argument("-c", action="store_true", help="Faz o commit com a mensagem gerada")
    parser.add_argument("-cp", action="store_true", help="Faz o commit e dá push")
    args = parser.parse_args()

    mensagem = gerar_mensagem_commit()

    if "Nenhuma alteração detectada" in mensagem:
        print(mensagem)
        return

    print("\nMensagem gerada:\n" + mensagem)

    if args.c or args.cp:
        print("\nExecutando commit...")
        subprocess.run(["git", "commit", "-m", mensagem])

    if args.cp:
        print("\nExecutando push...")
        subprocess.run(["git", "push"])
    
    elif not args.c or not args.cp:
        print("\nRemovendo alterações do staging (git reset)...")
        subprocess.run(["git", "reset"])
