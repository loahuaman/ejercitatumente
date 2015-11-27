# -*- coding: utf-8 -*-
import pygame

class Boton(pygame.sprite.Sprite):
    def __init__(self,background_image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_normal=background_image
        self.indice = 0
        self.bloquear = False
        # Creamos seis imagenes seleccion por si acaso
        self.imagen_seleccion = []
        
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def setIndice(self, num):
        #cada vez que el indice del boton es modificado desbloqueo el boton
        self.bloquear= False
        self.indice = num
        #mostramos el numero correspondiente al indice del boton
        self.setNumeroImagen(self.indice)
    
    def ocultarNumero(self):
        ##no mostramos la imagen con numero
        self.imagen_actual = self.imagen_normal
            
    def verificarIndice(self, num):
        #self.bloquear= False
        #si el indice
        if self.indice == num:
            #print('Vas por buen camino')
            #retorno true si el indice coincide con el numero del click
            return True
        else:
            #print('Lo siento, no tienes buena memoria')
            #retorno false si el indice no coincide con el numero del click
            return False
    
    def setImageSeleccion(self, images):
        self.imagen_seleccion = images

    def setBloquer(self, valor):
        self.bloquear = valor
    
    def getBloquer(self):
        return self.bloquear
    
    def setNumeroImagen(self, num):
        #modifico la imagen amostrar solo si el boton no esta bloqueado
        if(not self.bloquear):
            self.imagen_actual = self.imagen_seleccion[num]
        
    def update(self,pantalla,cursor,time):
        
        pantalla.blit(self.imagen_actual,self.rect)
# ---------------------------------------------------------------------
