qs=["What is your name?",
    "What is your fav. color?",
    "What is your guest?"]

n=0
while True:
    print("Type q to quit.")
    a=input(qs[n])
    if a == 'q':
        break
    n = (n + 1) % qs.__len__()