from roboid import *
import keyboard
import random

hamster = Hamster()

timer = False
time = 0

racing_timer = False
racing_time = 0
racing_sec = 0

is_using_skill = False
skill_timer = False
skill_time = 100
skill_cooltimer = False
skill_cooltime = 0

led = False
music = False

is_forward = False
is_backward = False

while True:
    if racing_timer == True:
        racing_time += 1

    if racing_time == 50:
        racing_sec += 1
        racing_time = 0
    
    if timer == True:
        time += 1

    if skill_timer:
        skill_time -= 1

    if skill_cooltimer == True:
        skill_cooltime -= 1

    if skill_time == 0:
        is_using_skill = False
        skill_timer = False
        skill_time = 100
        skill_cooltime = 500
        skill_cooltimer = True
    
    if skill_cooltime == 0:
        skill_cooltimer = False

    if led == True:
        hamster.leds(random.randint(1, 7), random.randint(1, 7))
        wait(50)
    else:
        hamster.leds(0, 0)

    if keyboard.is_pressed('up'):
        racing_timer = True
        if is_using_skill == True:
            skill_timer = True
            speed = 100
        else:
            timer = True
            speed = 35 + time
        hamster.wheels(speed, speed)
        is_forward = True
    else:
        timer = False
        time = 0
        speed = 0
        hamster.stop()
        is_forward = False
        is_backward = False
        led = False
        music = False
        
    if keyboard.is_pressed('down'):
        hamster.wheels(-50, -50)
        is_backward = True

    if is_forward == True:
        if keyboard.is_pressed('left'):
            hamster.wheels(50, 100)
        elif keyboard.is_pressed('right'):
            hamster.wheels(100, 50)
    elif is_backward == True:
        if keyboard.is_pressed('left'):
            hamster.wheels(-50, -100)
        elif keyboard.is_pressed('right'):
            hamster.wheels(-100, -50)
    else:
        if keyboard.is_pressed('left'):
            hamster.wheels(-50, 50)
        elif keyboard.is_pressed('right'):
            hamster.wheels(50, -50)

    if keyboard.is_pressed('space'):
        if skill_cooltime == 0:
            is_using_skill = True

    wait(20)