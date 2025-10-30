#Variant 4

#1️ Kirjuta programm, mis antud arvu n (1–9) põhjal kuvab ekraanile n loomakest.
#Kahe loomakese vahel on tühikurida (tühikute veerg).
#Lubatud on tühik pärast viimast loomakest.
 # ^---^
# ( o o )
#  ! = !/)

#print("Sisesta arv 1-9: ")
#n=int(input("Sisesta arv (1-9):"))
#if 1<=n<=9:
#    for i in range(n):
#        print("  ^---^", end=" ")
#    print()
#
#    for i in range(n):
#        print(" ( o o )", end=" ")
#    print()
#
#    for i in range(n):
 #       print("  ! = !/)", end=" ")
  #  print()
#else:
 #   print("Arv peab olema 1 kuni 9!")

#2️ Väljasta naturaalarvude astmed, mis ei ületa arvu n×100.
#Kasutaja määrab astme näitaja ja arvu n.


#n=int(input("Sisesta arv n: "))
#k=int(input("Sisesta astme näitaja k: "))
#limit=n*100
#arv=1

#while arv ** k <= limit:
#    print(arv** k)
 #   arv+= 1

#3️ Antud on klassi õpilaste füüsika hinded.
#Leia minimaalne ja maksimaalne hinne (hinded ja õpilaste arv genereeritakse juhuslikult).

import random