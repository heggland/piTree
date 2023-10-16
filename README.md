# Raspberry Pi RGB Christmas Tree Discord Bot

This guide provides instructions on setting up a Discord bot to control an RGB Christmas tree using a Raspberry Pi. The bot allows users to change the color of the Christmas tree lights through Discord commands. The setup assumes you have a Raspberry Pi with GPIO pins connected to an RGB Christmas tree.

## Prerequisites

1. Raspberry Pi with Raspbian OS
2. RGB Christmas tree hardware
3. Discord account and a bot token


## Setup Steps

* Place the bot token inside the `id.example` file, rename the file to simply `id`

### 1. Update the system

```bash
sudo apt update
cd /home/pi
```

### 2. Install python packages
```bash
sudo apt install python3-pip python3-cffi
sudo apt install python3.11-venv
```

### 3. Create a virtual environment
```bash
python3 -m venv myenv
source /home/pi/tree/myenv/bin/activate
```

### 4. Install pip packages
```bash
pip install discord.py
pip install gpiozero
pip install colorzero
```

### 5. Create systemd service
Create a service file for your Discord bot.
```bash
sudo nano /etc/systemd/system/piTree_app.service
```
paste the following into the file:
```ini
[Unit]
Description=My Christmas Tree App
After=network.target

[Service]
ExecStart=/home/pi/tree/myenv/bin/python /home/pi/tree/app.py
WorkingDirectory=/home/pi/tree
User=pi
Group=pi
Restart=always

[Install]
WantedBy=multi-user.target
```


### 6. Enable and start the service
```bash
sudo systemctl enable piTree_app.service
sudo systemctl daemon-reload
```

### 7. Stop/start service
```bash
sudo systemctl stop piTree_app.service
sudo systemctl start piTree_app.service
```

### 8. Commands
* to turn on: .c <r> <g> <b> | e.g. .c 0 128 0
* to turn off: .off
* to view info: .help

### Additional info
* Thanks to The Pi Hut for tree.py script https://github.com/ThePiHut/rgbxmastree/tree/master
* If you found this program useful and would like to show your appreciation, you can <a href="https://www.buymeacoffee.com/heggland" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Cup Of 		Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px 		rgba(190, 190, 190, 0.5) !important;" ></a>
