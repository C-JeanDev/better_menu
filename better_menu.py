from print_color import print
import os
import platform

plat: str = platform.system() 

if plat == 'Windows':
    from msvcrt import getch
else:
    from getch import getch

def _clear():
    if plat == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

_ENTER = 10
_W = 119
_S = 115
_J = 106
_K = 107


class menu:
    def __init__(self, menu: dict[str, callable], ind: str = '>', color: str = 'white'):
        self.menu = menu
        self.color = color
        self.ind = ind+' '

    def _print_menu(self, keys):
        for i in keys:
            if self.ind in i:
                print(i, color=self.color, format='bold')
            else:
                spazi = ' '*(len(self.ind)-1)
                print(f'{spazi} {i}', format='bold')

    def start(self):
        index: int = 0
        keys = list(self.menu.keys())
        keys[index] = self.ind + keys[index]
        self._print_menu(keys)
        while True:
            key = ord(getch())

            if key in [_W, _K]:
                _clear()
                keys = list(self.menu.keys())
                if index == 0:
                    index = len(keys) - 1
                else:
                    index -= 1
                keys[index] = self.ind + keys[index]
                self._print_menu(keys)
            elif key in [_S, _J]:
                _clear()
                keys = list(self.menu.keys())
                if index+1 < len(keys):
                    index += 1
                else:
                    index = 0
                keys[index] = self.ind + keys[index]
                self._print_menu(keys)

            elif key == _ENTER:
                if v := list(self.menu.values())[index]:
                    v()
                    return index
