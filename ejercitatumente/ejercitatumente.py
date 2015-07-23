# Modulos
import pygame
from pygame.locals import * #importamos algunas constantes y funciones

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
        self.imagen_normal=background_image
        self.imagen_seleccion=background_image
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        pantalla.blit(self.imagen_actual,self.rect)
 

# ---------------------------------------------------------------------

 
# Funciones

# ---------------------------------------------------------------------

 

# ---------------------------------------------------------------------

 
def main():
    pygame.init() # inicializo el modulo
    # fijo las dimensiones de la pantalla a 800,400 
    pantalla=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("juego ejercita tu mente") # Titulo de la Ventana
    imagenfondo=pygame.image.load("mar.jpg").convert()#capturando una imagen de fondo
    boton=pygame.image.load("boton.png").convert_alpha()
    pantalla.blit(imagenfondo,(0,0))
    botonr=Boton(boton,80,100)
    cursor1=Cursor()
    
    
    #-----para que la ventana se quede hasta cerrar
    salir=False  
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# pygame.QUIT( para que cierre cruz de la ventana) 
                salir = True
        cursor1.update() #se actualiza el cuadro invisible que actua como boton del cursor
        botonr.update(pantalla, cursor1) #se actualiza cada boton al acercar el cursor
        pygame.display.update() #actualizo el display
    pygame.quit()
    
 

main()
