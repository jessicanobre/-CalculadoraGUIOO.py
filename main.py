import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, operacao, a, b):
        self._resultado = 0
        self._operacao = operacao
        self._a = a
        self._b = b

    def somar(self):
        self._resultado = self._a + self._b

    def subtrair(self):
        self._resultado = self._a - self._b

    def multiplicar(self):
        self._resultado = self._a * self._b

    def dividir(self):
        if self._b != 0:
            self._resultado = self._a / self._b
        else:
            self._resultado = "Erro: Divisão por zero"

    def get_resultado(self):
        if self._operacao == 1:
            self.somar()
        elif self._operacao == 2:
            self.subtrair()
        elif self._operacao == 3:
            self.multiplicar()
        elif self._operacao == 4:
            self.dividir()
        else:
            return "Operação inválida"
        return self._resultado

    def reset(self):
        self._resultado = 0

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operacao = operacao_var.get()

        calc = Calculadora(operacao, a, b)
        resultado = calc.get_resultado()

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Erro: Entrada inválida")

janela = tk.Tk()
janela.title("Calculadora")

label_a = tk.Label(janela, text="Valor A:")
label_a.grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(janela)
entry_a.grid(row=0, column=1, padx=9, pady=10)

label_b = tk.Label(janela, text="Valor B:")
label_b.grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(janela)
entry_b.grid(row=1, column=1, padx=9, pady=10)

operacao_var = tk.IntVar()
operacao_var.set(1)

botao_soma = tk.Radiobutton(janela, text="Somar", variable=operacao_var, value=1)
botao_soma.grid(row=2, column=0, padx=10, pady=10)

botao_subtrair = tk.Radiobutton(janela, text="Subtrair", variable=operacao_var, value=2)
botao_subtrair.grid(row=2, column=1, padx=10, pady=10)

botao_multiplicar = tk.Radiobutton(janela, text="Multiplicar", variable=operacao_var, value=3)
botao_multiplicar.grid(row=3, column=0, padx=10, pady=10)

botao_dividir = tk.Radiobutton(janela, text="Dividir", variable=operacao_var, value=4)
botao_dividir.grid(row=3, column=1, padx=10, pady=10)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
