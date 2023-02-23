# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 22:42:25 2022

@author: Lenovo
"""

liste=["Antananarivo","Fianarantsoa","Majunga","Tamatave"]
foko=["MERINA","BETSILEO","ANTANDROY","BETSIMISARAKA",""]
dicti={"nom":"RAKOTOARIMANANA","prenom":"Mamy Nirina"}
liste.append('Toliara')
liste.insert(2,'Diego')
print(liste)
if 'Antsirabe' in liste:
    print("Antsirabe est vraiment est dans la liste")
else:
    print("non")
"""couplage index,valeur de la liste"""  
print("couple de pair entre index et valeur de la liste avec la methode ENUMARATE:")  
for index,valeur in enumerate(liste):
    print(index,valeur )

print("couple de pair entre les valeurs de deux listes avec la methode ZIP:")
for k,v in zip(foko,liste):
    print(k,":",v)

"""list comprehension:code professionnel plus python"""
"""exemple de methode classique:C1"""
liste_1=[]
for i in range(10):
    liste_1.append(i**2)
print("le resultat de la methode classique est:",liste_1)

""" transformer C1 avec un code list comprehension"""
liste_2=[i**2 for i in range(10) if i<6]
print("le resultat de la list comprehension est: ",liste_2)

"""dict comprehension"""
liste_3={k:v for k,v in enumerate(liste)}
print("le resultat du dict comprehension est: ",liste_3)

""" transformer C1 avec un code tuple comprehension"""
liste_4=tuple(i**2 for i in range(10) if i<6)
print("le resultat du tuple(generateur) comprehension est: ",liste_4)


    