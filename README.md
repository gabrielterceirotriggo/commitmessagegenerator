# commitmessagegenerator

Generate objective and technical commit messages with AI (Google Gemini) automatically using your `git diff`.

## 📦 Install

```bash
pip install commitmessagegenerator
```

Or, if you're using a `venv`:

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate in Windows
pip install commitmessagegenerator
```

## ⚙️ Configuring

## IMPORTANT - BEFORE CREATING THIS FILE ADD '.venv' TO YOUR .gitignore SO YOUR API KEY ISN'T EXPOSED

Create a `.env` file in the directory where you will run commitgen (usually the root of your Git project):

```
GEMINI_API_KEY=your-gemini-api-key
```

## 🚀 Usage

With the terminal, inside any Git repository with pending changes, run:

```bash
commitgen (-c/-cg)
```

The command will:

- Read the git diff;
- Send it to the Google Gemini API;
- Return a commit message suggestion directly in your terminal.

## 🧩 Requisites

- Python 3.8 or higher
- Gemini API Key (Google Generative AI, free at: https://aistudio.google.com/app/apikey)
- Initialized Git repository
- Python dependencies (Automatically installed with the package):
  - `GitPython`
  - `google-generativeai`
  - `python-dotenv`

## 📄 License

```
MIT License
```
