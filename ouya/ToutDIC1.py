###################################################################
##################################################Premier Semestre
#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""Fonction qui cree une matrice carrée et linitialise a la matrice nulle"""
def CreeMatCar(n):
	return [ [0.0 for j in range(0,n)] for i in range(0,n) ]

"""Fonction qui cree une matrice identite"""
def CreeMatId(n):
	I=CreeMatCar(n)
	for i in range(0,n):
		I[i][i]=1.0
	return I

"""Fonction qui remplit une matrice"""
def FillMat(M):
	print("Donnez les éléments de votre matrice")
	i=0
	while i<len(M):
		print("Elements de la ",i+1," eme ligne")	
		j=0
		while j< len(M):
			M[i][j]=float(input("element "+str(j+1)+": "))
			j+=1
		i+=1

"""Fonction qui copie une matrice ds une autre matrice"""
def CopyMatr(A):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			B[i][j]=A[i][j]
	return B



"""Fonction qui calcule le produit de deux matrices"""
def ProdMat(A,B):
	n=len(A)
	AB=CreeMatCar(n)           #initialisation de AB que la fonction va renvoyer
	for i in range(0,n):              #Parcours des lignes
		for j in range(0,n):    #Parcours des colonnes
			AB[i][j]=0   #Initialisation de AB[i][j]
			for k in range(0,n):     ): #Variable k qui va nous permettre de fai#Variable k qui va nous permettre de faire la somme des lignes et des colonnesre la somme des lignes et des colonnes
				AB[i][j]+=(A[i][k])*(B[k][j])
	return AB	

"""Fonction qui permute deux colonnes d une matrice"""
def PermCol(M,j,i):
	for k in range(len(M)-1,-1,-1):
		(M[k][j],M[k][i])=(M[k][i],M[k][j])

"""Fonction qui calcule la difference A- aI"""
def DiffMatI(A,a):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			if i!=j:
				B[i][j]=A[i][j]
			else:
				B[i][j]=A[i][j]-float(a)
	return B

"""Fonction qui calcule la somme des diagonales"""
def Trace(A):
	n=len(A)
	t=0
	for j in range(0,n):
		t+= A[j][j]
	return t
			
"""Fonction qui calcule le produit des diagonales"""
def ProdDiag(M):
	j=0
	p=1
	while j<len(M):			
		p=p*M[j][j]
		j+=1	
	return p

"""Fonction qui triangule une matrice carre--triangulaire supérieure--"""
def Triangule(M):
	sign=1
	n=len(M) -1
	for i in range(n,0,-1):#A partir de  la derniere jusqua la 2eme ligne 
		for j in range(0,i):#Mij=0 si j<i
			if M[i][j+1] !=0.0:#Si c'est nulle, jai qu'a faire une permutation pour avoir 0
				q=(M[i][j])/(M[i][j+1]) 
				if q!=0.0:#Si c'est nulle, pas besoin de le rendre nulle
					for k in range(n,-1,-1):#A chaque combinaison, c'est les éléments de toute la colonne qui doivent changer
						M[k][j]= M[k][j] - q*M[k][j+1]
			else:
				PermCol(M,j+1,j)
				sign=sign*(-1)#le determinant est multipli par -1 si on permute deux colonnes de la matrice
	return M,sign

"""Fonction qui calcule le determinant une matrice carre"""
def Determinant(M):
	(Mtriang,sign)=Triangule(M)
	return round(sign*ProdDiag(Mtriang),2)


"""Fonction qui calcule les+ coefficients du polynome caracteristique"""				
def PolyCarac(A):
	n=len(A)
	l=list()
	if n%2==0:
		l.append(1)
	else:
		l.append(-1)
	Bi=CreeMatId(n)
	for i in range(1,n+1):
		Ai=ProdMat(A,Bi)
		a=round((1/i)*Trace(Ai),2)
		if i != n:
			l.append(a)
		Bi=DiffMatI(Ai,a)
		
	return l

"""Fonction qui met dans une chaine le polynome caracteristique"""
def ChaiPoly(l,n):
	car="?^"
	chai=" "
	i=n
	for el in l:
		if el<0:
			if i==n:
				chai= chai + " "+str(el) +car +str(i)			
			if i>1 and i<n:	
				chai= chai+ " " +str(el) +car +str(i)
			if i==1:
				chai= chai +" " + str(el) + "?  "
			if i==0:
				chai=chai +" " + str(el)
		if el>0:
			if i==n:
				chai= chai + str(el) +car +str(i)			
			if i>1 and i<n:		
				chai= chai+ "+  " + str(el) +car +str(i) 
			if i==1:
				chai= chai + "+  "+ str(el) + "? "
			if i==0:
				chai=chai + "+  " +str(el)
		i-=1
	return chai

def ChaiPolyWakh(l,n):
	car="t à la puissance"
	chai=" "
	i=n
	for el in l:
		if el<0:
			if i==n:
				chai= chai + "moins "+str(el) +car +str(i)			
			if i>1 and i<n:	
				chai= chai+ "moins " +str(el) +car +str(i)
			if i==1:
				chai= chai +" moins" + str(el) + "t  "
			if i==0:
				chai=chai +"moins " + str(el)
		if el>0:
			if i==n:
				chai= chai + str(el) +car +str(i)			
			if i>1 and i<n:		
				chai= chai+ "+  " + str(el) +car +str(i) 
			if i==1:
				chai= chai + "+  "+ str(el) + "t "
			if i==0:
				chai=chai + "+  " +str(el)
		i-=1
	return chai		

###################################################################
###################################################deuxieme Semestre
import math as m
import time
from basicFunctions import *
n=0

#############################################
#Fonctions pour la resolution par Gauss
def recherchepivot(k,A):
	i=k
	while i!=n and A[i][k]==0:
		i+=1
	if i!=n:
		return i
	else:
		return -1


def permutation(i0,i,A,b):
    A[i],A[i0] = A[i0],A[i]
    b[i],b[i0] = b[i0],b[i]
    return A,b

def elimination(k,A,b):
	i=k+1
	while i < n:
		r = A[i][k]/A[k][k]
		b[i] -= r*b[k]
		j=k
		while j < n:
			A[i][j]= round(A[i][j] - r*A[k][j],2)
			j+=1
		i+=1
	return A,b

def remonte(A,b):
	x = CreerListe(n)        
	x[n-1] = round(b[n-1]/A[n-1][n-1],3)
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= A[i][j]*x[j]
		x[i]/=A[i][i]
		x[i]=round(x[i],3)
	return x


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


##########################################################
#Fonctions pour la resolution par LU
def eliminationLU(k,A):
	i=k+1
	while i < n:
		r = A[i][k]/A[k][k]
		j=k
		while j < n:
			A[i][j] -= r*A[k][j]
			A[i][j]=round(A[i][j],2)
			j+=1
		i+=1
	return A

def descente(L,b):
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= L[i][j]*y[j]
	return y


#mm remonte que Gauss
"""def remonte(A,b):
	n=len(A)
	x = CreerListe(n)       
	x[n-1] = b[n-1]/A[n-1][n-1]
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= A[i][j]*x[j]
		x[i]/=A[i][i]
	return x"""


def factLU(A):
	global n
	n=len(A)
	k=0
	arret=0
	L=CreeMatCar(n)
	while k!=n and arret!=1:
		L[k][k]=1
		if A[k][k] !=0:
			for i in range(k+1,n):
				L[i][k]=round(A[i][k]/A[k][k],2)
			A=eliminationLU(k,A)
			k+=1
		else:
			arret=1
	if arret==0 and A[n-1][n-1]!=0:
		return L
	else:
		print("Les conditions ne sont pas reunies")
		return 0

def solveSystLU(A,b):
	t1=time.time()
	L=factLU(A)
	if L!=0:
		y=descente(L,b)
		x=remonte(A,y)
		t2=time.time()
		t=t2-t1
		#print("La solution de votre systeme est \n",x)
		return x,L,t*1000000
	else:
		#print("Ce systeme ne peut pas etre resolu par la methode LU")
		return 0



####################################################################
#Fonctions Pour la resolution par Cholesky
def factCholesky(A):
	n=len(A)
	B=CreeMatCar(n)
	for j in range(n):
		B[j][j]=A[j][j]
		for k in range(j):
			B[j][j] -=B[j][k]*B[j][k]
		B[j][j]= round(m.sqrt(B[j][j]),2)
		for i in range(j+1,n):
			B[i][j]=A[i][j]
			for k in range(j):
				B[i][j]-=B[i][k]*B[j][k]
			B[i][j]=round(B[i][j]/B[j][j],2)
	return B

def descenteChol(L,b):
	n=len(L)
	y = CreerListe(n)        
	for i in range(n):
		y[i] = b[i] 
		for j in range(i):
			y[i] -= L[i][j]*y[j]
		y[i]/=L[i][i]
	return y



def remonteChol(B,b):
	n=len(B)
	x = CreerListe(n)       
	x[n-1] = round(b[n-1]/B[n-1][n-1],3)
	for i in range(n-2,-1,-1):
		x[i] = b[i]
		for j in range(i+1,n):
			x[i] -= B[j][i]*x[j]
		x[i]/=B[i][i]
		x[i]=round(x[i],3)
	return x

def solveSystCholesky(A,b):
	t1=time.time()
	B=factCholesky(A)
	y=descenteChol(B,b)
	x=remonteChol(B,y)
	t2=time.time()
	t=t2-t1
	print(x)
	#return x,B,t*1000000
	
#######################################################
##########################Fonction BasicFunction
import time

"""def playError():
		pygame.init()
		son = pygame.mixer.Sound("error.wav")
		son.play()
		time.sleep(1)
		son.stop()"""

#Fonctions de creation de matrices nulles et vecteurs nuls
def CreeMatCar(n):
	return [ [0.0 for j in range(n)] for i in range(n) ]

def CreerListe(n):
	return [0.0 for i in range(n)]

#Fonction qui copie une matrice ds une autre matrice
def CopyMatr(A):
	n=len(A)
	B=CreeMatCar(n)
	for i in range(0,n):
		for j in range(0,n):
			B[i][j]=A[i][j]
	return B

#Fonction qui copie un vecteurdans un autre vecteur
def CopyVec(b):
	n=len(b)
	v=list()
	for j in range(n):
		v.append(b[j])	
	return v


#Fonction qui teste si un caracter est un nombre 0 1....9"""
def estNombre(carac):
	if carac in ("0","1","2","3","4","5","6","7","8","9"):
		return 1
	else :
		return 0


#Fonction qui teste si dans une chaine il y a autre caractere k un nombre----#ex "az122" return 1 et "1255" return 0
def pasJustqDnbres(chaine):
	for i in range(len(chaine)):
		if i==0:
			if estNombre(chaine[i])==0 and chaine[i] !="-":
				return 1
		else:
			if estNombre(chaine[i])==0:
				return 1
	return 0


print(pasJustqDnbres("-25"))

##################################################################
############################Methode iterative
#!/usr/bin/python3
# -*-coding:Utf-8 -*
from foncNeed import *

"""Resous un systeme avec la methode de gradient"""
def SolveSystIterGrad(A,b,x,err):
	n=len(A)
	r=SomVect(b,ProdVectNbre(-1,ImVect(A,x)))
	d=r
	while NormeVect(r)>err:
		ad=ImVect(A,d)
		t=ProdScal(r,d)/ProdScal(ad,d)
		x=SomVect(x,ProdVectNbre(t,d))
		r=SomVect(r,ProdVectNbre(-t,ad))
		d=r
	for i in range(n):
		x[i]=round(x[i],2)
	return x

"""Resous un systeme avec la methode de gradient conjugue"""
def SolveSystIterGradConj(A,b,x,err):
	r=SomVect(b,ProdVectNbre(-1,ImVect(A,x)))
	d=r
	rp=r
	while NormeVect(r)>err:
		ad=ImVect(A,d)
		t=ProdScal(r,d)/ProdScal(ad,d)
		x=SomVect(x,ProdVectNbre(t,d))
		r=SomVect(r,ProdVectNbre(-t,ad))
		d=SomVect(r,ProdVectNbre((NormeVect(r)/NormeVect(rp)),d))
		rp=r
	return x

"""Test
A=[[2.0,-1.0,0.0],[-1.0,2.0,-1.0],[0.0,-1.0,2.0]]
b=[1.0,0.0,0.0]
x=[0.0,0.0,0.0]
err=1.0E-15
x=SolveSystIterGrad(A,b,x,err)
print(x)"""

###########################################################################
##################Contenu du fichier FonctionNeed
"""Fonction qui cree une matrice carrée et linitialise a la matrice nulle"""
def CreeMatCar(n):
	return [ [0.0 for j in range(0,n)] for i in range(0,n) ]

"""Fonction qui cree un vecteur et linitialise a 0"""
def CreerVect(n):
	return [0.0 for i in range(n)]

"""Fonction qui calcule l'image d'un vecteur par une matrice"""
def ImVect(A,d):
	n=len(A)
	r= CreerVect(n)
	for i in range(n):
		r[i]=0
		for j in range(n):
			r[i] +=A[i][j]*d[j]
	return r

"""Fonction qui calcule la somme de deux vecteurs"""
def SomVect(a,b):
	n=len(a)
	return [ a[i]+b[i] for i in range(n)]

"""Fonction qui calcule le produit scalaire de deux vecteurs"""
def ProdScal(a,b):
	n=len(a)
	r=0
	for i in range(n):
		r+=a[i]*b[i]
	return r

"""FOnction qui calcule le produit d'un nbre et d'un vecteur"""
def ProdVectNbre(nb,v):
	n=len(v)
	return [nb*v[i] for i in range(n)]

"""Focntion qui calcule la norme au carre d'un vecteur"""
def NormeVect(v):
	n=len(v)
	r=0
	for i in range(n):
		r+=v[i]*v[i]
	return r