print("Bem Vindo a minha calculadora")

num1 = input("Digite o primeiro numero ")
num1 = int(num1)
num2 = input("Digite o segundo numero ")
num2 = int(num2)
simbolo = input("Digite a operação a ser feita ")


if(simbolo == "+"):
    print(num1 + num2)

elif(simbolo == "-"):
    print(num1 - num2)

elif(simbolo == "*"):
    print(num1 * num2)

elif(simbolo == "/"):
    print(num1 / num2)

else:
    print("Voce digitou algum operador inexistente")


