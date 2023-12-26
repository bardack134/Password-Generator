# Password Generator Project
import random

# Definición de listas de caracteres
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('''
     .--------.
    / .------. \\
   / /        \\ \\
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | YALE |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'LGB
'.________________.'
''')



# Solicitar al usuario la longitud de letras, símbolos y números deseados
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Lista para almacenar el resultado final de la contraseña
password = []

# Generar letras aleatorias y agregarlas a la lista de contraseñas
for i in range(0, nr_letters):
    random_number_letter = random.choice(letters)
    password.append(random_number_letter)

# Generar símbolos aleatorios y agregarlos a la lista de contraseñas
for i in range(0, nr_symbols):
    random_number_symbol = random.randint(0, len(symbols)-1)
    password.append(symbols[random_number_symbol])

# Generar números aleatorios y agregarlos a la lista de contraseñas
for i in range(0, nr_numbers):
    random_number_numbers = random.randint(0, len(numbers)-1)
    password.append(numbers[random_number_numbers])

# usamos la funcion shuffle para mezclar nuestra lista
random.shuffle(password)

# Convertir la lista de contraseñas en una cadena
password_string = ''.join(password)

# Imprimir la contraseña generada
print(password_string)


