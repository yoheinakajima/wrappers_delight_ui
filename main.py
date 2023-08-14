import openai
from app import app
from wrappers_delight import wrapper

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Enable reflection, so we have a reflection to see in the app.
wrapper.ChatWrapper.enable_reflection()

# Engage ChatCompletion API to generate a log to see in the app.
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact."},
    ]
)

print(response.choices[0].message.content)

# Initiate Flask app for reviewing log and reflections.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
