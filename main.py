from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Configurações de HS e Antena
CONFIG_HS = {
    "verAddr": "Ativo", 
    "hs_value": "1.0", 
    "antena": "active", 
    "regedit": "enabled", 
    "precision": "max", 
    "auto_headshot": "true"
}

@app.route('/')
def home():
    # Verifica se o index.html existe para mostrar o site, senão mostra o JSON
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    return jsonify(CONFIG_HS)

@app.route('/config')
def config():
    return jsonify(CONFIG_HS)

if __name__ == '__main__':
    # CORREÇÃO AQUI: O Railway define a porta automaticamente
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
