from all_of_the_blocks_list_dont_touch import all as blockslist
from PIL import Image, ImageStat
from math import sqrt

def image_grid(imgs, rows, cols):
    if len(imgs) == rows*cols:
        raise("r,c not correct")

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    i = 0
    for img in imgs:
        grid.paste(img, box=(i%cols*w, i//cols*h))
        i+= 1
    return grid

def closest_color(rgb):
    r, g, b, _ = rgb
    color_diffs = []
    texture = ""
    for color in blockslist:
        if len(color[0]) > 3:
            cr, cg, cb, _ = tuple(color[0])
        else:
            cr, cg, cb = tuple(color[0])
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

img_name = input("Enter filename with file extension [png, jpeg, jpg] like 'discord.png':\n")

src_img = Image.open(img_name)
w,h = src_img.size

texture_cache = {}

textures = []
for y in range(1,h):
    for x in range(1,w):
        texture = closest_color(src_img.getpixel((x,y)))[1]
        texloaded = None
        keyabletext = texture.replace("_","").replace(".","")
        try:
            texture_cache[keyabletext]
        except:
            texture_cache[keyabletext] = Image.open("blocks/s/" + texture)
            texloaded = texture_cache[keyabletext]
        else:
            texloaded = texture_cache[keyabletext]
        textures.append(texloaded)


image_grid(textures,h,w-1).save("final.png")