"""
Función para generar datos simulados del modelo logístico.
"""

import numpy as np
from src import modelo


def generar_datos(n, theta, rng, rango_x=(-2, 2)):
    """
    Genera X ~ Uniforme y Y ~ Bernoulli(sigma(theta_0 + theta_1 X)).
    """
    X = rng.uniform(rango_x[0], rango_x[1], size=n)
    p = modelo.probabilidad(X, theta)
    Y = rng.binomial(1, p)
    return X, Y