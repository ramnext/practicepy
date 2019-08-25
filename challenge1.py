list = ["walking dead", "antrage", "the sopranos", "vampire daialys"]

print("challenge 1.")
for i , name in enumerate(list):
    print("no:{idx}, {val}".format(idx=i,val=name))

print("challenge 2.")
for i in range(25, 51):
    print(i)

print("challenge 3.")
num_list1 = [8, 19, 148, 4]
num_list2 = [9, 1, 33, 83]

result_list = []
for i in num_list1:
    for j in num_list2:
        result_list.append(i * j)

[print(f"num{i:^3} is {x:>8,}") for i, x in enumerate(result_list)]