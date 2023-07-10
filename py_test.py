import os
for i in range(1000,2000):
    print(f'{i}')
    msg = os.popen(f'nc 192-168-1-43.pvp2319.bugku.cn {i}').read()
    if msg:
        print(f'!!!{i}!!!')
