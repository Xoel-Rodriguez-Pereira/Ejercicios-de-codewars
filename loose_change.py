def loose_change(cents):
    change = cents
    COINS_TYPES = ['Pennies', 'Nickels', 'Dimes', 'Quarters']
    COINS_VALUES = [1, 5, 10, 25]
    coinsDictionary = dict.fromkeys(COINS_TYPES, 0)
    ZERO = 0
    ONE = 1
    
    try:

        coinsIndex = len(COINS_TYPES) - ONE
        while change > ZERO:

            if change < ONE: # Como no existen monesdas de menos de un penny, no podemos operar con < 1
                return coinsDictionary

            elif change >= COINS_VALUES[coinsIndex]:
                coinsDictionary[COINS_TYPES[coinsIndex]] = change // COINS_VALUES[coinsIndex] 
                change -= COINS_VALUES[coinsIndex] * coinsDictionary[COINS_TYPES[coinsIndex]]
        
        coinsIndex -= ONE

        return coinsDictionary
    
    except:

        return coinsDictionary

if __name__ == '__main__':
    
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}

    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}

    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
     
    # Comprobando que pasa si el input es un string 
    assert loose_change('Isaac') == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

    print ('Se han superado todos los casos test :)')