alunos = []

while True:
    print("=== CadEst  ===")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Remover aluno")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":  
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula: ")
        curso = input("Curso: ")

        matricula_existe = False
        for aluno in alunos:
            if aluno[1] == matricula:
                matricula_existe = True
                break

        if matricula_existe:
            print("Erro: matrícula já cadastrada.")
        else:
            aluno = [nome, matricula, curso]
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")

    elif opcao == "2":  
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(f"Nome: {aluno[0]}, Matrícula: {aluno[1]}, Curso: {aluno[2]}")

    elif opcao == "3":  
        matricula = input("Digite a matrícula do aluno: ")
        aluno_encontrado = False
        for aluno in alunos:
            if aluno[1] == matricula:
                print(f"Nome: {aluno[0]}, Curso: {aluno[2]}")
                aluno_encontrado = True
                break

        if not aluno_encontrado:
            print("Aluno não encontrado.")

    elif opcao == "4":  
        matricula = input("Digite a matrícula do aluno para remover: ")
        aluno_removido = False
        for aluno in alunos:
            if aluno[1] == matricula:
                alunos.remove(aluno)
                print("Aluno removido com sucesso.")
                aluno_removido = True
                break

        if not aluno_removido:
            print("Aluno não encontrado.")

    elif opcao == "5":  
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
