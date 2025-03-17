# Pedidos Service 🛒

Este é o micro serviço de Pedidos do projeto de e-commerce. Ele permite o cadastro de pedidos, a verificação do status dos pedidos e a visualização do histórico de pedidos por cliente.

## Funcionalidades ✨

- Cadastro de pedidos (produto, quantidade, forma de pagamento).
- Verificação do status dos pedidos.
- Histórico de pedidos por cliente.

## Requisitos 📋

- Python 3.7+
- Flask

## Instalação 🔧

1. Clone o repositório:

    ```bash
    git clone https://github.com/CodeCaman/cloud-developer-2TCNPZ.git
    cd cloud-developer-2TCNPZ
    git checkout feature/pedidos
    cd projetos/e-commerce/pedidos-service
    ```

## Como Rodar Localmente

1. Certifique-se de ter o Python e o Flask instalados.
   
2. Crie um ambiente virtual e ative-o:

    ```bash
    python3 -m venv venv
    source venv\Scripts\activate
    ou
    .\venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip3 install -r requirements.txt
    ```

4. Execute o serviço:
    ```sh
    python app.py
    ```
5. O serviço estará disponível em `http://0.0.0.0:8080`.

## Como Rodar com Docker

1. Certifique-se de ter o Docker instalado.
2. Construa a imagem Docker:
    ```sh
    docker build -t pedidos-service .
    ```
3. Execute o container:
    ```sh
    docker run --name pedidos-service-container -p 8080:8080 pedidos-service
    ```
4. O serviço estará disponível em `http://0.0.0.0:8080`.

## Endpoints 🔄

### `GET /`

Renderiza a página inicial com os formulários para cadastro de pedidos e verificação de status.

### `POST /pedidos`

Cadastra um novo pedido com base nos dados fornecidos no formulário.

### `GET /pedidos/<int:pedido_id>`

Retorna o status do pedido especificado.

### `GET /clientes/<int:cliente_id>/pedidos`

Retorna o histórico de pedidos do cliente especificado.

### `GET /status`

Retorna o status do serviço.

## Exemplos de Requisições e Respostas 📬

### Cadastro de Pedido

**Requisição:**
```bash
curl -X POST http://localhost:8080/pedidos -H "Content-Type: application/json" -d '{"cliente_id": 20, "itens": [{"produto_id": 100, "quantidade": 5}], "forma_pagamento": "pix"}'
```

**Resposta:**

```bash
{
    "id": 1
}
```

### Verificação de Status do Pedido

**Requisição:**

```bash
curl http://localhost:8080/pedidos/1
```
**Resposta:**

```bash
{
    "status": "em processamento"
}
ou
{
    "status": "enviado"
}
ou
{
    "status": "entregue"
}
```

### Ver Histórico de Pedidos por Cliente

**Requisição:**

```bash
curl http://localhost:8080/clientes/20/pedidos
```
**Resposta:**

```bash
[
    {
        "id": 1,
        "cliente_id": 20,
        "itens": [
            {
                "produto_id": 100,
                "quantidade": 5
            }
        ],
        "forma_pagamento": "pix",
        "status": "em processamento",
        "data_criacao": "2025-03-12T15:35:02.245151"
    }
]
```
### Verificar Status do Serviço

**Resposta:**

```bash
curl http://localhost:8080/status
```

**Resposta:**

```bash
{
    "status": "ok"
}
```

## Estrutura do Projeto 📁

- `app.py`: Contém a lógica principal do serviço, incluindo as rotas e o processamento dos dados.
- `templates/index.html`: Página HTML para interação com o serviço.
- `README.md`: Este arquivo, contendo a descrição do projeto e instruções de uso.
- `requirements.txt`: Lista de dependências do projeto.

## Dependências 📦

- blinker==1.9.0
- click==8.1.8
- colorama==0.4.6
- Flask==3.1.0
- itsdangerous==2.2.0
- Jinja2==3.1.6
- MarkupSafe==3.0.2
- Werkzeug==3.1.3
