from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Configurações de HS + Comando de Skip
CONFIG_HS = {
    "verAddr": "Ativo", 
    "hs_value": "1.0", 
    "antena": "active", 
    "regedit": "enabled", 
    "precision": "max", 
    "auto_headshot": "true",
    "skipResourceDownload": "true",
    "skipUpdate": "true",
    "updateVersion": "1.100.0"
}

@app.route('/')
@app.route('/version.json')
@app.route('/config.json')
@app.route('/ver')
def home():
    return jsonify(CONFIG_HS)

@app.route('/<path:path>')
def catch_all(path):
    # Retorna o JSON para qualquer arquivo que o APK pedir (.bin, .dat, .json)
    return jsonify(CONFIG_HS)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
