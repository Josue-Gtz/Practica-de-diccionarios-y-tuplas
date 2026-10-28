    %% Propiedades Base -> Categorías Principales
    Pelo[Pelo] -->|Implica| Mamifero[Mamífero]
    DaLeche[DaLeche] -->|Implica| Mamifero
    Plumas[Plumas] -->|Implica| Ave[Ave]
    Vuela[Vuela] & PoneHuevos[PoneHuevos] -->|Implica| Ave

    %% Subcategorías
    Mamifero & ComeCarne[ComeCarne] -->|Implica| Carnivoro[Carnívoro]
    Mamifero & Pezunas[Pezuñas] -->|Implica| Ungulado[Ungulado]
    Mamifero & Cuadrupedo[Cuadrupedo] & Transporte[Transporte] -->|Implica| Equino[Equino]

    %% Animales Carnívoros
    Carnivoro & Leonado[Leonado] & Manchas[Manchas] -->|Implica| Guepardo[Guepardo]
    Carnivoro & Leonado & Rayas[Rayas] -->|Implica| Tigre[Tigre]

    %% Animales Ungulados y Equinos
    Ungulado & CuelloLargo[CuelloLargo] & Manchas -->|Implica| Jirafa[Jirafa]
    Ungulado & Rayas -->|Implica| Cebra[Cebra]
    Equino & Alto[Alto] & OrejasPequenas[OrejasPequeñas] -->|Implica| Caballo[Caballo]

    %% Animales Aves
    Ave & Nada[Nada] & BlancoYNegro[BlancoYNegro] -->|Implica| Pinguino[Pingüino]
    Ave & VuelaMuyBien[VuelaMuyBien] -->|Implica| Albatros[Albatros]
    Ave & RepitePalabras[RepitePalabras] & TamanoMedio[TamañoMedio] -->|Implica| Loro[Loro]
    Ave & RepitePalabras & ColaLarga[ColaLarga] -->|Implica| Perico[Perico]
