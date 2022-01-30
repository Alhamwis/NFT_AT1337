import numpy as np
from PIL import Image
import os 
import random




dirname = os.path.dirname(__file__)
dimension = 480,480 # 480 * 480

for i in range(10):
    
    bg = random.sample(range(0,256), 3)
    ol =(0,0,0)
    hd =(255,229,204)
    ew =random.sample(range(0,256), 3)
    bk =random.sample(range(0,256), 3)
    ey =(255,255,255)
    
    ee = random.sample(range(0,256), 3)


    
    
    
    
    



    x = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg], 
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, ol, ew, ew, ew, ol, hd, hd, hd, ol, ew, ew, ew, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, ol, ol, ol, ew, ew, ew, ol, hd, hd, hd, ol, ew, ew, ew, ol, bg, bg, bg],
    [bg, bg, bg, bg, ol, hd, hd, hd, ol, ew, ew, ew, ol, ol, ol, ol, ol, ew, ew, ew, ol, bg, bg, bg],
    [bg, bg, bg, bg, ol, hd, hd, hd, ol, ew, ew, ew, ol, hd, hd, hd, ol, ew, ew, ew, ol, bg, bg, bg],
    [bg, bg, bg, bg, ol, hd, hd, hd, ol, ol, ol, ol, ol, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, bk, bk, bk, hd, hd, hd, hd, ol, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, bk, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, bk, bk, bk, bk, bk, bk, hd, hd, hd, hd, hd, hd, hd, bk, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, bk, bk, bk, ol, ol, ol, ol, ol, bk, bk, bk, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg] 
    ]
    y = [
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, ee, ee, ee, hd, hd, hd, hd, ee, ee, ee, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ey, ew, ew, hd, hd, hd, hd, ey, ew, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, ey, ew, ew, hd, hd, hd, hd, ey, ew, ew, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, ol, ol, ol, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, ol, ol, ol, ol, ol, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, hd, ol, ol, bk, bk, bk, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, bk, ol, bk, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, hd, ol, hd, ol, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
] 
    s = random.sample(range(0,500), 1)
    g = random.choice(s)
    if g > 250:               
    
        pixels = x
    else:
         pixels = y
            
    
    array = np.array(pixels, dtype=np.uint8) #uint8 0 255 RGB 0 255
    
    newImage = Image.fromarray(array)
    newImage = newImage.resize(dimension, resample=0)
    
    Imagename = dirname + '/AT1337/' + (str(i)) + '.png' 
    newImage.save(Imagename)
    


