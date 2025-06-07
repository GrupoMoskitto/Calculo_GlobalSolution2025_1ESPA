# Monitoramento de Vazão de Água para Prevenção de Alagamentos

## Descrição
Este projeto foi desenvolvido para apoiar a Defesa Civil no monitoramento da vazão de água em uma área urbana sujeita a alagamentos. Ele analisa a taxa de entrada de água em uma bacia de contenção durante uma tempestade, utilizando a função matemática $f(t) = 600 \cdot e^{0.15t} \cdot \sin(0.7t)$, onde $f(t)$ representa a vazão (em L/min) e $t$ é o tempo (em minutos). O objetivo é prever riscos, identificar momentos críticos e propor medidas preventivas.

## Membros do Grupo Moskitto GS:
- [**Gabriel Kato**](https://github.com/kato8088) - RM560000
- [**Gabriel Couto**](https://github.com/rouri404) - RM559579
- [**João Vitor de Matos**](https://github.com/joaomatosq) - RM559246

## Funcionalidades
1. **Gráfico Dinâmico**: Visualização da vazão, derivada e volume acumulado ao longo do tempo.
2. **Análise do Limite**: Estudo do comportamento da função quando $t \to +\infty$.
3. **Derivada em $t=10$**: Interpretação da taxa de variação da vazão em $t=10$ minutos.
4. **Integral Definida**: Cálculo do volume acumulado de água entre 0 e 20 minutos, com avaliação do risco de alagamento.
5. **Interface Gráfica**: Sistema interativo com alertas de risco implementado em Python com Tkinter.

## Estrutura do Projeto
- [**GS2025_1-Calculo.pdf**](GS2025_1-Calculo.pdf): Documento com a descrição do problema e tarefas.
- [**calculos-fiap-gs.ipynb**](calculos-fiap-gs.ipynb): Notebook Jupyter com cálculos, gráficos e análises (usando NumPy, Matplotlib, SymPy e SciPy).
- [**monitoramento_risco.py**](monitoramento_risco.py): Script Python com interface gráfica Tkinter para monitoramento.
- [**memorial_calculo_vazao.pdf**](memorial_calculo_vazao.pdf): Documento com gráficos gerados (vazão e volume acumulado).
- [**requirements.txt**](requirements.txt): Lista de dependências necessárias.

## Requisitos
Para executar o projeto, instale as dependências listadas em `requirements.txt`:
```bash
pip install -r requirements.txt
```

Dependências:
- Python 3.13.3
- numpy
- matplotlib
- sympy
- scipy
- tkinter

## Como Executar
1. **Notebook Jupyter**:
   - Abra o arquivo `calculos-fiap-gs.ipynb` em um ambiente Jupyter.
   - Execute as células para visualizar cálculos, gráficos e resultados.

2. **Interface Gráfica**:
   - Execute o script `monitoramento_risco.py`:
     ```bash
     python monitoramento_risco.py
     ```
   - A interface exibe botões para calcular a derivada em $t=10$, verificar o volume acumulado e exibir gráficos.

## Video Explicativo
[![Video Youtube](https://img.youtube.com/vi/JtKeJYBKplU/0.jpg)](https://www.youtube.com/watch?v=JtKeJYBKplU)