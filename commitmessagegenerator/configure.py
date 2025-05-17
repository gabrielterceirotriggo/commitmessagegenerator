import os
def api_key(key):
    if os.path.exists(".env"):
        with open(".env", "r+") as outfile:
            lines = outfile.readlines()
            gemini_api_key = next((line for line in lines if line.startswith("GEMINI_API_KEY=")), None)
            if gemini_api_key:
                outfile.seek(0)
                outfile.truncate()
                outfile.writelines([line if not line.startswith("GEMINI_API_KEY=") else f"GEMINI_API_KEY={key}\n" for line in lines])
            else:
                outfile.write(f"GEMINI_API_KEY={key}\n")
    else:
        with open(".env", "w") as outfile:
            outfile.write(f"GEMINI_API_KEY={key}\n")

    if os.path.exists(".gitignore"):
        with open(".gitignore", "r+") as outfile:
            lines = outfile.readlines()
            env_in_gitignore = next((line for line in lines if line.strip() == ".env"), None)
            if not env_in_gitignore:
                outfile.write(".env\n")
