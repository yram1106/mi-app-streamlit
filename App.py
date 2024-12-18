import streamlit as st

# Título principal de la aplicación
st.title('Explorando Widgets y Sidebar en Streamlit')

# Widgets en el Sidebar
st.sidebar.header('Información Personal')

# Input Box (Edad): rango de 0 a 100 años
edad = st.sidebar.slider('¿Cuál es tu edad?', 0, 100, 25)
st.sidebar.write(f'Tu edad es: {edad} años.')

# Text Input (Nombres y Apellidos)
nombre_apellido = st.sidebar.text_input('¿Cuál es tu nombre y apellido?')
st.sidebar.write(f'Tu nombre y apellido: {nombre_apellido}')

# Slider (Seleccionar Mes): del 1 al 12
mes = st.sidebar.slider('Selecciona un mes', 1, 12, 1)
st.sidebar.write(f'Se ha seleccionado el mes: {mes}')

# Checkbox (Acepta Términos)
terminos_aceptados = st.sidebar.checkbox('Acepto los términos y condiciones')
if terminos_aceptados:
    st.sidebar.write("¡Has aceptado los términos y condiciones!")
else:
    st.sidebar.write("No has aceptado los términos y condiciones.")

# Radio Buttons (Género)
genero = st.sidebar.radio('Selecciona tu género', ['Masculino', 'Femenino'])
st.sidebar.write(f'Tu género seleccionado es: {genero}')

# Selectbox (Selecciona tu País)
pais = st.sidebar.selectbox('Selecciona tu país', ['Argentina', 'Colombia', 'Ecuador', 'México', 'Perú'])
st.sidebar.write(f'Tu país seleccionado es: {pais}')

# Button (Enviar Información)
if st.sidebar.button('Enviar Información'):
    st.sidebar.write('La información se ha enviado')

# File Uploader (Cargar Archivo)
archivo = st.sidebar.file_uploader("Cargar un archivo", type=["txt", "csv", "xlsx"])
if archivo is not None:
    st.sidebar.write("Archivo cargado:", archivo.name)

# Date Input (Selecciona una Fecha)
fecha = st.sidebar.date_input('Selecciona una fecha')
st.sidebar.write(f'La fecha seleccionada es: {fecha}')

# Time Input (Selecciona una Hora)
hora = st.sidebar.time_input('Selecciona una hora')
st.sidebar.write(f'La hora seleccionada es: {hora}')

# Mostrar la información en la parte principal de la página
st.subheader('Resumen de la Información Ingresada')
st.write(f'Edad: {edad} años')
st.write(f'Nombre y Apellido: {nombre_apellido}')
st.write(f'Mes seleccionado: {mes}')
st.write(f'Género seleccionado: {genero}')
st.write(f'País seleccionado: {pais}')
st.write(f'Términos Aceptados: {"Sí" if terminos_aceptados else "No"}')
st.write(f'Fecha seleccionada: {fecha}')
st.write(f'Hora seleccionada: {hora}')