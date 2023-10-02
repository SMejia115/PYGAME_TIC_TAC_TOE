import pygame 
from button import Button

#Imagen de fondo 
background_image = pygame.image.load("./images/tic-tac-toe-background.jpg")

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((800,600))
  pygame.display.set_caption("TIC TAC TOE")

  #Poner imagen de fondo 
  screen.blit(background_image, [0,0])

  #Boton de titulo
  title_button = Button(100, 100, 600, 100, pygame.image.load("./images/buttons/title.png"), pygame.image.load("./images/buttons/tittle2.png"), lambda: print("Title button clicked"))
  title_button.draw(screen)

  #Boton para jugar
  play_button = Button(300, 300, 200, 100, pygame.image.load("./images/buttons/playButton1.png"), pygame.image.load("./images/buttons/playButton2.png"), lambda: print("Play button clicked"))
  title_button.draw(screen)

  #Booleano para saber si el juego esta corriendo o no
  quit_game = False

  #Ciclo para que el juego se mantenga corriendo y se actualice la pantalla
  while not quit_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game = True
      
    pygame.display.flip()

run_game()


  


