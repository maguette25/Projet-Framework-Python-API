#======= Les Importations =============================

from fastapi import FastAPI

import json
#==================== initialisation de l'application ==================================

app = FastAPI()

@app.get("/")
def Accueil ():
    return ("API creer avec succes !!! ")

#========================= Recuperation de la liste des etudiants par json ====================

@app.get("/ListeEtudiantValide")
def ListeEtudiantValide(): 
    chemin_fichier = '../Donnees/Fichier_Propre.json'

    #essaie d'ouvrir le fichier
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            # json.load() convertit le fichier JSON en dictionnaire ou liste Python
            donnees = json.load(fichier)
        
        print("Le fichier JSON a été chargé avec succès !")
        print(donnees)

    # l'exception si le chemin du fichier est introuvable
    except FileNotFoundError:
        return(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
    
    # l'exception si le fichier n'est pas valide
    except json.JSONDecodeError:
        return("Erreur : Le fichier n'est pas un JSON valide.")

    return donnees