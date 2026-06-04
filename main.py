from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import math

class DetecteurBakrApp(App):
    def build(self):
        # Configuration de la cible fixe (X, Y, Profondeur Z)
        self.X_cible, self.Y_cible, self.Z_cible = 1.5, 2.0, -0.8
        
        # Simulation des pas du prospecteur
        self.trajectoire = [
            (0.0, 0.0, 0.0),
            (0.5, 0.8, 0.0),
            (1.0, 1.5, 0.0),
            (1.4, 2.0, 0.0),
            (1.5, 2.1, 0.0),
            (2.2, 2.5, 0.0)
        ]
        self.etape = 0

        # Layout Principal (Vertical, adapté au format allongé du Redmi 12)
        layout_principal = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # 1. Titre de l'application
        self.titre = Label(
            text="PROJECT BAKR — SCANNER", 
            font_size='22sp', 
            bold=True, 
            size_hint_y=0.1,
            color=get_color_from_hex('#78909C')
        )
        layout_principal.add_widget(self.titre)

        # 2. Grand Affichage : Distance globale
        self.lbl_distance = Label(
            text="--- m", 
            font_size='56sp', 
            bold=True, 
            size_hint_y=0.25,
            color=get_color_from_hex('#FFD54F')
        )
        layout_principal.add_widget(self.lbl_distance)

        # 3. Indicateur Visuel Central (Flèche et Guidage Latéral)
        self.lbl_guidage_x = Label(
            text="Appuyez sur SCAN", 
            font_size='24sp', 
            bold=True,
            size_hint_y=0.25,
            halign='center'
        )
        layout_principal.add_widget(self.lbl_guidage_x)

        # 4. Indicateur de Profondeur (En bas)
        self.lbl_profondeur = Label(
            text="Profondeur : ---", 
            font_size='20sp', 
            size_hint_y=0.15,
            color=get_color_from_hex('#B0BEC5')
        )
        layout_principal.add_widget(self.lbl_profondeur)

        # 5. Gros Bouton Tactile d'action
        self.btn_scan = Button(
            text="BALAYAGE TERRAIN (SCAN)", 
            font_size='20sp', 
            bold=True, 
            size_hint_y=0.2,
            background_color=get_color_from_hex('#0288D1')
        )
        self.btn_scan.bind(on_press=self.calculer_position)
        layout_principal.add_widget(self.btn_scan)

        return layout_principal

    def calculer_position(self, instance):
        if self.etape >= len(self.trajectoire):
            self.lbl_guidage_x.text = "Fin de la ligne.\nCible localisée !"
            self.lbl_guidage_x.color = get_color_from_hex('#FFFFFF')
            self.btn_scan.text = "RECOMMENCER"
            self.etape = 0
            return

        # Récupération des coordonnées courantes du téléphone
        x_tel, y_tel, z_tel = self.trajectoire[self.etape]
        self.btn_scan.text = f"PAS N°{self.etape + 1} ENREGISTRÉ"
        self.etape += 1

        # Calculs géométriques
        ecart_x = self.X_cible - x_tel
        profondeur = abs(self.Z_cible - z_tel)
        distance_globale = math.sqrt((self.X_cible - x_tel)**2 + (self.Y_cible - y_tel)**2 + (self.Z_cible - z_tel)**2)

        # Mise à jour des textes
        self.lbl_distance.text = f"{distance_globale:.2f} m"
        self.lbl_profondeur.text = f"Profondeur : {profondeur:.1f} m en BAS"

        # Logique des couleurs et flèches de guidage direct
        if abs(ecart_x) < 0.2:
            self.lbl_guidage_x.text = "🎯 ALIGNÉ\n(Droit devant !)"
            self.lbl_guidage_x.color = get_color_from_hex('#00E676') # Vert fluo clair
        elif ecart_x > 0:
            self.lbl_guidage_x.text = f"➡️ {abs(ecart_x):.1f} m\nà DROITE"
            self.lbl_guidage_x.color = get_color_from_hex('#29B6F6') # Bleu indicateur
        else:
            self.lbl_guidage_x.text = f"⬅️ {abs(ecart_x):.1f} m\nà GAUCHE"
            self.lbl_guidage_x.color = get_color_from_hex('#FF7043') # Orange alerte

if __name__ == '__main__':
    DetecteurBakrApp().run()
