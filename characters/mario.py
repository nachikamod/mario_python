class Mario():
    def __init__(self, imParse, pg, screen, num, col):
        self.imgParse = imParse
        self.game = pg
        self.scn = screen
        self.number = num
        self.collision = col

    def animateMario(self):
        mario = self.scn.blit(self.imgParse(self.game, 'assets/images/dynamic/mario/idle.png').parsedImageBroadcaster(), (self.number.mario_x, self.number.mario_y))
        self.collision.marioCollider = self.game.Rect(mario)