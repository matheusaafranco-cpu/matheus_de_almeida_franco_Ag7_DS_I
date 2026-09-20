def executar_classificacao():
    print("=" * 60)
    print("   SISTEMA DE CLASSIFICAÇÃO DE CONSUMO DE ÁGUA   ")
    print("=" * 60)

    # 1. Validação estrita do tipo de imóvel
    tipos_validos = ["comercial", "casa", "apartamento"]
    
    while True:
        tipo_imovel = input("\nInforme o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
        if tipo_imovel in tipos_validos:
            break
        print("Opção inválida! Por favor, digite novamente: comercial, casa ou apartamento.")

    # 2. Entrada e validação do consumo mensal em m³
    while True:
        try:
            consumo = float(input("Informe o consumo mensal de água (em m³): "))
            if consumo < 0:
                print("O consumo de água não pode ser negativo. Digite novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite novamente um valor numérico (ex: 12.5).")

    print("\n" + "-" * 60)
    print("RESULTADO DA ANÁLISE:")

    # 3. Regras de Negócio exigidas na atividade
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

    print("-" * 60)


def main():
    while True:
        # Executa o cálculo de consumo
        executar_classificacao()
        
        # Pergunta se deseja calcular novamente
        while True:
            resposta = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
            if resposta in ["s", "n"]:
                break
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")
        
        # Se a resposta for 'n', encerra o programa
        if resposta == "n":
            print("\nObrigado por utilizar o sistema. Encerrando programa...")
            break


if __name__ == "__main__":
    main()