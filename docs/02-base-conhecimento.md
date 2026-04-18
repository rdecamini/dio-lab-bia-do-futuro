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
DADOS DO USUARIO E PERFIL

TRANSAÇÕES

PRATELEIRA DE PRODUTOS
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
