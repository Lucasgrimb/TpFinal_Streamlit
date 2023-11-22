
# Clasificador de Artículos de Moda - TpFinal_Streamlit

Este repositorio contiene los archivos y recursos necesarios para ejecutar una aplicación de clasificación de artículos de moda desarrollada con una Red Neuronal Convolucional (CNN). Desplegamos la aplicación usando Streamlit y permite a los usuarios clasificar imágenes de ropa en varias categorías, similares a las encontradas en el dataset Fashion MNIST.

## Contenido del Repositorio

- `TpFinalChona.ipynb`: Un Jupyter Notebook que contiene el código para construir, entrenar y evaluar la CNN. Incluye explicaciones detalladas de cada paso del proceso, siguiendo la consigna del trabajo.
- `modeloChona.h5`: El modelo de la CNN entrenado y guardado en el formato HDF5. Este archivo se usa para hacer predicciones en la aplicación Streamlit.
- `app.py`: El script de Python para ejecutar la aplicación Streamlit. Este script carga el modelo entrenado y muestra una interfaz de usuario para subir imágenes y ver las predicciones.
- `requirements.txt`: Un archivo que lista todas las dependencias necesarias para ejecutar la aplicación, para que el entorno de ejecución en Streamlit tenga todo lo necesario.

## Uso de la Aplicación

Para probar el clasificador de artículos de moda, entrá a la aplicación en Streamlit con el link: [Clasificador de Moda en Streamlit](https://tpfinalapp-pebyh63kyacrxjsvvpxkkh.streamlit.app/).

## Instrucciones para Ejecutar Localmente

Para ejecutar la aplicacion en tu computadora, sigue estos pasos:

1. Cloná el repositorio en tu máquina local.
2. Fijate de tener Python instalado y crea un entorno virtual.
3. Instala las dependencias necesarias con `pip install -r requirements.txt`.
4. Ejecuta el script `app.py` con Streamlit usando el comando `streamlit run app.py`.

