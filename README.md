# Python Image >> Minecraft
*Image >> Minecaft Schematic Coming SOON! (Probably)*

Image to Minecraft generator, IN PYTHON!

![](https://img.shields.io/github/directory-file-count/achoolucgust/python-image-to-minecraft) ![](https://img.shields.io/github/directory-file-count/achoolucgust/python-image-to-minecraft?extension=py&type=file&label=python%20files)  ![](https://img.shields.io/github/last-commit/achoolucgust/python-image-to-minecraft) 

![](https://img.shields.io/badge/really-buggy-red) ![](https://img.shields.io/badge/kind%20of-confusing-blue)

# How to use
## Setup
### Getting the version
1. Find a version in your `.minecraft/versions` folder. By default:

![1.19.2 folder in versions folder](https://cdn.discordapp.com/attachments/971690756047765534/1054851567251116082/image.png)

`%appdata%/Roaming/.minecraft/versions` 

![versions folder](https://cdn.discordapp.com/attachments/971690756047765534/1054851567616000020/image.png)

2. Find the `.jar` file in that folder.

![1.19.2.jar](https://cdn.discordapp.com/attachments/971690756047765534/1054851566886199306/image.png)

4. If that doesn't exist, you might be picking a snapshot, try using a version like `1.19.2` instead of `1.19.2-pre`
5. Copy and Paste that file to the folder this script is in.
6. Rename this JAR file to version.zip
### Running the Script
1. Make sure you have the modules already installed. 
`pip install pillow pathlib` are the only two you need.
2. Create new folders: `blocks/final/`, and `blocks/s/`

![blocks/final and blocks/s](https://cdn.discordapp.com/attachments/971690756047765534/1054851685006184560/image.png)

3. Run `init.py` and wait for it to finish.
You should see the folder `/final` and `/s` in `./blocks`

![blocks/final and blocks/s](https://cdn.discordapp.com/attachments/971690756047765534/1054851685006184560/image.png)

Don't forget to remove everything in `blocks/final`, `blocks/s` and `./__pycache__` when picking a new version.

![pycache](https://cdn.discordapp.com/attachments/971690756047765534/1054853157366272081/image.png)

4. Now you can run `main.py`. The first prompt should ask you what the file name of your PNG/Image file is. Don't forget to include the file extension: like `testimage.png`

![testimage.png](https://cdn.discordapp.com/attachments/971690756047765534/1054851386879258685/testimage.png)

There's also an option that asks how many blocks to skip, For this one, it just skips x amount of pixels to reduce difficulty to build and file size. If you want full resolution (1 block for 1 pixel), you would enter `1`, but if you wanted to reduce the file size in half (1 block for 2 pixels), that would be `2`
After waiting for that script to finish, you should now see final.png in the folder.

![final.png](https://cdn.discordapp.com/attachments/971690756047765534/1054851102903898172/image.png)
