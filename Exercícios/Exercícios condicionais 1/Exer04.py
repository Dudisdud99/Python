a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))
d = int(input('Digite um valor para D: '))
e = int(input('Digite um valor para E: '))

maior = a

if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e


print(f'O maior é {maior}')