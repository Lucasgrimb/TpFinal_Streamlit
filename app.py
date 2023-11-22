import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Función para cargar y preparar la imagen
def load_and_prep_image(image):
    # Convertir la imagen a escala de grises
    image = image.convert('L')
    # Redimensionar la imagen a 28x28 (como en Fashion MNIST)
    image = image.resize((28, 28))
    # Convertir la imagen en un array de numpy y normalizar
    image = np.array(image)
    image = image / 255.0
    # Añadir una dimensión extra al principio
    image = np.expand_dims(image, axis=0)
    return image

# Nombres de las categorías del Fashion MNIST
class_names = ['Camiseta/top', 'Pantalón', 'Suéter', 'Vestido', 'Abrigo',
               'Sandalia', 'Camisa', 'Zapatilla deportiva', 'Bolso', 'Botín']

# Cargar el modelo
model = load_model('modeloChona.h5')

# Título de la aplicación
st.title("Clasificador de Moda con Fashion MNIST")

# Subida de archivos
uploaded_file = st.file_uploader("Sube una imagen de ropa...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)
    image = load_and_prep_image(image)
    prediction = model.predict(image)
    
    # Obtener el índice de la categoría con la mayor probabilidad y la probabilidad
    predicted_category = np.argmax(prediction[0])
    confidence = np.max(prediction[0])
    
    # Convertir la confianza de formato decimal a porcentaje
    confidence_percentage = round(confidence * 100)

    # Mostrar la predicción y la confianza como un porcentaje
    st.write(f'Predicción: {class_names[predicted_category]} con una probabilidad de {confidence_percentage}%')
