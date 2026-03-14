# CRUD
# CREATE
# READ
# UPDATE
# DELETE
from tkinter import *
from tkinter import messagebox

class TkAlumno:
    
    def __init__(self,app):
        self.app = app
        self.app.title("CRUD DE ALUMNOS")
        self.app.geometry("640x480")
        
        frame = LabelFrame(self.app, text="Datos del Alumno")
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        
        ### DNI ###
        self.lb_dni = Label(frame, text="DNI: ")
        self.lb_dni.grid(row=1,column=0, pady=10, padx=10)
        self.txt_dni = Entry(frame)
        self.txt_dni.grid(row=1,column=1, pady=10, padx=10)
        
        ##### NOMBRE ####
        lb_nombre = Label(frame,text='NOMBRE : ')
        lb_nombre.grid(row=2,column=0, pady=10, padx=10)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=2,column=1, pady=10, padx=10)

        ##### EMAIL ####
        lb_email = Label(frame,text='EMAIL : ')
        lb_email.grid(row=3,column=0, pady=10, padx=10)
        self.txt_email = Entry(frame)
        self.txt_email.grid(row=3,column=1, pady=10, padx=10)
        
app = Tk()

if __name__ == "__main__":
    app_alumno = TkAlumno(app)
    app.mainloop()