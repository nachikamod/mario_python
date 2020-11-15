import json
import assets.values.integers as num
import assets.values.strings as st
import assets.values.booleans as bools
import plugins.keyEvents as controls
import assets.values.colliders as collision
import plugins.physics.collisionDetectors as detectCollsions
from plugins.imageParser import ImageParser as imParse
from buildMap import BuildMap as bMap
from characters.mario import Mario as player 

class Settings():
    def __init__(self, pg):
        self.game = pg
    
    def loadDefaults(self):
        self.screenSize = num.screenDimensions
        self.icon = imParse(self.game, 'assets/images/static/logo.png')
        self.screen = self.game.display.set_mode(num.screenDimensions)
        self.game.display.set_caption(st.appName)
        self.game.display.set_icon(self.icon.parseImage)

    def createSession(self):
        groundJson = open('assets/maps/stage_1.json')
        ground = json.load(groundJson)

        sessionStage_1 = open('assets/maps/session_stage_1.json', 'w')
        json.dump(ground, sessionStage_1)

        groundJson.close()
        sessionStage_1.close()


    def setBackground(self):
        self.screen.fill(num.backgroundColor)

    def setFPS(self):
        return num.fps

    def setControls(self):
        return controls.keyEvents(self.game, num, bools)

    def buildMapRelay(self):
        return bMap(imParse, self.game, self.screen, collision).sketch_ground()

    def buldMarioRelay(self):
        if not bools.isJump:
            if(not bools.collide):
                num.mario_y += 10
        return player(imParse, self.game, self.screen, num, collision).animateMario()

    def physicsRelay(self):
        return detectCollsions.marioGround(collision, bools)