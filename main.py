# Faça um algoritimo que leia a idade de uma pessoa expressa em anos e mostre-a expressa em dias e também em horas. 

print('Calculadora de dias e horas de vida')

idade = int(input('Digite quantos anos você tem:'))

dias = idade*365
horas = dias*24

print ('Você já viveu: ', dias, 'dia(s)', 'e', horas, 'hora(s)')