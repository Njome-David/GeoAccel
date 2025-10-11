import numpy as np

def plus_grand(valeurs):
    if not valeurs:
        return [], None

    max_val = max(valeurs.values())
    auteurs_max = [auteur for auteur, val in valeurs.items() if val == max_val]
    return auteurs_max, max_val

def calcul_acceleration(S, M, R, alpha, beta, gamma, sigma, epsilon, d):
    """
    Calcule l'accélération selon les paramètres fournis.
    Protège contre la division par zéro en forçant D minimale.
    Retourne un float.
    """
    D = np.sqrt(R**2 + d**2)
    if D == 0:
        D = 1e-12  # évite ZeroDivisionError si R et d sont tous deux zéro

    arr = np.array([beta * M, -sigma * D, epsilon * S], dtype=float)
    result = np.exp(arr)
    answer = np.prod(result) * alpha * (D ** (-gamma))
    return float(answer)
