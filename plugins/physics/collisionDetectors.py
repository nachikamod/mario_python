def marioGround(detect, bools):
    booleans = []

    for data in detect.groundCollider:
        if detect.marioCollider.colliderect(data):
            #bools.collide = True
            booleans.append(True)
        else:
            #bools.collide = False
            booleans.append(False)

    bools.collide = any(booleans)

    booleans.clear()

    detect.groundCollider.clear()