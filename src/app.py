import json
import pandas as pd
import requests
import streamlit as st

# ============== CONFIGURAÇÃO OLLAMA ==============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:120b-cloud"

# ============== CARREGAR DADOS ==============
perfil = json.load(open('.\data\perfil_investidor.json'))
transacoes = pd.read_csv('.\data/transacoes.csv')
produtos = json.load(open('.\data\produtos_financeiros.json'))
historico = pd.read_csv('.\data\historico_atendimento.csv')

# ============== MONTAR CONTEXTO ==============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} - RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES
{historico.to_string(index=False)}

PRATELEIRA DE PRODUTOS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============== SYSTEM PROMPT ==============
SYSTEM_PROMPT = """Você é o Finance "Fin", um agente financeiro inteligente amigo. educativo e consultivo.

OBJETIVO
Ensinar conceitos de finanças pessoais de forma simples, usando dados do usuario como exemplos, para que seja possivel o usuario entender e tormar decisões mais assertivas ao seu objetivo

REGRAS:
1. NUNCA recomende investimentos especificos, apenas explique como funciona;
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Use dados fornecidos para dar exemplos personalizados;
5. Linguagem simples, como se fosse uma conversa entre amigos;
6. Sempre pergunte se o usuário entendeu;
7. Responde sempre de forma sucinta e direta, com no maximo 3 paragrafos;
8. JAMAIS responda perguntas fora do contexto financeiro e educativo
"""

# ============== CHAMAR OLLAMA =============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============== INTERFACE ==============
st.title("Finance, mas pode me chamar de Fin =D")

if pergunta := st.chat_input("Sua pergunta sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
