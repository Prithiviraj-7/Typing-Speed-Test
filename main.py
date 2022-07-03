import pygame
import random
import time
import math

pygame.init()

screen = pygame.display.set_mode([1000,700])

background_color = (255,255,255)
title_color = (0,0,255)
text_color = (0,0,0)
sky_blue = (135,206,235)
title_font = pygame.font.Font(None,72)
subtitle_font = pygame.font.Font(None,48)
text_font = pygame.font.SysFont('cambria',28)

def get_sentences():
    f = open("sentences.txt",'r')
    text = f.read()
    sentences = text.split('\n')
    sentence = random.choice(sentences)
    f.close()
    return sentence

def speed_test(sentence,input_text,time_elapsed,keystrokes):
    count = 0
    for i,character in enumerate(sentence):
        try:
            if input_text[i] == character:
                count += 1
        except:
            pass
    
    accuracy = count/len(input_text)*100
    accuracy = "{:.2f}".format(accuracy)

    words = sentence.split()
    input_words = input_text.split()
    correct_words = 0

    for i,word in enumerate(words):
        try:
            if words[i] == input_words[i]:
                correct_words += 1
        except:
            pass
    
    incorrect_words = len(input_words) - correct_words

    wpm = len(input_words)*60/time_elapsed
    wpm = math.floor(wpm)

    screen.fill(sky_blue)

    value = title_font.render("RESULTS",True,text_color)
    screen.blit(value,(390,100))
    value_1 = title_font.render(str(wpm)+" WPM",True,(0,100,0))
    value_2 = text_font.render("(words per minute)",True,text_color)
    value_3 = text_font.render("Accuracy                 " +str(accuracy)+"%",True,text_color)
    value_4 = text_font.render("Correct words               " +str(correct_words),True,text_color)
    value_5 = text_font.render("Incorrect words            " +str(incorrect_words),True,text_color)
    value_6 = text_font.render("Keystrokes                     " +str(keystrokes),True,text_color)
    value_7 = text_font.render("Reset",True,text_color)
    image = pygame.image.load(r'reset.png')
    image = pygame.transform.scale(image,(75,75))
    screen.blit(value_1,(400,200))
    screen.blit(value_2,(380,250))
    screen.blit(value_3,(350,350))
    screen.blit(value_4,(350,400))
    screen.blit(value_5,(350,450))
    screen.blit(value_6,(350,500))
    screen.blit(image,(450,550))
    screen.blit(value_7,(550,565))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] > 450 and pos[0] < 525 and pos[1] > 550 and pos[1] < 625:
                    test_screen()
    return            


def run(sentence):
    input_text = ""
    flag = 1
    keystrokes = 0
    while True:
        value = text_font.render(input_text,True,text_color)
        pygame.draw.rect(screen,background_color,(50,350,900,200))
        screen.blit(value,(75,400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            if event.type == pygame.KEYDOWN:
                if flag == 1:
                    start_time = time.time()
                    flag = 0
                if event.key == pygame.K_BACKSPACE:
                    keystrokes += 1
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    time_elapsed = time.time() - start_time
                    speed_test(sentence,input_text,time_elapsed,keystrokes)
                    return
                else:
                    keystrokes += 1
                    input_text = input_text + event.unicode
        pygame.display.update()       

def test_screen():
    screen.fill(sky_blue)

    value_1 = title_font.render("TYPING TEST",True,text_color)
    screen.blit(value_1,(350,100))

    #for i in range(3):
    pygame.draw.rect(screen,background_color,(50,200,900,100))
    sentence = get_sentences()
    value = text_font.render(sentence,True,text_color)
    screen.blit(value,(75,240))  
    pygame.draw.rect(screen,background_color,(50,350,900,200))
    pygame.display.update()
    run(sentence)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def title_screen():
    pygame.display.set_caption("TYPING TEST")
    screen.fill(background_color)

    value_1 = title_font.render("TYPING SPEED TEST",True,title_color)
    screen.blit(value_1,(250,100))

    image_1 = pygame.image.load(r'title_page.jpg')
    screen.blit(image_1,(250,200))

    value_2 = subtitle_font.render("Press ENTER to continue",True,title_color)
    screen.blit(value_2,(250,550))

    image_2 = pygame.image.load(r'enter_key.jpg')
    image_2 = pygame.transform.scale(image_2,(150,150))
    screen.blit(image_2,(670,500))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] > 680 and pos[0] < 810 and pos[1] > 520 and pos[1] < 615:
                    test_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    test_screen()


title_screen()
pygame.quit()