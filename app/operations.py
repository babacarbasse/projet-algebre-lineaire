#!/usr/bin/env python
# coding=utf-8
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
       if i!=pivot and matrice[i][pivot] != 0 :
           a=float(matrice[i][pivot])/float(matrice[pivot][pivot])
           while j < colonne:
                matrice[i][j]= matrice[i][j] - (matrice[pivot][j]*a)
                identite[i][j]= identite[i][j] - (identite[pivot][j]* a)
                j+=1
       i=i+1
    return matrice,identite
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
def inverser(matrice,ligne,colonne):
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
    else :
            matriceIdentite.append(-1) 
    return matriceIdentite
def addition(mat1,mat2):
    resultat = list()
    for i in range(len(mat1)):
        colonne = list()
        for j in range(len(mat1[0])):
            colonne.append(mat1[i][j]+mat2[i][j])
        resultat.append(colonne)
    return  resultat
def multiplier(mat1,mat2):
    resultat = list()
    for i in range(len(mat1)):
        ligne = list()
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat1[0])):
                element= element+ mat1[i][k]*mat2[k][j]
            ligne.append(element)
        resultat.append(ligne)
    return resultat

def solveSystGauss(A,b):
	global n
	n=len(A)
	t1=time.time()
	k = 0
	arret = 0
	while k!=n and arret!=1:
		i0 = recherchepivot(k,A)
		if i0 == -1:
			arret = 1
		else:
			if i0 == k:
				A,b = elimination(k,A,b)
				k+=1
			else: 
				A,b = permutation(i0,k,A,b)
				A,b = elimination(k,A,b)
				k+=1
	if k==n and A[n-1][n-1]!=0:
		# equation solutions
		x = remonte(A,b)  
		t2=time.time()
		t=t2-t1
		return x,t*1000000
	else:
		# no unique solution
		#print("Ce systeme n'admet pas de solution unique")
		return 0