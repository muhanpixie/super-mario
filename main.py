from src import setup
from src.game import Game
# from src.states import main_menu, load_screen, level

def main():
    state = setup.states['main_menu']
    game = Game(state)
    game.run()

if __name__ == '__main__':
    main()