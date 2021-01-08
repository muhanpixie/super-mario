from src import setup
from src.game import Game
from src.states import main_menu

def main():
    game = Game()
    state = main_menu.MainMenu()
    game.run(state)

if __name__ == '__main__':
    main()