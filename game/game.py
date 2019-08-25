from Deck import Deck
from Player import Player

class Game:
    def __init__(self):
        name1 = input("プレーヤー１の名前 ")
        name2 = input("プレーヤー２の名前 ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = f"このラウンドは{winner}が勝ちました！"
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = f"{p1n}は{p1c}、{p2n}は{p2c}を引きました"
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay:"
            response = input(m)
            if response == 'q':
                break

            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print(f"ゲーム終了、{win}")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return f"{p1.wins}勝{p2.wins}敗：" + p1.name + "の勝利です！"
        elif p1.wins < p2.wins:
            return f"{p2.wins}勝{p1.wins}敗：" + p2.name + "の勝利です！"
        else:
            return "引き分け！"

if __name__ == "__main__":
    game = Game()
    game.play_game()