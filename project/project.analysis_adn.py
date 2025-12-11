# chef de projet :abdeldjelil samira ikram ,Master 1 Microbiologie et contrôle de Qualité ,11/12/2025
# liste de  membres :
# tahraoui hanene
# dib merwa
# belamri merwa
# messaoudi fatima 
# dali youcef ines

import pandas as pd

# Données : Séquences ADN, Longueur , Pourcentage de GC
data = {
    "Séquence":["ATGCGTACGTA","GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"]
    "Longueur": [11, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}
1# Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)
print("**************** Creattion et affichage ****************,"\n")
      
# Affichage du tableau
print("Tableau des séquences ADN :", "\n")
print(df, "\n" "\n")

# Opérations sur les tableaux:
print("************** Opérations **************","\n")

#1) sélectionner la colonne "longueur"
longueurs = df["longueur"]
print(longueurs,"\n")

#3)Filtrage dont la longueur est supérieure à 10
print("************* Filtrage avec la longueur *************","\n")

filtered_df = df[df["longueur de séquence"] > 10] 
print(filtered_df,"\n") 
