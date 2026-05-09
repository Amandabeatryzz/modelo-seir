# Modelo SEIR em Python

Projeto de simulação epidemiológica utilizando o modelo SEIR.

---

## Sobre o Projeto

O modelo SEIR divide a população em quatro grupos:

- S → Suscetíveis
- E → Expostos
- I → Infectados
- R → Recuperados

O objetivo do projeto é simular o espalhamento de doenças infectocontagiosas utilizando equações diferenciais.

---

## Tecnologias Utilizadas

- Python
- NumPy
- SciPy
- Matplotlib

---

## Instalação

Instale as bibliotecas com:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute o projeto com:

```bash
python seir.py
```

---

## Resultado

O programa gera um gráfico mostrando:

- evolução dos suscetíveis;
- crescimento dos infectados;
- pico epidemiológico;
- recuperação da população.

---

## Estrutura do Projeto

```text
modelo-seir/
│
├── seir.py
├── requirements.txt
├── README.md
└── grafico.png
```

---

## Autor

Projeto desenvolvido para estudo de modelagem epidemiológica com Python.
