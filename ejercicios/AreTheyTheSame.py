def comp(numberListA, numberListB):

    if numberListA == numberListB:
        return True
    
    if numberListA == None:
        return False
    
    if numberListB == None:
        return False
    
    if len(numberListA) != len(numberListB):
        return False
    
    copyNumberListB = numberListB[:]
    index = 0

    while numberListA[index] ** 2 in copyNumberListB:
        copyNumberListB.remove(numberListA[index] ** 2)
        index += 1

        if len(copyNumberListB) == 0:
            break

    if index == len(numberListA):
        return True
    
    else:
        return False


if __name__ == '__main__':

    numberListA = []
    numberListB = []
    assert comp(numberListA, numberListB)

    numberListA = None
    numberListB = []
    assert not comp(numberListA, numberListB)

    numberListA = []
    numberListB = None
    assert not comp(numberListA, numberListB)

    numberListA = [121, 144, 19, 161, 19, 144, 19, 11]
    numberListB = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(numberListA, numberListB)

    numberListA = [121, 144, 19, 161, 19, 144, 19, 11]
    numberListB = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert not comp(numberListA, numberListB)

    numberListA = [121, 144, 19, 161, 19, 144, 19, 11]
    numberListB = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert not comp(numberListA, numberListB)

    numberListA = [121, 144, 19, 161, 19, 144, 19, 11]
    numberListB = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 123124]
    assert not comp(numberListA, numberListB)