#!/home/pi/tree/.venv/bin/python

from pathlib import Path
import subprocess
from time import sleep

import discord
from discord.ext import commands

from scripts.tree import RGBXmasTree
from scripts.color import setColor

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(command_prefix=".", intents=intents)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))

@client.event
async def on_message(message):
    if message.content.startswith(".off"):
        try:
            subprocess.run(["python3", "/home/pi/tree/scripts/off.py"])
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))
            await message.delete()
        except Exception as e:
            await message.channel.send(f"Error running off.py: {e}")

    elif message.content.startswith(".c"):
        print(message.author.id)
        command_args = message.content.split()[1:]
        if len(command_args) == 3:
            try:
                r, g, b = map(int, command_args)
                setColor(r, g, b)
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=(f'leds: {r} {g} {b}')))
                await message.delete()
            except ValueError:
                await message.channel.send(
                    "Invalid RGB values. Please provide integers for R, G, and B. e.g. .c 126 0 0"
                )
    
    elif message.content.startswith(".help"):
        await message.channel.send(
            "Commands:\n"
            "\t.c <R> <G> <B> - set color of tree\n"
            "\t.off - turn off tree\n"
            "\t.help - shows this message"
        )
        await message.delete()

token =  Path('/home/pi/tree/id').read_text()
client.run(token)
