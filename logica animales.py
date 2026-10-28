
hechos = {
    "Mamifero": ["Pelo", "DaLeche"],
    "Ave": ["Plumas", "Vuela", "PoneHuevos"],
    
    "Carnívoro": ["Mamífero", "ComeCarne"],
    "Ungulado": ["Mamífero", "Pezuñas"],
    "Equino": ["Mamífero", "Cuadrupedo", "Transporte"],
    
    "Guepardo": ["Carnivoro", "Leonado", "Manchas"],
    "Tigre": ["Carnívoro", "Leonado", "Rayas"],
    "Jirafa": ["Ungulado", "CuelloLargo", "Manchas"],
    "Cebra": ["Ungulado", "Rayas"],
    "Pinguino": ["Ave", "Nada", "BlancoYNegro"],
    "Albatros": ["Ave", "VuelaMuyBien"],
    "Loro": ["Ave", "RepitePalabras", "TamañoMedio"],
    "Perico": ["Ave", "RepitePalabras", "ColaLarga"],
    "Caballo": ["Equino", "Alto", "OrejasPequeñas"]
}



print("Guepardo  ¿Es Leonado?:", "Leonado" in hechos["Guepardo"])

print(" \nTigre ¿Tiene Rayas?:", "Rayas" in hechos["Tigre"])

print(" \nJirafa ¿Tiene CuelloLargo?:", "CuelloLargo" in hechos["Jirafa"])

print(" \nCebra ¿Es Ungulado?:", "Ungulado" in hechos["Cebra"])

print("\nPinguino ¿Sabe Nada?:", "Nada" in hechos["Pinguino"])

print("\nAlbatros ¿VuelaMuyBien?:", "VuelaMuyBien" in hechos["Albatros"])

print(" \nLoro¿Es de TamañoMedio?:", "TamañoMedio" in hechos["Loro"])

print("\nPerico ¿Tiene ColaLarga?:", "ColaLarga" in hechos["Perico"])

print("\nCaballo ¿Tiene OrejasPequeñas?:", "OrejasPequeñas" in hechos["Caballo"])
