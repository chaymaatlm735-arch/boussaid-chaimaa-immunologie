#Boussaid Chaimaa M1 immunologie 08/12/2025
#Belkenadil Bouchra Sanaa Nesrine
#Kaid Ines Safia
#Djabeur Djezzar Djezia 
#Benameur Hidayat
#Hamzaoui Aroua 


import pandas as tb
import numpy as np
# Données : séquences ADN , Longueur , Pourcentage GC
data ={ 
    "Séquence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT"," TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
    "Longueur" :[12,12,12,10,11,10,10],
    "Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]   
}

# 1)Créer et afficher le tableau en utilisant la bibliothèque pandas:
# Création de tableau :
df= tb.DataFrame(data)
print("1 ********** Création et Affichage du tableau **********","\n""\n")

#Affichage de tableau :
print(df,"\n""\n")
# 2)a-Sélectionner  uniquement la colonne “Longueur”:
Longueur =df["Longueur"]
# 2)Afficher uniquement la colonne "Longueur":
print("2 ********** Affichage de la colonne longueur **********","\n""\n")
print(Longueur,"\n""\n")

# 3) Filtrer les séquences dont la longueur est > 10 :
print("3 ********** Filtrage dont la longueur est > 10 **********","\n""\n")
filtered_df = df[df["Longueur"] > 10]
print(filtered_df,"\n""\n")


#4) Calculer le pourcentage moyen de GC:
print("4 ********** Calcul de pourcentage moyen de GC **********","\n""\n")

average_gc = df["Pourcentage GC"].mean()
print(f"Le Pourcentage moyen de GC est: {average_gc:.3f}%")
print("\n")


# 5) Ajouter une colonne "Catégorie GC":
print("5 ********** Ajout d'une colonne 'Catégorie GC' **********","\n""\n")
conditions = [
    (df['Pourcentage GC'] >= 55),
    (df['Pourcentage GC'] >= 45) & (df['Pourcentage GC'] < 55),
    (df['Pourcentage GC'] < 45)
]
choix = ['Riche', 'Moyen', 'Faible']
df['categorie GC'] = np.select(conditions, choix, default='inconnu')
print(df,"\n""\n")


 # 6) Ajouter une colonne donnant le nombre de "G" dans chaque séquence:
print("6 ********** Ajout d'une colonne donnant le nombre de G **********","\n""\n")
df["Nombre de G"] = df["Séquence"].str.count("G")
print(df,"\n")


# 7) Calculer l‟écart-type du %GC et de la longueur des séquences:
print("7 ********* Calcul de l'écart-type du %GC & de la longueur *********","\n")
data = {
    "%GC": [50, 66.67, 58.33, 40, 45.45, 60, 50],
    "Longueur": [12, 12, 12, 10, 11, 10, 10]
}
écart_type_GC = df["Pourcentage GC"].std()
écart_type_long = df["Longueur"].std()

print("Écart-type du %GC est:", round(écart_type_GC,3))
print("Écart-type de la longueur des séquences est :", round(écart_type_long))
#(On écrit :.1f si l’on veut garder un seul chiffre après la virgule)
#(On écrit :.2f si l’on veut garder deux chiffre après la virgule)...


# 8) Sauvgarde et chargement des données avec panda:
df.to_csv("tableau_sequences.csv",inedx=False)

#8) Télécharger un fichier csv et l'importer dans un Dataframe:
df_loaded = tb.read_csv("tableau_sequences.csv")
print(df_loaded)
