#!/usr/bin/env python3
import os

import random
def pause():
    programPause = input("Pulsa <ENTER> para continuar...")
guesses_made = 0

name = input('Hola! Cómo te llamas?\n')

nn = 1
print ('Hola, {0}, estoy pensando en un número entre 1000 y 9999.'.format(name))
while nn == 1:
 number = random.randint(1000, 9999)

 numtex = str(number)
 list1 = [numtex[0],numtex[1],numtex[2],numtex[3]]
 ll=set(list1)
 kk=len(list1)
 mm=len(ll)

 if mm+kk == 8:
    nn=0
    break

while guesses_made < 10:

 guess = int(input('Elige un numero: '))
 guesses_made += 1
 num2t=str(guess)
 def resultado (a,b):
   popm = {a}
   popm.remove(a)
   poph = {a}
   poph.remove(a)
   for i in range(0,4):     

    if (str(num2t[i]) in ll):
     poph.add(int(num2t[i])) #""" añade a la lista heridos"""
     
    if num2t[i] == numtex[i]:
     
     popm.add(int(num2t[i])) #""" añade a la lista murders"""


   her = poph - popm 
   mor = len(popm)
   ff= str(guess) +" "+ str(mor) + " muertos " + str(len(her)) + " heridos"
   print (ff)
    
 resultado(guess,number)
 

 if guess == number:
    break

if guess == number:
        print ('Buen trabajo, '+str(name)+'! Has adivinado mi numero '+str(number)+' en {1} intentos!'.format(name, guesses_made))
else:
        print ('Se acabó la partida. El numero que estaba pensando era {0}'.format(number))
pause()
