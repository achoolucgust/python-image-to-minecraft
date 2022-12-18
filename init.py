import zipfile
import pathlib
import os
import shutil
from PIL import Image, ImageStat

colors = []

input("\n\n1. Find a version in your .minecraft folder. By default:\n%%appdata%%/Roaming/.minecraft\nAnd find a '.jar' file.\n\n2. if that doesn't exist, your picking a snapshot.\nTry using a flat version like 1.19.2 instead of 1.19.2-pre\n\n3. Copy and Paste that file to this folder imagetoblock\n\n4. Rename this JAR file to version.zip\n\n5. Press [Enter]\n\n")

print("Opening version.zip...")
archive = zipfile.ZipFile('version.zip')
print("Copying Block Textures...")
PREFIX = 'assets/minecraft/textures/block'
out = pathlib.Path('blocks/')
for archive_item in archive.namelist():
    if archive_item.startswith(PREFIX):
        print(archive_item)
        destpath = out.joinpath(archive_item[len(PREFIX):])
        os.makedirs(destpath.parent, exist_ok=True)
        with archive.open(archive_item) as source, open(destpath, 'wb') as dest:
            shutil.copyfileobj(source, dest)

for item_name in os.listdir('blocks/s/'):
    item = pathlib.Path('blocks/s/' + item_name)
    if item_name.endswith(".png"): 
        img = Image.open(item)
        w,h = img.size
        if w == h:
            print("-=" + item_name)
            av = ImageStat.Stat(img).median
            if len(av) > 3:
                notignored = av[3] > 150
            else:
                notignored = False
            if notignored:
                new_image = Image.new("RGB", img.size, tuple(av))
                colors.append([av,item_name])
                new_image.save(f"blocks/final/{item_name}")
print(colors)

f = open("all_of_the_blocks_list_dont_touch.py", "w+")
f.write("all = " + str(colors))
f.close()
input("\n\n\n\n\n\n\nYou may now run main.py.\n[Enter] to exit")