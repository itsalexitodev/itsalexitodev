import random
print("Hola como te llamas")
name = input()
print("Hola", name)
print("estoy pensando en un numero del 0 al 10, lo puedes adivinar?")
number = random.randint(0, 10)
while True:
    estimacion = int(input())
    if estimacion == number:
        print("Correct!")
        break
    if estimacion < number:
        print("Too low!")
    elif estimacion > number:
        print("Too high!")
