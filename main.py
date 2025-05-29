def cadastrar_alunos():
    # Cria uma lista para armazenar os alunos
    alunos = []
    while True:
        # Solicita o nome do aluno e garante que não seja vazio
        nome = input("Nome: ")
        while not nome.strip():
            nome = input("Nome não pode ser vazio. Digite novamente: ")

 # Solicita a idade do aluno e trata erro de conversão
        try:
            idade = int(input("Idade: "))
        except ValueError:
            idade = int(input("Idade inválida. Digite um número: "))

        # Solicita as notas do aluno
        notas = []
        for i in range(3):  # cada aluno tem 3 notas
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota deve ser entre 0 e 10.")
                except ValueError:
                    print("Digite um número válido.")
        # Pergunta se deseja cadastrar outro aluno
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
        if continuar != 's':
            break
        # Verifica se o aluno já foi cadastrado
        if any(aluno["nome"].lower() == nome.lower() for aluno in alunos):
            print("Aluno já cadastrado. Tente novamente.")
            continue

        # Calcula a média das notas
        media = sum(notas) / len(notas)

        # Cria um dicionário com os dados do aluno
        aluno = {
            "nome": nome,
            "idade": idade,
            "notas": notas,
            "media": media
        }

        # Adiciona o aluno à lista
        alunos.append(aluno)
    return alunos

def mostrar_aprovados(alunos):
    # Exibe os alunos aprovados (média maior que 7)
    print("\nAlunos aprovados (média > 7):")
    for aluno in alunos:
        if aluno["media"] > 7:
            print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

def mostrar_nomes_unicos(alunos):
    # Mostra os nomes únicos dos alunos cadastrados
    nomes_unicos = set(aluno["nome"] for aluno in alunos)
    print("\nNomes únicos:", nomes_unicos)

def salvar_em_arquivo(alunos, nome_arquivo="alunos.txt"):
    # Salva os dados dos alunos em um arquivo texto
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(f"aluno{aluno['nome']}idade:{aluno['idade']}Notas:{aluno['notas']}Média:{aluno['media']:.2f}\n")
    print(f"\nDados salvos em '{nome_arquivo}'")

def main():
    # Função principal: executa o fluxo do programa
    alunos = cadastrar_alunos()
    mostrar_aprovados(alunos)
    mostrar_nomes_unicos(alunos)
    salvar_em_arquivo(alunos)

if __name__ == "__main__":
    main()
