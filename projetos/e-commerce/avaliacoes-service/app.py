# app.py - Microserviço de Avaliações (versão simplificada)
from flask import Flask, jsonify, request
from datetime import datetime

# Inicialização da aplicação Flask
app = Flask(__name__)

# Dados de exemplo
sample_reviews = [
    {
        "id": "rev-001",
        "product_id": "prod-001",
        "user_id": "user-001",
        "title": "Smartphone excelente!",
        "comment": "Comprei este smartphone e estou muito satisfeito. A câmera é incrível e a bateria dura o dia todo.",
        "rating": 5,
        "review_date": "2023-01-15T14:30:00",
        "photos": ["https://example.com/photos/review1-1.jpg", "https://example.com/photos/review1-2.jpg"],
        "helpfulness": {"likes": 12, "dislikes": 2},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"camera": 5, "battery": 4, "design": 5, "performance": 4}
    },
    {
        "id": "rev-002",
        "product_id": "prod-001",
        "user_id": "user-002",
        "title": "Bom, mas com alguns problemas",
        "comment": "O smartphone é bom, mas esquenta muito quando uso por muito tempo. A câmera é excelente!",
        "rating": 3,
        "review_date": "2023-02-20T10:15:00",
        "photos": [],
        "helpfulness": {"likes": 5, "dislikes": 1},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"camera": 5, "battery": 2, "design": 4, "performance": 3}
    },
    {
        "id": "rev-003",
        "product_id": "prod-002",
        "user_id": "user-003",
        "title": "Notebook perfeito para trabalho",
        "comment": "Comprei para trabalho e atendeu todas as expectativas. Rápido e com boa duração de bateria.",
        "rating": 5,
        "review_date": "2023-03-05T16:45:00",
        "photos": ["https://example.com/photos/review3-1.jpg"],
        "helpfulness": {"likes": 8, "dislikes": 0},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"performance": 5, "battery": 4, "design": 5, "keyboard": 4}
    },
    {
        "id": "rev-004",
        "product_id": "prod-003",
        "user_id": "user-004",
        "title": "Camiseta de boa qualidade",
        "comment": "O material é bom e não desbotou após várias lavagens. Recomendo!",
        "rating": 4,
        "review_date": "2023-02-28T09:30:00",
        "photos": [],
        "helpfulness": {"likes": 3, "dislikes": 0},
        "status": "approved",
        "verified_purchase": True,
        "attributes": {"quality": 4, "comfort": 5, "sizing": 4}
    },
    {
        "id": "rev-005",
        "product_id": "prod-001",
        "user_id": "user-005",
        "title": "Aguardando moderação",
        "comment": "Esta é uma avaliação que ainda não foi moderada.",
        "rating": 2,
        "review_date": "2023-03-10T11:20:00",
        "photos": [],
        "helpfulness": {"likes": 0, "dislikes": 0},
        "status": "pending",
        "verified_purchase": False,
        "attributes": {"camera": 2, "battery": 3, "design": 2, "performance": 2}
    }
]

# Respostas às avaliações
sample_responses = [
    {
        "id": "resp-001",
        "review_id": "rev-002",
        "user_id": "seller-001",
        "comment": "Agradecemos seu feedback. O aquecimento pode ocorrer em uso intenso. Sugerimos atualizar o software para a versão mais recente que melhorou este aspecto.",
        "response_date": "2023-02-22T14:30:00",
        "is_seller": True,
        "status": "active"
    },
    {
        "id": "resp-002",
        "review_id": "rev-003",
        "user_id": "user-006",
        "comment": "Concordo totalmente! Também uso para trabalho e é excelente.",
        "response_date": "2023-03-07T10:15:00",
        "is_seller": False,
        "status": "active"
    }
]

# Resumo de avaliações por produto
sample_summaries = {
    "prod-001": {
        "product_id": "prod-001",
        "average_rating": 4.0,
        "total_reviews": 3,
        "distribution": {"5": 1, "4": 0, "3": 1, "2": 1, "1": 0},
        "attribute_averages": {"camera": 4.0, "battery": 3.0, "design": 3.67, "performance": 3.0},
        "last_updated": "2023-03-10T11:20:00"
    },
    "prod-002": {
        "product_id": "prod-002",
        "average_rating": 5.0,
        "total_reviews": 1,
        "distribution": {"5": 1, "4": 0, "3": 0, "2": 0, "1": 0},
        "attribute_averages": {"performance": 5.0, "battery": 4.0, "design": 5.0, "keyboard": 4.0},
        "last_updated": "2023-03-05T16:45:00"
    },
    "prod-003": {
        "product_id": "prod-003",
        "average_rating": 4.0,
        "total_reviews": 1,
        "distribution": {"5": 0, "4": 1, "3": 0, "2": 0, "1": 0},
        "attribute_averages": {"quality": 4.0, "comfort": 5.0, "sizing": 4.0},
        "last_updated": "2023-02-28T09:30:00"
    }
}

# Informações dos produtos (adicionando esta estrutura para suportar as novas funções)
sample_products = {
    "prod-001": {
        "id": "prod-001",
        "name": "Smartphone Galaxy X10",
        "category": "Eletrônicos",
        "price": 2499.90,
        "brand": "Samsung",
        "description": "Smartphone com tela AMOLED de 6.5\", 128GB de armazenamento e 8GB de RAM"
    },
    "prod-002": {
        "id": "prod-002",
        "name": "Notebook ProBook Ultra",
        "category": "Informática",
        "price": 4899.90,
        "brand": "HP",
        "description": "Notebook com processador Intel i7, 16GB de RAM e SSD de 512GB"
    },
    "prod-003": {
        "id": "prod-003",
        "name": "Camiseta Casual Básica",
        "category": "Vestuário",
        "price": 79.90,
        "brand": "Essentials",
        "description": "Camiseta 100% algodão, corte regular, disponível em várias cores"
    }
}

# Rotas do microserviço

@app.route('/avaliacoes/produtos/<product_id>', methods=['GET'])
def get_product_reviews(product_id):
    """
    Retorna as avaliações de um produto
    """
    # Parâmetros opcionais
    status = request.args.get('status', 'approved')  # Por padrão, retorna apenas aprovadas
    
    # Filtra as avaliações
    if status == 'all':
        reviews = [r for r in sample_reviews if r['product_id'] == product_id]
    else:
        reviews = [r for r in sample_reviews if r['product_id'] == product_id and r['status'] == status]
    
    # Para cada avaliação, adiciona suas respostas
    reviews_with_responses = []
    for review in reviews:
        review_data = dict(review)
        review_data['responses'] = [r for r in sample_responses if r['review_id'] == review['id'] and r['status'] == 'active']
        reviews_with_responses.append(review_data)
    
    return jsonify({
        'reviews': reviews_with_responses,
        'total': len(reviews_with_responses),
        'product_id': product_id
    })

# Rota para verificar a saúde do serviço
@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificação de saúde do serviço
    """
    return jsonify({'status': 'ok', 'service': 'avaliações'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)