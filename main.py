from core.acceleration import calcul_acceleration
from core.acceleration import plus_grand

S = 2
M = " "
R = " "
print("Determinons la valeur de lacceleration pour differents chercheurs\n")

while S!=0 and S!=1 :
    S=int(input("Choissisez la nature du terrain\n Rocher:0 \t Sol:1\n"))

while True:
    try:
        M=float(input("Entrez la valeur de magnitude\n"))
        break
    except ValueError:
        print("Valeur Invalide")

while True:
    try:
        R=float(input("Entrez la valeur de la distane epicentrale en km\n"))
        break
    except ValueError:
        print("Valeur Invalide")

AuteursAcc = {}
AuteursAcc["Mc Guire"] = calcul_acceleration(S,M,R,0.306,0.89,1.17,0,-0.20,0)
AuteursAcc["Joyner-Boore"] = calcul_acceleration(S,M,R,0.955,0.573,1.00,0.0059,0,7.3)
AuteursAcc["Petrovski"] = calcul_acceleration(S,M,R,0.599,0.539,0.844,0,0,0)
AuteursAcc["Sabette-Pugliese"] = calcul_acceleration(S,M,R,0.274,0.705,1,0,0.389,5.8)

for auteur,val in AuteursAcc.items() :
    print(f"D'apres {auteur}, L'acceleration est de {val} m/s^2\n")

auteurs_max,max_val = plus_grand(AuteursAcc)

print(f"L'acceleration la plus grande est de {max_val} m/s^2 donnee par\n")
for max in auteurs_max :
     print(f"{max}\n")