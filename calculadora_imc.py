altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura ** 2
print("Seu IMC é: ", imc)

if imc < 18.5:
  calorias = 1.2 * peso * 30
  print("Você está abaixo do peso. É indicado ganhar peso. Para isso, você precisa consumir", calorias, "calorias diárias.")
elif imc >= 18.5 and imc < 25:
  calorias = peso * 30
  print("Seu peso está dentro do normal. Para manter seu peso, você pode consumir até", calorias, "calorias diárias.")
elif imc >= 25 and imc < 30:
  calorias = 0.8 * peso * 30
  print("Você está com sobrepeso. É indicado perder um pouco de peso. Para isso, você precisa consumir até", calorias, "calorias diárias.")
else:
  calorias = 0.6 * peso * 30
  print("Você está obeso. Para perder peso, você precisa consumir até", calorias, "calorias diárias.")