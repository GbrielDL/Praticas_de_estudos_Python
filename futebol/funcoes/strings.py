def leiaStr(msg):
    ok = False
    while not ok:
        try:
            enter = str(input(msg)).strip()
        except:
            print('\033[31mError\033[m')
        else:
            if enter.isnumeric():
                print(f'\033[31m\'{enter}\' não é uma palavra\033[m')
                continue
            else:
                ok = True
        return enter
    
    
def linha():
    lin = '-=' * 25
    return lin