from flask import Flask, render_template, request

app = Flask(__name__)


def validar_renda(renda):
    try:
        renda = float(renda)
        limite_renda = 1000.0  # Limite de renda
        if renda >= limite_renda:
            return renda
        else:
            return None, "Erro: Sua renda mensal é muito baixa para solicitar um empréstimo."
    except ValueError:
        return None, "Erro: Por favor, insira uma renda válida."


def calcular_emprestimo(renda, valor_emprestimo, prazo, taxa_juros_anual):
    try:
        taxa_juros_mensal = taxa_juros_anual / 12 / \
            100  # Convertendo taxa anual para mensal
        valor_prestacao = (valor_emprestimo * taxa_juros_mensal) / \
            (1 - (1 + taxa_juros_mensal) ** -prazo)
        return taxa_juros_anual, valor_prestacao, None
    except ZeroDivisionError:
        return None, None, "Erro: Prazo do empréstimo não pode ser zero."


@app.route('/', methods=['GET', 'POST'])
def index():
    renda_valida = None
    resultado_validacao_renda = None
    resultado_calculo_emprestimo = None

    if request.method == 'POST':
        renda_input = request.form['renda']
        renda_valida, resultado_validacao_renda = validar_renda(renda_input)

        if renda_valida is not None:
            valor_emprestimo = float(request.form['emprestimo'])
            prazo_emprestimo = int(request.form['prazo'])
            taxa_juros_anual = float(request.form['juros'])

            taxa_juros_anual, prestacao_mensal, erro_calculo = calcular_emprestimo(
                renda_valida, valor_emprestimo, prazo_emprestimo, taxa_juros_anual)

            if erro_calculo is not None:
                resultado_calculo_emprestimo = erro_calculo
            else:
                resultado_calculo_emprestimo = {
                    'taxa_juros_anual': taxa_juros_anual,
                    'prestacao_mensal': prestacao_mensal,
                    'custo_total': prestacao_mensal * prazo_emprestimo
                }

    return render_template('index.html', renda_valida=renda_valida,
                           resultado_validacao_renda=resultado_validacao_renda,
                           resultado_calculo_emprestimo=resultado_calculo_emprestimo)


if __name__ == '__main__':
    app.run(debug=True)
