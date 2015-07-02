# Modulos
import pygame
 

# Constantes

 

# Clases

# ---------------------------------------------------------------------

 

# ---------------------------------------------------------------------

 
# Funciones

# ---------------------------------------------------------------------

 

# ---------------------------------------------------------------------

 
def main():
    pygame.init() # inicializo el modulo
      # fijo las dimensiones de la pantalla a 500,400 y creo una superficie que va ser la principal
    pantalla=pygame.display.set_mode((500,400))
    
    pygame.display.set_caption("Mi Ventana") # Titulo de la Ventana
    pygame.display.update() #actualizo el display
    pygame.quit()
    quit()

 
if __name__ == '__main__':

   main()
