import pygame, sys 
from pygame.math import Vector2
import random
 
 

#RGB-VÄRIT
BACKROUND_PURPLE = ( 247, 141, 195 )
DARK_PURPLE = (150, 5, 81)
PURPLE = ( 250, 112, 163 )
SNAKE_PURPLE = (222, 38, 134)
FONTTI =  "agencyfb"
 
 
class Kolikko:
    def __init__(self, kaarmeen_tila):
        self.kolikko = pygame.transform.scale(pygame.image.load("kolikko.png"), (23, 23))
        self.sijainti = self.aseta_kolikko(kaarmeen_tila)
 
    def satunnainen_sijainti(self): 
        x = random.randint(1, 23-2)
        y = random.randint(3, 25-2)
        return Vector2(x, y)
 
    def aseta_kolikko(self, kaarmeen_tila): 
        paikka = self.satunnainen_sijainti()
        while paikka in kaarmeen_tila:
            paikka = self.satunnainen_sijainti()
        return paikka
 
    def piirra_ruudulle(self, naytto, nelio): 
        kolikon_kuutio = pygame.Rect((self.sijainti.x * nelio), (self.sijainti.y * nelio), nelio, nelio)
        naytto.blit(self.kolikko, kolikon_kuutio)
    
 
 
class Snake:
    def __init__(self):
        self.palaset = [Vector2(4, 13), Vector2(3, 13), Vector2(2, 13)]
        self.suunta = Vector2(1, 0)
        self.lisaa_pituutta = False
 
    def restart(self): 
        self.palaset = [Vector2(4, 13), Vector2(3, 13), Vector2(2, 13)]
        self.suunta = Vector2(1, 0)
 
    def liikuta_kaarmetta(self): 
        self.palaset.insert(0, self.palaset[0] + self.suunta)
        if self.lisaa_pituutta == True:
            self.lisaa_pituutta = False
        else:
            self.palaset = self.palaset[:-1]
 
    def piirra_ruudulle(self, naytto, nelio):
        for pala in self.palaset:
            kaarme_pala = ((pala.x * nelio), (pala.y * nelio), nelio, nelio)
            pygame.draw.rect(naytto, SNAKE_PURPLE,  kaarme_pala, 0, 4)
            pygame.draw.rect(naytto, DARK_PURPLE, kaarme_pala, 1, 4)
 
 
 
class SnakeGame:
    def __init__(self):
        pygame.init() 
 
        self.kello = pygame.time.Clock()
        self.tila = False
    
        self.korkeus, self.leveys = 23*23, 23*25  
        self.naytto = pygame.display.set_mode((self.korkeus, self.leveys))
        
        self.sivu_px = 500
        self.ruutu_tausta_k = pygame.Surface((self.sivu_px, self.sivu_px))
        self.ruutu_tausta_k.fill(BACKROUND_PURPLE)
 
        self.ruutu = 21
        self.nelio = self.sivu_px // self.ruutu  
        self.__round, self.__score, self.__high_score = 1, 0, 0
 
        self.mato = Snake()
        self.coin = Kolikko(self.mato.palaset)
        self.main()
 
 
    def score_function(self):
        self.__score += 1    
        if self.__score == (21*21)-3:
            self.game_over()
 
 
    def new_record(self, tulos: int):
        if tulos > self.__high_score:
            self.__high_score = tulos
 
 
    def round_function(self):
        self.__round += 1
        if self.__round == 1000:
            self.__round = 1
 
 
    def piirra_taustaruudukko(self, area): 
        for rivi in range(self.ruutu):
            for sarake in range(self.ruutu):
                kaava = pygame.Rect(rivi * self.nelio, sarake * self.nelio, self.nelio, self.nelio)
                if (rivi+sarake) % 2 == 0:
                    pygame.draw.rect(area, PURPLE, kaava)
                else:
                    pygame.draw.rect(area, BACKROUND_PURPLE, kaava)
 
        seinat = [((0, 0), (0, 483)), ((0, 0), (483, 0)), ((0, 483), (483, 483)), ((483, 483), (483, 0))]
        [pygame.draw.line(area, DARK_PURPLE, i[0], i[1], 2) for i in seinat]
 
 
    def piirra_kaikki_tapahtumat(self):
        def naytto_asetukset(self):
            pygame.display.set_caption("Snake Game")
            fontti = pygame.font.SysFont(FONTTI, 26)
 
            self.naytto.fill(BACKROUND_PURPLE)
            self.piirra_taustaruudukko(self.ruutu_tausta_k) 
            self.naytto.blit(self.ruutu_tausta_k, (23, 23*3)) 
 
            tekstit = [ ("SNAKE GAME", (21, 21)), (f"ROUND: {self.__round}", (21*7, 21)),
            (f"SCORE: {self.__score}", (21*12, 21)), (f"HIGH SCORE: {self.__high_score}", (21*17, 21))]
            [self.naytto.blit(fontti.render(i[0], True, DARK_PURPLE), i[1]) for i in tekstit]
        naytto_asetukset(self)
 
        def hahmo_asetukset(self):
            self.mato.piirra_ruudulle(self.naytto, self.nelio)
            self.coin.piirra_ruudulle(self.naytto, self.nelio)
        hahmo_asetukset(self)
 
   
    def paivita_naytto(self):
        if self.tila: 
            def points_tapaus(self): 
                if self.mato.palaset[0] == self.coin.sijainti:
                    self.coin.sijainti = self.coin.aseta_kolikko(self.mato.palaset)   
                    self.mato.lisaa_pituutta = True
                    self.score_function()
            points_tapaus(self)
 
            def tarkista_ruutuun_tormays(self): 
                if self.mato.palaset[0].x == (self.ruutu + 1) or self.mato.palaset[0].x == 0:
                    self.game_over()
                    self.mato.restart()
                if self.mato.palaset[0].y == (self.ruutu + 3) or self.mato.palaset[0].y == 2:
                    self.game_over()
                    self.mato.restart()
            tarkista_ruutuun_tormays(self)
 
            def tarkista_hantaan_tormays(self):
                tail = self.mato.palaset[1:]
                if self.mato.palaset[0] in tail:
                    self.game_over() 
            tarkista_hantaan_tormays(self)
 
            self.mato.liikuta_kaarmetta() 
 
 
    def game_over(self):
        self.tila = False
        self.mato.restart()
        self.round_function()
        self.coin.sijainti = self.coin.aseta_kolikko(self.mato.palaset)
        self.new_record(self.__score)
        self.__score = 0
 
 
    def main(self): 
        KAARMEEN_NOPEUS = pygame.USEREVENT
        pygame.time.set_timer(KAARMEEN_NOPEUS, 145) # <- nopeutta voi säätää
 
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
                elif tapahtuma.type == KAARMEEN_NOPEUS: 
                    self.paivita_naytto() 
 
                elif tapahtuma.type == pygame.KEYDOWN:
                    if self.tila == False:
                        self.tila = True
 
                    elif (tapahtuma.key == pygame.K_UP or tapahtuma.key == pygame.K_w) and self.mato.suunta != Vector2(0, 1):
                            self.mato.suunta = Vector2(0, -1) 
 
                    elif (tapahtuma.key == pygame.K_DOWN or tapahtuma.key == pygame.K_s) and self.mato.suunta != Vector2(0, -1):
                        self.mato.suunta = Vector2(0, 1)
 
                    elif (tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a) and self.mato.suunta != Vector2(1, 0):
                        self.mato.suunta = Vector2(-1, 0) 
                    
                    elif (tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d) and self.mato.suunta != Vector2(-1, 0):
                        self.mato.suunta = Vector2(1, 0) 
 
            self.piirra_kaikki_tapahtumat()  
            pygame.display.flip()
            self.kello.tick(60)
 
SnakeGame()
