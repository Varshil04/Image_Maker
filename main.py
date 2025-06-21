from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_API_KEY")
from flask import Flask, request, jsonify

client = genai.Client(api_key=api_key)
app = Flask(__name__)

@app.route('/')
def generate_condtent():
    return jsonify({"status": "server is running"}), 200

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.get_json()
    text = data.get('text')
    
    if not text:
        return jsonify({"error" : "Text is required"}),400
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text,
        config=genai.types.GenerateContentConfig(
            system_instruction="You are a useful car enthusiast. Provide detailed and engaging responses about cars.",
        )
    )
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run()