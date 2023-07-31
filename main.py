from tkinter import *
import random

x_roz_canvas = 600
y_roz_canvas = 450
rozmiarpikseli = 10
szerokosc = int(x_roz_canvas/rozmiarpikseli)
wysokosc = int(y_roz_canvas/rozmiarpikseli)

def stworz_liste(szerokosc,wysokosc):
    lista = []
    for i in range(wysokosc):
        wiersz = []
        for j in range(szerokosc):
            wiersz.append(0)
        lista.append(wiersz)
    return lista

def losowa_lista():
    list = stworz_liste(szerokosc,wysokosc)
    for i in range(len(list)):
        for j in range(len(list[0])):
            liczba = random.uniform(0,1)
            if liczba<0.5:
                list[i][j] = 0
            else:
                list[i][j] = 1
    return list

poprzedni_stan1 = stworz_liste(szerokosc,wysokosc)

lista1 = losowa_lista()
def okno():
    root = Tk()
    root.geometry("600x500")
    root.title("Gra w życie")

    pole_gry = Canvas(root, height=y_roz_canvas, width=x_roz_canvas, bg="white")
    pole_gry.grid(row=1, column=0,columnspan = 3)

    pole_iteracji_wartosc = IntVar()
    pole_iteracji_wartosc.set(50)
    pole_iteracje = Entry(root, width=10,textvariable=pole_iteracji_wartosc,justify="center")
    pole_iteracje.grid(row=0, column=1,sticky = "WE")

    def rysuj(lista,iteracje):
        try:
            iteracje = int(iteracje)
            if iteracje > 0:
                x = gra_w_zycie_krok_po_kroku(lista)
                narysuj_wynik(x)
                pole_gry.after(20,lambda :rysuj(x,iteracje-1))
        except:
            print("Wprowadź liczbe")
    def narysuj_wynik(list):
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] == 1:
                    pole_gry.create_rectangle(j * rozmiarpikseli, i * rozmiarpikseli,
                                                                 j * rozmiarpikseli + rozmiarpikseli,
                                                                 i * rozmiarpikseli + rozmiarpikseli, tag='kwad3',
                                                                 fill='black', outline="")
                else:
                    pole_gry.create_rectangle(j * rozmiarpikseli, i * rozmiarpikseli,
                                                                 j * rozmiarpikseli + rozmiarpikseli,
                                                                 i * rozmiarpikseli + rozmiarpikseli, tag='kwad4',
                                                                 fill='white', outline="")

    przycisk = Button(root, text="Po n iteracjach", bd=4, command=lambda: narysuj_wynik(gra_w_zycie(pole_iteracje.get())))
    przycisk.grid(row=0, column=0, sticky = "WE")

    przycisk1 = Button(root, text="Krok po kroku", bd=4, command=lambda: rysuj(lista1,pole_iteracje.get()))
    przycisk1.grid(row=0, column=2, sticky="WE")
    return root

def sasiad(list,i,j):
    if i > 0:
        minus_i = i-1
    else:
        minus_i = len(list)-1
    if i < len(list)-1:
        plus_i = i+1
    else:
        plus_i = 0
    if j > 0:
        minus_j = j-1
    else:
        minus_j = len(list[i]) - 1
    if j< len(list[i])-1:
        plus_j = j+1
    else:
        plus_j = 0
    suma = list[minus_i][minus_j] + list[minus_i][j] + list[minus_i][plus_j] + list[i][minus_j] +\
           list[i][plus_j]+ list[plus_i][minus_j] + list[plus_i][j]+ list[plus_i][plus_j]
    return suma

def gra_w_zycie(iteracje):
    try:
        iteracje = int(iteracje)
        lista = losowa_lista()
        poprzedni_stan = stworz_liste(szerokosc, wysokosc)
        for l in range(iteracje):
            for i in range(len(lista)):
                for j in range(len(lista[i])):
                    if lista[i][j] == 1:
                        wartosc = sasiad(lista,i,j)
                        # print("I = {} J = {} sasiad = {}".format(i,j,wartosc))
                        if wartosc == 2 or wartosc == 3:
                            poprzedni_stan[i][j] = 1
                        else:
                            poprzedni_stan[i][j] = 0
                    elif lista[i][j]==0:
                        wartosc=sasiad(lista,i,j)
                        if wartosc == 3:
                            poprzedni_stan[i][j]=1
                        else:
                            poprzedni_stan[i][j]=0
            lista = poprzedni_stan
            poprzedni_stan = stworz_liste(szerokosc,wysokosc)
            # print("Iteracja {} Lista: {}".format(l,lista))
        return lista
    except:
        print("Wprowadź liczbe")

def gra_w_zycie_krok_po_kroku(lista):
    global poprzedni_stan1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] == 1:
                wartosc = sasiad(lista,i,j)
                # print("I = {} J = {} sasiad = {}".format(i,j,wartosc))
                if wartosc == 2 or wartosc == 3:
                    poprzedni_stan1[i][j] = 1
                else:
                    poprzedni_stan1[i][j] = 0
            elif lista[i][j]==0:
                wartosc=sasiad(lista,i,j)
                if wartosc == 3:
                    poprzedni_stan1[i][j]=1
                else:
                    poprzedni_stan1[i][j]=0
    lista = poprzedni_stan1
    poprzedni_stan1 = stworz_liste(szerokosc,wysokosc)
    return lista

if __name__ == '__main__':
    root =okno()
    root.mainloop()