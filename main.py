import os
import random
os.system('clear')

print('=====')
print('clase 31- reto de diccionario')
print('=====')
print('\n')


person = {
  'name': 'Nicolas',
  'lastName': 'Molina',
  'age': 29
}

#Escribe tu solución 👇
print('====')
print('Solucion #1')
print('====')
person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')
print(  list(person.keys())   )
print(  list(person.values())  )
print('\n')


person = {
  'name': 'Nicolas',
  'lastName': 'Molina',
  'age': 29
}

print('====')
print('Solucion #2')
print('====')
person.update({"twitter":"@nicobytes"})
person['name'] = "Felipe"
person.pop('age')
print(  list(person.keys())    )
print(  list(person.values())  )
print('\n')
