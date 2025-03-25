# Histórico de Cotações

Uma aplicação web para visualizar o histórico de cotações de empresas na bolsa de valores.

## Sobre o Projeto

Esta aplicação permite aos usuários visualizar graficamente o histórico de preços de fechamento de ações através de um ticker escolhido. Utilizando a biblioteca yfinance para obter dados históricos e Plotly para visualização interativa.

Acesse: https://wgabbriel-stock-chart.streamlit.app/

## Funcionalidades

- Consulta de histórico de cotações por ticker
- Visualização gráfica de preços de fechamento
- Interface simples e intuitiva

## Requisitos

- Python 3.6 ou superior
- Bibliotecas necessárias:
  - streamlit
  - yfinance
  - plotly

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/WGabbriel/stock_chart_app
cd stock_chart_app
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

Para iniciar a aplicação, execute:
```bash
streamlit run app.py
```

A aplicação estará disponível no navegador em `http://localhost:8501`.

## Como Usar

1. No painel lateral, digite o ticker da empresa que deseja analisar
2. O gráfico de histórico de preços será exibido automaticamente
3. Por padrão, o ticker "GOOGL" (Google) é carregado

## Estrutura do Projeto

```
Estatistica/
│
├── app.py                  # Aplicação principal Streamlit
├── data_science/           # Módulo de ciência de dados
│   ├── __init__.py
│   └── grafic.py           # Funções para gerar gráficos
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```
