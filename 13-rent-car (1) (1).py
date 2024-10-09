# 13-rent-car.py um programa que pergunte a quantidade de km
# percorrridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado,
# Calcule o preço a pagar,sabendo que o 
# Carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# Variaveis 
dias_locados = int(input("Dias alugados:"))
km_percorridos =float(imput("Quantos km foram percorridos?"))

# calculo do oreco total
total = (dias_locados*60)+(km_percorrido*0.15)
print(f"O valor total a pagar é R$(total:.2f)")
                           