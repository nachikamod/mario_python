def marioGround(detect, bools):
    booleans = []

    for data in detect.groundCollider:

        if detect.marioCollider.colliderect(data):
            if (detect.marioCollider.bottom - 3) == data.top:
                booleans.append(True)
            
            elif (detect.marioCollider.right - (500 - data.left)) == data.left:
                #print(str(detect.marioCollider.right - (500 - data.left)) + ' : ' + str(data.left))
                bools.collideLeftGround = True

            elif (detect.marioCollider.left - (500 - data.right)) == data.right:
                bools.collideRightGround = True
        else:
            booleans.append(False)
            #bools.collideLeftGround = False

    bools.collideTopGround = any(booleans)

    booleans.clear()

    detect.groundCollider.clear()