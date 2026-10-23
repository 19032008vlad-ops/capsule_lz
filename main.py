from graphic import steam_stats
from login import loger


@loger
def run_logger_demo():
    print("Tests function loger is complited and  is written in logs.csv")


@loger
def build_steam_stats():
    stat = steam_stats('steam_players.csv')
    stat.plot(top_n= 100)


def main():
 choose = input('Choose file: 1 - logger, 2 - steam_stats: ').strip()
 match choose:
         case '1':
            run_logger_demo()
         case '2':
            build_steam_stats()
         case _:
            print("Error! Try choice 1 or 2")

if __name__ == '__main__':
    main()