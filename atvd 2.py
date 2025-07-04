# linha decorativa
print("--" * 26)
# Mensagem de boas-vindas com nome e sobrenome
print('Seja bem-vindo à bordo, by Jean Ricardo Land Miranda')
print("--" * 26)

# Exibe o menu para o cliente
print("Cardápio:\n"
    "Menu 1:\n"
    " Bife Acebolado (BA)\n"
    "   P - R$16\n"
    "   M - R$18\n"
    "   G - R$22\n"
    "Menu 2:\n" 
    "Filé de Frango (FF)\n"
    "   P - R$15\n"
    "   M - R$17\n"
    "   G - R$21")

# Inicializa o acumulador do valor total
total = 0

while True:  # Estrutura de repetição para múltiplos pedidos
    sabor = input("Digite o sabor do lanche (BA/FF): ").strip().upper() 
    if sabor not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente") 
        continue  # Volta ao início do loop

    tamanho = input("Digite o tamanho do lanche (P/M/G): ").strip().upper()  
    if tamanho not in ["P", "M", "G"]: 
        print("Tamanho inválido. Tente novamente")  # Mensagem de erro exigida
        continue  # Volta ao início do loop

    # Estrutura com base no  sabor e tamanho digitado pelo input do cliente,
    if sabor == "BA":
        if tamanho == "P":
            valor = 16
            print("Você escolheu Bife Acebolado - P")
        elif tamanho == "M":
            valor = 18
            print("Você escolheu Bife Acebolado - M")
        else:
            valor = 22
            print("Você escolheu Bife Acebolado - G")
    elif sabor == "FF":
        if tamanho == "P":
            valor = 15
            print("Você escolheu Filé de Frango - P")
        elif tamanho == "M":
            valor = 17
            print("Você escolheu Filé de Frango - M")
        else:
            valor = 21
            print("Você escolheu Filé de Frango - G")

    print(f"Valor: R${valor}")
    total += valor  # Acumulador de acordo com os pedidos
    print(f"Pedido adicionado. Valor atual do pedido: R${total:.2f}")

    continuar = input("Deseja pedir mais alguma coisa(S/N): ").strip().upper()
    if continuar == "N":
        print(f"Obrigado por usar nosso sistema. Valor total do pedido: R${total}. Até logo!")
        break  # Encerra o loop se o cliente não quiser mais pedir
