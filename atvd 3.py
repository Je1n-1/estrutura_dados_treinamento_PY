# Imprime uma linha de separação decorativa
print('---' * 14)
print('Boas Vindas, by Jean Ricardo Land Miranda')
print('---' * 14)

# Dicionário com os preços dos modelos de camisetas
precos = {
    'MCS': 1.80,  # Manga Curta Simples
    'MLS': 2.10,  # Manga Longa Simples
    'MCE': 2.90,  # Manga Curta Estampa
    'MLE': 3.20   # Manga Longa Estampa
}

# Função para obter o desconto baseado na quantidade de camisetas
def obter_desconto(qtd):
    if 1 <= qtd <= 19:
        return 0.0
    elif 20 <= qtd <= 199:
        return 0.05
    elif 200 <= qtd <= 1999:
        return 0.07
    elif 2000 <= qtd <= 20000:
        return 0.12
    else:
        return None  # Quantidade fora do limite permitido

# Função para escolher o modelo da camiseta
def escolha_modelo():
    while True:
        modelo = input('Escolha o modelo desejado (MCS, MLS, MCE, MLE): ').strip().upper()
        if modelo in precos:
            return modelo
        print("Modelo inválido. Tente novamente.")

# Função para obter o número de camisetas e calcular o desconto
def num_camisetas():
    while True:
        try:
            qtd = int(input('Digite o número de camisetas: '))
            desconto = obter_desconto(qtd)
            if desconto is None:
                print("Quantidade fora do limite permitido (1 a 20000).")
                continue
            return qtd, desconto
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Função para escolher o tipo de frete
def calcular_frete():
    while True:
        print("\nEscolha o tipo de frete:")
        print("0 - Retirar na fábrica (R$0)")
        print("1 - Transportadora (R$100)")
        print("2 - Sedex (R$200)")
        escolha = input("Digite o número correspondente ao frete: ").strip()
        if escolha == '0':
            return 0
        elif escolha == '1':
            return 100
        elif escolha == '2':
            return 200
        else:
            print("Opção de frete inválida. Tente novamente.")

# Execução principal
modelo = escolha_modelo()
res = num_camisetas()
frete = calcular_frete()

# Exibe os resultados do pedido se a quantidade for válida 
if res is not None:
    qtd, desconto = res
    preco_unitario = precos[modelo] * qtd  # Calcula o preço total sem desconto
    valor_com_desconto = preco_unitario * (1 - desconto)  # Aplica o desconto
    total_com_frete = valor_com_desconto + frete  # Soma o frete ao valor final
    print(f"\nModelo escolhido: {modelo}")
    print(f" Preço unitário: R${precos[modelo]:.2f}")
    print(f"Quantidade de camisetas: {qtd}")
    print(f"Preço total das camisetas sem desconto: R${preco_unitario:.2f}")
    print(f"Desconto aplicado: R${desconto * 100:.0f}%")
    print(f"Valor total com desconto: R${valor_com_desconto:.2f}")
    print(f"Frete: R${frete:.2f}")
    print(f"Total geral: R${total_com_frete:.2f}")
else:
    print("Pedido não processado devido a quantidade inválida.")
