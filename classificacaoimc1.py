temperatura = float(input("digite a temperatura atual:" ))
if temperatura <10:
    print("muito frio")
elif 10 <= temperatura <= 24:
    print("agradavel")
elif 25 >= temperatura <= 30:
    print("quente")
else:
    print("muito quente") 