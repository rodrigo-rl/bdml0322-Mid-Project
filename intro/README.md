![](https://api.brandy.run/core/core-logo-wide)

# Mid Project: Big Data & Machine Learning

Bienvenid@ al proyecto de mitad del bootcamp. En ese primer projecto, tendrás la oportunidad de poner en práctica tus conocimientos adquiridos en python, profundizarles, aprender más y sobretodo explorar por tu propria cuenta un problema en busca de soluciones.

En ese proyecto, crearás una API para servir datos de una bbdd que crearás. Deberás diseñar la API, definir los endpoints y sus parámetros, además de escribir las funciones que ejecutaran lo necesário para devolver la respuesta esperada. (Las API deben devolver un objeto JSON).

Partirás de un dataset (a eligir), pero no será apenas esa información sobre la cual trabajarás. Utilizando otras API o el proceso de webscraping, deberás enriquecer los datos que tienes, traendole información complementar y relacionada.

También crearás un dashboard de visualización de datos en Streamlit, que consumirá los datos de tu API y permitirá interactuar con las visualizaciones.

## Objetivos

Los objetivos de ese proyecto son:

- Creación de una API
  - Definición de endpoints y parámetros
  - Conexión con bbdd
- Creación de un Dashboard Streamlit
  - Preparación de datos para visualización
  - Parametrización de las visualizaciones
- Conexión de servicios
  - Dashboard debe recibir los datos de la API
- Adicional:
  - Data Cleaning/Wrangling
  - Data Enrichment (API, Webscraping)

## Instrucciones

Eligir uno de los datasets disponibles

**Datasets**

- [Data Covid-19 Global](https://www.kaggle.com/baguspurnama/covid-confirmed-global)
- [Palmer Archipelago Penguins](https://www.kaggle.com/parulpandey/palmer-archipelago-antarctica-penguin-data)
- [Open Data BCN](https://www.kaggle.com/xvivancos/barcelona-data-sets)
- [UEFA Euro Cup 2020](https://www.kaggle.com/mcarujo/euro-cup-2020)

**Tareas**

- Utilizar de APIs y/o Webscraping para enriquecer esos datos
  - Debes decidir si enriquecerás todos los datos y en seguida guardar la base de datos o si las peticiones a APIs y/o webscraping se hará solo en el momento en que los datos sean necesários.
- Preparar los datos, crear funciones de limpieza y formatación, etc.
- Guardar los datos en una base de datos
  - Debes eligir entre MongoDB y Postgres, y la organización de los datos, i.e.: tablas, collections, atributos, etc.
- Crear una API para servir los datos disponibles. Debes crear diferentes endpoints segun la necesidad, utilizar de los métodos y parámetros que mejor se adequen a cada tipo petición.
- Crear un dashboard que consuma datos de la API creada por ti y genere visualizaciones interactivas. Usa de tu creatividad y las posibilidades de Streamlit. No hay limites más que tu imaginación. Acuérdate que los diferentes widgets de streamlit sirven para que puedas interactuar con las visualizaciones, para que no sean genéricas, sino que hechas según el interés del usuário.

**Tecnologías**

- flask
- streamlit
- pandas
- matplotlib
- seaborn
- plotly
- folium
- mongoDB
- postgres
- Docker
- Heroku

## Requisitos del proyecto

1. Crear un único repo para el proyecto, la organización es esencial. separa el dashboard y la api en dos carpetas dentro de tu repo. No dejes más que el esencial en la raiz del repo.

1. Documentar un README.md de tu proyecto. Es importante que describas las instrucciones de uso y comentes un poco sobre tu proyecto. Acuerdate que esa es la portada de lo que has hecho. Puedes buscar en otros [repo con grandes readme](https://github.com/matiassingers/awesome-readme) por inspiración.

1. Crear un fichero `requirements.txt` o `requirements.yml` para que qualquier persona pueda instalar y ejecutar tus programas sin tener que hacer debugging.

**Pasos**

- L1: Crear api con FastAPI
- L1: Crear dashboard en streamlit
- L1: Base de datos en MongoDB o PostgreSQL
- L2: Utilizar de datos geoespaciales y geoqueries en MongoDB o Postgres ([Usando PostGIS](https://postgis.net/))
- L2: Tener la base de datos en el Cloud (Hay servicios gratis en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2), [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql), entre otros)
- L2: Generar reporte [pdf](https://pyfpdf.readthedocs.io/en/latest/) de los datos visibles en Streamlit, descargable mediante boton.
- L2: Un dashboard de multiples páginas en Streamlit
- 🔥 L3: Que el dashboard te envie el reporte pdf por e-mail
- 🔥 L3: Poder subir nuevos datos a la bbdd via la API (usuario y contraseña como headers del request)
- 🔥🔥 L4: Poder actualizar la base de datos via Streamlit (con usuario y contraseña, en una página a parte. El dashboard debe hacer la petición anterior que añade datos via API)
- 🔥🔥 L4: Crear contenedor Docker y hacer deploy de los servicios en el cloud ([Heroku](heroku.com). Los dos servicios deben subirse separadamente)

```
Leyenda:
- L1: Obligatório
- L2: Un retito más
- L3: Vamos calentando
- L4: Advanced
```
