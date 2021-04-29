import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255,165,0)
green = (0,255,0)
# width and height of the window
W,H = 600,400

game_display = pygame.display.set_mode((W,H))
pygame.display.set_caption('Welcome to F.R.I.E.N.D.S!')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu',30)
score_font = pygame.font.SysFont('ubuntu',25)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, green)
    game_display.blit(text,[0,0])

def draw_snake(snake_size,snake_pixels):
    for pix in snake_pixels:
        pygame.draw.rect(game_display,white,[pix[0],pix[1],snake_size,snake_size])

def run_game():
    game_over = False
    game_close = False

    x = W/2
    y = H/2

    x_speed,y_speed = 0,0

    snake_pixels = []
    snake_len = 1

    food_x = round(random.randrange(0,W-snake_size)/10.0)*10.0
    food_y = round(random.randrange(0,H-snake_size)/10.0)*10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render('GAME OVER!1-QUIT OR 2- Restart', True, red)
            game_display.blit(game_over_message,[W/10,H/2])
            print_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    
                    if event.key == pygame.K_2:
                        run_game()

                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0

                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                    
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size

                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                
        if x >= W or x < 0 or y >= H or y < 0 :
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)

        pygame.draw.rect(game_display,orange,[food_x,food_y,snake_size,snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_len:
            del snake_pixels[0]
        
        for pix in snake_pixels[:-1]:
            if pix == [x,y]:
                game_close = True
        
        draw_snake(snake_size,snake_pixels)
        print_score(snake_len - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0,W-snake_size)/10.0)*10.0
            food_y = round(random.randrange(0,H-snake_size)/10.0)*10.0
            snake_len += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()
    
run_game()


