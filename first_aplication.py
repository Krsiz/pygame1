from pygame import *
# westrtfhyjguhkijkl,;
window = display.set_mode((700, 500))
display.set_caption("First project")
#character coordinates
x = 100
y = 395
#character and background image
img1 = transform.scale(image.load('monkey_003.png'), (100, 100))
background = transform.scale(image.load("fail_1.jpg"), (700,500))
#we place the images on the application window
window.blit(background,(0,0))
window.blit(img1, (x,y))

display.update()

run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_w:
                print('up')
                y = y - 10
                window.blit(img1, (x,y))
                display.update()

        if e.type == KEYDOWN:
            if e.key == K_s:
                print('down')
                y = y + 10
                window.blit(img1, (x,y))
                display.update()

        if e.type == KEYDOWN:
            if e.key == K_a:
                print('left') 
                x = x - 10
                window.blit(img1, (x,y))
                display.update()

        if e.type == KEYDOWN:
            if e.key == K_d:
                print('right') 
                x = x + 10
                window.blit(img1, (x,y))
                display.update()


        if e.type == QUIT:
            quit()
            run = False

time.delay(5000)