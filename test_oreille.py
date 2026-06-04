import numpy as np
import time

print("=== PROJECT BAKR : CERVEAU DE GUIDAGE GÉOPHYSIQUE ===")
time.sleep(1)

simulation_tensions = [0.150, 0.120, 0.080, 0.045, 0.090, 0.130]
courant_I = 0.020
K = 12.566

# Variable pour stocker la résistivité du piquet précédent
resistivite_precedente = None

for i, v_mesure in enumerate(simulation_tensions):
    print(f"\n--- Mesure au Piquet N°{i+1} ---")
    time.sleep(1)
    
    # Calcul de la résistivité
    rho_actuel = K * (v_mesure / courant_I)
    print(f"-> Résistivité calculée : {rho_actuel:.2f} Ohm.m")
    
    # ALGORITHME DE DÉCISION (Le guidage)
    if resistivite_precedente is not None:
        # On calcule la variation en pourcentage
        variation = ((rho_actuel - resistivite_precedente) / resistivite_precedente) * 100
        
        if variation < -5:  # Si ça baisse de plus de 5%
            print(f"💡 GUIDAGE : [ ⬇️ AVANCE ENCORE ! ] La résistivité chute de {abs(variation):.1f}%.")
        elif variation > 5:  # Si ça remonte de plus de 5%
            print(f"⚠️ GUIDAGE : [ ⬆️ ANOMALIE DÉPASSÉE ! ] Ça remonte de {variation:.1f}%. Recule au piquet précédent.")
        else:
            print("💡 GUIDAGE : [ Stabilité ] Le sol ne change pas sur cette portion.")
            
    else:
        print("💡 GUIDAGE : Premier point enregistré. Avance au piquet suivant pour comparer.")
        
    # On garde en mémoire la valeur actuelle pour le prochain piquet
    resistivite_precedente = rho_actuel

print("\n=== FIN DE LA SIMULATION DE GUIDAGE ===")
