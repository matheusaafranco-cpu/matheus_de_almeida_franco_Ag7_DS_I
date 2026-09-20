<div align="center">

# 💧 Monitor de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44D26?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

*Sistema em Python para classificação do perfil de consumo de água e apoio a campanhas ambientais.*

</div>

---

## 📌 Sobre o Projeto

O **Monitor de Consumo de Água** foi desenvolvido para auxiliar companhias de saneamento em campanhas de conscientização ambiental. A aplicação solicita o tipo de imóvel e o consumo mensal do morador para classificar o perfil de uso e emitir alertas educativos automáticos.

---

## 📋 Regras de Negócio

| Tipo de Imóvel | Consumo ($m^3$) | Mensagem Exibida |
| :--- | :--- | :--- |
| 🏬 **Comercial** | Qualquer valor | *Tarifa comercial aplicada – consulte o plano corporativo.* |
| 🏢 **Apartamento** | Menor que $10\text{ m}^3$ | *Consumo econômico – excelente controle de água!* |
| 🏠 **Casa / Apartamento** | Até $25\text{ m}^3$ | *Consumo moderado – dentro do padrão residencial.* |
| ⚠️ **Demais casos** | Acima de $25\text{ m}^3$ | *Consumo excessivo – adote medidas de economia e verifique vazamentos.* |

---

## 💻 Como Executar

Para rodar a aplicação, certifique-se de ter o **Python 3** instalado e execute o arquivo no terminal:

```bash
python app.py