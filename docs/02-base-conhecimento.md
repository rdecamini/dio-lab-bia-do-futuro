# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Como Finance vai usar? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores para gerar personalização do atendimento |
| `perfil_investidor.json` | JSON | Personalizar o entendimento das duvidas e necessidades do usuário |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil, momento e objetivo |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar para entender em qual momento de vida o usuário esta |



---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados não foram modificados até o presente momento.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON/CSV seguirão duas possibilidades, sendo injeção direto no prompt (Crtl+C, Ctrl+V) ou serão carregados via codigo, conforme exemplo:

```python
import pandas as pd
import json

#CSVs
historico = pd.read.csv('data/historico_atendimento.csv')
transacoes = pd.read.csv('data/transacoes.csv')

#JSON
with open('data/perfil_investidor.json', 'r', 'encoding='utf-8') as f:
   perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', 'encoding='utf-8') as f:
   produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
DADOS DO USUARIO E PERFIL (data/perfil_investidor.json)
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES (data/transacoes.csv)
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

PRATELEIRA DE PRODUTOS (data/produtos_financeiros.json)
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
   {
    "nome": "COE - Amazon",
    "categoria": "COE",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 10000.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Objetivo: Construir reserva de emergência

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55

Produtos
- Produto: COE - Amazon
- Categoria: COE
- Risco: Alto
- Aplicação minima: 10000.00
```
