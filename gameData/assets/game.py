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
import assets.player as player
import assets.world as world
import assets.sound as sound
import assets.questmenu as questmenu
import assets.ui as ui
import assets.items as items
import dpylib as dl
from os import path

pygame.init()

class Game(object):
    def __init__(self,surf):
        self.state="menu"
        self.surf=surf
        #scrolling text handler
        self.st=mainmenu.ScrollingText(self.surf,"menu")
        self.st.game=self
        #logo screen
        self.logos=mainmenu.Logos(self.surf)
        self.logos.game=self
        #mainmenu objects
        self.mm=mainmenu.Menu(self.surf)
        self.mm.game=self

        #sound
        self.snd=sound.Mix()

        #gameworld and player objects
        self.gw=world.World(self.surf)
        items.loadItems("items.json")
        self.player=player.Player(384.0,224.0,self.gw)
        self.gw.game=self
        self.gw.player=self.player
        self.gw.playername="playername"

        #overworld objects
        self.ow=overworld.Overworld(self.surf)
        self.ow.game=self
        self.go=True

        #questhandler and questmenu
        self.qm=questmenu.Menu(self.surf)
        self.qm.game=self
        self.qm.quests=[]


    def Update(self,dt):
        self.events=pygame.event.get()
        if self.state == "scrolling":
            self.st.Draw(dt)
        if self.state == "logos":
            self.logos.Draw(dt)
        if self.state == "menu":
            self.mm.Draw()
        if self.state == "quests":
            self.qm.Draw()
        if self.state == "overworld":
            self.ow.Draw(dt)
        if self.state == "game":
            self.gw.Update(dt)
            self.surf.blit(self.gw.surf,(0,0))
        pygame.display.flip()
