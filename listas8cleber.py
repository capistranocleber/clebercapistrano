frutas =["maçã", "banana", "uva"]
numeros =[1,2,3,4]

print("primeira fruta:", frutas[0])
print("ultima fruta:", frutas[-1])

frutas[1] = "banana-nanica"
print("após alterar:", frutas)

frutas.append("morango")
frutas .insert(1, "pera")
print("Após adicionar;", frutas)

frutas.remove("uva")
ultima = frutas.pop()
print("Após remover 'uva' e pop():", frutas, "| Última removida:", ultima)

print("tamanho da lista 'frutas':", len(frutas))

print("fatiamento [0:2]", frutas[0:2])

print("tem 'maçã'?," "maçã"in frutas)

print("lista original 'numeros':", numeros)
print("soma dos numeros:", sum(numeros))
print("maior numero:", max(numeros))
print("menor numero:", min(numeros))
numeros.reverse()
print("reversa:", numeros)
numeros.sort()
print("ordenada crescente:", numeros)
numeros.sort(reverse=True)
print("ordenada decrescente:", numeros)

for fruta in frutas:
    print("frutas:", fruta)

quadrados = [n * n for n in [1,2,3,4,5]]

coordenadas = (10, 20)
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

print("X:", coordenadas[0], "| Y:", coordenadas[1])

print("primeiros 3 'dias':", dias[:3])

print("tamanho da tupla 'dias':", len(dias))

print("tem 'segunda'?", "segunda" in dias)

print("contagem de 'terça':", dias.count("terça"))
print("Índice de 'quarta':", dias.index("quarta"))

aluna = {"id": 1, "nome": "Cleber", "nota": 9.2}
pessoa = {"nome": "Marizete", "idade": 25}

print("nome da pessoa:", pessoa["nome"])

pessoa["cidade]"] = "Florianópolis"
pessoa["idade]"] = 26
print("pessoa atualizada:", pessoa)

removido = pessoa.pop("idade")
print("valor removido (idade):", removido)
print("Após pop('idade'):", pessoa)

print("Quantidade de chaves em 'aluna':", len(aluna))

print("chaves de 'aluna':", list(aluna.keys()))
print("valores de 'aluna':", list(aluna.values()))
print("itens de 'aluna':", list(aluna.items()))

print("chave 'nota' existe?", "nota" in aluna)

print("turma (com default):", aluna.get("turma","não cadastrada"))

aluna.update({"nota": 9.5, "turma": "A"})
print("Aluna após update:", aluna)

for chave, valor in aluna.items():
    print(f"{chave} -> {valor}")

frutas = ["maçã", "banana", "uva"]
numeros = [1,2,3,4]

print("primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])


frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

frutas.append("morango")
frutas.insert(1,"pera")
print("Após adicionar:", frutas)

frutas.remove("uva")
ultima = frutas.pop()
print("Após remover 'uva' e pop:", frutas,"| Última removida:", ultima)


