nota = float(input("digite a nota (0 a 10): "))
if nota < 5:
    print("reprovada")
elif 5<= nota <= 6.9:
    print("recuperacao")
elif 7<= nota <= 8.9:
    print("aprovasda")
elif 9 <= nota <= 10:
    print("aprovada com excelencia")
else:
    print("nota invalida")