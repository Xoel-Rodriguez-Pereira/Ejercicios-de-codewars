def stock_list (stock, categories):

    result = ''

    if stock != []:
        CountBooksInCategorie = [0] * len(categories)
        
        for i in stock:
            
            stockList = i.split(' ')
            if stockList[0][0] in categories:
                
                CountBooksInCategorie[categories.index(stockList[0][0])] += int(stockList[1])
            
            '''elif stockList[0][0] not in categories:

                categories.append(stockList[0][0])
                CountBooksInCategorie.append(int(stockList[1]))'''

        for index in range(len(CountBooksInCategorie)):

            result += '({0} : {1}) - '.format(categories[index], CountBooksInCategorie[index])

        result = result[:-3]


    return result

    



if __name__ == '__main__':
    b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
    c = ["A", "B", "C", "W"]
    assert stock_list(b, c) == "(A : 20) - (B : 114) - (C : 50) - (W : 0)"
    
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    assert stock_list(b, c) == "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    assert stock_list(b, c) == "(A : 200) - (B : 1140)"

    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = []
    assert stock_list(b, c) == ""

    b = []
    c = ["A", "B"]
    assert stock_list(b, c) == ""

    print ('Se han pasado todos los casos test')