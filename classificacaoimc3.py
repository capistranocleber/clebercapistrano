inventario = []

item = input("digite um item (ou'sair' para encerrar): ")
if item == "sair":
    print("voce encerrou") 
else:  
    
    
    inventario.append(item)
    inventario.sort()

print("Itens no inventario:")
inventario

print("total de itens:", len(inventario))




