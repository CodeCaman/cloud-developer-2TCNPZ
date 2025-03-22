# app.py - Microserviço de Produtos (versão simplificada)
from flask import Flask, jsonify, request

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_products = [
    {
        "id": "prod-001",
        "name": "Smartphone XYZ",
        "description": "Smartphone de última geração com câmera de alta resolução",
        "price": 1999.99,
        "stock": 50,
        "category_id": "cat-002",
        "supplier_id": "sup-001",
        "features": {
            "color": "Preto",
            "memory": "128GB",
            "screen": "6.5 polegadas"
        },
        "images": ["https://example.com/images/phone1.jpg", "https://example.com/images/phone2.jpg"],
        "status": "active",
        "sku": "PHONE-XYZ-128"
    },
    {
        "id": "prod-002",
        "name": "Notebook ABC",
        "description": "Notebook leve e potente para trabalho",
        "price": 4500.00,
        "stock": 20,
        "category_id": "cat-001",
        "supplier_id": "sup-002",
        "features": {
            "color": "Prata",
            "memory": "16GB RAM",
            "processor": "Intel Core i7",
            "storage": "512GB SSD"
        },
        "images": ["https://example.com/images/laptop1.jpg"],
        "status": "active",
        "sku": "NOTE-ABC-16"
    },
    {
        "id": "prod-003",
        "name": "Camiseta Casual",
        "description": "Camiseta de algodão confortável",
        "price": 59.90,
        "stock": 100,
        "category_id": "cat-003",
        "supplier_id": "sup-003",
        "features": {
            "color": "Azul",
            "size": "M",
            "material": "100% Algodão"
        },
        "images": ["https://example.com/images/tshirt1.jpg"],
        "status": "active",
        "sku": "SHIRT-CASUAL-M"
    }
]

# Histórico de preços simulado
sample_price_history = {
    "prod-001": [
        {"previous_price": 2199.99, "new_price": 1999.99, "change_date": "2023-01-15", "reason": "Promoção de Verão"},
        {"previous_price": 2299.99, "new_price": 2199.99, "change_date": "2022-11-20", "reason": "Black Friday"}
    ],
    "prod-002": [
        {"previous_price": 4799.00, "new_price": 4500.00, "change_date": "2023-02-10", "reason": "Ajuste de Mercado"}
    ]
}

# Rotas do microserviço

@app.route('/produtos', methods=['GET'])
def get_all_products():
    """
    Retorna todos os produtos
    """
    return jsonify([{
        'id': product['id'],
        'name': product['name'],
        'price': product['price'],
        'stock': product['stock'],
        'category_id': product['category_id'],
        'supplier_id': product['supplier_id'],
        'status': product['status']
    } for product in sample_products])

@app.route('/produtos/<product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retorna um produto específico pelo ID
    """
    product = next((p for p in sample_products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Produto não encontrado'}), 404

# Rota para verificar a saúde do serviço
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'produtos'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6004)