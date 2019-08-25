import random
answers = ["cat", "dog", "elephant"]

def hangman(answers):
    wrong = 0
    stages = ["",
                "______________      ",
                "|                   ",
                "|             |     ",
                "|             o     ",
               r"|            /|\    ",
               r"|            / \    "
                ]
    word = random.choice(answers)
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！！！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね"
        c = input(msg)
        if c in rletters:
            cind = rletters.index(c)
            board[cind] = c
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
       print("\n".join(stages))
       print(f"あなたの負け！正解は{word}.")

hangman(answers)