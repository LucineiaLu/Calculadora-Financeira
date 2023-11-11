# Calculadora-Financeira



https://github.com/LucineiaLu/Calculadora-Financeira/assets/149438779/4250d57d-78f1-4c85-b8f1-fc2fdc1c2397



Projeto 1: Calculadora Financeira com Validação de Renda

Versão da páginas Web : [Uploading index<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Financeira</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        #calculator {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        input {
            width: 200px;
            padding: 10px;
            margin: 5px;
        }

        button {
            padding: 10px 20px;
            background-color: #4caf50;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
</head>

<body>
    <div id="calculator">
        <h1>Calculadora Financeira</h1>

        <label for="renda">Digite sua renda mensal:</label>
        <input type="text" id="renda">

        <button onclick="validarRenda()">Validar Renda</button>

        <div id="resultado" style="display:none;">
            <label for="emprestimo">Informe o valor do empréstimo desejado:</label>
            <input type="text" id="emprestimo">

            <label for="prazo">Informe o prazo do empréstimo (em meses):</label>
            <input type="text" id="prazo">

            <label for="juros">Informe a taxa de juros anual (%):</label>
            <input type="text" id="juros">

            <button onclick="calcularEmprestimo()">Calcular Empréstimo</button>

            <h2 id="resultado-juros" style="color: #4caf50;"></h2>
            <h2 id="resultado-prestacao" style="color: #4caf50;"></h2>
            <h2 id="resultado-total" style="color: #4caf50;"></h2>
        </div>
    </div>

    <script>
        function validarRenda() {
            var renda = parseFloat(document.getElementById('renda').value);

            if (isNaN(renda) || renda < 1000) {
                alert("Erro: Sua renda mensal é muito baixa para solicitar um empréstimo.");
            } else {
                document.getElementById('resultado').style.display = 'block';
            }
        }

        function calcularEmprestimo() {
            var emprestimo = parseFloat(document.getElementById('emprestimo').value);
            var prazo = parseInt(document.getElementById('prazo').value);
            var juros = parseFloat(document.getElementById('juros').value);

            var taxa_juros_mensal = juros / 12 / 100;
            var prestacao = (emprestimo * taxa_juros_mensal) / (1 - Math.pow(1 + taxa_juros_mensal, -prazo));

            document.getElementById('resultado-juros').innerHTML = "Taxa de juros anual: " + juros.toFixed(2) + "%";
            document.getElementById('resultado-prestacao').innerHTML = "Prestação mensal: R$" + prestacao.toFixed(2);
            document.getElementById('resultado-total').innerHTML = "Custo total do empréstimo: R$" + (prestacao * prazo).toFixed(2);
        }
    </script>
</body>

</html>.html…]()


Neste projeto, os alunos criarão uma calculadora financeira em Python que ajudará os
usuários a calcular empréstimos com base em sua renda. A aplicação incluirá as seguintes
etapas:

➔ Validação de Renda:

◆ Os usuários inserirão informações sobre sua renda mensal.

◆ A aplicação verificará se a renda inserida é válida e está dentro de um limite
específico.

➔ Cálculo de Empréstimo:

◆ Após a validação bem-sucedida da renda, os usuários poderão inserir o valor
do empréstimo desejado e o prazo.

◆ A aplicação calculará a taxa de juros apropriada e o valor das prestações
mensais.

➔ Apresentação dos Resultados:

◆ A aplicação exibirá os resultados do cálculo, incluindo o valor das prestações
mensais e o custo total do empréstimo.




https://github.com/LucineiaLu/Calculadora-Financeira/assets/149438779/c288b025-41a8-4b2e-b5b5-35d3cba8fbe4




![calculator-1680905_1280](https://github.com/LucineiaLu/Calculadora-Financeira/assets/149438779/5debf502-c0c8-485d-af46-2cbeb97e8462)
