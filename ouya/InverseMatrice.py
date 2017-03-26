#!/usr/bin/env python
import os
def ligneColonne() :
    ligne  = input("Saisir le nombre de lignes ")
    colonne = input("Saisir le nombre de colonnes")
    return int(ligne) , int(colonne)
def saisir(matrice,ligne,colonne):
    i,j=0,0
    while i<ligne :
       matcol = list()
       while j<colonne :
        print("     Saisir Matrice[{},{}]".format(i+1,j+1))
        entree=input()
        matcol.append(int(entree))
        j= j+ 1
       matrice.append(matcol)
       i=i+1
       j=0
        
    return matrice
def identite(identite,ligne,colonne) :
    i,j=0,0
    while i<ligne :
        matligne = list()
        while j <colonne :
            if i==j :
                matligne.append(1)
            else :
                matligne.append(0)
            j=j+1
        identite.append(matligne)
        i=i+1
        j=0
    return identite
def recherchePivot(matrice,k,ligne) :
    i=k
    while i < ligne:
        if matrice[i][k]!= 0 :
            return i
        i=i+1
    return -1
def remonte(matrice,matId,ligne, colonne ) :
    pivot,i=0,0
    while pivot<ligne :
        b=matrice[pivot][pivot]
        while i<colonne:
            a=matrice[pivot][i]
            d=matId[pivot][i]
            matrice[pivot][i]= float(a) / float(b)
            matId[pivot][i]= float(d) / float(b)
            matId[pivot][i]=format(matId[pivot][i],'.2f')
            i+=1
        pivot+=1
        i=0
    return matrice,matId
def permutation(matrice,matId,k,pivot) :
    mat=list()
    mat.append(matrice[k])
    matrice[k] = matrice[pivot]
    matrice[pivot]= mat[0]
    mat=list()
    mat.append(matId[k])
    matId[k] = matId[pivot]
    matId[pivot] =  mat[0]
    return matrice,matId
def elimination(matrice,identite,pivot,ligne,colonne ) :
    i=0
    while i < ligne :
       j=0
       if i!=pivot and matrice[i][pivot]!=0 :
           a=float(matrice[i][pivot])/float(matrice[pivot][pivot])
           while j < colonne:
                matrice[i][j]= matrice[i][j] - (matrice[pivot][j]*a)
                identite[i][j]= identite[i][j] - (identite[pivot][j]* a)
                j+=1
       i=i+1
    return matrice,identite

#partie principale 
matrice= list()
ligne,colonne =ligneColonne()
print("            Matrice ")
matrice  =saisir(matrice, ligne,colonne)
matriceIdentite = list()
matriceIdentite =identite(matriceIdentite,ligne,colonne)
k=0
arret = 1
while k<ligne and arret == 1 :
    pivot=recherchePivot(matrice,k,ligne)
    if pivot==k :
        matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
        k=k+1
    else :
        if pivot==-1 :
            arret = 0
        else :
            matrice,matriceIdentite = permutation(matrice,matriceIdentite,k,pivot)
            pivot = k
            matrice,matriceIdentite =elimination(matrice,matriceIdentite,pivot,ligne,colonne)
            k=k+1
if arret==1 and matrice[ligne-1][colonne-1]!=0 :
    matrice,matriceIdentite = remonte(matrice,matriceIdentite,ligne,colonne)
    for element in matriceIdentite:
        print("         {}".format(element))
else :
    print("Pas de solution unique")
os. system (" pause ")
