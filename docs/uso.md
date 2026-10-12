# Uso

## Sintaxis

```
python conversor.py <valor> <origen> <destino>
```

| Argumento | Descripción |
|-----------|-------------|
| `valor` | Número a convertir (admite decimales y negativos). |
| `origen` | Unidad de partida: `C`, `F` o `K`. |
| `destino` | Unidad de llegada: `C`, `F` o `K`. |

Las unidades no distinguen mayúsculas de minúsculas: `c` y `C` son equivalentes.

## Ejemplos de ejecución

De Celsius a Fahrenheit:

```
$ python conversor.py 100 C F
100 °C = 212.00 °F
```

De Fahrenheit a Kelvin:

```
$ python conversor.py 32 F K
32 °F = 273.15 K
```

De Kelvin a Celsius:

```
$ python conversor.py 0 K C
0 K = -273.15 °C
```

## Mensajes de error

Si el valor no es un número:

```
$ python conversor.py abc C F
Error: 'abc' no es un número válido
```

Si la unidad no existe:

```
$ python conversor.py 10 C X
Error: Unidad de destino no válida: X
```

Si faltan argumentos, se muestra la ayuda de uso:

```
$ python conversor.py
Uso: python conversor.py <valor> <origen> <destino>
Unidades disponibles: C (Celsius), F (Fahrenheit), K (Kelvin)
```
