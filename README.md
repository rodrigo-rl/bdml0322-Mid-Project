# bdml0322-Mid-Project

## Presentación
Este es el projecto de mitad de curso del bootcamp de Big Data y Machine Learning.

La idea de este proyecto es enseñar una serie de datos sobre la EUROCOPA 2020 en el entorno de streamlit a partir de una serie de datos que se han descargado de Kaggle. 

Lo primero que se hace es realizar un filtrado de los datos y se van a subir a MongoDB. Una vez que los datos están en el formato correcto se va desarrollar una API con una serie de end-points para conectarse a esa base de datos y obtener los datos que nos interesan. 

Se ha generado una imagen docker de esa API, que se ha subido a Heroku para poder conectarse desde cualquier punto y por último se ha hecho el dashboard en streamlit para mostrar una serie de datos.

¡Espero que disfrutéis tanto de mi proyecto como yo de desarollarlo!

## Base de datos y API

Los datos se han descargado de la plataforma Kaggle (https://www.kaggle.com/mcarujo/euro-cup-2020) y se pueden encontrar en la carpeta **Data/eurocup_2020_results.csv**. Una vez descargados se ha realizado un proceso de filtrado y de procesado de los datos (por ejemplo, las tres últimas columnas de datos son cadenas de caracteres y deberían ser listas de diccionarios).

Para realizar este filtrado y la organización de los datos para poder presentarlos se han escrito estos programas en python:

![image](https://user-images.githubusercontent.com/101878865/171048303-7aeefee8-68e9-48a2-a488-9da81b5db300.png)

- Players.ipynb -->
- Teams.ipynb -->
- data_management.ipynb -->
- goals_per_team.ipynb -->
