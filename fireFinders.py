from sense_hat import SenseHat
from math import sqrt
from time import sleep
import sys
import pygame
from picamera import PiCamera
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
camera = PiCamera()

sense = SenseHat()
sense.clear()


#VARIABLES

Gr_a = 1
Gr_b = 0

a=3
b=3

drone_location = [5, 5]
drone_current_location = "display1"
current_display = "display1"

##COLOURS

green= [0, 102, 0]
cute_green= [0, 204,0]
yellow= [255, 255, 0]
blue= [0, 128, 255]
cute_blue = [0, 255, 255]
grey= [64, 64, 64]
red= [153, 0, 0]
o = [0, 0, 0]

g = green
cg = cute_green
br = yellow
b = blue
cb = cute_blue
gr = grey
r = red

##DISPLAYS

Map = [o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,
       o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o,]

display1 = [gr, gr, gr, gr, gr, gr, gr, gr, 
            gr, br, gr, gr, gr, gr, gr, gr,
            gr, gr, g, g, g, g, g, g, 
            gr, gr, g, g, g, g, g, g,
            gr, gr, g, g, g, g, g, g,
            gr, gr, g, g, g, r, r, r,
            gr, gr, g, g, g, g, r, r,
            gr, gr, g, g, g, r, r, r]

display2 = [gr, gr, gr, gr, gr, gr, gr, gr, 
            gr, gr, gr, gr, gr, gr, gr, gr,
            g, g, g, g, g, g, gr, gr, 
            g, g, g, g, g, g, gr, gr,
            g, g, g, g, g, g, br, gr,
            r, g, r, g, g, g, gr, gr,
            r, r, r, g, g, g, gr, gr,
            r, r, r, g, g, g, gr, gr]

display3 = [gr, gr, g, g, g, r, r, r, 
            gr, gr, g, g, g, r, r, r,
            gr, gr, g, g, g, r, g, g,
            gr, gr, g, g, g, g, g, g,
            br, gr, g, g, g, g, g, g,
            gr, gr, g, g, g, g, g, g,
            gr, gr, gr, gr, gr, gr, gr, gr, 
            gr, gr, gr, gr, gr, gr, gr,gr]

display4 = [r, r, g, g, g, g, gr, gr, 
            r, r, r, g, g, g, br, gr,
            r, r, r, g, g, g, gr, gr,
            g, g, g, g, g,g, gr, gr,
            g, g, g, g, g, g, gr, gr,
            g, g, g, g, g, g, gr, gr,
            gr, gr, gr, gr, gr, gr, gr, gr, 
            gr, gr, gr, gr, gr, gr, gr, gr]



sense.set_pixels(display1)

image = [
r,r,w,w,w,w,r,r,
r,r,r,w,w,r,r,r,
w,r,r,r,r,r,r,w,
w,w,r,r,r,r,w,w,
w,w,r,r,r,r,w,w,
w,r,r,r,r,r,r,w,
r,r,r,w,w,r,r,r,
r,r,w,w,w,w,r,r]


XDistance = 0
YDistance = 0
##FUNCTIONS

def check_visibility():
    global drone_current_location, current_display, drone_location
    if(drone_current_location == current_display and drone_location[0]<=7 and drone_location[0]>=0 and drone_location[1]<=7 and drone_location[1]>=0):
        #sense.clear()
        sense.set_pixel(drone_location[0], drone_location[1], blue)            
    #else:
        #sense.clear()
        #sense.set_pixel(drone_location[0], drone_location[1], 0, 0, 0)
            
def update_map_location(Gr_a, Gr_b):
    if(Gr_a != 0):
        if(Gr_a == 1):
            sense.set_pixels(display1)
            current_display = "display1"
        elif(Gr_a == 2):
            sense.set_pixels(display2)
            current_display = "display2"
    elif(Gr_b != 0):
        if(Gr_b == 1):
            sense.set_pixels(display3)
            current_display = "display3"
        elif(Gr_b == 2):
            sense.set_pixels(display4)
            current_display = "display4"

def get_event():
    global Gr_a, Gr_b
    for event in sense.stick.get_events():
        if(event.direction == "right"):
            if(Gr_a == 1):
                Gr_a += 1
                update_map_location(Gr_a, Gr_b)
            elif(Gr_b == 1):
                Gr_b += 1
                update_map_location(Gr_a, Gr_b)
        if(event.direction == "left"):
            if(Gr_a == 2):
                Gr_a -= 1
                update_map_location(Gr_a, Gr_b)
            elif(Gr_b == 2):
                Gr_b -= 1
                update_map_location(Gr_a, Gr_b)
        if(event.direction == "up" and Gr_b != 0):
            Gr_a = Gr_b
            Gr_b = 0
            update_map_location(Gr_a, Gr_b)
        if(event.direction == "down" and Gr_a != 0):
            Gr_b = Gr_a
            Gr_a = 0
            update_map_location(Gr_a, Gr_b)    

def update_drone_location():
    global a, b, drone_location, drone_current_location, current_display, XDistance, YDistance
    
    acceleration=sense.get_accelerometer_raw()
    x=acceleration['x']
    y=acceleration['y']
    #x=round(x,0)
    #y=round(y,0)
    sleep(0.1)
    #xy_acceleration=sqrt((x**2)+(y**2))
    #xy_acceleration=xy_acceleration*9.8
    x_Acceleration = x*9.8
    y_Acceleration = y*9.8
    sleepa=0.1
    x_speed=sleepa*x_Acceleration
    y_speed=sleepa*y_Acceleration
    xDistance=x_speed*sleepa
    yDistance=y_speed*sleepa

    YDistance += yDistance
    XDistance += xDistance

    if YDistance>=0.1:
        YDistance = 0
        drone_location[1] += 1
        try:
            sense.set_pixel(drone_location[0],drone_location[1]-1, cb)          
        except:
            if(drone_location[1]>7):
                drone_location[1] = 0
                drone_location[0] = drone_location[0]
                if(drone_current_location == "display1"):
                    sense.set_pixels(display3)
                    current_display = "display3"
                    drone_current_location = "display3"
                elif(drone_current_location == "display2"):
                    sense.set_pixels(display4)
                    current_display = "display4"
                    drone_current_location  = "display4"
                else:
                    drone_location[1] = 7
                    sense.show_message("Lost Connection", text_colour = red, scroll_speed=0.05)
                    if(drone_current_location == "display1"):
                        sense.set_pixels(display1)
                        current_display = current_display
                    elif(drone_current_location == "display2"):
                        sense.set_pixels(display2)
                        current_display = current_display
                    elif(drone_current_location == "display3"):
                        sense.set_pixels(display3)
                        current_display = current_display
                    elif(drone_current_location == "display4"):
                        sense.set_pixels(display4)
                        current_display = current_display
    elif YDistance<=-0.1:
        drone_location[1] -= 1
        YDistance = 0
        try:
            sense.set_pixel(drone_location[0],drone_location[1]+1,cb)
        except:
            if(drone_location[1]<0):                
                if(drone_current_location == "display3"):
                    sense.set_pixels(display1)
                    current_display = "display1"
                    drone_current_location= "display1"
                    drone_location[1]=7
                elif(drone_current_location == "display4"):
                    sense.set_pixels(display2)
                    current_display = "display2"
                    drone_current_location  = "display2"
                    drone_location[1]=7
                else:
                    drone_location[1] = 7
                    sense.show_message("Lost Connection", text_colour = red,scroll_speed=0.05)
                    if(drone_current_location == "display1"):
                        sense.set_pixels(display1)
                        current_display = current_display
                    elif(drone_current_location == "display2"):
                        sense.set_pixels(display2)
                        current_display = current_display
                    elif(drone_current_location == "display3"):
                        sense.set_pixels(display3)
                        current_display = current_display
                    elif(drone_current_location == "display4"):
                        sense.set_pixels(display4)
                        current_display = current_display
            
    elif XDistance>=0.1:
        #a+=1
        drone_location[0] += 1
        XDistance = 0
        #sense.set_pixel(a-1, b,0,0,0)
        try:
            sense.set_pixel(drone_location[0]-1,drone_location[1],cb)
        except:
            print("entered")
            if(drone_location[0]>7):                
                if(drone_current_location == "display1"):
                    sense.set_pixels(display2)
                    current_display = "display2"
                    drone_current_location = "display2"
                    drone_location[0] = 0
                elif(drone_current_location == "display3"):
                    sense.set_pixels(display4)
                    current_display = "display4"
                    drone_current_location  = "display4"
                    drone_location[0]=0
                else:
                    drone_location[0] = 0
                    sense.show_message("Lost Connection", text_colour=red,scroll_speed=0.05)
                    if(drone_current_location == "display1"):
                        sense.set_pixels(display1)
                        current_display = current_display
                    elif(drone_current_location == "display2"):
                        sense.set_pixels(display2)
                        current_display = current_display
                    elif(drone_current_location == "display3"):
                        sense.set_pixels(display3)
                        current_display = current_display
                    elif(drone_current_location == "display4"):
                        sense.set_pixels(display4)
                        current_display = current_display

    elif XDistance <=-0.1:
        #a-=1
        XDistance = 0
        drone_location[0] -= 1
        #sense.set_pixel(a+1, b,0,128, 255)
        try:
            sense.set_pixel(drone_location[0]+1,drone_location[1], cb)
        except:
            if(drone_location[0]<0):                
                if(drone_current_location == "display2"):
                    sense.set_pixels(display1)
                    current_display = "display1"
                    drone_current_location = "display1"
                    drone_location[0] = 7
                elif(drone_current_location == "display4"):
                    sense.set_pixels(display3)
                    current_display = "display3"
                    drone_current_location = "display3"
                    drone_location[0]=7
                else:
                    sense.show_message("Lost Connection", text_colour = red,scroll_speed=0.05)
                    if(drone_current_location == "display1"):
                        sense.set_pixels(display1)
                        current_display = current_display
                    elif(drone_current_location == "display2"):
                        sense.set_pixels(display2)
                        current_display = current_display
                    elif(drone_current_location == "display3"):
                        sense.set_pixels(display3)
                        current_display = current_display
                    elif(drone_current_location == "display4"):
                        sense.set_pixels(display4)
                        current_display = current_display


def fire_finder():
    
    t = SenseHat().get_temperature()
    sense= SenseHat()
    h = SenseHat().get_humidity()
    p = SenseHat().get_pressure()
    c = SenseHat().get_compass()

    fire = t>50

    
    if (t>30):
        pygame.mixer.init()
        pygame.mixer.music.load('Tsunami Siren Sound Effect #1 I Tsunami Warning Siren Sound Effect I Tsunami Alarm Sound Effect.mp3')
        pygame.mixer.music.play()
        camera.rotation = 180
        camera.start_preview()

    photo_list = [].

    for x in range(0,20):
        print(t)
        sleep(0.5)
        if (t > 30):
            sense.set_pixels(image)
            sleep(0.5)
            name = "/home/pi/Desktop/Imagens/Foto%s.jpg" % x
            camera.capture(name)
            photo_list.append(name)
            name = ""
            sense.clear()
            print(h)
            print(p)
            print(c)

        print(photo_list)
    camera.stop_preview()
            
    fromaddress = 'firefindersteam@sapo.pt'
    toaddress = 'rodrigo.luis.pinho@gmail.com'
    text = 'condições metriológicas.'
    text1 = "Tem fotos para consultar no Raspberry pi3 \nPressure; %s \nTemperature: %s \nHumidity: %s \nCompass: %s" %(p, t, h, c)
    username = 'firefindersteam@sapo.pt'
    password = 'thefirefinders'
    msg = MIMEText(text1, 'plain', 'utf-8')
    msg ['From'] = fromaddress
    msg ['To'] = toaddress
    msg ['Subject'] = Header(text, "utf-8")
    server = smtplib.SMTP_SSL('smtp.sapo.pt', 465)
    server.login(username,password)
    server.sendmail(fromaddress,toaddress,msg.as_string())
    server.quit()
    return fire

 
while True:
    if !fire_finder():
        get_event()
        update_drone_location()
        check_visibility()
        fire_finder()

    else:
        fire_finder()