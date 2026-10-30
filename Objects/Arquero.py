# Classe Arquero (Goleiro)

class Arquero:
    def __init__(self, pontoX, pontoY, anchura, altura):
        self.pontoX = pontoX
        self.pontoY = pontoY
        self.anchura = anchura
        self.altura = altura

    def iniciarArquero(self, pygame, ventana):
            pygame.draw.rect(ventana, (255,250,0), (self.pontoX, self.pontoY, self.anchura, self.altura))

    def defensaPorteria(pontoX, movimento):
        pontoX += movimento