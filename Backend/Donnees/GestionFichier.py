#=============== Les importations ================================

import pandas as pd

#================== Lire le fichier csv et le stocker ======================

fichier_propre = pd.read_csv('donnees_propres.csv')

#=============== Conversion du fichier en fichier json =============================

# recuperation pour une liste de dictionnaire 
fichier_propre.to_json("Fichier_Propre.json", orient="records", force_ascii=False, indent=4)

# recuperation pour une dictionnaire de dictionnaire
fichier_propre.to_json("Fichier_Propre_index.json", orient="index", force_ascii=False, indent=4)

