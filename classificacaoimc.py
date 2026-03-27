peso = float(input("digite seu peso em kg(ex.: 68.5): "))
altura = float(input("digite sua altura em metros(ex.: 1.65): "))

imc = peso / (altura ** 2)
if imc < 18.5:
    categoria = "magreza"
elif imc < 25:
    ctegoria = "normal"
elif imc < 30:
    categoria = "sobrepeso"
else:
    categoria = "obesidade"

print(f"imc = {imc:.2f} - {categoria}")

