import numpy as np

# 1. Función sigmoide
def sigmoide(t):
    return 1.0 / (1.0 + np.exp(-t))



# 2. Probabilidad predicha p_theta(x)

def probabilidad(x, theta):
    theta0, theta1 = theta
    return sigmoide(theta0 + theta1 * x)


# 3. Superficie de riesgo RS(theta)
def superficie_riesgo(theta, x, y):

    # 1) Probabilidades predichas
    p = probabilidad(x, theta)

    # 2) Evitamos log(0) recortando p a un rango seguro
    p = np.clip(p, 1e-12, 1 - 1e-12)

    # 3) Log-verosimilitud por punto
    log_p = np.log(p)
    log_1mp = np.log(1 - p)

    # 4) Fórmula final: promedio negativo
    n = len(y)
    return -np.sum(y * log_p + (1 - y) * log_1mp) / n