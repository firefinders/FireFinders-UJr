
from guizero import *
from sys import *

STATUS = "Fire finders"
t = 0
app=App(title="Hackathon: ideias inteligentes", width = (990), height = 700)
app.attributes("-fullscreen", True)

status_message= Text(app, text="Status: " + STATUS, size=60)

def start_protocol():
   set_temperature_range()

def set_temperature_range():
   t=temperature.get()
   print("Temperature Range", str(t))

def objetivo():
    print("Este projeto tem como objetivo assegurar os ambientes naturais deste pais. O Fire Finders vigia as areas florestais diariamente e caso um incendio seja encontrado o quartel mais próximo será alertado.")
    info("Objetivo", "Este projeto tem como objetivo assegurar os ambientes naturais deste pais. O Fire Finders vigia as areas florestais diariamente e caso um incendio seja encontrado o quartel mais próximo será alertado.")
def quit_():
    quit()

temperature_text = Text(app, text="Danger Temperature", size=15)
temperature = TextBox(app)
StartButton = PushButton(app, command=start_protocol, text="Começar Protocolo")
my_map=Picture(app,image="map.gif")
ObjectiveButton = PushButton(app, command=objetivo, text="Objetivo do Projeto")
ExitButton = PushButton(app, command=quit_, text="Exit")
app.display()
