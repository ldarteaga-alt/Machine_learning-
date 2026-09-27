"""
Función para ajustar el modelo logístico.
"""

import numpy as np
from scipy.optimize import minimize
from src import modelo


def ajustar_modelo(x, y, theta_inicial=(0.0, 0.0), maxiter=100):
    resultado = minimize(
        fun=modelo.superficie_riesgo,
        x0=np.array(theta_inicial, dtype=float),
        args=(x, y),
        method="BFGS",
        options={"maxiter": maxiter}
    )
    return {
        "theta": resultado.x,
        "RS": resultado.fun,
        "success": resultado.success,
        "nit": resultado.nit,
    }
