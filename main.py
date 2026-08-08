from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Configurações de HS + Comando de Skip (Pular Download)
CONFIG_HS = {
    "verAddr": "Ativo", 
    "hs_value": "1.0", 
    "antena": "active", 
    "regedit": "enabled", 
    "precision": "max", 
    "auto_headshot": "true",
    "skipResourceDownload": "true",
    "skipUpdate": "true",
    "updateVersion": "2.0"
}

@app.route('/')
def home():
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    return jsonify(CONFIG_HS)

@app.route('/config')
def config():
    return jsonify(CONFIG_HS)

@app.route('/ver')
def ver():
    return jsonify(CONFIG_HS)

@app.route('/<path:path>')
def catch_all(path):
    return jsonify(CONFIG_HS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
