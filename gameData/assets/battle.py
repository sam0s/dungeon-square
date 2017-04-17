#################################
# sam0s #######################
#################################


import pygame
from random import choice,randint
from pygame import *
import dpylib
import ui


pygame.init()
font=pygame.font.Font(None,15)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Battle(object):
    def __init__(self,surf,world):
        self.surf=surf
        self.world=world
        self.enemydisp = Surface((800,128))
        self.enemydisp.fill((0,0,0))
        self.buttons=[ui.Button(300,300,100,32,"Attack",self.surf),ui.Button(300,364,100,32,"Items",self.surf)]
        self.baseDamageMatrix=[12,15]

        self.mode = 'fight'

    def NewEnemy(self):
        #set level of enemy
        self.enemy='orc'


        #Use the dungeon level cap to create the enemies level
        self.enemyLevel=randint(self.world.dungeonLevelCap-4,self.world.dungeonLevelCap+1)
        #self.enemyLevel=20
        #this will be changed to have MONSTER_BASE_HEALTH * MONSTER_LEVEL (in some way or another)
        self.enemyHp=self.enemyMaxHp=self.enemyLevel*18


        self.enemyNum=0
        self.enemyName="Orc"
        self.world.logtext.append("The "+self.enemyName+" is level "+str(self.enemyLevel)+".")

    def Attack(self):

        #player attack
        #print self.world.player.activeWeapon[0].ad
        dmg=randint(0,self.world.player.atk+self.world.player.activeWeapon[0].ad)
        self.enemyHp-=dmg
        self.world.logtext.append(self.world.playername+" does "+str(dmg)+" damage.")
        #check for enemy death, and xp algorithim
        if self.enemyHp<=0:
            xpgive=18*(self.enemyLevel/2)+4
            self.world.logtext.append("Enemy Slain! "+"You get "+str(xpgive))
            self.world.player.giveXp(xpgive)
            self.world.battle=False
            self.world.ChangeState("game")



        #ENEMY ATTACK
        dmg=self.baseDamageMatrix[self.enemyNum]+self.enemyLevel*2
        dmg=(randint(0,5*dmg))/6
        self.world.player.hp-=dmg
        self.world.logtext.append("The "+self.enemyName+" does "+str(dmg)+" damage.")


        #test player death
        if self.world.player.hp<=0:
            self.world.ChangeState("menu")




    def Draw(self):
        if self.mode == 'fight':
            self.surf.fill((0,0,220))
            self.surf.blit(self.enemydisp,(0,0,))
            self.surf.blit(self.world.images[3],(672,0))


            dpylib.bar(self.enemydisp,(0,210,0),(210,0,0),130,4,165,25,self.enemyHp,self.enemyMaxHp)
            dpylib.bar(self.world.hudsurf,(0,210,0),(210,0,0),130,4,165,25,self.world.player.hp,self.world.player.maxhp)
            self.world.hudsurf.blit(self.world.images[2],(1,1))

            for e in self.world.events:
                #button handling
                if e.type == MOUSEBUTTONUP:
                    for b in self.buttons:
                        if b.rect.collidepoint(e.pos):
                            if b==self.buttons[0]:
                                self.Attack()
                            if b==self.buttons[1]:
                                self.mode = 'items'

                if e.type == QUIT:
                    self.world.Close()
            for b in self.buttons:
                b.Update()
        #items mode
        else:
            self.world.esc.tab="items"
            self.world.ChangeState("escmenu")


class Button(Entity):
    def __init__(self,surf):
        pass