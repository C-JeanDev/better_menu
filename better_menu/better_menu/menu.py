from print_color import print
import os
import platform

plat: str = platform.system()

if plat == 'Windows':
    from msvcrt import getch
else:
    from getch import getch


class Menu:

    def __init__(self, menu: dict[str, callable], ind: str = '>', color: str = 'white'):
        self.__ENTER = 10 if plat == 'Linux' else 13
        self.__W = 119
        self.__S = 115
        self.__J = 106
        self.__K = 107
        self.menu = menu
        self.color = color
        self.ind = ind+' '
        self.title_and_color = None
        self.sub_title_and_color = None

    def __clear(self) -> None:
        if plat == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def __print_menu(self, keys) -> None:

        if self.title_and_color:
            print(self.title_and_color[0],
                  color=self.title_and_color[1], format='bold', end='')

        if self.sub_title_and_color:
            print(self.sub_title_and_color[0],
                  color=self.sub_title_and_color[1], end='')

        for i in keys:
            if self.ind in i:
                print(i, color=self.color, format='bold')
            else:
                spaces = ' '*(len(self.ind)-1)
                print(f'{spaces} {i}', format='bold')

    def title(self, title: str, color: str = 'white') -> None:
        self.title_and_color = title+'\n', color

    def sub_title(self, sub_title: str, color: str = 'white') -> None:
        self.sub_title_and_color = sub_title+'\n', color

    def init(self) -> int:
        self.__clear()
        index: int = 0
        keys = list(self.menu.keys())
        keys[index] = self.ind + keys[index]
        self.__print_menu(keys)
        while True:
            key = ord(getch())
            if key in [self.__W, self.__K]:
                self.__clear()
                keys = list(self.menu.keys())
                if index == 0:
                    index = len(keys) - 1
                else:
                    index -= 1
                keys[index] = self.ind + keys[index]
                self.__print_menu(keys)
                
            elif key in [self.__S, self.__J]:
                self.__clear()
                keys = list(self.menu.keys())
                if index+1 < len(keys):
                    index += 1
                else:
                    index = 0
                keys[index] = self.ind + keys[index]
                self.__print_menu(keys)

            elif key == self.__ENTER:
                if callable(v := list(self.menu.values())[index]):
                    v()
                    return index
