# from __future__ import division
# import pygame
# from pygame.locals import *

# def iterate(z, c, k=0):
#     step = 536.842 / (k + 13.42)
#     if k > 255:
#         return 255 
#     elif abs(z) > 2:
#         return int(k * k / 255)
#     return iterate(z ** 2 + c, c, k + step)

# scale = 80
# mx0, jx0, y0 = -2.5, -1.9, -1.5

# W, H = 600, -int(2 * y0 * scale)
# jW, jH = 300, H
# jX, jY = 0, 0
# mW, mH = W - jW, H
# mX, mY = jX + jW, 0

# pygame.init()
# screen = pygame.display.set_mode((W, H), 0, 32)
# screen.fill((0, 0, 0))
# pygame.draw.rect(screen, (64, 64, 64), (mX, 0, 6, H), 0)
# pygame.display.update()


# for x in range(7, mW): # Mandelbrot
#     for y in range(mH):
#         c = x / scale + mx0 + 1j * (y / scale + y0)
#         k = iterate(0, c)
#         screen.set_at((x + mX, H - y + mY), (k, k, k))
#     pygame.display.update()

# mainloop = True
# while mainloop:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             mainloop = False
#     x, y = pygame.mouse.get_pos()
#     cx = (x - mX) / scale + mx0
#     cy = (H - y - mY) / scale + y0
#     c = cx + cy * 1j
#     for x in range(jW): # Julia
#         for y in range(jH):
#             k = iterate(x / scale + jx0 + (y / scale + y0) * 1j, c)
#             screen.set_at((x + jX, H - y + jY), (k, k, k))
#     t = pygame.font.SysFont("monospace", 14)
#     text = "C = %s + %si" % (round(cx, 3), round(cy, 3))
#     t1 = t.render(text, 0, (128, 128, 128))
#     screen.blit(t1, (0, 0)) 
#     pygame.display.update()
# pygame.quit()



# Python code for Julia Fractal
from PIL import Image
   
# driver function
if __name__ == "__main__":
    
    # setting the width, height and zoom 
    # of the image to be created
    w, h, zoom = 1920,1080,1
   
    # creating the new image in RGB mode
    bitmap = Image.new("RGB", (w, h), "white")
  
    # Allocating the storage for the image and
    # loading the pixel data.
    pix = bitmap.load()
     
    # setting up the variables according to 
    # the equation to  create the fractal
    cX, cY = -0.7, 0.27015
    moveX, moveY = 0.0, 0.0
    maxIter = 255
   
    for x in range(w):
        for y in range(h):
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
            i = maxIter
            while zx*zx + zy*zy < 4 and i > 1:
                tmp = zx*zx - zy*zy + cX
                zy,zx = 2.0*zx*zy + cY, tmp
                i -= 1
  
            # convert byte to RGB (3 bytes), kinda 
            # magic to get nice colors
            pix[x,y] = (i << 21) + (i << 10) + i*8
  
    # to display the created fractal
    bitmap.show()