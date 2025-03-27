from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Microserviço rodando!"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/info')
def info():
    return "Nossa aplicação é muito boa e concluimos o desafio 3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)