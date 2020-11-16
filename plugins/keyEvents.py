import json

def keyEvents(pg, num, bools):
    keys = pg.key.get_pressed()


    if(keys[pg.K_RIGHT] or keys[pg.K_d]) and not bools.collideLeftGround:
        if not(((num.width/2)-20) == num.mario_x):
            num.mario_x += 10
        else:
            read = open('assets/maps/session_stage_1.json', 'r')
            readJson = json.load(read)

            read.close()

            for d in readJson['ground']:
                write = open('assets/maps/session_stage_1.json', 'w')
                readJson['ground'][d]['start'] = readJson['ground'][d]['start'] - 10
                readJson['ground'][d]['end'] = readJson['ground'][d]['end'] - 10
                json.dump(readJson, write)
                write.close()

    elif((keys[pg.K_LEFT] or keys[pg.K_a]) and num.mario_x > 0) and bools.collideRightGround:
        num.mario_x -= 10

    if not bools.isJump:
        if keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP]:
            bools.isJump = bools.collideTopGround
            
    else:
        if num.jumpCount >= -10:
            neg = 1
            if num.jumpCount < 0:
                neg = -1
            num.mario_y -= (num.jumpCount ** 2) * 0.5 * neg
            num.jumpCount -= 1
        
        else:
            bools.isJump = False
            num.jumpCount = 10
