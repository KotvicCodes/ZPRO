

myvariable = f'I am variable myvariable from module {__name__}'

def say_hello():
    print(f'Hello! I am function say_hello from module {__name__} ')

print(f'This is an executable statement from module {__name__}')

if __name__ == '__main__':
    print('Tato část se spustí jen při zavolání jako skript')
    print('Tady klidně mohu zase zavolat funkci z modulu say_hello')
    say_hello()