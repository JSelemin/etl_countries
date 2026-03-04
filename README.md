# Global Country Data Pipeline

Pequeño pipeline de datos que extrae información de países desde una API REST pública, transforma datos JSON anidados y los carga en una base de datos relacional SQLite en forma de cuatro tablas.

### Tecnologías

- Python

- requests

- pandas

- SQLite

### Flujo

- Extracción de datos desde API REST.

- Normalización de campos anidados.

- Creación de tablas relacionales.

- Carga en SQLite

## Ejecución

```
pip install -r requirements.txt
python main.py
```
