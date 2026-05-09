import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ----------------------------
# MODELO SEIR
# ----------------------------

# População total
N = 1000

# Condições iniciais
S0 = 999   # suscetíveis
E0 = 0     # expostos
I0 = 1     # infectados
R0 = 0     # recuperados

# Parâmetros do modelo
beta = 0.3      # taxa de transmissão
sigma = 1/5     # taxa de incubação
gamma = 1/10    # taxa de recuperação

# Tempo da simulação (160 dias)
t = np.linspace(0, 160, 160)

# ---------------------------------
# FUNÇÃO DO SISTEMA SEIR
# ---------------------------------

def modelo_seir(y, t, N, beta, sigma, gamma):
    
    # Separando as variáveis
    S, E, I, R = y

    # Equações diferenciais
    dSdt = -beta * S * I / N
    
    dEdt = (beta * S * I / N) - (sigma * E)
    
    dIdt = (sigma * E) - (gamma * I)
    
    dRdt = gamma * I

    return dSdt, dEdt, dIdt, dRdt

# Vetor inicial
y0 = S0, E0, I0, R0

# Resolvendo o sistema
resultado = odeint(
    modelo_seir,
    y0,
    t,
    args=(N, beta, sigma, gamma)
)

# Separando resultados
S = resultado[:, 0]
E = resultado[:, 1]
I = resultado[:, 2]
R = resultado[:, 3]

# ---------------------------------
# GRÁFICO
# ---------------------------------

plt.figure(figsize=(10,6))

plt.plot(t, S, label='Suscetíveis (S)')
plt.plot(t, E, label='Expostos (E)')
plt.plot(t, I, label='Infectados (I)')
plt.plot(t, R, label='Recuperados (R)')

plt.xlabel('Tempo (dias)')
plt.ylabel('Número de pessoas')

plt.title('Simulação do Modelo SEIR')

plt.legend()

plt.grid(True)

plt.savefig("grafico.png")

plt.show()
