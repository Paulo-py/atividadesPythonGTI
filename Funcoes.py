horas = int(input("Quantas horas o carro permaneceu no estacionamento? "))
if horas == 1:
    preco = 8
else:
    preco = 8 + (horas - 1) * 5
print("Valor total a pagar : R$", preco)