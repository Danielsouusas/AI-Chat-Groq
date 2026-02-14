from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# 🔑 COLOQUE SUA CHAVE DA GROQ AQUI ABAIXO
client = Groq(api_key="AIzaSyAALYb1BcmaU6QsV3w-duFSJ2SWqHwxgIs")

@app.route('/gerar', methods=['POST'])
def gerar():
    try:
        data = request.json
        pergunta = data.get("prompt", "")
        print(f"🚀 MOTOR GROQ RECEBEU: {pergunta}")

        # Llama 3.3 - O modelo mais rápido do mercado atual
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": pergunta}],
        )
        
        resposta = completion.choices[0].message.content
        print("✅ Resposta gerada com sucesso!")
        return jsonify({"resultado": resposta})

    except Exception as e:
        print(f"💥 ERRO NA GROQ: {str(e)}")
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*40)
    print("⚡ MOTOR GROQ ATIVADO - VELOCIDADE MÁXIMA")
    print("📍 Servidor rodando em: http://127.0.0.1:5000")
    print("="*40 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)