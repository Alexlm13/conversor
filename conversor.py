"""Conversor de temperaturas entre Celsius, Fahrenheit y Kelvin.
 
Uso:
    python conversor.py <valor> <origen> <destino>
 
Ejemplo:
    python conversor.py 100 C F
"""
 
import sys
 
UNIDADES = ("C", "F", "K")
 
 
def a_celsius(valor: float, origen: str) -> float:
    """Convierte un valor desde la unidad de origen a grados Celsius."""
    if origen == "C":
        return valor
    if origen == "F":
        return (valor - 32) * 5 / 9
    if origen == "K":
        return valor - 273.15
    raise ValueError(f"Unidad de origen no válida: {origen}")
 
 
def desde_celsius(valor: float, destino: str) -> float:
    """Convierte un valor en grados Celsius a la unidad de destino."""
    if destino == "C":
        return valor
    if destino == "F":
        return valor * 9 / 5 + 32
    if destino == "K":
        return valor + 273.15
    raise ValueError(f"Unidad de destino no válida: {destino}")
 
 
def convertir(valor: float, origen: str, destino: str) -> float:
    """Convierte una temperatura entre dos unidades (C, F o K)."""
    origen = origen.upper()
    destino = destino.upper()
    return desde_celsius(a_celsius(valor, origen), destino)
 
 
def simbolo(unidad: str) -> str:
    """Devuelve el símbolo de la unidad (Kelvin no lleva el signo de grado)."""
    unidad = unidad.upper()
    return unidad if unidad == "K" else f"°{unidad}"
 
 
def main(argumentos: list[str]) -> int:
    if len(argumentos) != 3:
        print("Uso: python conversor.py <valor> <origen> <destino>")
        print("Unidades disponibles: C (Celsius), F (Fahrenheit), K (Kelvin)")
        return 1
 
    texto_valor, origen, destino = argumentos
 
    try:
        valor = float(texto_valor)
    except ValueError:
        print(f"Error: '{texto_valor}' no es un número válido")
        return 1
 
    try:
        resultado = convertir(valor, origen, destino)
    except ValueError as error:
        print(f"Error: {error}")
        return 1
 
    print(f"{valor:g} {simbolo(origen)} = {resultado:.2f} {simbolo(destino)}")
    return 0
 
 
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))