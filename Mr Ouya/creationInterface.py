#!/usr/bin/env python
# coding=utf-8
from PIL import Image, ImageTk
import PIL
import os
from Tkinter import *
from tkMessageBox import *
import Tkinter
import tkMessageBox
import numpy as np
import pygame
from pygame.locals import *
#Initialisation
pygame.mixer.init()
global playSound
from operations import *
playSound = True

def creation() :
    pygame.mixer.music.load("sonbutton.mp3")
    if playSound == True : 
        pygame.mixer.music.play()
    fenetre = Tk()
    fenetre.geometry('1400x800')
    fenetre.title('Fenetre Principale')
    fenetre.configure(background='navajo white')
    sbar = Scrollbar(fenetre)
    image = PIL.Image.open("bannerESP.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo, width=650, height=75)
    label.image = photo # keep a reference!
    label.pack()

    image = PIL.Image.open("moi.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo, width=150, height=150)
    label.image = photo # keep a reference!
    label.pack(pady = 5)

    button_frame = Frame(fenetre)
    button_frame.pack()

    reset_button = Button(button_frame, text='Couper son', command=lambda: changeSound(2))
    run_button = Button(button_frame, text='Jouer son', command=lambda: changeSound(1))
    
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    reset_button.grid(row=0, column=0)
    run_button.grid(row=0, column=1)

    HelpButton = Button(fenetre, text= 'Help', width=5 , bg='green',height='0',font="arial 10 bold",command=lambda:showHelp(1)).pack()

    add = Button(fenetre, text= ' Addition', width=50 , bg='gray',height='2',font="arial 16 bold",command=lambda:saisieLigneColonne(1)).pack(pady = 10)
    multi= Button(fenetre, text= ' Multiplication', width=50 , bg='gray',height='2',font="arial 16 bold",command=lambda:saisieLigneColonne(2)).pack(pady = 10)
    inverse= Button(fenetre, text= ' Inverse', width=50 , bg='gray',height='2',font="arial 16 bold",command=lambda:saisieLigneColonne(4)).pack(pady = 10)
    resoluSyst = Button(fenetre, text=' Résolution systeme lineaire', width=50, bg='gray', height='2', font="arial 16 bold",
                     command=lambda: saisieLigneColonne(6)).pack(pady=10)
    fermer = Button(fenetre, text=' Quitter', width=25, bg='green', height='1', font="arial 16 bold",
                     command=lambda: exit()).pack(pady=5)
    return fenetre

    
def create_matrice(fenetre,ligne ,colonne,ligne2, colonne2,resButton,choix) :
   pygame.mixer.music.load("soundSolution.mp3")
   if playSound == True : 
        pygame.mixer.music.play()
   i=0
   try :
        resButton.configure(state=DISABLED)
        global resultatFrame
        while i<ligne:
            j=0
            matcol=list()
            while j<colonne :
                matcol.append(float(matcell1[i][j].get()))
                j+=1
            matrice1.append(matcol)
            i+=1
        i=0
        if choix==1 or choix==2 or choix == 6 :
            while i<ligne2:
                j=0 ;
                matcol2=list()
                while j<colonne2 :
                    matcol2.append(float(matcell2[i][j].get()))
                    j+=1
                matrice2.append(matcol2)
                i+=1
        if choix==1 :
            resultat=addition(matrice1,matrice2)
        if choix==2 :
                    resultat=multiplier(matrice1,matrice2)
        if choix==4 :
                    resultat=inverser(matrice1,ligne,colonne)
        if choix==6:
                    listR = []
                    for item in matrice2:
                        listR.append(item[0])
                    a = np.array(matrice1)
                    b = np.array(listR)
                    resultat = np.linalg.solve(a, b)
        if choix==6:
            resultatFrame = Frame(fenetre, padx=40, pady=40, bg='black')
            for i in range(len(resultat)):
                ligneText = StringVar()
                ligneText.set("{}".format(resultat[i]))
                ligneLabel = Label(resultatFrame, textvariable=ligneText, width=20, height=2, bg='gold',
                                   font="arial 12 bold", borderwidth=5)
                ligneLabel.grid(row=i)
        else:
            resultatFrame=Frame(fenetre,padx=40,pady=40,bg='black')
            for i in range(len(resultat)):
                for j in range(len(resultat[0])):
                        ligneText=StringVar()
                        ligneText.set("{}".format(resultat[i][j]))
                        ligneLabel=Label(resultatFrame,textvariable=ligneText, width=20,height= 2, bg='gold',font="arial 12 bold",borderwidth=5)
                        ligneLabel.grid(row=i,column=j)
        resultatFrame.pack(anchor="center")
   except:
       if choix == 6 :
           resultatFrame = Frame(fenetre, padx=40, pady=40, bg='black')
           ligneText = StringVar()
           ligneText.set("Pas de solution.")
           ligneLabel = Label(resultatFrame, textvariable=ligneText, width=20, height=2, bg='gold',
                              font="arial 12 bold", borderwidth=5)
           ligneLabel.grid(row=1, column=1)
           resultatFrame.pack(anchor="center")
       else:
            showerror("Erreur matrice", "Les elements des matrices ne sont pas correctement remplis. Veuillez reinitialiser et recommencer")
        
    
def changeSound(choix) :
    global playSound
    if choix == 1 :
        playSound = True
    else :
        playSound = False

def saisie(matriceFrame1,fenetre,ligne, colonne,colonneMat2,choix,reinit,add):
  pygame.mixer.music.load("sonbutton.mp3")
  if playSound == True : 
    pygame.mixer.music.play()
  try :
    ligne=int(ligne)
    colonne=int(colonne)
    ligne2=ligne
    colonne2= colonne
    if choix ==2 :
        ligne2=colonne
        colonne2 = int(colonneMat2)
    if choix == 6:
        ligne2=ligne
        colonne2= 1
    matriceFrame1.pack(anchor="nw")
    for i in range(ligne):
        matcol=list()
        for j in range(colonne):
            p=Entry(matriceFrame1,background="black",width=30, foreground="gold")
            p.insert(0,'Mat[%s-%s]' % (i,j))
            p.grid(row=i,column=j)
            matcol.append(p)
        matcell1.append(matcol)
    resButton=Button(matriceFrame1,text='Resultat',bg='red',font="arial",command=lambda:create_matrice(fenetre,ligne,colonne,ligne2,colonne2,resButton,choix))
    if ligne>=ligne2 :
        i = ligne-1
    else :
        i=ligne2-1
    resButton.grid(row=i/2,column=colonne+1,rowspan=colonne+1,columnspan=2)
    if choix == 1 or choix==2 :
        for i in range(ligne2):
            matcol=list()
            for j in range(colonne2):
                p=Entry(matriceFrame1,background="black",width=30,foreground="gold")
                p.insert(0,'Mat2[%s-%s]' % (i,j))
                p.grid(row=i,column=j+colonne+4)
                matcol.append(p)
            matcell2.append(matcol)
    if choix == 6 :
        for i in range(ligne2):
            matcol=list()
            for j in range(colonne2):
                p=Entry(matriceFrame1,background="black",width=30,foreground="gold")
                p.insert(0,'Vect[%s]' % (i))
                p.grid(row=i,column=j+colonne+4)
                matcol.append(p)
            matcell2.append(matcol)
    reinit.configure(state=NORMAL)
    add.configure(state=DISABLED)
  except :
    showerror("Erreur Saisie ligne/colonne", "Les valeurs saisies sont incorrectes. Veuillez entrer des entiers")

def reinitialiser(fenetre_addition,add,reinit) :
    pygame.mixer.music.load("sonbutton.mp3")
    if playSound == True : 
        pygame.mixer.music.play()
    global matriceFrame1
    global matrice1
    global matrice2
    global matcell1
    global matcell2
    matriceFrame1.destroy()
    matriceFrame1=Frame(fenetre_addition ,bg="gold",padx=0)
    add.configure(state=NORMAL)
    reinit.configure(state=DISABLED)
    resultatFrame.destroy()
    matrice1= list()
    matrice2=list()
    matcell1 =list()
    matcell2=list()
    
def saisieLigneColonne(choix):
    pygame.mixer.music.load("sonbutton.mp3")
    if playSound == True : 
        pygame.mixer.music.play()
    global matriceFrame1
    fenetre.withdraw()
    fenetre_addition=Toplevel(fenetre, bg='black')
    fenetre_addition.geometry('1400x800')
    fenetre_ligne_col= Frame(fenetre_addition, borderwidth=0,background='black')
    fenetre_ligne_col.pack(anchor="nw")
    matriceFrame1= Frame(fenetre_addition ,bg="black",padx=0)
    matriceFrame1.pack(anchor="nw")  
    lignecolonneValeur=list()
    if choix==1 or choix==3:
        ligneText=StringVar()
        ligneText.set("Nombre de lignes :")
        ligneLabel=Label(fenetre_ligne_col,textvariable=ligneText, width=20,height= 2, bg='gold',font="arial 8 bold")
        ligneLabel.pack(side="left" ,  fill=X)   
        ligneEntry=Entry(fenetre_ligne_col,width=14)
        ligneEntry.pack(side="left",padx=10, fill=X)
        colText=StringVar()
        colText.set("Nombre de colonnes :")
        colLabel=Label(fenetre_ligne_col, textvariable=colText,  width=20,height= 2, bg='gold',font="arial 8 bold")
        colLabel.pack(side="left", fill=X)   
        colEntry=Entry(fenetre_ligne_col,width=14)
        colEntry.pack(side="left", padx=10, fill=X)
        add = Button(fenetre_ligne_col, text= 'OK', width=10 , bg='green',height='2',font="arial 9 bold",command=  lambda: saisie( matriceFrame1,fenetre_addition,ligneEntry.get(),colEntry.get(),"0",choix,reinit,add))    
    if choix==4:
        ligneText=StringVar()
        ligneText.set("Nombre de lignes / Colonnes :")
        ligneLabel=Label(fenetre_ligne_col,textvariable=ligneText, width=20,height= 2, bg='gold',font="arial 8 bold")
        ligneLabel.pack(side="left" ,  fill=X)   
        ligneEntry=Entry(fenetre_ligne_col,width=14)
        ligneEntry.pack(side="left",padx=10, fill=X)
        add = Button(fenetre_ligne_col, text= 'OK', width=10 , bg='green',height='2',font="arial 9 bold",command=  lambda: saisie( matriceFrame1,fenetre_addition,ligneEntry.get(),ligneEntry.get(),"0",choix,reinit,add))    
    if choix==2 :
        ligneText=StringVar()
        ligneText.set("Nombre de lignes matrice1 :")
        ligneLabel=Label(fenetre_ligne_col,textvariable=ligneText, height= 2, bg='gold',font="arial 8 bold")
        ligneLabel.pack(side="left" ,  fill=X)   
        ligneEntry=Entry(fenetre_ligne_col,width=14)
        ligneEntry.pack(side="left",padx=10, fill=X)
        colText=StringVar()
        colText.set("Nombre de colonnes  matrice1/Nombre de lignes matrice2:")
        colLabel=Label(fenetre_ligne_col, textvariable=colText,height= 2, bg='gold',font="arial 8 bold")
        colLabel.pack(side="left", fill=X)   
        colEntry=Entry(fenetre_ligne_col,width=14)
        colEntry.pack(side="left", padx=10, fill=X)
        ligneText2=StringVar()
        ligneText2.set("Nombre de colonnes matrice2 :")
        ligneLabel2=Label(fenetre_ligne_col,textvariable=ligneText2,height= 2, bg='gold',font="arial 8 bold")
        ligneLabel2.pack(side="left" ,  fill=X)   
        ligneEntry2=Entry(fenetre_ligne_col,width=14)
        ligneEntry2.pack(side="left",padx=10, fill=X)
        add = Button(fenetre_ligne_col, text= 'OK', width=20 , bg='green',height='2',font="arial 9 bold",command=  lambda: saisie( matriceFrame1,fenetre_addition,ligneEntry.get(),colEntry.get(),ligneEntry2.get(),choix,reinit,add))
    if choix==6 :
        ligneText = StringVar()
        ligneText.set("Nombre de lignes matrice / Nombre de lignes vecteur :")
        ligneLabel = Label(fenetre_ligne_col, textvariable=ligneText, height=2, bg='gold', font="arial 8 bold")
        ligneLabel.pack(side="left", fill=X)
        ligneEntry = Entry(fenetre_ligne_col, width=14)
        ligneEntry.pack(side="left", padx=10, fill=X)
        colText = StringVar()
        colText.set("Nombre de colonnes  matrice")
        colLabel = Label(fenetre_ligne_col, textvariable=colText, height=2, bg='gold', font="arial 8 bold")
        colLabel.pack(side="left", fill=X)
        colEntry = Entry(fenetre_ligne_col, width=14)
        colEntry.pack(side="left", padx=10, fill=X)
        add = Button(fenetre_ligne_col, text='OK', width=20, bg='green', height='2', font="arial 9 bold",
                     command=lambda: saisie(matriceFrame1, fenetre_addition, ligneEntry.get(), colEntry.get(),
                                            "0", choix, reinit, add))
    add.pack(pady = 10,side="left")
    reinit=Button(fenetre_ligne_col,text='Reinitialiser',width=20,bg='green',height='2',font="arial 9 bold",command=lambda:reinitialiser(fenetre_addition,add,reinit),state=DISABLED)
    reinit.pack(pady = 10,side="left")
    retour = Button(fenetre_ligne_col, text= 'Menu principal' , bg='green',height='2',font="arial 9 bold",command=lambda:retourMenuPrincipal(fenetre_addition))
    retour.pack(side="left")

def retourMenuPrincipal(fenetre_addition) :
    pygame.mixer.music.load("sonbutton.mp3")
    if playSound == True : 
        pygame.mixer.music.play()
    fenetre_addition.destroy()
    fenetre.deiconify()
    global matrice1
    global matrice2
    global matcell1
    global matcell2
    matrice1= list()
    matrice2=list()
    matcell1 =list()
    matcell2=list()

def showHelp(choice) :
    tkMessageBox.showinfo("Aide", "Ce programme vous permet de résoudre quelques opérations sur les matrices à savoir l'inverse d'une matrice, la resolution d'un système lineaire, l'addition et la multiplicatio de deux matrices. \n \n \t \t @copyright Babacar Niang")

def exit() :
    pygame.mixer.music.load("soundExit.mp3")
    if playSound == True : 
        pygame.mixer.music.play()
    if tkMessageBox.askyesno('Confirmer la fermeture','Êtes-vous sûr de vouloir quitter ?'):
        fenetre.destroy()


fenetre=creation()
matriceFrame1=Frame()
resultatFrame=Frame()
matrice1= list()
matrice2=list()
matcell1 =list()
matcell2=list()