from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(name)
CORS(app, resources={r"/": {"origins": ""}})

client = Groq(api_key="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")

@app.after_request
def add_header(response):
response.headers['Access-Control-Allow-Origin'] = '*'
response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
return response

@app.route('/')
def home():
return "Servidor CORE IA online! 🚀"

@app.route('/gerar', methods=['POST', 'OPTIONS'])
def gerar():
if request.method == 'OPTIONS':
return jsonify({"status": "ok"}), 200
try:
data = request.json
pergunta = data.get("prompt", "")
completion = client.chat.completions.create(
model="llama-3.3-70b-versatile",
messages=[{"role": "user", "content": pergunta}],
)
resposta = completion.choices[0].message.content
return jsonify({"resultado": resposta})
except Exception as e:
return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)