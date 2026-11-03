import pygame

def EscenarioJuego(ventana, anchuraVentana, alturaVentana):
    pygame.draw.rect(ventana, (112, 209, 244), (0, 0, anchuraVentana, alturaVentana-140), width=0)
    pygame.draw.rect(ventana, (0, 255, 0), (0, alturaVentana-140, anchuraVentana, 140), width=0)