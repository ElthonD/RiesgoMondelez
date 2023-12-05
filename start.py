import streamlit as st
import numpy as np
from PIL import Image

### App de Inicio

def createPage():
    
    # Title of the main page
    pathLogo = './img/AI27Mondelez.png'
    display = Image.open(pathLogo)
    display = np.array(display)
    # st.image(display, width = 400)
    # st.title("Aplicación DataDriven")
    col1, col2, col3 = st.columns([1,5,1])
    col2.image(display, use_column_width=True)
    #col2.title("Aplicación DataDriven")

    col2.markdown('Bienvenido a ***Aplicación Táctico-Estrátegico AI27 Mondelez***, está aplicación provee los pasos tácticos-estrátegicos a seguir para la operación del cliente ***Mondelez***')

    col2.write(""" 
    Está aplicación contiene:
    + ***Probabilidad estática de robos.***
    + ***Mapa planner de robos.***
    + ***Chatbot para reglas de negocios enfocada al riesgo.***
    """)

    return True
