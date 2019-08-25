import os

print(os.getcwd())
fpath = os.path.join(".", "st.txt")

print(fpath)

st = open(file=fpath, mode="w+", encoding="utf-8")
st.write("pythonからこんにちは!")
st.close()

with open(file = fpath, mode = "w+", encoding="utf-8") as f:
    f.write("Python から こんにちは！！！")

st_list = []
with open(file = fpath, mode = "r", encoding = "utf-8") as f:
    st_list.append(f.read())

print(st_list)