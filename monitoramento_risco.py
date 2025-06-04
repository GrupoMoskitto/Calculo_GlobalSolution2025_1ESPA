import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from sympy import symbols, sin, exp, diff, lambdify
from scipy.integrate import quad

mplstyle.use('seaborn-v0_8-muted')

# Definindo a função simbólica
t = symbols('t')
f_sym = 600 * exp(0.15 * t) * sin(0.7 * t)
f_prime = diff(f_sym, t)
f_second = diff(f_sym, t, 2)

# Funções numéricas
f_lamb = lambdify(t, f_sym, modules=['numpy'])
f_prime_lamb = lambdify(t, f_prime, modules=['numpy'])
f_second_lamb = lambdify(t, f_second, modules=['numpy'])

# Intervalo de tempo
t_vals = np.linspace(0, 20, 1000)
limite_volume = 8000
taxa_escoamento = 50

# Volume acumulado e líquido
volume_acumulado = [quad(f_lamb, 0, t_)[0] for t_ in t_vals]
volume_liquido = [v - taxa_escoamento * t_ for v, t_ in zip(volume_acumulado, t_vals)]


# Interface
def mostrar_derivada():
    derivada = f_prime_lamb(10)
    if derivada > 1000:
        alerta = "Alerta: Vazão aumentando muito rápido!"
    elif derivada > 0:
        alerta = "Vazão aumentando."
    elif derivada < 0:
        alerta = "Vazão diminuindo."
    else:
        alerta = "Vazão estável."

    messagebox.showinfo("Derivada em t=10", f"f'(10) ≈ {derivada:.2f} L/min²\n\n{alerta}")


def mostrar_volume():
    vol_final = volume_liquido[-1]
    if vol_final > limite_volume:
        alerta = "Alerta: Volume acima do limite!"
    else:
        alerta = "Volume dentro do limite."

    messagebox.showinfo("Volume acumulado", f"Volume líquido final: {vol_final:.2f} L\n\n{alerta}")


def plotar_graficos():
    fig, axs = plt.subplots(3, 1, figsize=(10, 12), constrained_layout=True)

    # Vazão
    axs[0].plot(t_vals, f_lamb(t_vals), color='steelblue', linewidth=2)
    axs[0].set_title('Vazão de Água', fontsize=14)
    axs[0].set_ylabel('Vazão (L/min)')
    axs[0].grid(True)

    # Derivada
    axs[1].plot(t_vals, f_prime_lamb(t_vals), color='darkorange', linewidth=2)
    axs[1].set_title("Derivada da Vazão", fontsize=14)
    axs[1].set_ylabel("df/dt (L/min²)")
    axs[1].grid(True)

    # Volume acumulado
    axs[2].plot(t_vals, volume_liquido, color='green', linewidth=2, label='Volume líquido')
    axs[2].axhline(y=limite_volume, color='red', linestyle='--', label='Limite Crítico')
    axs[2].fill_between(t_vals, volume_liquido, limite_volume,
                        where=(np.array(volume_liquido) > limite_volume),
                        color='red', alpha=0.2, interpolate=True)
    axs[2].set_title("Volume de Água Acumulado", fontsize=14)
    axs[2].set_xlabel("Tempo (min)")
    axs[2].set_ylabel("Volume (L)")
    axs[2].legend()
    axs[2].grid(True)

    plt.suptitle("Monitoramento de Risco de Alagamento", fontsize=16, fontweight='bold')
    plt.show()


# Interface Tkinter
janela = tk.Tk()
janela.title("Sistema de Monitoramento de Alagamentos")
janela.geometry("420x300")
janela.configure(bg="#f0f4f7")

frame = tk.Frame(janela, bg="#f0f4f7")
frame.pack(expand=True, pady=20)

titulo = tk.Label(frame, text="Monitoramento da Vazão", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#333")
titulo.pack(pady=10)

btn1 = tk.Button(frame, text="Calcular Derivada em t = 10 min", command=mostrar_derivada, width=35, height=2, bg="#e1f5fe")
btn1.pack(pady=5)

btn2 = tk.Button(frame, text="Verificar Volume Acumulado", command=mostrar_volume, width=35, height=2, bg="#e8f5e9")
btn2.pack(pady=5)

btn3 = tk.Button(frame, text="Exibir Gráficos", command=plotar_graficos, width=35, height=2, bg="#fff3e0")
btn3.pack(pady=10)

janela.mainloop()
