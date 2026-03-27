notas = []
nota = float(input("digite uma nota: "))
notas.append(nota)

if len(notas) > 0:
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade

    if media >= 7:
        situacao = "aprovado"
    else:
        situacao = "recuperacao"
        
    print("notas digitadas:", notas)
    print(f"media: {media:.2f}")
    print("situacao:", situacao)
else:
    print("nenhuma nota foi digitada")
