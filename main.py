from typing import Dict
from core.acceleration import calcul_acceleration, plus_grand
from core.models import MODELS


def ask_int_choice(prompt: str, allowed: tuple = ("0", "1")) -> int:
    while True:
        val = input(prompt).strip().lower()
        if val in allowed:
            return int(val)
        print("Valeur invalide — entrez 0 ou 1.")


def ask_float(prompt: str, min_value: float = None) -> float:
    while True:
        try:
            v = float(input(prompt).strip())
            if min_value is not None and v < min_value:
                print(f"Valeur doit être >= {min_value}")
                continue
            return v
        except ValueError:
            print("Valeur invalide, entrez un nombre.")


def compute_for_models(S: int, M: float, R: float) -> Dict[str, float]:
    results: Dict[str, float] = {}
    for name, params in MODELS:
        alpha, beta, gamma, sigma, epsilon, d = params
        accel = calcul_acceleration(S, M, R, alpha, beta, gamma, sigma, epsilon, d)
        results[name] = accel
    return results


def print_results(results: Dict[str, float]) -> None:
    print("\nRésultats (triés) :")
    for name, val in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f" - {name}: {val:.4e} m/s²")
    winners, max_val = plus_grand(results)
    if max_val is None:
        print("\nAucun résultat calculable.")
    else:
        print(f"\nAccélération maximale : {max_val:.4e} m/s²")
        print("Auteur(s) :", ", ".join(winners))


def main() -> None:
    print("Calculer l'accélération selon différents auteurs\n")
    S = ask_int_choice("Nature du terrain (0=Rocher, 1=Sol) : ")
    M = ask_float("Entrez la magnitude (M) : ")
    R = ask_float("Entrez la distance épicentrale en km (R >= 0) : ", min_value=0.0)

    results = compute_for_models(S, M, R)
    print_results(results)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompu par l'utilisateur.")