#Escribe un programa que se encargue de comprobar si un número es o no primo.
#Hecho esto, imprime los números primos entre 1 y 100.

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True

for n in range(1, 101):
    if is_prime(n) is True:
        print(n)
