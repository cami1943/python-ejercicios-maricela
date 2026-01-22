import re

# Abrir el archivo
name = input("Enter file: ")
if len(name) < 1:
    name = "regex_sum_2328577.txt"  # tu archivo real

handle = open(name)

# Encontrar todos los números en el archivo
numbers = list()

for line in handle:
    nums = re.findall('[0-9]+', line)
    for n in nums:
        numbers.append(int(n))

# Calcular la suma
print("Count:", len(numbers))
print("Sum:", sum(numbers))
