import pygame
import random


pygame.init()

# setting the game window 
window_width = 800
window_height = 600

# set the display mode
window = pygame.display.set_mode((window_width, window_height))
# set the caption 
pygame.display.set_caption("Pygame Demo")

# set the colors
white =(255,255,255)
black =(0,0,0)
red = (255,0,0)
# gameover bool
game_over = False

# adjusted snake head positions
x1= window_width/2
y1= window_height/2

# change in x1, y1
x1_change =0
y1_change =0

# length of snake , score , snakebody
length_of_snake =1
score = 0
snake_body=[]


# snake touch window game stops
if x1 >= window_width or x1 < 0 or y1>=window_height or y1 <0 :
    game_over =True

# check frame rate
clock = pygame.time.Clock()

# Randomized food positions
food_x = round(random.randrange(0,window_width-10)/10) *10
food_y = round(random.randrange(0,window_height-10)/10) *10

#running event loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True
        #check for arrow keys press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0   
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0   
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10   
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10   

    #adjust x1 changes
    x1 += x1_change
    y1 += y1_change   
    #fill window black 
    window.fill(black)     
    

    # contain the length of the snake while travesing to just length of the snake.
    
    snake_head = []
    # append every single x1, y1
    snake_head.append(x1)
    snake_head.append(y1)
    # add it to snake head
    snake_body.append(snake_head)

    # for every x1,y1 added to snake head and then added to snakebody tuple.
    # start deleting the entries from the beginning if the snakebody exceeds snake_length
    if len(snake_body) > length_of_snake:
        del snake_body[0]
    # if snake touches itself, then it is gameover
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over=True
    
    # display score on the screen using blit
    font_style = pygame.font.SysFont(None,50)
    score_text = font_style.render("Score: "+str(score),True,white)
    window.blit(score_text,(10,10))

    # snake eats food then add new randomized food locations and update lenght and score 
    if x1 == food_x and y1==food_y:
        food_x = round(random.randrange(0,window_width-10)/10) *10
        food_y = round(random.randrange(0,window_height-10)/10) *10
        length_of_snake += 1
        score +=1

    #Draw food and snake location on screen
    pygame.draw.rect(window,red,[food_x,food_y,10,10])
    #pygame.draw.rect(window,white,[x1,y1,10,10])
    for segment in snake_body:
        pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
        if x1 >= window_width or x1 < 0 or y1>=window_height or y1 <0:
            game_over =True
    
    # update display 
    pygame.display.update()
    

    clock.tick(15)