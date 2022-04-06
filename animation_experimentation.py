from sense_hat import SenseHat
from time import sleep
import random

s = SenseHat()
default = True

p = (190, 174, 243)
b = (0,0,0)
w = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
#prow = [p, p, p, p, p, p, p, p] #this does not work, when replace this with a whole row
  #a pixel list must have 64 elements in it
  
  #when creating designs, helps to draw it out by hand 

default = [
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, b, p, p, p, p, b, p,
p, p, p, p, p, p, p, p,
p, p, b, p, p, b, p, p,
p, p, p, b, b, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p
]

shock_high = [
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, b, p, p, p, p, b, p,
p, p, p, b, b, p, p, p,
p, p, p, b, b, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p
]

shock_low = [
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, p, b, p, p, p, p, b,
p, p, p, p, b, b, p, p,
p, p, p, p, b, b, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p
]

lsmile_eClosed = [
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, b, b, p, p, b, b, p,
p, p, p, p, p, p, p, p,
p, p, b, p, p, b, p, p,
p, p, p, b, b, p, p, p
]

hsmile_eClosed = [
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, p, p, p, p, p, p, p,
p, b, b, p, p, b, b, p,
p, p, p, p, p, p, p, p,
p, p, b, p, p, b, p, p,
p, p, p, b, b, p, p, p,
p, p, p, p, p, p, p, p
]

def smile_nod():
  #s.clear(w)
    
  s.set_pixels(hsmile_eClosed)
  sleep(0.25)
    
  for i in range(2):
    s.set_pixels(lsmile_eClosed)
    sleep(0.25)
    s.set_pixels(hsmile_eClosed)
    sleep(0.25)

def shock():
  s.set_pixels(shock_low)
  for i in range(2):
    sleep(0.25)
    s.flip_h()
    
def random():#may work in actual environment, as its a browser, may not import all things 
  while True:
    rand_face = []
    for i in range(64):
      rand1 = random.randint(0, 255)
      rand2 = random.randint(0, 255)
      rand3 = random.randint(0, 255)
      r_colour = (rand1, rand2, rand3)
  
      #rand_face.append(rand)
      
    s.set_pixels(rand_face)
    sleep(0.5)
    
  

#s.show_message("Hello", text_colour = yellow, back_colour = blue)
s.set_pixels(default)
sleep(0.25)

default = False

print(random.randint(0,9))
  
if default == False:
  #could do, if previous state == default, for more fluid animation
  #could pass the previous display as a paramter
  
  smile_nod()
  sleep(0.25) #if you dont use this sleep funct, program may miss out the next line 
  #as there is no break, skips next line
  
  shock()
  
  random()
  
  
  
  
