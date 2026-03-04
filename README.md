[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/JSelemin/etl_countries/README.en.md)

# Global Country Data Pipeline

Pequeño pipeline de datos que extrae información de países desde una API REST pública, transforma datos JSON anidados y los carga en una base de datos relacional SQLite en forma de cuatro tablas. El flujo sigue un diseño ETL (Extract → Transform → Load), utilizando pandas para las etapas de transformación y permitiendo un posterior análisis en herramientas como Excel o Power BI.

### Tecnologías

- Python

- pandas

- requests

- SQLite

### Flujo

- Extracción de datos desde API REST.

- Fragmentación del DataFrame inicial.

- Conversión y normalización de estructuras JSON anidadas.

- Eliminación de columnas irrelevantes.

- Creación de tablas relacionales.

- Carga en SQLite.

## Ejecución

```bash
pip install -r requirements.txt
python main.py
```

## Estructura de la base de datos

La base de datos se estructura en cuatro tablas relacionadas mediante la clave _alpha3Code_.

#### Tabla _countries_

Primary Key: alpha3Code

- alpha3Code

- name

- capital

- subregion

- region

- population

#### Tabla _borders_

Foreign Key: countries.alpha3Code

- alpha3Code

- borders

#### Tabla _currencies_

Foreign Key: countries.alpha3Code

- alpha3Code

- code

- name

- symbol

#### Tabla _languages_

Foreign Key: countries.alpha3Code

- alpha3Code

- iso639_1

- iso639_2

- name

- nativeName