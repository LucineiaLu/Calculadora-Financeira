import tkinter as tk
from tkinter import messagebox

def validar_renda():
    try:
        renda_mensal = float(renda_entry.get())
        limite_renda = 1000.0  # Limite de renda
        if renda_mensal >= limite_renda:
            return renda_mensal
        else:
            messagebox.showerror("Erro", "Sua renda mensal é muito baixa para solicitar um empréstimo.")
            return None
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma renda válida.")
        return None

def calcular_emprestimo():
    renda = validar_renda()
    if renda is not None:
        try:
            valor_emprestimo = float(valor_emprestimo_entry.get())
            prazo_emprestimo = int(prazo_emprestimo_entry.get())
            taxa_juros_anual = float(taxa_juros_entry.get())

            taxa_juros_mensal = taxa_juros_anual / 12 / 100
            valor_prestacao = (valor_emprestimo * taxa_juros_mensal) / \
                (1 - (1 + taxa_juros_mensal) ** -prazo_emprestimo)

            custo_total = valor_prestacao * prazo_emprestimo

            resultado_label.config(text=f"Taxa de juros anual: {taxa_juros_anual:.2f}%\n"
                                       f"Prestação mensal: R${valor_prestacao:.2f}\n"
                                       f"Custo total do empréstimo: R${custo_total:.2f}")

            salvar_button["state"] = "normal"
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para o empréstimo, o prazo e a taxa de juros.")

def salvar_resultado():
    try:
        with open("resultado_emprestimo.txt", "w") as arquivo:
            arquivo.write(resultado_label.cget("text"))
        messagebox.showinfo("Sucesso", "Resultado do empréstimo salvo com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível salvar o resultado: {str(e)}")

app = tk.Tk()
app.title("Calculadora Financeira")

renda_label = tk.Label(app, text="Renda Mensal:")
renda_label.pack()
renda_entry = tk.Entry(app)
renda_entry.pack()

valor_emprestimo_label = tk.Label(app, text="Valor do Empréstimo:")
valor_emprestimo_label.pack()
valor_emprestimo_entry = tk.Entry(app)
valor_emprestimo_entry.pack()

prazo_emprestimo_label = tk.Label(app, text="Prazo do Empréstimo (em meses):")
prazo_emprestimo_label.pack()
prazo_emprestimo_entry = tk.Entry(app)
prazo_emprestimo_entry.pack()

taxa_juros_label = tk.Label(app, text="Taxa de Juros Anual (%):")
taxa_juros_label.pack()
taxa_juros_entry = tk.Entry(app)
taxa_juros_entry.pack()

calcular_button = tk.Button(app, text="Calcular", command=calcular_emprestimo)
calcular_button.pack()

resultado_label = tk.Label(app, text="")
resultado_label.pack()

salvar_button = tk.Button(app, text="Salvar Resultado", command=salvar_resultado, state="disabled")
salvar_button.pack()

app.mainloop()
