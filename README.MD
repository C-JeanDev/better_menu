# Better Menu 
better_menu is a [Python](https://www.python.org/) library for creating simple but cool menu(s) very fastly.

# Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable) to install Pydeas
```bash 
pip install better_menu
```


## Get Started
#### For an example of the final output check
![img](menu.png)

### The menu constructor 
the `Menu` constructor takes in `1 argument (and other optionals 2)` : a menu dictionary that has the voice and a function that will be executed if the voice is chosen

```python
m = {
  '1. Insert User': insert_user,
  '2. Exit': exit
}
```
Now pass the menu to the constructor

```python
from better_menu.menu import Menu

m = {
  '1. Insert User': insert_user,
  '2. Exit': exit
}

menu = Menu(m)
menu.init()
```

### Title and Subtitle
You can add a title and a subtitle that will be printed within the menu

```python
from better_menu.menu import Menu

m = {
  '1. Insert User': insert_user,
  '2. Exit': exit
}

menu = Menu(m)
menu.title('Title')
menu.subtitle('Subtitle')
menu.init()
```

### Option Argument (indicator, color)
`Indicator (ind)`: indicate the indicator of the selcted voice

`Color (color)`: indicate the color of the title or subtitle or of the selcted voice if passed to the menu constructor

```python
from better_menu.menu import Menu

m = {
  '1. Insert User': insert_user,
  '2. Exit': exit
}
#set the indicator of the selcted voice to '>' and the color of the selected voice to red
menu = Menu(m, ind='>', color='red') 

# set the color of the title to 'black'
menu.title('Title', color='black') 

# set the color of the subtitle to 'blue'
menu.subtitle('Subitle', color='blue')

menu.init()
```

[Better Menu v1.0.13](https://github.com/C-JeanDev/better_menu)
