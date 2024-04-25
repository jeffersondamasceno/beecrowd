linha = input()
token = linha.split()
codigo1 = token[0]
numero1 = int(token[1])
valor1 = float(token[2])

linha = input()
token = linha.split()
codigo2 = token[0]
numero2 = int(token[1])
valor2 = float(token[2])

total = numero1 * valor1 + numero2 * valor2

print("VALOR A PAGAR: R$ {:.2f}".format(total))