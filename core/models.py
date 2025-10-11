"""
Définition centralisée des modèles/auteurs et de leurs paramètres.
Importer MODELS depuis core.models dans main.py et gui/app.py :
from core.models import MODELS
"""
from typing import List, Tuple

# (name, (alpha, beta, gamma, sigma, epsilon, d))
MODELS: List[Tuple[str, Tuple[float, ...]]] = [
    ("Mc Guire", (0.306, 0.89, 1.17, 0.0, -0.20, 0.0)),
    ("Joyner-Boore", (0.955, 0.573, 1.00, 0.0059, 0.0, 7.3)),
    ("Petrovski", (0.599, 0.539, 0.844, 0.0, 0.0, 0.0)),
    ("Sabette-Pugliese", (0.274, 0.705, 1.0, 0.0, 0.389, 5.8)),
]