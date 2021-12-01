from PIL import Image
import glob
import random

#
# LOAD defs
#

ROOT_DIR = 'Uncle_Fellow/Sagittarius'
IMAGE_RESOLUTION = (1501, 1501)

layer0options = []
def load_layer0():
    print("")
    print("#layer0options")
    for filename in glob.glob(ROOT_DIR+'/00_background/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer0options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer0options)
load_layer0()

layer1options = []
def load_layer1():
    print("")
    print("#layer1options")
    for filename in glob.glob(ROOT_DIR+'/01_body/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer1options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer1options)
load_layer1()

layer2options = []
def load_layer2():
    print("")
    print("#layer2options")
    for filename in glob.glob(ROOT_DIR+'/02_atmosphere/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer2options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer2options)
load_layer2()

layer3options = []
def load_layer3():
    print("")
    print("#layer3options")
    for filename in glob.glob(ROOT_DIR+'/03_expression/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer3options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer3options)
load_layer3()

layer4options = []
def load_layer4():
    print("")
    print("#layer4options")
    for filename in glob.glob(ROOT_DIR+'/04_hat/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer4options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer4options)
load_layer4()

layer5options = []
def load_layer5():
    print("")
    print("#layer5options")
    for filename in glob.glob(ROOT_DIR+'/05_glasses/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer5options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer5options)
load_layer5()

layer6options = []
def load_layer6():
    print("")
    print("#layer6options")
    for filename in glob.glob(ROOT_DIR+'/06_accessories/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer6options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer6options)
load_layer6()

layer7options = []
def load_layer7():
    print("")
    print("#layer7options")
    for filename in glob.glob(ROOT_DIR+'/07_prop/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer7options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer7options)
load_layer7()

layer8options = []
def load_layer8():
    print("")
    print("#layer8options")
    for filename in glob.glob(ROOT_DIR+'/08_scenario/*.png'): 
        im=Image.open(filename)
        #check if correct resolution
        if(im.size == IMAGE_RESOLUTION):
            print(im.size)
            layer8options.append(im)
        else:
            print('B A D')
            print(im)
    print(layer8options)
load_layer8()

#
# RUN
#

current = 0
while current < 111: 
    # load random images for the current PFP
    layer0image = random.choice(layer0options)
    layer1image = random.choice(layer1options)
    layer2image = random.choice(layer2options)
    layer3image = random.choice(layer3options)
    layer4image = random.choice(layer4options)
    layer5image = random.choice(layer5options)
    layer6image = random.choice(layer6options)
    layer7image = random.choice(layer7options)
    layer8image = random.choice(layer8options)

    # composite all the random choices together 
    composite_image = Image.alpha_composite(layer0image.convert('RGBA'),layer1image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer2image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer3image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer4image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer5image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer6image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer7image.convert('RGBA'))
    composite_image = Image.alpha_composite(composite_image.convert('RGBA'),layer8image.convert('RGBA'))

    # save 
    new_name = ROOT_DIR + "/__Resluts/"+"HHH"+str(current)+".png"
    composite_image.save(new_name)
    print(new_name)

    # loop
    current += 1
