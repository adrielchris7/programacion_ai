# Práctica: un catálogo reproducible con MCP

Resuelve **7 ejercicios**: los ejercicios 1–5 de este documento y los ejercicios
6–7 de [CALIDAD.md](./CALIDAD.md#ejercicios-de-calidad).

[GUIA.md](./GUIA.md) explica cómo construir el proyecto en ocho secciones;
esas secciones no son ejercicios adicionales. Crear un repositorio Git o un
commit no es requisito de entrega: para comprobar la reproducción basta una
copia del proyecto sin `.venv`.

## Ejercicio 1 · Punto de entrada

Ejecuta `uv run python -c "import main"`. Explica por qué no consulta el catálogo.
Identifica también la condición que impide iniciar el transporte al importar
`server.py`. Distingue registrar una herramienta de iniciar el servidor.


### Answer: 

No consulta el catálogo porque el código de búsqueda vive dentro de main(), que solo se invoca si el archivo se ejecuta directamente mediante la condición if __name__ == "__main__":. Al usar import, solo se define el módulo sin invocar la función.   

## Ejercicio 2 · Datos y argumentos

Copia `data/courses.json` a `data/extra_courses.json` y agrega un curso cuyo título
incluya Python. Usa `--catalog` para consultar esa copia desde `main.py` y comprueba
que aparecen tres resultados. Prueba una ruta inexistente y registra el código
de salida. La herramienta MCP sigue usando el catálogo predeterminado.

## Ejercicio 3 · Niveles y destinos

Compara una misma consulta con DEBUG, INFO y ERROR. Después usa
`--log-level ERROR --log-file logs/app.log`. Explica por qué el archivo conserva
mensajes que no aparecen en consola y por qué stdout debe reservarse al protocolo
en `server.py`.

### Answer:

### 1. Evidencia de logs registrados
Al ejecutar la aplicación guardando la salida en un archivo (`--log-file logs/app.log`), el archivo registra todos los eventos producidos por el módulo:


DEBUG | catalog.search | Reading catalog: C:\...\data\courses.json

INFO  | catalog.search | Search completed: 2 matches 

  - Consola vs. Archivo: El logger raíz recibe todos los mensajes (DEBUG, INFO, ERROR). La consola solo mostró ERROR porque el parámetro --log-level ERROR filtró su salida; en cambio, el archivo (--log-file) se configuró para guardar todo desde DEBUG en adelante.   


  - Por qué reservar stdout en MCP: El protocolo MCP usa stdout para transferir datos en formato JSON entre servidor y cliente. Si mandas mensajes de log por stdout, contaminas los datos y rompes la conexión. Por eso los logs van a stderr. 


## Ejercicio 4 · Mejorar el diagnóstico

Añade al mensaje INFO de `catalog/search.py` la cantidad total de cursos leídos,
además de la cantidad de coincidencias. Usa argumentos de logging. Comprueba
que la consulta directa y la llamada MCP siguen devolviendo los mismos cursos.

### Answer:


Se actualizó el mensaje de registro INFO dentro de catalog/search.py para incluir tanto el número de coincidencias como el número total de cursos leídos del archivo.

```python
logger.info(
    "Search completed: %d matches out of %d total courses",
    len(matches),
    len(courses),
)
```
  - Al ejecuitar main.py y client.py, la aplicacion continua devolviendo los mismos dos cursos esperados.
  - El log emitido ahora proporciona mayor contexto sobre el volumen de datos analizado (ej. `2 matches out of 3 total courses`).


## Ejercicio 5 · Reproducción y llamada MCP

Desde una copia limpia, ejecuta `uv sync --locked` y `client.py` con `python`,
`astronomy` y una cadena de espacios. Identifica la herramienta disponible y
distingue respuesta vacía de error. Explica qué aportan `pyproject.toml`,
`uv.lock` y `.python-version` y por qué no se entrega `.venv`.


### Answer


### Preguntas del ejercicio
- **Herramienta disponible:** `find_courses`[cite: 3, 5].
- **Diferencia entre respuesta vacía y error:** Una respuesta vacía (`astronomy`) es un resultado exitoso que indica 0 coincidencias en el catálogo[cite: 3, 4]. Un error (`" "`) ocurre cuando la petición es inválida y viola los criterios de la herramienta[cite: 3].
- **Aporte de los archivos de configuración:** 
  - `pyproject.toml`: Especifica las dependencias directas y compatibilidad[cite: 3].
  - `uv.lock`: Congela las versiones exactas de todos los paquetes para asegurar que el entorno sea idéntico en cualquier máquina[cite: 2, 3].
  - `.python-version`: Fija la versión exacta del intérprete Python a utilizar[cite: 3].
- **¿Por qué no se entrega `.venv`?** Es una carpeta pesada y dependiente del sistema operativo local; `uv` la reconstruye de forma idéntica en cualquier momento ejecutando `uv sync --locked`[cite: 3, 4].


## Entregables

- El proyecto con código, datos pequeños, `pyproject.toml`, `uv.lock`,
  `.python-version` y `Makefile`.
- Un README con comandos, resultados de las llamadas y explicaciones de los
  ejercicios, incluida la evidencia de las comprobaciones de calidad. Puedes
  pegar la salida de terminal en bloques de código o incluir capturas donde se
  vean los comandos y sus resultados; cualquiera de las dos opciones es válida.

Para calidad, muestra el aviso de Ruff por el import sin usar y su corrección,
y el resultado final de Ruff, mypy y pytest sobre las pruebas existentes. No se
pide crear pruebas nuevas.

Comprueba la ejecución desde una copia limpia. Entrega el proyecto sin `.venv`,
cachés ni logs.
