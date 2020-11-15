import json
from plugins.imageParser import ImageParser as imParse
import assets.values.integers as num

class BuildMap():
    def __init__(self, imParse, pg, screen, col):
        self.imgParser = imParse
        self.game = pg
        self.scn = screen
        self.collision = col
    
    def sketch_ground(self):
        groundJson = open('assets/maps/session_stage_1.json')
        ground = json.load(groundJson)

        count = 0
        for d in ground['ground']:
            if count == 0:
                if(ground['ground'][d]['start'] >= 0 and ground['ground'][d]['start'] < 960):
                    if ground['ground'][d]['end'] > 960:
                        self.collision.groundCollider.append(self.game.Rect(ground['ground'][d]['start'], 620, 960, 80))
                    else:
                        self.collision.groundCollider.append(self.game.Rect(ground['ground'][d]['start'], 620, ground['ground'][d]['end'], 80))
                elif ground['ground'][d]['start'] < 0 and ground['ground'][d]['end'] > 0:
                    self.collision.groundCollider.append(self.game.Rect(0, 620, ground['ground'][d]['end'], 80))
                count = count + 1
            else:
                count = count + 1
                if count == 2:
                    count = 0

            for plot in range(ground['ground'][d]['start'], ground['ground'][d]['end'], 40):
                self.scn.blit(self.imgParser(self.game, 'assets/images/static/map/ground/ground_block.png').parsedImageBroadcaster(), (plot, ground['ground'][d]['elv']))

        print(self.collision.groundCollider)

        groundJson.close()

        