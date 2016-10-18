#Importing the necessary librarys

import sys
import pygame
import time
from pygame import *
from graphics import*
pygame.init()

#Defining variables such as colors, score, speed, windows size etc.

h = 1 
s1 = 1
s2 = 1
score1 = 0
score2 = 0
screen = x, y = 800, 600
black = 0, 0, 0
white = 255, 255, 255

#Creating the window and ball

win = pygame.display.set_mode(screen)
ball = pygame.image.load("ball.jpg")
ballimg = ball.get_rect()

a = 240 # Y-value for paddle 1
b = 240 # Y-value for paddle 2

def p1(a): #paddle 1
    pygame.draw.rect(win, white, (0, a, 20, 120), 0)
def p2(b): #paddle 2
    pygame.draw.rect(win, white, (780, b, 20, 120), 0)

def scorescreen(win, ballimg, scorewin): #Defines the scorescreen with all of the text

    #Creates a font and lists that are about to become strings
    font = pygame.font.Font(None, 50)
    textlist = ["Game Over. Player", scorewin[2], "wins!"]
    scorelist = ["The score is now", scorewin[0], "to", scorewin[1]]

    #Converts the lists to strings
    texttext = ' '.join(str(x) for x in textlist)
    scoretext = ' '.join(str(y) for y in scorelist)

    #Loads the text
    text1 = font.render(texttext, 1, (255,255,255))
    text2 = font.render(scoretext, 1, (255,255,255))
    text3 = font.render("Do you want to play again? [y/n]", 1, (255,255,255))

    #Positions all the text
    textp1 = text1.get_rect()
    textp1.centerx = win.get_rect().centerx
    textp1.centery = win.get_rect().centery - 100

    textp2 = text2.get_rect()
    textp2.centerx = win.get_rect().centerx
    textp2.centery = win.get_rect().centery 
    
    textp3 = text3.get_rect()
    textp3.centerx = win.get_rect().centerx
    textp3.centery = win.get_rect().centery + 100

    win.blit(text1, textp1) #"Draws" the text onto the screen
    pygame.display.flip()   
    time.sleep(1)           #Delays parts of the text so that one row shows up at a time
    win.blit(text2, textp2) 
    pygame.display.flip()   #Updates the entire screen to show the text
    time.sleep(1)           
    win.blit(text3, textp3) 
    pygame.display.flip()
    
    while True: 				#Makes the program wait
        pygame.event.wait() 	#Nothing happens until you press a key
        keys = pygame.key.get_pressed()
        if keys[K_y] == True: 	#If you press "Y" you play again
            ballimg.left = 1  	#The position of the ball is reset
            ballimg.top = 1
            return 1
            break

        elif keys[K_n] == True: #If you press "N", h = 0 and the program exits
            return 0
            break


while h == True: #The main loop of the game, while "h" is true, the game continues to run

    ballimg = ballimg.move(s1, s2)  #Moving the ball
     
    keys = pygame.key.get_pressed() #Checks if any keys are pressed

    if b <= 0:      #Stops the paddles from going outside the window
        b = 0       #                     --||--
    if b >= 480:    #                     --||--
        b = 480     #                     --||--
    if a <= 0:      #                     --||--
        a = 0       #                     --||--
    if a >= 480:    #                     --||--
        a = 480     #                     --||--

    if keys[K_UP] == True:      #Moves the paddles
        b = b - 1               #     --||--
    if keys[K_DOWN] == True:    #     --||--
        b = b + 1               #     --||--
    if keys[K_w] == True:       #     --||--
        a = a - 1               #     --||--
    if keys[K_s] == True:       #     --||--
        a = a + 1               #     --||--
        

    if ballimg.left < 20 and ballimg.top >= a - 35 and ballimg.bottom <= a + 155:    #Makes the ball bounce on the paddles         				
        if s1 < 0:
            s1 = -s1
        
    if ballimg.right > 780 and ballimg.top >= b - 35 and ballimg.bottom <= b + 155:  #Makes the ball bounce on the paddle
        if s1 > 0:
            s1 = -s1


    if ballimg.left == 0:  #Ends the game and gives player 2 a point and goes to the score screen
        score2 += 1
        h = scorescreen(win, ballimg, [score1, score2, 2])
        if h == 1:
	        s1 = 1			#resets the direction of the ball
	        a = 240			#resets the position of the paddles
	        b = 240

    if ballimg.right == x: #Ends the game and gives player 1 a point and goes to the score screen
        score1 += 1
        h = scorescreen(win, ballimg, [score1, score2, 1])
        if h == 1:
	        s1 = 1			#resets the direction of the ball
	        a = 240			#resets the position of the paddles
	        b = 240

    if ballimg.top == 0  or ballimg.bottom == y: #Makes the ball bounce from the top and bottom
        s2 = -s2
    

    win.fill(black) #After every ball "tick" the screen makes everything black to cover the ball "trace"
    win.blit(ball, ballimg) #Draws the ball over and over again
    p1(a) #Calls the paddle 1 function
    p2(b) #Calls the paddle 2 function
    pygame.display.flip() #Updates the entire window

    for event in pygame.event.get(): #Gives you the ability to quit the game by pressing "[Esc]"
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE] == True: #If you press escape, h = false and the main loop ends
            h = False

    pygame.time.delay(1)

pygame.quit() #Exits pygame
sys.exit()    #Closes the program
        
