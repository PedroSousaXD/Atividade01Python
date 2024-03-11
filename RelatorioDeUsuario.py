from pathlib import Path
import datetime

def criar_relatorio_usuario():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    profissao = input("Digite sua profissão: ")
    frase_do_dia = input("Digite sua frase do dia: ")

    data_atual = datetime.datetime.now()
    pasta_data = data_atual.strftime("%Y-%m-%d")
    pasta_path = Path(pasta_data)
    pasta_path.mkdir(parents=True, exist_ok=True)

    nome_arquivo = pasta_path / f"{nome}.txt"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Profissão: {profissao}\n")
        arquivo.write(f"Frase do dia: {frase_do_dia}\n")

    print(f"Relatório para {nome} criado com sucesso em {nome_arquivo}")

if __name__ == "__main__":
    criar_relatorio_usuario()
