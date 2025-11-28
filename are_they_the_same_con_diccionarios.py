def comp(numberListA, numberListB):
    pass

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