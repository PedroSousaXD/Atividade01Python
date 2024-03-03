def main():
    alunos = {}

    num_alunos = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(num_alunos):
        nome = input(f"Digite o nome do {i+1}º aluno: ")

        nota_prova = float(input(f"Digite a nota da prova do {i+1}º aluno: "))
        nota_trabalho = float(input(f"Digite a nota do trabalho do {i+1}º aluno: "))
        nota_atividade = float(input(f"Digite a nota da atividade do {i+1}º aluno: "))

        nota_maxima = 10
        peso_prova = 0.5
        peso_trabalho = 0.3
        peso_atividade = 0.2

        soma_pesos = peso_prova + peso_trabalho + peso_atividade
        peso_prova /= soma_pesos
        peso_trabalho /= soma_pesos
        peso_atividade /= soma_pesos

        media = (nota_prova * peso_prova + nota_trabalho * peso_trabalho + nota_atividade * peso_atividade)

        if media >= 7:
            situacao = "Aprovado"
        elif 5 <= media < 7:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        alunos[nome] = {"Nota da Prova": nota_prova,
                        "Nota do Trabalho": nota_trabalho,
                        "Nota da Atividade": nota_atividade,
                        "Média": media,
                        "Situação": situacao}

    print("\n== Dados dos Alunos ==")
    for nome, info in alunos.items():
        print(f"Nome: {nome} | Nota da Prova: {info['Nota da Prova']} | Nota do Trabalho: {info['Nota do Trabalho']} | Nota da Atividade: {info['Nota da Atividade']} | Média: {info['Média']:.2f} | Situação: {info['Situação']}")

if __name__ == "__main__":
    main()
