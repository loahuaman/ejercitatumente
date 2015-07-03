# Modulos
import pygame
 

# Constantes

verde=(52,170,70) 

# Clases

# ---------------------------------------------------------------------

 

# ---------------------------------------------------------------------

 
# Funciones

# ---------------------------------------------------------------------

 

# ---------------------------------------------------------------------

 
def main():
    pygame.init() # inicializo el modulo
    # fijo las dimensiones de la pantalla a 500,400 
    pantalla=pygame.display.set_mode((500,400))
    
    pygame.display.set_caption("Mi Ventana") # Titulo de la Ventana
    pantalla.fill(verde) #el color de la ventana
    pygame.display.update() #actualizo el display
    #-----para que la ventana se quede hasta cerrar
    salir=False  
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:# pygame.QUIT( para que cierre cruz de la ventana) 
                salir = True
    
    pygame.quit()
    quit()

 

main()
