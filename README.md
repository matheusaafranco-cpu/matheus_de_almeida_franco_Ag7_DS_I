# 💧 Monitor de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-E44D26?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

---

## 📌 Sobre o Projeto

O **Monitor de Consumo de Água** é um script interativo desenvolvido em Python para campanhas de conscientização ambiental de companhias de saneamento. O sistema solicita o tipo de imóvel e o consumo mensal do morador para classificar o uso de água e emitir alertas educativos.

O programa conta com validações estritas para entradas incorretas e permite a execução contínua de novos cálculos até que o usuário opte por encerrar o programa.

---

## ⚙️ Regras de Negócio e Classificação

| Tipo de Imóvel | Consumo ($m^3$) | Alerta / Mensagem Exibida |
| :--- | :--- | :--- |
| **Comercial** | Qualquer valor | *Tarifa comercial aplicada – consulte o plano corporativo.* |
| **Apartamento** | Menor que $10\text{ m}^3$ | *Consumo econômico – excelente controle de água!* |
| **Casa / Apartamento** | Até $25\text{ m}^3$ | *Consumo moderado – dentro do padrão residencial.* |
| **Outros / Excedente** | Acima dos limites | *Consumo excessivo – adote medidas de economia e verifique vazamentos.* |

---

## ✨ Funcionalidades

- **Validação de Imóvel:** Aceita apenas os tipos `comercial`, `casa` ou `apartamento`. Caso o usuário digite um valor diferente, solicita a entrada novamente.
- **Tratamento de Erros:** Bloqueia valores negativos ou entradas não numéricas para o consumo mensal.
- **Modo Repetição:** Pergunta no final se o usuário deseja realizar um novo cálculo (`s`/`n`), aceitando exclusivamente essas duas opções.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** 🐍
- **[Git](https://git-scm.com/)** & **[GitHub](https://github.com/)** 🐙

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.
2. Clone o repositório ou navegue até a pasta do projeto:
   ```bash