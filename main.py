import pygame as pg
from settings import Settings as config
import assets.values.booleans as bools

pg.init()

conf = config(pg)

conf.loadDefaults()
conf.createSession()

while bools.isPlaying:
    conf.setBackground()
    conf.buildMapRelay()

    for event in pg.event.get():
        if event.type is pg.QUIT:
            bools.playing = False

    conf.setControls()

    conf.buldMarioRelay()  

    conf.physicsRelay()  
    
    pg.display.flip()
    pg.time.delay(conf.setFPS())