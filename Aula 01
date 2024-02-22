import datetime

def calcular_limite_credito(tipo, tempo_ativo, renda_faturamento):
    if (tipo == 'PF' and tempo_ativo >= 3) or (tipo == 'PJ' and tempo_ativo >= 15):
        return renda_faturamento * 0.4
    else:
        return None

def main():
    tipo = input("Digite 'PF' para Pessoa Física ou 'PJ' para Pessoa Jurídica: ").upper()
    nome = input("Nome: ")

    if tipo == 'PF':
        cpf = int(input("CPF: "))
    elif tipo == 'PJ':
        cnpj = int(input("CNPJ: "))
    else:
        print("Tipo de pessoa inválido.")
        return

    data_inicio = input("Data de Início (DD/MM/AAAA): ")

    if tipo == 'PF':
        salarios = []
        for i in range(3):
            salario = float(input(f"Salário {i+1}/3 dos últimos meses: "))
            salarios.append(salario)
        renda_faturamento = sum(salarios) / 3  # Calcula a média dos salários
    else:
        faturamentos = []
        for i in range(3):
            faturamento = float(input(f"Faturamento {i+1}/3 dos últimos meses: "))
            faturamentos.append(faturamento)
        renda_faturamento = sum(faturamentos) / 3  # Calcula a média dos faturamentos

    data_inicio = datetime.datetime.strptime(data_inicio, '%d/%m/%Y').date()
    tempo_ativo = (datetime.date.today() - data_inicio).days / 30

    limite_credito = calcular_limite_credito(tipo, tempo_ativo, renda_faturamento)

    tipo_pessoa = "Pessoa Física" if tipo == 'PF' else "Pessoa Jurídica"
    print(f"\n{tipo_pessoa}\nNome: {nome}")
    if tipo == 'PF':
        print(f"CPF: {cpf}")
    elif tipo == 'PJ':
        print(f"CNPJ: {cnpj}")
    print(f"Data de Início: {data_inicio.strftime('%d/%m/%Y')}\nRenda/Faturamento: R$ {renda_faturamento:.2f}")

    if limite_credito is not None:
        print("\nAnálise de crédito aprovada!")
        print(f"Limite de Crédito: R$ {limite_credito:.2f}")
    else:
        print("\nAnálise de crédito pendente. Volte após 3 meses (PF) ou 15 meses (PJ) para nova análise.")

if __name__ == "__main__":
    main()
