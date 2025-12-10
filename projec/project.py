#Boussaid chaimaa M1 immunologie 08/12/2025
#Belkenadil bouchra sanaa nesrine
#Kaid ines safia
#Djabeur djezzar djezia 
#Benameur hidayat
#Hamzaoui aroua 



import pandas as tb
# donnes : sequences ADN , Longeur , Pourcentage GC
data ={ 
    "sequence":["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT"," TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
    "Longeur" :[12,12,12,10,11,10,10],
    "Pourcentage GC":[50,66.67,58.33,40,45.45,60,50]   

}
#creation d un DataFrame (tableau pandas)
df= tb.DataFrame(data)
print("************** Creation et Affichage ***************","\n""\n")
#affichage de tableau 
print("Tableau des sequences ADN :", "\n")
print(df)
# afficher uniquement la Longeur 
Longeur =df["Longeur"]
print("********* longeur *********","\n")
print(Longeur,"\n")
# filtrer la longeur > 10 
print("********* Filtrage avec longeur >10 ********* ")
filtered_df = df[df["Longeur"]>10]
print(filtered_df)

#4Calculer la moyenne du pourcentage de GC
print("************* Calcul de la moyenne *************")
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%")


























#sauvgarder et chargement des donnes avec panda 
df.to_csv("tableau_sequences.csv",inedx=False)

#telecharger un fichier csv et mettre dans dataframe
df_loaded = tb.read_csv("tableau_sequences.csv")
print(df_loaded)
