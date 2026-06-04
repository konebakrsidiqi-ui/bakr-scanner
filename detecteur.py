import math
import time
import random

print("=== PROJECT BAKR : DÉTECTEUR DE PROSPECTION DIRECTE ===")
print("Initialisation du scanner de terrain...")
time.sleep(1)

# Position fictive de la cible cachée dans le sol (Coordonnées X, Y, Profondeur Z)
# La cible est à 1.5m sur la droite, 2m devant, et 0.8m sous le sol
X_cible, Y_cible, Z_cible = 1.5, 2.0, -0.8

# On simule la marche du prospecteur (6 étapes de rapprochement)
trajectoire_prospecteur = [
    (0.0, 0.0, 0.0),  # Point de départ
    (0.5, 0.8, 0.0),
    (1.0, 1.5, 0.0),
    (1.4, 2.0, 0.0),  # Ici on est presque aligné !
    (1.5, 2.1, 0.0),
    (2.2, 2.5, 0.0)   # On s'éloigne
]

for etape, (x_tel, y_tel, z_tel) in enumerate(trajectoire_prospecteur):
    print(f"\n--- Scan Position N°{etape + 1} ---")
    time.sleep(1)
    
    # 1. Calcul de la distance sur l'axe Gauche/Droite (Axe X)
    ecart_x = X_cible - x_tel
    
    # 2. Calcul de la profondeur (Axe Z)
    profondeur = abs(Z_cible - z_tel)
    
    # 3. Calcul de la distance globale en ligne droite (Théorème de Pythagore 3D)
    distance_globale = math.sqrt((X_cible - x_tel)**2 + (Y_cible - y_tel)**2 + (Z_cible - z_tel)**2)
    
    print(f"[📡] Distance globale de l'objectif : {distance_globale:.2f} m")
    
    # --- LE CERVEAU DE DÉCISION (GUIDAGE DIRECT) ---
    # Guidage Gauche / Droite
    if abs(ecart_x) < 0.2:
        direction_x = "ALIGNÉ (Droit devant)"
    elif ecart_x > 0:
        direction_x = f"{abs(ecart_x):.1f} m à DROITE"
    else:
        direction_x = f"{abs(ecart_x):.1f} m à GAUCHE"
        
    # Affichage de l'instruction de prospection sur l'écran
    print(f"📢 ÉCRAN : DETECTION à {direction_x}")
    print(f"📢 ÉCRAN : PROFONDEUR à {profondeur:.1f} m en BAS")

print("\n=== FIN DU SCAN DE PROSPECTION ===")
