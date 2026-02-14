from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

# Correção: __name__ com dois underscores
app = Flask(__name__)

# Configuração simplificada e funcional do CORS
CORS(app, resources={r"/*": {"origins": "*"}}) 

# Recomendado: Colocar a chave em variável de ambiente, mas mantendo a sua por ora
client = Groq(api_key="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")

@app.route('/')
def home():
    return "Servidor CORE IA online! 🚀"

@app.route('/gerar', methods=['POST', 'OPTIONS'])
def gerar():
    # O Flask-CORS já cuida do OPTIONS automaticamente, 
    # mas manteremos sua lógica para garantir.
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    try:
        data = request.json
        if not data:
            return jsonify({"erro": "JSON não enviado"}), 400
            
        pergunta = data.get("prompt", "")
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": pergunta}],
        )
        
        resposta = completion.choices[0].message.content
        return jsonify({"resultado": resposta})
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"erro": str(e)}), 500

# Necessário para rodar localmente, a Vercel usa o objeto 'app'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)