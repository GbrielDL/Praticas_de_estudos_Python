def leiaInt(msg):
    valor = 0
    ok = False
    
    while not ok:
        try:
            enter = str(input(msg))
        except:
            print('\033[31mError\033[m')
            continue
        else:
            if enter.isnumeric():
                valor = int(enter)
                ok = True
            else:
                print(f'\033[33m\'{enter}\' não é um valor inteiro\033[m')
                continue
        return valor
    
