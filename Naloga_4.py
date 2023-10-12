

def izpisi_trikotnik(dolzina):
    for x in range(int(dolzina)+1):
        for y in range(x):
            print("*",end='')
        print()

dolzinaPiramide=input("Vpisi dolzino piramide: ")
izpisi_trikotnik(dolzinaPiramide)
