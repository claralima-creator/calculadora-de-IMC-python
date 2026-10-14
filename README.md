# 🐍 Calculadora de IMC em Python

Um projeto desenvolvido durante meus estudos de programação com o objetivo de praticar lógica de programação, validação de dados e estruturas condicionais utilizando Python.

O programa solicita o peso, a altura e a idade do usuário, valida as informações fornecidas e calcula o Índice de Massa Corporal (IMC), apresentando a classificação correspondente para adultos.

## ✨ Funcionalidades

- ⚖️ Entrada e validação do peso.
- 📏 Validação da altura dentro de um intervalo definido.
- 🎂 Validação da idade em anos inteiros.
- 🚫 Tratamento de entradas inválidas e encerramento com mensagens de orientação.
- 🧮 Cálculo do IMC.
- 📊 Classificação do resultado em diferentes faixas.
- 👤 Restrição da classificação adulta para pessoas com 18 anos ou mais.

## 🛠️ Tecnologias e conceitos utilizados

- **Python 3**
- Variáveis e conversão de tipos com `float()` e `int()`
- Estruturas condicionais: `if`, `elif` e `else`
- Tratamento de exceções: `try` e `except`
- Operadores relacionais e lógicos
- Atribuição com expressão walrus (`:=`)
- Encerramento do programa com `sys.exit()`
- Formatação de valores com *f-strings*

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório ou baixe os arquivos do projeto.
3. Abra o terminal na pasta do projeto.
4. Execute o comando abaixo, substituindo `imc.py` pelo nome real do seu arquivo, se necessário:

```bash
python imc.py
```

5. Informe o peso em quilogramas, a altura em metros e a idade em anos inteiros.

## 🧮 Fórmula utilizada

O IMC é calculado dividindo o peso pela altura ao quadrado:

**IMC = peso (kg) / altura² (m)**

O programa apresenta a classificação de acordo com as faixas de referência para adultos implementadas no código.

## 📚 Objetivo de aprendizagem

Este projeto faz parte da minha jornada de aprendizado em programação. Com ele, pratiquei a validação de entradas, o tratamento de erros e a construção de regras de decisão para resolver um problema de forma estruturada.

## ⚠️ Observação

Este programa tem finalidade educacional. O IMC é uma medida de triagem e não substitui uma avaliação individual realizada por um profissional de saúde.

---

**Desenvolvido como parte dos meus estudos de Python.** 💚
