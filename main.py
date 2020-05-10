import pygame

pygame.init()

ventana = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption("Pong")
ancho, alto = pygame.display.get_surface().get_size()

fondobase = 245, 225, 235
colors = [(200, 0, 0), (0, 0, 200)]

pelota = pygame.image.load("ball.png")
pelotaXY = pelota.get_rect()
pelotaXY.move_ip(ancho/8, alto/8)

jugador1 = pygame.image.load("bate.png")
jugador1XY = jugador1.get_rect()
jugador1XY.move_ip(50, alto/2)

jugador2 = pygame.image.load("palazul.png")
jugador2XY = jugador2.get_rect()
jugador2XY.move_ip(ancho-50, alto/2)

tipoletra = pygame.font.Font("mifuente.ttf", 20)
tipoletrapuntos = pygame.font.Font("mifuente.ttf", 40)
puntos = [0, 0]

delta_pelota = 10
delta_jugador = 10
vector = [1, 1]
counter = 0

run = True
while run:
  fondo = fondobase

  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_ESCAPE]:
    run = False

  if (puntos[0] < 21 and puntos[1] < 21):
    if (counter == 100):
      delta_pelota += 1
      counter = 0
    counter += 1

    pelotaXY = pelotaXY.move([vector[0] * delta_pelota, vector[1] * delta_pelota])

    if pelotaXY.left < 0:
      vector[0] = -vector[0]
      puntos[1] = puntos[1] + 1
      fondo = colors[1]
    if pelotaXY.right > ancho:
      vector[0] = -vector[0]
      puntos[0] = puntos[0] + 1
      fondo = colors[0]

    if pelotaXY.top < 0 or pelotaXY.bottom > alto:
      vector[1] = -vector[1]

    if keys[pygame.K_w]:
      if (jugador1XY[1] > 0):
        jugador1XY = jugador1XY.move(0, -delta_jugador)
    if keys[pygame.K_s]:
      if (jugador1XY[1] < alto - 100):
        jugador1XY = jugador1XY.move(0, delta_jugador)

    if keys[pygame.K_UP]:
      if (jugador2XY[1] > 0):
        jugador2XY = jugador2XY.move(0, -delta_jugador)
    if keys[pygame.K_DOWN]:
      if (jugador2XY[1] < alto - 100):
        jugador2XY = jugador2XY.move(0, delta_jugador)

    if jugador1XY.colliderect(pelotaXY):
      vector[0] = 1
    if jugador2XY.colliderect(pelotaXY):
      vector[0] = -1

  ventana.fill(fondo)
  ventana.blit(tipoletra.render("Jugador 1", 0, (130, 0, 0)), (20, 20))
  ventana.blit(tipoletrapuntos.render(str(puntos[0]), 0, colors[0]), (40, 50))
  ventana.blit(tipoletra.render("Jugador 2", 0, (0, 0, 130)), (ancho - 100, 20))
  ventana.blit(tipoletrapuntos.render(str(puntos[1]), 0, colors[1]), (ancho - 60, 50))
  ventana.blit(pelota, pelotaXY)
  ventana.blit(jugador1, jugador1XY)
  ventana.blit(jugador2, jugador2XY)
  if (puntos[0] >= 21):
    ventana.blit(tipoletrapuntos.render("Ganador 1", 0, colors[0]), (ancho/2 - 100, 200))
  elif (puntos[1] >= 21):
    ventana.blit(tipoletrapuntos.render("Ganador 2", 0, colors[1]), (ancho/2 - 100, 200))

  pygame.display.update()
  pygame.display.flip()
  pygame.time.Clock().tick(60)
    
pygame.quit()