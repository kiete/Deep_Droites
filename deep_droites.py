from random import *
from math import *
#voici la liste de points utilisee pour les essai
# la droite sera de la forme ax+b, nous nous attendrons à obtenir a=0 et b=2
# en pratique avec 100 générations à 20 de populations nous obtenons
# a = 0.0044 et b = 1.9937
points = list()
points.append([1,2])
points.append([2,2])
def distance (point , droite):
    #Nous allons calculer la distance point/droite
    a=droite[0]
    b=-1
    c=droite[1]
    x=point[0]
    y=point[1]
    #d = abs(int(droite[0])*int(point[0])+int(droite[1])-int(point[1]))/sqrt(int(droite[0])*int(droite[0])+1)
    d= abs(a*x+b*y+c)/sqrt(a*a+b*b)
    return d
def generateur_random1 (n,delta,population):
    # Nous allons generer des valeurs entre 0 et 1
    # Puis nous allons nous debrouiller pour que chaque coef de la droite de type ax+b ressorte
    # De la forme (a+r1)x+b+r2 avec -0.5<ri,r2<0.5
    liste_val = []
    while len(liste_val)<population:
        a = random()+n-0.5
        if (a<(n+delta) and (a>(n-delta))):
            liste_val.append (a)
    return liste_val
def test_droites(droite,points,population,afficher=False):
    #la droite est de la forme ax+b
    # l'argument droite est la meilleure droite generee du lancement precedent
    liste_a_tester = list()
    a,b= droite[0] , droite[1]
    best_distance=0
    for i in points:
        best_distance += distance(i , droite)
    #on genere une liste de a et une liste de b alternatifs
    liste_a = generateur_random1(a,0.2,population)
    liste_b = generateur_random1(b,0.2,population)
    best_a = droite[0]
    best_b = droite[1]
    for i in range (population):
        # on assemble la liste de a et de b pour creer des droites alternatives
        ax = liste_a[i]
        bx = liste_b[i]
        d=0
        for j in points :
            # on somme la distance entre la droite et l'ensemble des points
            d += distance(j,[ax,bx])
        if d < best_distance:
            # Si la droite est meilleure, elle deviens la best droite
            best_distance = d
            best_a = ax
            best_b = bx
    if afficher:
        print(best_distance)
    return [best_a,best_b]
def evolution (points , nb_evolutions , population,afficher = False):
    # on definit un best provisiore avec la droite d'equation de base y=x
    best = test_droites([1,0],points,population,afficher)
    nb = nb_evolutions
    for i in range(nb_evolutions):
        # on reinjecte le meilleur dans la fonction de test pour lui en generer un sous groupe
        best = test_droites(best,points,population,afficher)
    return best
#print distance([1,2],[0.8371403011347871,-0.09884969223291107]) 
#print distance([2,-5],[-0.5,0.5]) 
# on peut rajouter l'argument True a la fonction evolution pour qu'elle affiche la distance entre point et droite
print(evolution(points, 100,20,True))