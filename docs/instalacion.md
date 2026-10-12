# Instalación

## Requisitos

- **Python 3.9 o superior**. Para comprobar tu versión:

    ```
    python --version
    ```

    En Linux y macOS el comando suele ser `python3`, y en Windows también funciona `py`.

- **Git**, para obtener el proyecto.
- **MkDocs**, solo si quieres ver o generar esta documentación en tu equipo.

El programa en sí no necesita instalar ninguna librería adicional.

## Obtener el proyecto

Clona el repositorio y entra en la carpeta:

```
git clone https://github.com/TU_USUARIO/conversor.git
cd conversor
```

Sustituye `TU_USUARIO` por el usuario de GitHub propietario del repositorio.

## Comprobar que funciona

Ejecuta una conversión de prueba:

```
python conversor.py 0 C K
```

Si todo va bien, verás:

```
0 °C = 273.15 K
```

## Instalar MkDocs

Instala MkDocs usando Python para llamar a pip:

```
python -m pip install mkdocs
```

Se recomienda `python -m pip` en lugar de `pip` a secas porque funciona aunque el comando `pip` no esté en el PATH del sistema. En Linux y macOS usa `python3 -m pip install mkdocs`.

## Ver la documentación en local

Desde la carpeta del proyecto (la que contiene `mkdocs.yml`), arranca el servidor de MkDocs:

```
python -m mkdocs serve
```

Abre `http://127.0.0.1:8000` en el navegador. Para parar el servidor, pulsa `Ctrl+C`.

## Generar el sitio final

```
python -m mkdocs build
```

Esto crea la carpeta `site/` con la web estática. Esa carpeta está en el `.gitignore`, así que no se sube al repositorio.

## Problemas frecuentes

| Error | Causa y solución |
|-------|------------------|
| `pip: command not found` | El comando `pip` no está en el PATH. Usa `python -m pip install mkdocs`. |
| `mkdocs: command not found` | La carpeta de scripts de Python no está en el PATH. Usa `python -m mkdocs serve`. |
| `Config file 'mkdocs.yml' does not exist` | No estás en la carpeta correcta. Entra en la carpeta del proyecto, la que contiene `mkdocs.yml` y la carpeta `docs/`, y vuelve a ejecutar el comando. Compruébalo con `ls`. |
| `externally-managed-environment` | Tu sistema no permite instalar paquetes globales. Crea un entorno virtual: `python3 -m venv ~/venv-mkdocs`, actívalo con `source ~/venv-mkdocs/bin/activate` e instala ahí MkDocs. |
