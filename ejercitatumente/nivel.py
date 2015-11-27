# -*- coding: utf-8 -*-

#Calse para controlar el VALOR del nivel
class Nivel:
    
    def __init__(self):
        #Defino constantes
        self.defaultConchasNivel = 2
        self.nivelMinimo = 0
        self.nivelMaximo = 4
        #El valor del nivel 
        self.nivel = self.nivelMinimo
        
    # Aumentamos el nivel en 1
    def aumentar(self):
        self.nivel += 1
        if self.nivel > self.nivelMaximo:
            self.nivel = self.nivelMaximo

    # Disminuye el nivel en 1
    def disminuir(self):
        self.nivel -= 1
        if self.nivel < self.nivelMinimo:
            self.nivel = self.nivelMinimo

    def controlarNivel(self):
        if not(self.nivel <= self.nivelMaximo and self.nivel > self.nivelMinimo):
            self.nivel = 0
        
    def cantidadConchas(self):
        self.controlarNivel()
        return (self.nivel+self.defaultConchasNivel)

    def valor(self):
       self.controlarNivel()
       return self.nivel
