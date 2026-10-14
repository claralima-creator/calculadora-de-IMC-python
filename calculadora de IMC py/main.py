import sys

print("Faixa de referência (adultos)")

#validando peso
peso_texto = input("Digite seu peso em kg:")

try:
   if (peso := float(peso_texto))<=0:
       sys.exit("O peso deve ser positivo")

except ValueError:
    sys.exit('Erro! Você precisa digitar um peso numérico')

#validando altura
altura_texto = (input("Digite sua altura em metros:"))
try:
    if not (0.5 <= (altura :=float(altura_texto)) <= 2.5):
        sys.exit("Altura inválida")
except ValueError:
    sys.exit("Erro! Digite apenas números!")

#validando idade
idade_texto = (input("Digite sua idade:"))
try:
    if (idade := int(idade_texto)) <=0:
        sys.exit("A idade deve ser positiva")
    elif idade <18:
       sys.exit("O IMC de adultos não se aplica a menores de 18 anos.")
except ValueError:
    sys.exit("Erro! Digite sua idade em anos inteiros")

#calculando o IMC
IMC = peso / altura ** 2

if IMC < 18.5:
    print(f"Seu IMC é: {IMC:.2f}")
    print("Abaixo do peso")
elif 18.5 <= IMC < 25:
    print(f"Seu IMC é: {IMC:.2f}")
    print("Peso normal")
elif 25 <= IMC < 30:
    print(f"Seu IMC é: {IMC:.2f}")
    print('Sobrepeso')
elif 30 <= IMC < 35:
    print(f"Seu IMC é: {IMC:.2f}")
    print('Obesidade grau 1')
elif 35 <= IMC < 40:
    print(f"Seu IMC é: {IMC:.2f}")
    print("Obesidade grau 2")
else:
    print(f"Seu IMC é: {IMC:.2f}")
    print("Obesidade grau 3")



