# commitgen

Gere mensagens de commit técnicas e objetivas com IA (Google Gemini) a partir do `git diff`.

## 📦 Instalação

```bash
pip install commitmessagegenerator
```

Ou, se estiver usando `venv`:

```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install commitmessagegenerator
```

## ⚙️ Configuração

Crie um arquivo `.env` no diretório onde você executará o `commitgen` (geralmente a raiz do seu projeto Git):

```
GEMINI_API_KEY=sua-chave-da-api-do-gemini
```

## 🚀 Uso

No terminal, dentro de qualquer repositório Git com alterações pendentes, execute:

```bash
commitgen
```

O comando irá:

- Ler o `git diff`;
- Enviar para a API Gemini da Google;
- Retornar uma sugestão de mensagem de commit diretamente no terminal.

## 🧩 Requisitos

- Python 3.8 ou superior
- API Key do Gemini (Google Generative AI)
- Repositório Git iniciado
- Dependências Python:
  - `GitPython`
  - `google-generativeai`
  - `python-dotenv`

Instale tudo com:

```bash
pip install -r requirements.txt
```

## 📄 Licença

MIT License
