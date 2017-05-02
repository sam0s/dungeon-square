#!/usr/bin/env python

"""
world.py

"""
__author__ = "Sam Tubb (sam0s)"
__copyright__ = "None"
__credits__ = []



import pygame
from random import choice
from pygame import *
import assets.mainmenu as mainmenu
import assets.overworld as overworld
import assets.world as world
from math import sqrt
import dpylib as dl
from os import path

pygame.init()

class Game(object):
    def __init__(self,surf):
        self.state="overworld"
        self.surf=surf

        #mainmenu objects
        self.mm=mainmenu.Menu(self.surf)
        self.mm.game=self

        #gameworld objects
        self.gw=world.World(self.surf)
        self.gw.game=self

        #overworld objects
        self.ow=overworld.Overworld(self.surf)
        self.ow.game=self
        self.go=True

    def Update(self,dt):
        if self.state == "menu":
            self.mm.Draw()
        if self.state == "overworld":
            self.ow.Draw()
        if self.state == "game":
            self.gw.Update(dt)
            self.surf.blit(self.gw.surf,(0,0))
        pygame.display.flip()
