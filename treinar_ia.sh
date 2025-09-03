#!/bin/bash

# Este script executa o pipeline de ETL para (re)treinar a base de conhecimento da IA.

echo "🧠 Iniciando o processo de ETL (treinamento)..."
echo "Lendo todos os arquivos da pasta /data e atualizando a base de conhecimento."

# Garante que estamos executando a partir do diretório do script
cd "$(dirname "$0")"

# Executa o comando do Docker Compose para rodar o script de ETL
docker-compose run --rm etl python3 etl_orchestrator.py

echo "✅ Treinamento concluído! A base de conhecimento foi atualizada com sucesso."