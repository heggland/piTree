#!/home/pi/tree/.venv/bin/python

from scripts.tree import RGBXmasTree

def setColor(r, g, b):
  tree = RGBXmasTree()
  tree.brightness = 0.1
  for pixel in tree:
    pixel.color = (r, g, b)
  tree.close()
  