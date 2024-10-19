import tkinter as GUI
import serial 
import time

# Crear ventana
ventana = GUI.Tk()
ventana.title("Comunicación con ESP32")
ventana.geometry("320x240")

# Variables globales
PUERTO = "COM3"
arduino = None  

def CONECTAR():
    global PUERTO, arduino
    puerto_ingresado = EntryCOM.get() 
    if arduino is not None and arduino.is_open:  
        LabelEstado.config(text="Ya esta conectado.", fg="green")
    elif puerto_ingresado == "COM3":
        try:
            arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=.1)
            LabelEstado.config(text="Puerto correcto, Conectado al ESP32", fg="green")
        except:
            LabelEstado.config(text="Error al conectar: ESP32 desconectado del puerto ", fg="red")
    else:
        LabelEstado.config(text="Error: Puerto incorrecto.", fg="red")

# Función para enviar número y recibir el resultado
def SEND():
    if arduino and arduino.is_open:  
        print("funcion ENVIO DE DATOS")
        x = SpinDATA.get()
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline().decode('utf-8')  
        LabelRECIVE.config(text="El resultado de la suma es: " + data)
    else:
        LabelRECIVE.config(text="Conectarse al puerto primero", fg="black")

# Función para cerrar el programa
def CERRAR():
    if arduino and arduino.is_open:
        arduino.close()
    ventana.destroy()

# Instancia de los objetos
LabelCOM_NAME = GUI.Label(ventana, text="Escribe el nombre del puerto: COM3")
EntryCOM = GUI.Entry(ventana)
BotonCONECT = GUI.Button(ventana, text="CONECTAR CON ESP32", command=CONECTAR)
LabelEstado = GUI.Label(ventana, text="", fg="red")  
SpinDATA = GUI.Spinbox(ventana, from_=0, to=500)
BotonSEND = GUI.Button(ventana, text="Sumar + 1", command=SEND)
LabelRECIVE = GUI.Label(ventana, text="El resultado es =")
BotonCerrar = GUI.Button(ventana, text="Cerrar ventana", command=CERRAR)

#incrustacion en la ventana
LabelCOM_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
LabelEstado.pack(padx=1, pady=2)  
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

# Iniciar el bucle de la GUI
ventana.mainloop()