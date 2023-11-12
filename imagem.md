![Captura de tela 2023-11-12 183431](https://github.com/LucineiaLu/Calculadora-Financeira/assets/149438779/4641a37e-fcee-4cee-953f-fac34bb39ab6)



![Captura de tela 2023-11-12 183303](https://github.com/LucineiaLu/Calculadora-Financeira/assets/149438779/54c2c7dd-a2c7-4672-9e51-62ce5af85094)


Passo a passo do Projeto: Calculadora Financeira com Validação de Renda

Validação de Renda:

A função validar_renda() é responsável por solicitar ao usuário a entrada da sua renda mensal.
A renda é convertida para um valor em ponto flutuante (float).
Um limite de renda de 1000.0 é definido. Se a renda mensal fornecida for igual ou superior a esse limite, a função retorna a renda validada. Caso contrário, uma mensagem de erro é exibida, indicando que a renda é muito baixa para solicitar um empréstimo, e a função retorna None.
Um bloco except ValueError trata erros de entrada, exibindo uma mensagem de erro se a entrada não for um número válido.
A renda validada é armazenada na variável renda_valida.

Cálculo de Empréstimo:

O usuário é solicitado a inserir o valor desejado do empréstimo (valor_emprestimo), o prazo em meses (prazo_emprestimo), e a taxa de juros anual em porcentagem (taxa_juros_anual).
A função calcular_emprestimo() é chamada, passando a renda validada, o valor do empréstimo, o prazo e a taxa de juros anual como argumentos.
A função calcula a taxa de juros mensal, e em seguida, calcula o valor da prestação mensal usando a fórmula da prestação em um empréstimo.
A função retorna a taxa de juros anual e o valor da prestação mensal.
Esses valores são atribuídos às variáveis taxa_juros_anual e prestacao_mensal, respectivamente.

Apresentação dos Resultados:

A função apresentar_resultados() é chamada, passando a taxa de juros anual, a prestação mensal, o valor do empréstimo e o prazo do empréstimo como argumentos.
A função calcula o custo total do empréstimo multiplicando a prestação mensal pelo prazo do empréstimo.
Os resultados são então apresentados na tela, mostrando a renda mensal, a taxa de juros anual, a prestação mensal, o valor do empréstimo e o custo total do empréstimo.
Execução do Programa:

O código finaliza com a execução das etapas acima, desde a validação da renda até a apresentação dos resultados, apenas se a renda validada for diferente de None.
O projeto fornece uma calculadora financeira interativa que orienta os usuários no cálculo de empréstimos com base em sua renda mensal, garantindo que a renda atenda a um limite mínimo antes de prosseguir com o cálculo.

