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

# Rota Principal (Site)
@app.route('/')
def home():
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    return jsonify(CONFIG_HS)

# Rota de Configuração (Onde o jogo geralmente busca)
@app.route('/config')
def config():
    return jsonify(CONFIG_HS)

# Rota de Verificação (Evita o Erro 404 no carregamento)
@app.route('/ver')
def ver():
    return jsonify(CONFIG_HS)

# Rota Genérica para qualquer outro pedido do jogo (Curinga)
@app.route('/<path:path>')
def catch_all(path):
    return jsonify(CONFIG_HS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
