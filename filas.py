from collections import deque 

def menu(): 
    print("\n--- Sistema de Controle de Fila - Açougue Bom Preço ---") 
    print("1 - Retirar Senha") 
    print("2 - Chamar Próxima Senha") 
    print("3 - Mostrar Fila Atual") 
    print("4 - Sair") 
    return input("Escolha uma opção: ") 

# Inicialização da fila 
fila = deque() 
contador_senha = 0 

while True: 
    opcao = menu() 

    if opcao == '1': 
        contador_senha += 1 
        senha = f"A{contador_senha}" 
        fila.append(senha) 
        print(f"Senha {senha} retirada com sucesso!") 

    elif opcao == '2': 
        if fila: 
            senha_chamada = fila.popleft() 
            print(f"Atenção! Senha chamada: {senha_chamada}") 
        else: 
            print("Fila vazia. Nenhuma senha para chamar.") 

    elif opcao == '3': 
        if fila: 
            print("Fila atual de senhas: ", list(fila)) 
        else: 
            print("Fila vazia.") 

    elif opcao == '4': 
        print("Sistema encerrado. Obrigado por utilizar!") 
        break 

    else: 
        print("Opção inválida. Tente novamente.") 
