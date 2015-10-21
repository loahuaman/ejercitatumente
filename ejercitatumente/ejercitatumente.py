#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulos
import pygame
from pygame.locals import * #importamos algunas constantes y funciones
import random
from pygame import time as pytime

# Constantes
WIDTH = 800
HEIGHT = 600

# Clases

# ---------------------------------------------------------------------
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)

    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,background_image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_normal=background_image
        self.indice = 0
        self.bloquear = False
        self.imagen_seleccion = []
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def setIndice(self, num):
        self.bloquear= False #cada vez que el indice del boton es modificado desbloqueo el boton
        self.indice = num
        self.setNumeroImagen(self.indice)#mostramos el numero correspondiente al indice del boton
    
    def ocultarNumero(self):
        self.imagen_actual = self.imagen_normal#no mostramos la imagen con numero
            
    def verificarIndice(self, num):
        #si el indice
        if self.indice == num:
            #retorno true si el indice coincide con el numero del click
            return True
        else:
            #retorno false si el indice no coincide con el numero del click
            return False
    
    def setImageSeleccion(self, image1, image2, image3, image4, image5, image6):
        self.imagen_seleccion.append(image1)
        self.imagen_seleccion.append(image2)
        self.imagen_seleccion.append(image3)
        self.imagen_seleccion.append(image4)
        self.imagen_seleccion.append(image5)
        self.imagen_seleccion.append(image6)
       

    def setBloquer(self, valor):
        self.bloquear = valor
    
    def getBloquer(self):
        return self.bloquear
    
    def setNumeroImagen(self, num):
        #modifico la imagen a mostrar solo si el boton no esta bloqueado
        if(not self.bloquear):
            self.imagen_actual = self.imagen_seleccion[num]
        
    def update(self,pantalla,cursor,time):
        pantalla.blit(self.imagen_actual,self.rect)

# ---------------------------------------------------------------------


# Funciones

# ---------------------------------------------------------------------
def load_image(filename, transparent=True):# para el fondo trasparente de la imagen

        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)

        return image


# ---------------------------------------------------------------------
movimiento  = True
posx, posy = 0, 500
#pencere = pygame.display.set_mode((1000, 600))
pez = pygame.Rect((posx, posy), (75, 50))
ima_pez = pygame.image.load("pez.png")
#---------------------------------------------------------------------------
#funcion principal
def main():
    pygame.init() # inicializo el modulo
    pygame.mixer.init()
    # fijo las dimensiones de la pantalla a 500,400 y creo una superficie que va ser la principal
    pantalla=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("juego ejercita tu mente") # Titulo de la Ventana
    texto=Boton(load_image('texto.png'),150,-30) #se crea un boton para "perdiste"
    
    imagenfondo=pygame.image.load("mar.jpg").convert()
    pygame.mixer.music.load("hakuna.mid")# Cargamos la cancion
    pygame.mixer.music.play()  # Le damos al Play
    pytime.wait(11) # 110000 Esperamos un tiempo a que acabe la cancion
    
    fondo = load_image('fondo.png')
    bimage1 = load_image('1.png')
    bimage2 = load_image('2.png')
    bimage3 = load_image('3.png')
    bimage4 = load_image('4.png')
    bimage5 = load_image('5.png')
    bimage6 = load_image('6.png')
    pantalla.blit(imagenfondo,(0,0)) #se agrega un fondo
    
    x=80 #se dan las pociciones en el eje x
    x1=270 
    x2=460 
    x3=80 
    x4=270 
    x5=460 
    
    boton1=Boton(fondo,x,100) #se crea un boton para cada concha en diferentes posiciones
    boton2=Boton(fondo,x1,100) 
    boton3=Boton(fondo,x2,100) 
    boton4=Boton(fondo,x3,300) 
    boton5=Boton(fondo,x4,300) 
    boton6=Boton(fondo,x5,300) 
    #Creo una lista y añado los botones a la lista para poder manipularlos mejor
    botones = []
    botones.append(boton1);
    botones.append(boton2);
    botones.append(boton3);
    botones.append(boton4);
    botones.append(boton5);
    botones.append(boton6);
    #dar las imagenes a cad boton
    for boton in botones:
        boton.setImageSeleccion(bimage1, bimage2, bimage3, bimage4, bimage5, bimage6);
   
    # Aqui daremos numeros en random a los botones  
    def iniciarAleatorio():
        #para los 6 botones
        indices = [0,1,2,3,4,5]
        #metodo que desordena la lista en random
        random.shuffle(indices)
        
        #cambiamos el valor del indice
        i = 0
        for boton in botones:
            # defino los indices de cada boton
            boton.setIndice(indices[i])
            i+=1
            
    iniciarAleatorio()
    cursor1=Cursor()
    clock = pygame.time.Clock()
    salir=False
    entrar = True
    click = 0
    limiteTiempo = 4000
    actualTiempo = pygame.time.get_ticks()
    ocultar = False
    yaOculte = False
    
    estadoJuego = 'JUGANDO'
    buenCamino = 0 
    ganasteoPerdiste = False

    while salir!=True:
        pantalla.blit(imagenfondo, (0, 0))
        if movimiento:
            pez.right += 8
        
        if pez.left > 800:
            pez.right = 0

        pantalla.blit(ima_pez, (pez.left, pez.top - 25))
        
        #esperamos 3 segundos, pasado los tres segundos se ocultaran los numeros
        if(estadoJuego == 'JUGANDO' and pygame.time.get_ticks()-actualTiempo >= limiteTiempo):
            entrar = True
            ocultar = True
        #preguntamos el estado del juego
        if estadoJuego == 'PERDISTE' or estadoJuego == 'GANASTE':
            if not ganasteoPerdiste:
                # capturamos el primer instante de tiempo desde que se ganó o perió
                # para empezar a contar 3 segundo
                actualTiempo = pygame.time.get_ticks()
                #True para asegurar que solo entre una vez
                ganasteoPerdiste = True
                #imprimo el estado del juego en los botones 
                if estadoJuego=='GANASTE':
                    botoni=Boton(load_image('tortuga.png'),270,10) #se crea un boton para "ganaste"
                    botoni.update(pantalla,cursor1,time)
                else:
                    botoni=Boton(load_image('tortuga1.png'),270,10) #se crea un boton para "perdiste"
                    botoni.update(pantalla,cursor1,time)
                    
            # oculto los numeros mientras no pase tres segundos
            if(pygame.time.get_ticks()-actualTiempo <= limiteTiempo):
                ocultar = True
                yaOculte = False
            else:
                #pasado el tiempo  reinicio las variables
                iniciarAleatorio()
                ganasteoPerdiste = False
                actualTiempo = pygame.time.get_ticks()
                
                click = 0
                ocultar = False
                yaOculte = False
                estadoJuego = 'JUGANDO'
                buenCamino = 0
            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if entrar:
                    #recorremos cada boton
                    for boton in botones:
                        #verificamos si el cursor dio click en algun boton
                        if cursor1.colliderect(boton.rect):
                            #almaceno el estado del boton antes de ser presionado
                            bloqueado = boton.getBloquer()
                            #modifico el numero a mostrar en el boton
                            boton.setNumeroImagen(click)
                            #bloqueo el boton para impedir que se le de click despues
                            boton.setBloquer(True)
                            #verifico si el numero de click corresponde con el numro de boton
                            acertaste = boton.verificarIndice(click)
                            
                            if not bloqueado:
                                #si el boton no esta bloqueado procedo a contar el click
                                click += 1
                                # definir la cantidad de botones
                                if click >= len(botones):
                                    click = 0
                                if acertaste:
                                    #vas por buen camino
                                    # contador para verificar si gane el jeugo
                                    buenCamino += 1
                                    if buenCamino >= len(botones):
                                        estadoJuego= 'GANASTE'
                                        entrar = False
                                else:
                                    #pierdes
                                    estadoJuego= 'PERDISTE'
                                    # False para no volver a detectar los eventos de los botones
                                    entrar = False
                            #salgo del ciclo for
                            break
            if event.type == pygame.QUIT:# pygame.QUIT( para que cierre cruz de la ventana)
                salir = True
        cursor1.update() #se actualiza el cuadro invisible que actua como boton del cursor
        time = clock.tick(5)
        for boton in botones:
            #llamo al update de cada boton
            boton.update(pantalla,cursor1,time)
            if ocultar and not yaOculte:
                #oculto los botones
                boton.ocultarNumero() #se actualiza cada boton al acercar el cursor
        if ocultar:
            # True para garantizar que los botones se oculten solo una vez
            yaOculte = True
        texto.update(pantalla,cursor1,time)
        pygame.display.update() #actualizo el display
        
    pygame.quit()

main()
