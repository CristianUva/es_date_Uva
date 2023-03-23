#3M Uva Cristian 
#Importo la libreria
import datetime
#Esercizio 1 Stampo data corrente
y = datetime.datetime.now()
print(y)
#Esercizio 2 Creo un adata con il mio compleanno
x = datetime.datetime(2006, 2, 9)
#Esercizio 3 Stampo la data del mio compleanno numerico
print(x)
#Esercizio 4 Stampo la data del vostro compleanno il più possibile come stringa: Wednesay 31 December 1975
print(x.strftime("%A %d %B %Y "))
#Esercizio 5 Calcolo la differenza tra la data corrente e la data del vostro compleanno
differenza = y - x
print(f"{differenza}")