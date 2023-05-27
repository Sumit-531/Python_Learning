row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

treasure = "X"
position = int(position)

if position == 11:
    map[0][0] = treasure
if position == 21:
    map[0][1] = treasure
if position == 31:
    map[0][2] = treasure
if position == 12:
    map[1][0] = treasure
if position == 22:
    map[1][1] = treasure
if position == 32:
    map[1][2] = treasure
if position == 13:
    map[2][0] = treasure
if position == 23:
    map[2][1] = treasure
if position == 33:
    map[2][2] = treasure

print(f"{row1}\n{row2}\n{row3}")