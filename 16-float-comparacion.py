import os
os.system('clear')

print('=====')
print('clase 16: comparación de float')
print('=====')
print('\n')


x = 3.3
y = 1.1 + 2.2
print('x :',x, 'tipo de dato: ', type(x))
print('y :',x, 'tipo de dato: ', type(y))
print('Son iguales x == y :', x == y)
print('\n')

print('1° Primera forma para comprar:' )
print('====')
y_str = format(y, ".2g")
x_str = str(x)
print('x_str :',x_str, 'tipo de dato: ', type(x_str))
print('y_str :',x_str, 'tipo de dato: ', type(y_str))
print('son iguales :',y_str == x_str)
print('\n')


print('2° Segunda forma de comprar:' )
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)
