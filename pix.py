import pygame
from pygame.locals import SRCALPHA
from collections import namedtuple

""" Render .pix files. """
EMPTY = '.'

Colour = namedtuple ('Colour', ['r', 'g', 'b', 'a'])
Pix = namedtuple ('Pix', ['colours', 'pixels'])

def getchannel (hex_,chan):
    return hex_[(chan*2):((chan+1)*2)]

def hex2colour (hex_):
    if len (hex_) == 6:
        hex_ = '{}FF'.format (hex_)
    return Colour (*[int ('0x{}'.format (getchannel (hex_, i)), 16) for i in range (4)])

def load_pix_file (pixfile):
    with open (pixfile,'r') as pfile:
        pixlines = pfile.readlines ()

    colours = {}
    pixels = []
    for line in pixlines:
        line = line.strip ()
        if '#' in line:
            pixel, colour = line.split ('#')
            colours[pixel] = hex2colour (colour)
        elif line:
            pixels.append (line)
    return Pix (colours, pixels)

def render_pix (pix):
    height = len (pix.pixels)
    width = len (max (pix.pixels))
    surface = pygame.Surface ((width,height),SRCALPHA,32)
    print (pix)
    for x in range (width):
        for y in range (height):
            if pix.pixels[y][x] != EMPTY:
                surface.set_at ((x, y), pix.colours[pix.pixels[y][x]])
    return surface

def load_pix (pixpath):
    """ Call this. """
    return render_pix (load_pix_file (pixpath))

