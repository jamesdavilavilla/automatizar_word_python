import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

doc = DocxTemplate("plantilla.docx")

nombre = "james davila"
telefono = "12378324"
correo = "jamesdavilavilla1@gmail.com"
fecha = datetime.today().strftime("%d/%m/%Y")

#diccionario de constantes
constantes = {'nombre': nombre, 'telefono': telefono, 'correo': correo, 'fecha': fecha}

df = pd.read_excel('Alumnos.xlsx')

#iterar indice y fila utilizando el metodo iterrows
for indice, fila in df.iterrows():
    contenido= {
        'nombre_alumno': fila['Nombre del Alumno'],
        'nota_mat' : fila['Mat'],
        'nota_fis' : fila['Fis'],
        'nota_qui' : fila['Qui'],
    }
    contenido.update(constantes)

#actualizar el documento con los datos del alumno
doc.render(contenido)
doc.save(f"Notas_de_{fila['Nombre del Alumno']}.docx")