import openai
from app import app

openai.api_key = "YOUR_OPENAI_KEY"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
