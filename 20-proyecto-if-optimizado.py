import os
import random
os.system('clear')

print('=====')
print('clase 20: Proyecto condicionales')
print('=====')
print('\n')

options = ('piedra', 'papel', 'tijera')
rounds=0


while True:

  rounds += 1

  print('\n')
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  print('\n')

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  computer_option = random.choice(options)


  if not user_option in options:
    print('esa opcion no es valida')

  if user_option == computer_option:
    print('\n')
    print('=====')
    print('empate')
    print('=====')
    print('Computadora: ', computer_option)
    print('Jugador: ', user_option)
    print('\n')
  #se coloca todas las jugadas donde gana el jugador
  #en caso contrario gana la computadora
  elif user_option == 'piedra' and computer_option == 'tijera' or user_option=='tijera' and computer_option=='papel' or user_option=='papel' and computer_option=='piedra':
    print('\n')
    print('=====')
    print('Jugador Gana!!!')
    print('=====')
    print('Computadora: ', computer_option)
    print('Jugador: ', user_option)
    print('\n')
  else:
    print('\n')
    print('=====')
    print('Computadora Gana!!!')
    print('=====')
    print('Computadora: ', computer_option)
    print('Jugador: ', user_option)
  continue
