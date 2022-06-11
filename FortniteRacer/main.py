import pygame
import keyboard

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

clock = pygame.time.Clock()
FPS = 30
run = True

while(run == True):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    joystick = pygame.joystick.Joystick(0)
    wheel = joystick.get_axis(0)
    pedals = joystick.get_axis(1)

    brake = joystick.get_button(7)
    radio = joystick.get_button(1)
    nextstation = joystick.get_button(0)
    boost = joystick.get_button(8)
    if(wheel > 0.0):
        keyboard.press("d")
    if(wheel < 0.0):
        keyboard.press("a")

    if(pedals < 0.0):
        keyboard.press("w")
    if(pedals > 0.0):
        keyboard.press("s")

    if(brake == 1):
        keyboard.press("space")
    if(radio == 1):
        keyboard.press("r")
    if(nextstation == 1):
        keyboard.press("c")
    if(boost == 1):
        keyboard.press("shift")

    pygame.time.wait(50)
    keyboard.release("d")
    keyboard.release("a")
    keyboard.release("w")
    keyboard.release("s")
    keyboard.release("space")
    keyboard.release("r")
    keyboard.release("c")
    keyboard.release("shift")