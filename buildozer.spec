[app]
# (str) Titre de ton application de prospection
title = Bakr Scanner

# (str) Nom du package (sans espaces)
package.name = bakrscanner

# (str) Domaine de l'organisation
package.domain = org.bakr

# (str) Source des fichiers (le dossier courant)
source.dir = .

# (str) Extensions de fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas

# (str) Version de l'application
version = 1.0

# (list) Dépendances de l'application (Kivy est obligatoire)
requirements = python3,kivy,numpy

# (str) Orientation (Portrait est idéal sur le terrain pour le Redmi 12)
orientation = portrait

# (bool) Indique si l'application doit s'exécuter en plein écran
fullscreen = 1

# (list) Permissions Android nécessaires pour les futurs capteurs (GPS/Stockage)
android.permissions = ACCESS_FINE_LOCATION, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) API Android cible
android.api = 33

# (int) API Android minimale
android.minapi = 21

# (str) Format de build (Sert à générer un APK directement)
android.build_mode = debug
