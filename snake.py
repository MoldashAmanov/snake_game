import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)
blue = (50, 153, 213)

display_width = 800
display_height = 600
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Змейка")



snake_block = 10 # Стандартная величина сдвига при нажатии клавиши


clock = pygame.time.Clock()
snake_speed = 15 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Ваш счет: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def message(msg, color): 
    """Функция, показывающая сообщения на игровом поле"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width/2, display_height/2])


def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False
    x1 = display_width/2 # Указываем начальное значение положения по оси х
    y1 = display_height/2 # Указываем начальное значение положения по оси у
    x1_change = 0 # В цикле while будут присваиваться значения изменения положения
    y1_change = 0 # В цикле while будут присваиваться значения изменения положения
    snake_list = [] # Список с текущей длиной змейки
    length_of_snake = 1
    # Переменная, в которой хранится расположение еды по оси х
    foodx = round(random.randrange(0, display_width - snake_block)/10.0) * 10.0
    # Переменная, в которой хранится расположение еды по оси н
    foody = round(random.randrange(0, display_height - snake_block)/10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("Вы проиграли! Нажмите Q для выхода или С для повторной игры", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block # Значение в пикселах
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # Условие, если змейка выходит за рамки экрана
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = [] # Длина змейки при движении
        snake_head.append(x1) # Добавляем значение при изменении по оси х
        snake_head.append(y1) # Добавляем значение при изменении по оси у
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block)/10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
game_loop()




