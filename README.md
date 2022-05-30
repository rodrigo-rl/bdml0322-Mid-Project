# bdml0322-Mid-Project

## Presentación
Este es el projecto de mitad de curso del bootcamp de Big Data y Machine Learning.

La idea de este proyecto es enseñar una serie de datos sobre la EUROCOPA 2020 en el entorno de streamlit a partir de una serie de datos que se han descargado de Kaggle. 

Lo primero que se hace es realizar un filtrado de los datos y se van a subir a MongoDB. Una vez que los datos están en el formato correcto se va desarrollar una API con una serie de end-points para conectarse a esa base de datos y obtener los datos que nos interesan. 

Se ha generado una imagen docker de esa API, que se ha subido a Heroku para poder conectarse desde cualquier punto y por último se ha hecho el dashboard en streamlit para mostrar una serie de datos.

¡Espero que disfrutéis tanto de mi proyecto como yo de desarollarlo!

## Base de datos y API

Los datos se han descargado de la plataforma Kaggle (https://www.kaggle.com/mcarujo/euro-cup-2020) y se pueden encontrar en la carpeta Data/eurocup_2020_results.csv. Una vez descargados se ha realizado un proceso de filtrado y de procesado de los datos (por ejemplo, las tres últimas columnas de datos son cadenas de caracteres y deberían ser listas de diccionarios).

Para realizar este filtrado 
In this case the data are the matches of the UEFA Euro 2020 from a kaggle database (). The raw data should be filtered and cleaned up before using them with Python. The filtered data is going to be stored in MongoDB

After that, it is going to be created an API with Python to connect the streamlit enviroment with the data in MongoDB.

I hope that you enjoy it as much as I enjoy programming it!

