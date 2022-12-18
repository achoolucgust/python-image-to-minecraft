# python-image-to-minecraft
Image to Minecraft generator, IN PYTHON!

# How to use
## Setup
### Getting the version
1. Find a version in your `.minecraft` folder. By default:
`%appdata%/Roaming/.minecraft` 
2. Find the `.jar` file in that folder.
3. If that doesn't exist, you might be picking a snapshot, try using a version like `1.19.2` instead of `1.19.2-pre`
4. Copy and Paste that file to the folder this script is in.
5. Rename this JAR file to version.zip
### Running the Script
1. Make sure you have the modules already installed. 
`pip install pillow pathlib` are the only two you need.
2. Create new folders: `blocks/final/`, and `blocks/s/`
2. Run `init.py` and wait for it to finish.
You should see the folder `/final` and `/s` in `./blocks`
Don't forget to remove everything in `blocks/final`, `blocks/s` and `./__pycache__` when picking a new version.
3. Now you can run `main.py`. The first prompt should ask you what the file name of your PNG/Image file is. Don't forget to include the file extension: `target.png`
After waiting for that script to finish, you should now see final.png in the folder.
