#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Modulos
import pygame
from pygame.locals import * #importamos algunas constantes y funciones
import random
from pygame import time as pytime
#importamos nuestras propias clases
from boton import Boton
from cursor import Cursor
from nivel import Nivel
# Constantes
WIDTH = 800
HEIGHT = 600

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
    bimages = []
    for indice in range(6):
        bimages.append(load_image(''+str(indice+1)+'.png'))
        
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
    #dar las imagenes a cada boton
    for boton in botones:
        boton.setImageSeleccion(bimages);
    
    nivel = Nivel()
    
    # Aqui daremos numeros en random a los botones  
    def iniciarAleatorio():
        #para los 6 botones
        indices = [0,1,2,3,4,5]
        indices = indices[:nivel.cantidadConchas()]
        #metodo que desordena la lista en random
        random.shuffle(indices)
        
        #cambiamos el valor del indice
        i = 0
        for boton in botones[:nivel.cantidadConchas()]:
            # defino los indices de cada boton
            boton.setIndice(indices[i])
            i+=1
            
    iniciarAleatorio()
    cursor1=Cursor()
    clock = pygame.time.Clock()
    salir=False
    entrar = True
    click = 0
    limiteTiempo = 3000
    actualTiempo = pygame.time.get_ticks()
    ocultar = False
    yaOculte = False
    
    estadoJuego = 'JUGANDO'
    buenCamino = 0 
    ganasteoPerdiste = False

    while salir!=True:
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
                pantalla.blit(imagenfondo,(0,0)) #se agrega un fondo
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
                    for boton in botones[:nivel.cantidadConchas()]:
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
                                if click >= len(botones[:nivel.cantidadConchas()]):
                                    click = 0
                                if acertaste:
                                    #vas por buen camino
                                    # contador para verificar si gane el jeugo
                                    buenCamino += 1
                                    if buenCamino >= len(botones[:nivel.cantidadConchas()]):
                                        estadoJuego= 'GANASTE'
                                        nivel.aumentar()
                                        entrar = False
                                else:
                                    #pierdes
                                    estadoJuego= 'PERDISTE'
                                    nivel.disminuir()
                                    
                                    # False para no volver a detectar los eventos de los botones
                                    entrar = False
                            #salgo del ciclo for
                            break
            if event.type == pygame.QUIT:# pygame.QUIT( para que cierre cruz de la ventana)
                salir = True
        cursor1.update() #se actualiza el cuadro invisible que actua como boton del cursor
        time = clock.tick(60)
        for boton in botones[:nivel.cantidadConchas()]:
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
