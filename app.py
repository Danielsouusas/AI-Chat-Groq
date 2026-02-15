from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

# CORREÇÃO: __name__ com dois underscores é o padrão Flask
app = Flask(__name__)

# CORREÇÃO: Liberando o CORS corretamente para o seu HTML conseguir acessar
CORS(app, resources={r"/*": {"origins": "*"}})

# Sua chave Groq
client = Groq(api_key="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")

@app.route('/')
def home():
    return "<h1>Servidor CORE IA online! 🚀</h1>"

@app.route('/gerar', methods=['POST', 'OPTIONS'])
def gerar():
    # O CORS precisa que o método OPTIONS responda 200 OK
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({"erro": "JSON inválido"}), 400
            
        pergunta = data.get("prompt", "")
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": pergunta}],
        )
        
        resposta = completion.choices[0].message.content
        return jsonify({"resultado": resposta})
        
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"erro": str(e)}), 500

# CORREÇÃO: O parâmetro correto é 'port', não 'porta'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)