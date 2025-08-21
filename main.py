'''this program serve as the final project, focusing on the creation a GIF image'''

import imageio.v3 as iio

def gif_animation(pic_1, pic_2, pic_3, pic_4, gif_name_file):
    '''A function to process a collection of images into a GIF'''
    
    filenames = [pic_1, pic_2, pic_3, pic_4]
    images = []

    for filenames in filenames:
        images.append(iio.imread(filenames))

    iio.imwrite(gif_name_file, images, duration=500, loop=0)

gif_animation("dino1.png", "dino2.png", "dino3.png", "dino4.png", "result_gif.gif")
