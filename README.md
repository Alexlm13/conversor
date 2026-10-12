# Conversor de temperaturas

Aplicación de línea de comandos escrita en Python que convierte temperaturas entre **Celsius (C)**, **Fahrenheit (F)** y **Kelvin (K)**. No necesita librerías externas

## Requisitos

- Python 3.9 o superior
- Git
- MkDocs (solo para ver o generar la documentación)

## Obtener el proyecto

```
git clone https://github.com/Alexlm13/conversor.git
cd conversor
```

## Uso

```
python conversor.py <valor> <origen> <destino>
```

Ejemplo:

```
$ python conversor.py 100 C F
100 °C = 212.00 °F
```

## Documentación

La documentación del proyecto está hecha con [MkDocs](https://www.mkdocs.org/) y se encuentra en la carpeta `docs/`.

Instalar MkDocs:

```
python -m pip install mkdocs
```

Ver la documentación en local (abre `http://127.0.0.1:8000`):

```
python -m mkdocs serve
```

Generar el sitio estático en la carpeta `site/`:

```
python -m mkdocs build
```

## Estructura del proyecto

```
conversor/
├── conversor.py
├── README.md
├── .gitignore
├── mkdocs.yml
└── docs/
    ├── index.md
    ├── instalacion.md
    └── uso.md
```
