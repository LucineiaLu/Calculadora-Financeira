import PySimpleGUI as sg

# Função para validar a renda do usuário


def validar_renda(renda_mensal):
    try:
        renda_mensal = float(renda_mensal)
        limite_renda = 1000.0  # Limite de renda
        if renda_mensal >= limite_renda:
            return renda_mensal
        else:
            sg.popup_error(
                "Erro: Sua renda mensal é muito baixa para solicitar um empréstimo.")
            return None
    except ValueError:
        sg.popup_error("Erro: Por favor, insira uma renda válida.")
        return None

# Função para calcular o empréstimo


def calcular_emprestimo(renda, valor_emprestimo, prazo, taxa_juros_anual):
    taxa_juros_mensal = taxa_juros_anual / 12 / \
        100  # Convertendo taxa anual para mensal
    valor_prestacao = (valor_emprestimo * taxa_juros_mensal) / \
        (1 - (1 + taxa_juros_mensal) ** -prazo)

    return taxa_juros_anual, valor_prestacao

# Apresenta os resultados


def apresentar_resultados(renda_valida, taxa_juros_anual, prestacao_mensal, valor_emprestimo, prazo_emprestimo):
    custo_total = prestacao_mensal * prazo_emprestimo
    sg.popup_ok("Resultados do Cálculo:",
                f"Renda Mensal: {renda_valida:.2f}",
                f"Taxa de juros anual: {taxa_juros_anual:.2f}%",
                f"Prestação mensal: R${prestacao_mensal:.2f}",
                f"Valor do empréstimo: R${valor_emprestimo:.2f}",
                f"Custo total do empréstimo: R${custo_total:.2f}")


# Layout da interface gráfica
layout = [
    [sg.Text("Digite sua renda mensal:"), sg.InputText(key="-RENDA-")],
    [sg.Text("Informe o valor do empréstimo desejado:"),
     sg.InputText(key="-VALOR_EMPRESTIMO-")],
    [sg.Text("Informe o prazo do empréstimo (em meses):"),
     sg.InputText(key="-PRAZO_EMPRESTIMO-")],
    [sg.Text("Informe a taxa de juros anual (%):"),
     sg.InputText(key="-TAXA_JUROS-")],
    [sg.Button("Calcular Empréstimo"), sg.Button("Sair")]
]

# Cria a janela
window = sg.Window("Calculadora Financeira").Layout(layout)

# Loop principal
while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    if event == "Calcular Empréstimo":
        renda_valida = validar_renda(values["-RENDA-"])

        if renda_valida is not None:
            valor_emprestimo = float(values["-VALOR_EMPRESTIMO-"])
            prazo_emprestimo = int(values["-PRAZO_EMPRESTIMO-"])
            taxa_juros_anual = float(values["-TAXA_JUROS-"])

            taxa_juros_anual, prestacao_mensal = calcular_emprestimo(
                renda_valida, valor_emprestimo, prazo_emprestimo, taxa_juros_anual)

            apresentar_resultados(renda_valida, taxa_juros_anual,
                                  prestacao_mensal, valor_emprestimo, prazo_emprestimo)

# Fecha a janela ao sair do loop principal
window.close()
