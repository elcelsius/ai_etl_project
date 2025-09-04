#!/bin/bash

# Este script simplifica a inicialização do chat interativo do copiloto.

echo "🚀 Iniciando o Copiloto de IA... Por favor, aguarde o carregamento dos modelos."

# Garante que estamos executando a partir do diretório do script
cd "$(dirname "$0")"

# Executa o comando do Docker Compose para iniciar o serviço de IA
docker-compose run --rm etl python3 query_handler.py

echo "✅ Sessão do copiloto encerrada."