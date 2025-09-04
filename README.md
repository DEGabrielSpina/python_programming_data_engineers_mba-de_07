📈 Exchange Rate Data Pipeline

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para capturar, tratar e armazenar cotações de moedas obtidas via API de câmbio.
As camadas de dados seguem a arquitetura raw → silver → gold, com persistência em banco de dados e em arquivos locais (formato parquet e json).

🚀 Fluxo do Pipeline

Extrair

Arquivo: api_exchangerate.py

Conecta-se à API de câmbio (URL e chave no .env).

Retorna os dados em formato JSON.

Carregar na camada Raw

Arquivo: upload_on_repo.py

Salva o JSON em disco, dentro do diretório configurado (dir_raw_path).

Transformar (camada Silver)

Arquivo: transfor_consist.py

Converte o JSON em DataFrame.

Remove registros nulos ou negativos.

Arquivo: upload_silver.py

Salva no banco (schema.table_silver) e em disco (dir_silver_path).

Enriquecer (camada Gold)

Arquivo: handle_rates.py

Calcula retorno percentual e volatilidade por moeda.

Arquivo: upload_gold.py

Persiste no banco (schema.table_gold) e em disco (dir_gold_path).

Consultar Silver

Arquivo: get_rates.py

Busca dados da camada silver via query definida no .env.

Orquestração

Arquivo principal: main.py

Executa o pipeline completo.

Filtra apenas os dados da data atual.

Finaliza salvando a camada gold.

🛠 Estrutura
.
├── main.py
├── services/
│   ├── api_exchangerate.py
│   ├── CRUD.py
│   ├── get_rates.py
│   ├── handle_rates.py
│   ├── log.py
│   ├── transfor_consist.py
│   ├── upload_gold.py
│   ├── upload_on_repo.py
│   └── upload_silver.py

⚙️ Configuração

O projeto usa variáveis de ambiente em .env.
Crie um arquivo .env (ou .env.example no Git) com os seguintes parâmetros:

# API
url=https://sua_api.com/exchangerate
api_key=SUA_CHAVE_API

# Banco
conn_url=postgresql://usuario:senha@host:porta/database
schema=nome_do_schema
table_silver=nome_tabela_silver
table_gold=nome_tabela_gold

# Queries
query_silver=SELECT * FROM schema.tabela_silver

# Diretórios locais
dir_raw_path=./data/raw
dir_silver_path=./data/silver
dir_gold_path=./data/gold

# Logs
log_path=./logs/app.log

▶️ Execução

Para rodar o pipeline completo:

python main.py

🧩 Dependências

Python 3.9+

Bibliotecas:

pandas

sqlalchemy

python-dotenv

requests

streamlit (se for usar a interface interativa)

Instalação:

pip install -r requirements.txt

📝 Logs

Implementados via log.py

Registram mensagens em arquivo definido por log_path no .env.

Exemplos: erros ao salvar no banco, problemas de conexão com API, avisos sobre dados inválidos.

📊 Exploração de Dados com Streamlit

Além do pipeline ETL, o projeto inclui um dashboard interativo em Streamlit para explorar a camada gold diretamente do banco (Neon/Postgres).

Arquivo: app.py
import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
conn_url = os.getenv("conn_url")
schema = os.getenv("schema")
table_gold = os.getenv("table_gold")

engine = create_engine(conn_url)

# Ler dados da camada gold
query = f"SELECT * FROM {schema}.{table_gold};"
df = pd.read_sql(query, con=engine)

st.title("📊 Exploração de Cotações - Camada Gold")

df["date"] = pd.to_datetime(df["date"])

# Filtro por moeda
moedas = df["coin"].unique()
moeda_escolhida = st.selectbox("Selecione a moeda", moedas)

df_filtrado = df[df["coin"] == moeda_escolhida]

st.subheader(f"Dados filtrados - {moeda_escolhida}")
st.dataframe(df_filtrado)

st.subheader("📈 Evolução da taxa de câmbio")
st.line_chart(df_filtrado.set_index("date")["rate"])

st.subheader("📈 Retorno percentual")
st.line_chart(df_filtrado.set_index("date")["return"])

st.subheader("📉 Volatilidade")
st.line_chart(df_filtrado.set_index("date")["volatility"])

Execução do dashboard
streamlit run app.py


Isso abrirá a interface em http://localhost:8501, permitindo filtrar moedas, visualizar séries históricas, retornos e volatilidades.

📌 Observações

As tabelas silver e gold são sobrescritas por data antes da inserção, garantindo consistência.

Linhas com valores nulos ou negativos em rate são descartadas.

O projeto suporta tanto persistência em banco de dados quanto em arquivos parquet/json.

O Streamlit é opcional, mas facilita a análise exploratória e a apresentação dos resultados.
