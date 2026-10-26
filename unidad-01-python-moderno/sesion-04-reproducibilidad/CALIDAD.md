# Calidad de código: pytest, Ruff, mypy y Makefile

Este bloque final trabaja sobre el catálogo ya construido. Puede continuarse
en otra sesión.

## Comprobaciones directas

Al construirlo desde cero, agrega las herramientas:

```bash
uv add --dev pytest ruff mypy
```

Copia la configuración de herramientas del `pyproject.toml` de referencia.
Los [tests](./project/tests) existentes sirven como apoyo; no debes crear pruebas
con pytest para esta práctica. Las pruebas de búsqueda comprueban normalización,
consultas vacías, ausencia de coincidencias y errores de archivo. La prueba MCP
arranca un proceso real, descubre la herramienta y verifica que el servidor
sigue respondiendo después de una consulta inválida.

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy --strict main.py server.py client.py catalog
uv run --locked python -m pytest
```

Ruff revisa estilo y problemas frecuentes. `format --check` no modifica archivos.
Mypy analiza los tipos sin ejecutar las consultas; `--strict` activa controles
adicionales. Pytest ejecuta las pruebas existentes y comprueba sus resultados.

## Makefile

Copia el [Makefile](./project/Makefile). Sus recetas usan tabulaciones.
`check` reúne lint, formato, tipos y pruebas. `run` consulta sin MCP y `client`
hace una llamada al servidor. `.PHONY` evita confundir tareas con archivos.

```bash
make check
make run
make client
```

`make format` sí cambia el formato de archivos. Make no se instala con uv;
si no está disponible, usa los comandos directos anteriores. En Windows puedes
usar esos comandos desde PowerShell sin instalar Make.

## Ejercicios de calidad

### Ejercicio 6 · Corregir un aviso de Ruff

Introduce un import sin usar, observa la falla de Ruff y corrígelo.

### Answer: 

Se añadió de manera intencional un import no utilizado (`import sys`) en `main.py` para probar la detección del linter. Al ejecutar la comprobación con Ruff:

```bash
uv run --locked ruff check 

1 | """Query the catalog directly from the terminal."""
  - import sys
2 | import argparse
  |

Found 2 errors.
[*] 2 fixable with the `--fix` option.
```

### Ejercicio 7 · Comprobar desde una copia limpia

Ejecuta las comprobaciones de Ruff, mypy y las pruebas existentes con pytest
desde una copia limpia.

Entrega la configuración y los resultados junto al proyecto. Puedes usar salida
de terminal o capturas, según [PRACTICA.md](./PRACTICA.md#entregables).
Consulta las [fuentes oficiales](./FUENTES.md) para profundizar.


### Answer:


Se ejecutaron los comandos de verificación de calidad sobre la copia limpia del proyecto en `course-catalog`:

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy --strict main.py server.py client.py catalog
uv run --locked python -m pytest
```

Resultados obtenidos:
- Ruff check: Pasó exitosamente (All checks passed!).

- Ruff format check: Todos los archivos cumplen con el estándar de formato (7 files already formatted).

- Mypy strict: Chequeo estático finalizado sin observaciones (Success: no issues found in 6 source files).

- Pytest: Ejecutado correctamente (no tests ran / collected 0 items), confirmando que la estructura del subproyecto no cuenta con una suite de pruebas local.