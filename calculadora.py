# Projeto 1: Calculadora Financeira com Validação de Renda

# Neste projeto, os alunos criarão uma calculadora financeira em Python que ajudará os usuários a calcular empréstimos com base em sua renda. A aplicação incluirá as seguintes etapas:
# ➔ Validação de Renda:
# ◆ Os usuários inserirão informações sobre sua renda mensal.
# ◆ A aplicação verificará se a renda inserida é válida e está dentro de um limite específico.
# ➔ Cálculo de Empréstimo:
# ◆ Após a validação bem-sucedida da renda, os usuários poderão inserir o valor do empréstimo desejado e o prazo.
# ◆ A aplicação calculará a taxa de juros apropriada e o valor das prestações mensais.
# ➔ Apresentação dos Resultados:
# ◆ A aplicação exibirá os resultados do cálculo, incluindo o valor das prestações mensais e o custo total do empréstimo.

# Função para validar a renda do usuário
def validar_renda():
    try:
        renda_mensal = float(input("Digite sua renda mensal: "))
        limite_renda = 1000.0  # Limite de renda
        if renda_mensal >= limite_renda:
            return renda_mensal
        else:
            print("Erro: Sua renda mensal é muito baixa para solicitar um empréstimo.")
            return None
    except ValueError:
        print("Erro: Por favor, insira uma renda válida.")
        return None

# Função para calcular o emprestimo
def calcular_emprestimo(renda, valor_emprestimo, prazo, taxa_juros_anual):
    taxa_juros_mensal = taxa_juros_anual / 12 / \
        100  # Convertendo taxa anual para mensal
    valor_prestacao = (valor_emprestimo * taxa_juros_mensal) / \
        (1 - (1 + taxa_juros_mensal) ** -prazo)

    return taxa_juros_anual, valor_prestacao

# Apresenta os resultados
def apresentar_resultados(taxa_juros_anual, prestacao_mensal, valor_emprestimo, prazo_emprestimo):
    custo_total = prestacao_mensal * prazo_emprestimo
    print("\nResultados do Cálculo:")
    print(f"Renda Mensal: {renda_valida:.2f}")
    print(f"Taxa de juros anual: {taxa_juros_anual:.2f}%")
    print(f"Prestação mensal: R${prestacao_mensal:.2f}")
    print(f"Valor do emprestimo: R${valor_emprestimo:.2f}")
    print(f"Custo total do empréstimo: R${custo_total:.2f}")


# Validação de Renda
renda_valida = validar_renda()
if renda_valida is not None:
    # Cálculo de Empréstimo
    valor_emprestimo = float(
        input("Informe o valor do empréstimo desejado: R$"))
    prazo_emprestimo = int(input("Informe o prazo do empréstimo (em meses): "))
    taxa_juros_anual = float(input("Informe a taxa de juros anual (%): "))

    taxa_juros_anual, prestacao_mensal = calcular_emprestimo(
        renda_valida, valor_emprestimo, prazo_emprestimo, taxa_juros_anual)

    # Apresentação dos Resultados
    print(f"Taxa de juros anual: {taxa_juros_anual:.2f}%")
    print(f"Prestação mensal: R${prestacao_mensal:.2f}")

    apresentar_resultados(taxa_juros_anual, prestacao_mensal, valor_emprestimo, prazo_emprestimo)

