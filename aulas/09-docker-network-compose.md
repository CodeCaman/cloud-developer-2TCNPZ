# Aula sobre Docker Networking e Docker Compose
## 1. Bridge (Padrão)

```bash
docker network create --driver bridge minha_bridge
```
> Características:
> 
> - Rede isolada padrão para containers
> 
> - Comunicação entre containers na mesma bridge
> 
> - NAT para acesso externo
> 
> Uso típico:
> 
> - Ambiente de desenvolvimento local
> 
> - Aplicações isoladas no mesmo host

## 2. Host

```bash
docker network create --driver host minha_host
```
> Características:
>
> - Remove o isolamento de rede do container
>
> - Container usa a stack de rede do host diretamente
>
> - Sem sobrecarga de NAT
>
> Uso típico:
>
> - Quando performance de rede é crítica
>
> - Aplicações que precisam de acesso direto a portas do host

## 3. Overlay

```bash
docker network create --driver overlay minha_overlay
```

> Características:
>
> - Conecta múltiplos daemons Docker (Swarm)
> 
> - Comunicação entre containers em hosts diferentes
> 
> - Criptografia opcional
> 
> Uso típico:
>
> - Ambientes distribuídos (Docker Swarm)
>
> - Comunicação entre serviços em clusters

## 4. Macvlan

```bash
docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 minha_macvlan
```

> Características:
> 
> - Atribui endereço MAC ao container
> 
> - Aparece como dispositivo físico na rede
> 
> - Sem NAT, máximo desempenho
> 
> Uso típico:
> 
> - Migração de workloads legados
> 
> - Quando containers precisam aparecer como hosts físicos

## 5. None

```bash
docker network create --driver none minha_none
```

> Características:
> 
> - Container sem interface de rede
> 
> - Isolamento total
> 
> Uso típico:
> 
> - Containers que não precisam de rede
> 
> - Processos batch/offline


## Quando usar cada tipo?

| Tipo      | Cenário Recomendado                      | Performance | Isolamento |
|-----------|------------------------------------------|-------------|------------|
| Bridge    | Desenvolvimento local, maioria dos casos | Médio       | Alto       |
| Host      | Aplicações performance crítica           | Máximo      | Mínimo     |
| Overlay   | Cluster Docker Swarm                     | Médio       | Alto       |
| Macvlan   | Containers que precisam de MAC real      | Máximo      | Médio      |
| None      | Containers sem necessidade de rede       | -           | Total      |

## Boas Práticas para Networking

### Desenvolvimento:
- Use redes bridge com nomes significativos
- Crie redes específicas para cada projeto

### Produção:
- Considere macvlan para cargas pesadas
- Overlay para ambientes distribuídos
- Evite rede host a menos que necessário

### Segurança:
- Isole redes por função (frontend, backend, db)
- Use redes internas para comunicação entre serviços
- Restrinja acesso externo quando possível

## Comandos de Rede no Docker

### Listar redes disponíveis
```bash
docker network ls
```
### Criar uma nova rede bridge
```bash
docker network create minha_rede
```
Cria uma nova rede bridge personalizada chamada "minha_rede"

### Executar containers em uma rede específica

```bash
docker run -d --name containerA --network minha_rede nginx
docker run -d --name containerB --network minha_rede nginx
```
- --network: Conecta o container à rede especificada
- Containers na mesma rede podem se comunicar pelo nome (DNS automático)

### Inspecionar uma rede

```bash
docker network inspect minha_rede
```
Mostra detalhes da rede, incluindo containers conectados e configurações IP

### Verificar IP de um container

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' containerA
```
Formatação personalizada para extrair apenas o endereço IP do container

### Testar conectividade entre containers

```bash
docker exec -it containerA /bin/bash

# Dentro do container:
apt-get update && apt-get install -y iputils-ping  # Instala o pacote ping

ping containerB
```
- Observação: A imagem oficial do Nginx é baseada em Debian e não vem com o ping instalado por padrão

- O pacote iputils-ping precisa ser instalado para usar o comando ping

- A comunicação pode ser testada tanto pelo nome do container quanto pelo IP

### Acessar um container em execução

```bash
docker exec -it containerA /bin/bash
```
Entra no container de forma interativa com terminal bash

## Docker Compose 🚀 


## 🔍 Comparativo

| Nome do Arquivo        | Compatibilidade             | Comentário                                                                 |
|------------------------|-----------------------------|---------------------------------------------------------------------------|
| `docker-compose.yml`   | ✅ Amplamente compatível     | Usado com `docker-compose` (CLI legado) e também com `docker compose` (CLI moderno) |
| `compose.yml`          | ✅ Docker Compose v2+        | Suportado apenas pelo `docker compose` (plugin integrado ao Docker moderno) |

---

## ✅ Recomendações

- Use `docker-compose.yml` para garantir **máxima compatibilidade** com ambientes locais, CI/CD e times diferentes.
- Use `compose.yml` apenas se você **tem certeza** de que todos usam o Docker moderno com suporte ao Compose v2+.


### Sobe os containers definidos no docker-compose.yml (e no override, se houver).
 
 ```bash
docker-compose up
```

### Com -d: roda em background (modo detached)

docker-compose up -d


### Para e remove todos os containers, redes e volumes anônimos criados pelo Compose.

 ```bash
docker-compose down
```

### Com --volumes: remove volumes também

```bash
docker-compose down --volumes
```

### Faz o build das imagens a partir dos Dockerfiles.
```bash
docker-compose build
```

### Força rebuild, mesmo sem alterações:
 
```bash
docker-compose build --no-cache
```

### Construir e iniciar serviços

```bash
docker-compose up --build
```

- --build: Constrói as imagens antes de iniciar os containers

### Ver logs dos serviços

```bash
docker-compose logs

docker-compose logs -f # Segue os logs em tempo real
```
- Mostra os logs de todos os serviços definidos no docker-compose.yml


### Apenas pausa ou reinicia containers (sem remover).

```bash
docker-compose stop   # Para os containers
docker-compose start  # Reinicia os containers parados
```

### Para e inicia novamente os containers.

```bash
docker-compose restart
```

### Executa um comando dentro de um container já rodando (como docker exec).

```bash
docker-compose exec produtos sh     # Entra no shell
docker-compose exec produtos ls -l  # Roda comando
```
Obs: O container precisa estar ativo (up)


### Roda um comando único em um container, mesmo que o serviço não esteja em up.

```bash
docker-compose run produtos bash
```

### Lista os containers que estão rodando no contexto do Compose atual.
 
```bash
docker-compose ps
```

### Valida e mostra a configuração final (útil para debug de override.yml).

```bash
docker-compose config
```

### Mostra os processos ativos dentro dos containers.

```bash
docker-compose top
``` 

### Puxa ou envia imagens de/para um registry (Docker Hub, GitHub, etc.).

```bash
docker-compose pull
docker-compose push
``` 

## docker-compose.override.yml em DEV

Vantagens de usar docker-compose.yml limpo e genérico (base de produção)

E um docker-compose.override.yml com configurações específicas para desenvolvimento:

- Montagem de volumes locais
- Variáveis de ambiente
- Comandos de debug
- Hot reload

Cada desenvolvedor pode manter um override para trabalhar com seu ambiente sem modificar o compose.yml principal.
Evita alterar arquivos de produção acidentalmente.
Separação de preocupações (infra vs dev)
É um passo para DevOps real (CI/CD, staging, etc.)

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
``` 
Ou usar perfis do Compose (desde v3.9+):

```bash
services:
  clientes:
    ...
    profiles:
      - dev
```
```bash
COMPOSE_PROFILES=dev docker-compose up
```

## Gerenciamento de Código

### Atualizar repositório local

```bash
git pull
```

### Commitar e enviar alterações

```bash
git add .
git commit -a -m "Added docker-compose"
git 
```