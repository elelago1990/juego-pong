import pygame
pygame.init()

#colores

BLANCO = ( 255, 255, 255)
ROJO = ( 255, 0, 0)
VERDEOSC = ( 3, 44, 16)

#fin lista de colores
#jugador
player_height = 90
player_width = 15
#fin jugador
#pantalla
size = (800,600)
ventana = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#coordenadas y velocidad jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0
#coordenadas y velocidad jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

#coordenadas de la pelota
pelota_x = 400
pelota_y = 300

pelota_speed_x = 3
pelota_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            # jugador 1 
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3

            # jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3


        if event.type == pygame.KEYUP:
            # jugador 1 
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0

            # jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
    
    if pelota_y > 590 or pelota_y < 10: 
        pelota_speed_y *= -1
    # revisar si la pelota sale del lado derecho
    if pelota_x > 800: 
        pelota_x = 400
        pelota_y = 300
        # invertir direccion si sale de la pantalla
        pelota_speed_x *= -1
        pelota_speed_y *= -1

    # revisar si la pelota sale del lado izquierdo
    if pelota_x < 0: 
        pelota_x = 400
        pelota_y = 300
        # invertir direccion si sale de la pantalla
        pelota_speed_x *= -1
        pelota_speed_y *= -1



    # modificas las coordenadas para que se muevan los jugadores/pelota
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed 
    #movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    ventana.fill(VERDEOSC)
    #zona de dibujo ----------------------------
    jugador1 = pygame.draw.rect(ventana, ROJO, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(ventana, ROJO, (player2_x_coor, player2_y_coor, player_width, player_height))

    pelota = pygame.draw.circle(ventana, BLANCO,(pelota_x,pelota_y), 10)
    #colisiones

    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)
pygame.quit()