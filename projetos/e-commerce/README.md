# Projeto de E-commerce com Microserviços, Docker e Serverless.

Bem-vindo ao projeto de e-commerce com microserviços! Este projeto tem como objetivo desenvolver uma aplicação de e-commerce, utilizando uma arquitetura baseada em microserviços, containers Docker e integração com serviços serverless.

---

## **Estrutura do Projeto**

O projeto está organizado em pastas, cada uma representando um microserviço específico. Abaixo está a estrutura de pastas:


[cloud-developer-2TCNPZ/projetos/e-commerce](https://www.mermaidchart.com/raw/95fd97ad-40d0-444c-b5de-1797feb624c4?theme=light&version=v0.1&format=svg)


### **Descrição das Pastas**
- **clientes-service/**: Contém o microserviço de Clientes.
- **usuarios-service/**: Contém o microserviço de Usuários.
- **permissoes-service/**: Contém o microserviço as Permissões.
- **produtos-service/**: Contém o microserviço de Produtos.
- **categorias-service/**: Contém o microserviço de Categorias.
- **estoque-service/**: Contém o microserviço de Estoque.
- **orcamentos-service/**: Contém o microserviço de Orçamentos.
- **fornecedores-service/**: Contém o microserviço de Fornecedores.
- **lojas-service/**: Contém o microserviço de Lojas.
- **pagamentos-service/**: Contém o microserviço de Formas de Pagamento.
- **pedidos-service/**: Contém o microserviço de Pedidos.
- **items-service/**: Contém o microserviço de Items do Pedidos.
- **avaliacoes-service/**: Contém o microserviço de Avaliações e Comentários.
- **frete-service/**: Contém o microserviço de Frete.
- **api-gateway/**: Contém o API Gateway para integração dos microserviços.
- **docker-compose.yml**: Arquivo para orquestrar todos os serviços com Docker.
- **README.md**: Documentação geral do projeto.

Cada pasta de microserviço contém:
- Código-fonte do microserviço.
- Dockerfile para containerização.
- README.md com instruções específicas do microserviço.

---

## **Como Contribuir**

### **1. Configuração do Ambiente**
Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:
- **Git**: [Instalação do Git](https://git-scm.com/)
- **Docker**: [Instalação do Docker](https://docs.docker.com/get-docker/)
- **Node.js** (ou outra linguagem de sua preferência): [Instalação do Node.js](https://nodejs.org/)
- **Editor de Código**: Recomendamos o [VS Code](https://code.visualstudio.com/).

### **2. Clonar o Repositório**
Clone o repositório para sua máquina local:
```
git clone https://github.com/camanducci/cloud-developer-2TCNPZ.git
cd cloud-developer-2TCNPZ
```
3. Criar uma Branch para o Microserviço

Cada grupo deve trabalhar em uma branch específica para seu microserviço. Para criar uma branch, use:

```
git checkout -b feature/nome-do-microservico
```
Substitua nome-do-microservico pelo nome do seu microserviço (ex: clientes, produtos, etc).


4. Desenvolver o Microserviço
- Navegue até a pasta do seu microserviço (ex: clientes-service/).
- Desenvolva o código do microserviço na linguagem de sua preferência (python, node).
- Crie um Dockerfile para containerizar o microserviço.
- Documente o microserviço em um README.md dentro da pasta.

5. Commits e Pushs
```
git add .
git commit -m "Adiciona funcionalidade X ao microserviço Y"
git push origin feature/nome-do-microservico
```

1. Abrir um Pull Request (PR)

Quando o microserviço estiver pronto:

1. Abra um Pull Request no GitHub para mergear a branch feature/nome-do-microservico na branch develop.

2. Aguarde a revisão do código.

3. Após a aprovação, o código será mergeado na branch develop.

7. Integração Final
Quando todos os microserviços estiverem na branch develop, um PR será aberto para mergear develop na main. Após testes e aprovação, o projeto estará completo!

---
### **3. Executando o Projeto Localmente**

1. Subir os Microserviços com Docker Compose

No diretório raiz do projeto, execute:

```
docker-compose --env-file .env -f docker-compose.yml -f docker-compose.dev.yml up -d
docker-compose --env-file .env -f docker-compose.yml -f docker-compose.prod.yml up -d
```
http://localhost:5082/

### **4. Acessar os Microserviços**

Cada microserviço estará disponível em uma porta específica. Consulte o README.md de cada microserviço para mais detalhes.

## Branches e Fluxo de Trabalho
### Branches Principais
main: Branch estável, onde o código final será integrado.

develop: Branch de desenvolvimento, onde as features são integradas antes de ir para a main.


### Branches de Feature
Cada grupo trabalha em uma branch específica para seu microserviço. Use o padrão:

```
feature/nome-do-microservico
```
Exemplo: feature/clientes, feature/produtos, etc.

### **Organização das Branches por Grupo**

Aqui está um exemplo de como as branches podem ser organizadas para cada grupo:

| Grupo                     | Branch                | Pasta no Repositório   |
|---------------------------|-----------------------|------------------------|
| Clientes        | `feature/clientes`    | `clientes-service/`    |
| Produtos      | `feature/produtos`    | `produtos-service/`    |
| Lojas                     | `feature/lojas`       | `lojas-service/`       |
| Formas de Pagamento       | `feature/pagamentos`  | `pagamentos-service/`  |
| Pedidos                   | `feature/pedidos`     | `pedidos-service/`     |
| Avaliações e Comentários  | `feature/avaliacoes`  | `avaliacoes-service/`  |
| Frete                     | `feature/frete`       | `frete-service/`       |
| API Gateway               | `feature/api-gateway` | `api-gateway/`         |

### Branches de Hotfix
Para correções urgentes, use branches do tipo:
```
hotfix/nome-do-fix
```

## Documentação dos Microserviços
Cada microserviço deve ter seu próprio README.md com as seguintes informações:

- Descrição do microserviço.
- Instruções para rodar localmente.
- Endpoints da API (se aplicável).
- Exemplos de requisições e respostas.

### **Módulos do Projeto**

#### **1. Módulo de Clientes e Usuários**
**Funcionalidades:**
- Cadastro de clientes (nome, e-mail, senha, endereço, telefone).
- Autenticação e autorização (login, logout, recuperação de senha).
- Perfil do cliente (editar dados, histórico de pedidos).

**Entidades:**
- `Clientes`: Armazena informações dos clientes.
- `Usuários`: Gerencia autenticação e permissões.

---

#### **2. Módulo de Produtos e Categorias**
**Funcionalidades:**
- Cadastro de produtos (nome, descrição, preço, estoque, categoria).
- Cadastro de categorias (ex: eletrônicos, roupas, alimentos).
- Busca e filtragem de produtos por categoria, preço, etc.

**Entidades:**
- `Produtos`: Armazena informações dos produtos.
- `Categorias`: Organiza os produtos em categorias.

---

#### **3. Módulo de Lojas (Multi-vendedores)**
**Funcionalidades:**
- Cadastro de lojas (nome, descrição, endereço, contato).
- Associação de produtos a lojas.
- Dashboard para lojas visualizarem vendas e estoque.

**Entidades:**
- `Lojas`: Armazena informações das lojas.
- `Produtos_Lojas`: Relaciona produtos a lojas.

---

#### **4. Módulo de Formas de Pagamento**
**Funcionalidades:**
- Cadastro de formas de pagamento (cartão de crédito, boleto, PIX).
- Integração com gateways de pagamento (ex: PagSeguro, Stripe).
- Histórico de transações.

**Entidades:**
- `Formas_Pagamento`: Armazena as opções de pagamento.
- `Transações`: Registra os pagamentos realizados.

---

#### **5. Módulo de Pedidos**
**Funcionalidades:**
- Criação de pedidos (associar produtos, cliente, forma de pagamento).
- Status do pedido (em processamento, enviado, entregue).
- Histórico de pedidos por cliente.

**Entidades:**
- `Pedidos`: Armazena informações dos pedidos.
- `Itens_Pedido`: Relaciona produtos a pedidos.

---

#### **6. Módulo de Avaliações e Comentários**
**Funcionalidades:**
- Avaliação de produtos por clientes (nota, comentário).
- Moderação de comentários.

**Entidades:**
- `Avaliações`: Armazena as avaliações dos produtos.

---

#### **7. Módulo de Frete**
**Funcionalidades:**
- Cálculo de frete com base no endereço do cliente.
- Integração com APIs de correios ou transportadoras.

**Entidades:**
- `Fretes`: Armazena as regras de cálculo de frete.

---

#### **8. Módulo de Cupons e Promoções**
**Funcionalidades:**
- Cadastro de cupons de desconto (valor fixo, porcentagem).
- Aplicação de cupons no checkout.
- Promoções sazonais (ex: Black Friday).

**Entidades:**
- `Cupons`: Armazena os cupons de desconto.
- `Promoções`: Armazena as regras de promoções.

---

#### **9. Módulo de Relatórios e Análises**
**Funcionalidades:**
- Relatório de vendas por período.
- Análise de produtos mais vendidos.
- Dashboard administrativo.

**Entidades:**
- Dados derivados dos outros módulos (não precisa de novas tabelas).


# Dúvidas e Suporte
Se tiver dúvidas ou precisar de ajuda, abra uma Issue no repositório ou entre em contato com o professor.
