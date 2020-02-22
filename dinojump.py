# Comp id: vw8fn
# name: Gina Wilson

# import statements
import pygame
import gamebox
import random

# creating the frame
camera = gamebox.Camera(800, 600)

# DINO
dino = gamebox.from_color(50, 570, "red", 10, 10)

# GROUND
ground = gamebox.from_color(400, 600, "tan", 1000, 50)

# Variables
score = 0
dino_gravity = 1


game_on = True

cacti = [
        gamebox.from_color(300, 555, "darkgreen", 5, 40),
        gamebox.from_color(700, 560, "darkgreen", 5, 50),
    ]

clouds = [
        gamebox.from_color(100, 400, "white", 10, 10),
        gamebox.from_color(300, 200, "white", 10, 10),
        gamebox.from_color(500, 300, "white", 10, 10),
        gamebox.from_color(700, 500, "white", 10, 10),
    ]

tumbleweeds = [
        gamebox.from_color(100, 575, "brown", 5, 5),
        gamebox.from_color(200, 585, "brown", 5, 5),
        gamebox.from_color(300, 580, "brown", 5, 5),
        gamebox.from_color(400, 595, "brown", 5, 5),
        gamebox.from_color(500, 590, "brown", 5, 5),
        gamebox.from_color(600, 595, "brown", 5, 5),
        gamebox.from_color(700, 575, "brown", 5, 5),
        gamebox.from_color(800, 595, "brown", 5, 5),
    ]

# This is the function

def tick(keys):
    """This function takes in one argument and displays an animated dino jumping game

    params:
    keys: this is a set: if the key is a space, it will cause the dino to jump"""
    global score, game_on, counter, button_press, dino_gravity
    # ------- INPUT ---------
    # We want the game to start when the space bar
    # is pressed
    if game_on == True:
        if pygame.K_SPACE in keys and dino.touches(ground) == True:
            dino.yspeed -= 20
        if dino.touches(ground) == False:
            dino.yspeed += dino_gravity
        dino.move_to_stop_overlapping(ground)

        dino.move_speed()
        keys.clear()

        camera.clear("lightblue")
        camera.draw(dino)
        camera.draw(gamebox.from_text(400, 100, "Score: " + str(score), 40, "black", bold=True))

        camera.draw(ground)

        camera.draw(cacti[0])
        camera.draw(cacti[1])
        cacti[0].x -= 2
        cacti[1].x -= 2

        camera.draw(clouds[0])
        camera.draw(clouds[1])
        camera.draw(clouds[2])
        camera.draw(clouds[3])
        clouds[0].x -= 1
        clouds[1].x -= 1
        clouds[2].x -= 1
        clouds[3].x -= 1

        camera.draw(tumbleweeds[0])
        camera.draw(tumbleweeds[1])
        camera.draw(tumbleweeds[2])
        camera.draw(tumbleweeds[3])
        camera.draw(tumbleweeds[4])
        camera.draw(tumbleweeds[5])
        camera.draw(tumbleweeds[6])
        camera.draw(tumbleweeds[7])
        tumbleweeds[0].x -= 2
        tumbleweeds[1].x -= 2
        tumbleweeds[2].x -= 2
        tumbleweeds[3].x -= 2
        tumbleweeds[4].x -= 2
        tumbleweeds[5].x -= 2
        tumbleweeds[6].x -= 2
        tumbleweeds[7].x -= 2

        if cacti[0].x <= 0:
            height = random.randint(-10, 10)
            dist = random.randint(-100, 100)
            cactus1 = gamebox.from_color(900, 560, "darkgreen", 5, 50)
            cactus1.y += height
            cactus1.x += dist
            cacti.remove(cacti[0])
            cacti.append(cactus1)

        if clouds[0].x == 0:
            elevation = random.randint(-100, 100)
            cloud1 = gamebox.from_color(850, 300, "white", 10, 10)
            cloud1.y += elevation
            clouds.remove(clouds[0])
            clouds.append(cloud1)

        if tumbleweeds[0].x == 0:
            depth = random.randint(-10, 10)
            tumbleweed1 = gamebox.from_color(850, 587, "brown", 5, 5)
            tumbleweed1.y += depth
            tumbleweeds.remove(tumbleweeds[0])
            tumbleweeds.append(tumbleweed1)


        # ----- SCORING ------
        if dino.touches(ground) == True or dino.touches(ground) == False:
            score += 1
            camera.draw(gamebox.from_text(400, 100, "Score: " + str(score), 40, "black", bold=True))


        # ----- COLLISION DETECTION -----
        # If the dino touches a cactus, the game ends
        for cactus in cacti:
            if dino.touches(cactus):
                game_on = False
                camera.draw(gamebox.from_text(400, 300, "You Lose!", 100, "Yellow", bold=False))

    else:
        if pygame.K_SPACE in keys:
            score = 0
            cacti.remove(cacti[0])
            cactus1 = gamebox.from_color(300, 555, "darkgreen", 5, 40)
            cacti.append(cactus1)
            cacti.remove(cacti[1])
            cactus2 = gamebox.from_color(700, 560, "darkgreen", 5, 50)
            cacti.append(cactus2)

            game_on = True



    #displays the image
    camera.display()

ticks_per_second = 60

# invokes the function
gamebox.timer_loop(ticks_per_second, tick)