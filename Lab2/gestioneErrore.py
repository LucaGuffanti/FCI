#esercizio a caso per comprendere la struttura di controllo try: except:

from typing import final

numero1 = int(input("inserire il primo numero: "))
numero2 = int(input("inserire il secondo numero: "))

try:
    divisione = numero1/numero2
    print(divisione)
except ZeroDivisionError:
    print("Il numero inserito come secondo è uno zero")
finally:
    print("ci abbiamo provato dai!")

