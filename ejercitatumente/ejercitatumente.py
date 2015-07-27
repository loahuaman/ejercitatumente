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

def load_image(filename, transparent=True):

        try: image = pygame.image.load(filename)

        except pygame.error, message:

                raise SystemExit, message

        image = image.convert()

        if transparent:

                color = image.get_at((0,0))

                image.set_colorkey(color, RLEACCEL)

        return image

 
# ---------------------------------------------------------------------

 
def main():
    pygame.init() # inicializo el modulo
    # fijo las dimensiones de la pantalla a 800,600 
    pantalla=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("juego ejercita tu mente") # Titulo de la Ventana
    imagenfondo=pygame.image.load("mar.jpg").convert()#capturando una imagen de fondo
    background_image = load_image('concha.png')
    pantalla.blit(imagenfondo,(0,0))
    
    
    
    x=80 #se dan las pociciones en el eje x
    x1=270 
    x2=460 
    x3=80 
    x4=270 
    x5=460 
    
    boton1=Boton(background_image,x,100)  #se crean los botones
    boton2=Boton(background_image,x1,100) 
    boton3=Boton(background_image,x2,100)
    boton4=Boton(background_image,x3,300) 
    boton5=Boton(background_image,x4,300)
    boton6=Boton(background_image,x5,300)

    cursor1=Cursor()
    salir=False  
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# pygame.QUIT( para que cierre cruz de la ventana) 
                salir = True
        cursor1.update() #se actualiza el cuadro invisible que actua como boton del cursor
        boton1.update(pantalla, cursor1) #se actualiza cada boton al acercar el cursor
        boton2.update(pantalla, cursor1)
        boton3.update(pantalla, cursor1)
        boton4.update(pantalla, cursor1)
        boton5.update(pantalla, cursor1)
        boton6.update(pantalla, cursor1)
        pygame.display.update() #actualizo el display
    pygame.quit()
    
 

main()
