from all_of_the_blocks_list_dont_touch import all as blockslist
from PIL import Image, ImageStat
from math import sqrt
import sys

def rest():
    def image_grid(imgs, rows, cols):
        if len(imgs) == rows*cols:
            raise("r,c not correct")

        w, h = imgs[0].size
        grid = Image.new('RGB', size=(cols*w, rows*h))
        grid_w, grid_h = grid.size
        i = 0
        for img in imgs:
            sys.stdout.write(f"\r{i%cols*w}-{i//cols*h}        \t        \t")
            grid.paste(img, box=(i%cols*w, i//cols*h))
            i+= 1
        return grid

    def closest_color(rgb):
        if len(rgb) > 3:
            r, g, b, _ = rgb
        else:
            r,g,b = rgb
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
    blocks_to_skip = float(input("How many blocks should it skip? (amount of pixels to skip to reduce file size and difficulty to build, e.x. `2` would skip 2 pixels)\n"))
    w,h = src_img.size
    src_img = src_img.copy()
    src_img.thumbnail((int(w/blocks_to_skip),int(h/blocks_to_skip)))
    w,h = src_img.size

    texture_cache = {}

    textures = []
    print("Finding correct textures for colors...\n\n")
    for y in range(0,h):
        for x in range(0,w):
            texture = closest_color(src_img.getpixel((x,y)))[1]
            texloaded = None
            keyabletext = texture.replace("_","").replace(".","")
            try:
                texture_cache[keyabletext]
            except:
                sys.stdout.write(f"\rCache in {x}-{y} {keyabletext} doesn't exist! Creating...")
                texture_cache[keyabletext] = Image.open("blocks/s/" + texture)
                texloaded = texture_cache[keyabletext]
            else:
                sys.stdout.write(f"\rCache in {x}-{y} {keyabletext} exists!        \t        \t")
                texloaded = texture_cache[keyabletext]
            textures.append(texloaded)
    print("\n\nStitching textures together...\n")

    image_grid(textures,h+1,w).save("final.png")

    print("\nUsed blocks:")
    for texture in texture_cache:
        print(texture.replace("png",""))

    input("\n\nFinished, [ENTER] to restart, [CTRL] + [C] to close\n")
    rest()
rest()