# Impressão da mensagem de boas-vindas com nome e sobrenome do desenvolvedor
print('---' * 14)
print('Boas Vindas, by Jean Ricardo Land Miranda')
print('---' * 14)   

# Lista para armazenar os funcionários (lista de dicionários)
list_funcionarios = []

# Variável global para controle do ID dos funcionários (inicializada com o RU)
id_global = 4961609

def cadastrar_funcionario():
    """
    Função para cadastrar um novo funcionário.
    Pergunta nome, setor e salário, armazena em um dicionário e adiciona à lista de funcionários.
    """
    global id_global

    print("--- CADASTRAR FUNCIONÁRIO ---")
    print(f"ID funcionário: {id_global}")
    nome = str(input("Digite o nome do funcionário: ")).strip()
    setor = str(input("Digite o setor: ")).strip()

    # Validação para garantir que o salário seja um número válido
    while True:
        try:
            salario = float(input("Digite o salário: ").strip())
            break
        except ValueError:
            print("Salário inválido. Tente novamente.")

    # Criação do dicionário com os dados do funcionário
    dicionario = {
        'id': id_global,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    # Adiciona uma cópia do dicionário à lista de funcionários
    list_funcionarios.append(dicionario)
    # Incrementa o ID global para o próximo cadastro
    id_global += 1

def consultar_funcionarios():
    """
    Função para consultar funcionários.
    ela permite consultar todos, por ID, por setor ou retornar ao menu principal.
    """
    while True:
        print("\n--- MENU DE CONSULTA DE FUNCIONÁRIOS ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = input("Qual opção deseja? ").strip()

        if opcao == '1':
            # Consulta e exibe todos os funcionários cadastrados
            print("--- Lista de Funcionários ---")
            if not list_funcionarios:
                print("Nenhum funcionário está cadastrado no momento.")
            else:
                for funcionario in list_funcionarios:
                    print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: {funcionario['salario']}")
        elif opcao == '2':
            # Consulta funcionário por ID
            print("--- Consulta por ID ---")
            while True:
                try:
                    id_consulta = int(input("Informe o ID do funcionário: ").strip())
                    funcionario = next((f for f in list_funcionarios if f['id'] == id_consulta), None)
                    if funcionario:
                        print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: {funcionario['salario']}")
                    else:
                        print("Funcionário não encontrado.")
                    break
                except ValueError:
                    print("ID inválido, tente novamente.")
        elif opcao == '3':
            # Consulta funcionários por setor
            print("--- Consulta por Setor ---")
            setor_consulta = input("Informe o setor: ").strip()
            encontrados = False
            for funcionario in list_funcionarios:
                if funcionario['setor'].lower() == setor_consulta.lower():
                    print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} | Setor: {funcionario['setor']} | Salário: {funcionario['salario']}")
                    encontrados = True
            if not encontrados:
                print("Nenhum funcionário encontrado para este setor.")
        elif opcao == '4':
            # Retorna ao menu principal
            return
        else:
            # Opção inválida, repete o menu de consulta
            print("Opção inválida.")

def remover_funcionario():
    """
    Função para remover um funcionário pelo ID.
    Se o ID não existir, informa e repete a pergunta.
    """
    print("--- REMOVER FUNCIONÁRIO ---")
    while True:
        try:
            id_remover = int(input("Informe o ID do funcionário a ser removido: ").strip())
            for i, funcionario in enumerate(list_funcionarios):
                if funcionario['id'] == id_remover:
                    removido = list_funcionarios.pop(i)
                    print(f"Funcionário {removido['nome']} foi removido com sucesso.")
                    return
            print("Funcionário não encontrado.")
            return
        except ValueError:
            print("ID inválido, tente novamente.")

if __name__ == "__main__":
    # Estrutura do menu principal do programa
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Remover Funcionário")
        print("4. Encerrar Programa")
        opcao = input("Qual opção deseja? ").strip()

        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            consultar_funcionarios()
        elif opcao == '3':
            remover_funcionario()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")
