import pygame

# Classe Balón (Bola)
class Balon(pygame.sprite.Sprite):
    def __init__(self, pontoX, pontoY, radioCirculo):
        super().__init__()

        self.pontoX = pontoX
        self.pontoY = pontoY
        self.radioCirculo = radioCirculo

        # Posições originais (para resetar o jogo)
        self.origemX = pontoX
        self.origemY = pontoY

        self.imagem = pygame.Surface((self.radioCirculo*2, self.radioCirculo*2), pygame.SRCALPHA)

        pygame.draw.circle(self.imagem, (255,0,0), (self.radioCirculo, self.radioCirculo), self.radioCirculo)

        self.rect = self.imagem.get_rect()
        self.rect.x = self.pontoX
        self.rect.y = self.pontoY

        # Variáveis de controle da Parábola
        self.emTrajeto = False
        self.progresso = 0.0  # Vai de 0.0 (início) a 1.0 (chegada no gol)
        self.alvoX = 0
        self.alvoY = 0
        
        # Força da curva (quanto maior, mais alto a bola sobe no meio do caminho)
        self.alturaParabola = 100 

    def iniciarBalon(self, ventana):
        ventana.blit(self.imagem, self.rect)

    def iniciarChute(self, coordsGol):
        """Chame esta função uma única vez quando o jogador clicar na tela"""
        self.alvoX = coordsGol[0]
        self.alvoY = coordsGol[1]
        self.progresso = 0.0
        self.emTrajeto = True

    def disparo(self):
        """Chame esta função a cada frame dentro do loop principal do jogo"""
        if self.emTrajeto:
            # Aumenta o progresso. Altere este valor para mudar a velocidade da bola!
            self.progresso += 0.01 

            if self.progresso >= 1.0:
                self.progresso = 1.0
                self.emTrajeto = False  # Chegou ao destino

            # 1. Interpolação Linear para o eixo X (Movimento suave de lado a lado)
            self.pontoX = self.origemX + (self.alvoX - self.origemX) * self.progresso

            # 2. Movimento Base do eixo Y (Linha reta em direção ao gol)
            y_linear = self.origemY + (self.alvoY - self.origemY) * self.progresso

            # 3. Arco da Parábola (Usando a curva de uma função quadrática invertida)
            # Arco será 0 no início (progresso 0), máximo no meio (progresso 0.5) e 0 no final (progresso 1)
            arco = 4 * self.alturaParabola * self.progresso * (1 - self.progresso)

            # Subtrai o arco para fazer a bola subir na tela (Y diminui quando sobe)
            self.pontoY = y_linear - arco

            # Atualiza a caixa de colisão real
            self.rect.x = int(self.pontoX)
            self.rect.y = int(self.pontoY)
            