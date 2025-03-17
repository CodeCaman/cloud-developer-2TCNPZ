from flask import Flask, jsonify, render_template, request
from datetime import datetime

app = Flask(__name__)

# Simulated database
pedidos = []
clientes = {}
produtos = {}

# Entidades
class Pedido:
    STATUS = ["em processamento", "enviado", "entregue"]

    def __init__(self, id, cliente_id, itens, forma_pagamento):
        self.id = id
        self.cliente_id = int(cliente_id)  # Garantir que cliente_id seja um inteiro
        self.itens = itens
        self.forma_pagamento = forma_pagamento
        self.status = "em processamento"
        self.data_criacao = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'itens': [item.to_dict() for item in self.itens],
            'forma_pagamento': self.forma_pagamento,
            'status': self.status,
            'data_criacao': self.data_criacao.isoformat()
        }

class ItemPedido:
    def __init__(self, produto_id, quantidade):
        self.produto_id = produto_id
        self.quantidade = quantidade

    def to_dict(self):
        return {
            'produto_id': self.produto_id,
            'quantidade': self.quantidade
        }

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

# Rotas para funcionalidades de pedidos
@app.route('/pedidos', methods=['POST'])
def criar_pedido():
    data = request.get_json()
    pedido_id = len(pedidos) + 1
    itens = [ItemPedido(item['produto_id'], item['quantidade']) for item in data['itens']]
    pedido = Pedido(pedido_id, data['cliente_id'], itens, data['forma_pagamento'])
    pedidos.append(pedido)
    print(f"Pedido criado: {pedido.to_dict()}")  # Log para depuração
    return jsonify({'id': pedido_id}), 201

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def status_pedido(pedido_id):
    pedido = next((p for p in pedidos if p.id == pedido_id), None)
    if pedido:
        return jsonify({'status': pedido.status})
    return jsonify({'error': 'Pedido não encontrado'}), 404

@app.route('/pedidos/<int:pedido_id>/status', methods=['PUT'])
def atualizar_status_pedido(pedido_id):
    data = request.get_json()
    novo_status = data.get('status')

    if novo_status not in Pedido.STATUS:
        return jsonify({'error': 'Status inválido'}), 400

    pedido = next((p for p in pedidos if p.id == pedido_id), None)
    if pedido:
        pedido.status = novo_status
        return jsonify({'status': pedido.status})
    return jsonify({'error': 'Pedido não encontrado'}), 404

@app.route('/clientes/<int:cliente_id>/pedidos', methods=['GET'])
def historico_pedidos(cliente_id):
    cliente_id = int(cliente_id)  # Garantir que cliente_id seja um inteiro
    historico = [p.to_dict() for p in pedidos if p.cliente_id == cliente_id]
    print(f"Histórico de pedidos para cliente {cliente_id}: {historico}")  # Log para depuração
    return jsonify(historico)

@app.route('/test', methods=['GET'])
def test():
    return jsonify([p.to_dict() for p in pedidos])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)