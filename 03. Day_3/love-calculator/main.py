print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 = name1.upper()
name2 = name2.upper()

# T occurs

t_occurs_n1 = name1.count("T")
t_occur_n2 = name2.count("T")
total_t_occ = t_occurs_n1 + t_occur_n2

r_occurs_n1 = name1.count("R")
r_occur_n2 = name2.count("R")
total_r_occ = r_occurs_n1 + r_occur_n2

u_occurs_n1 = name1.count("U")
u_occur_n2 = name2.count("U")
total_u_occ = u_occurs_n1 + u_occur_n2

e_occurs_n1 = name1.count("E")
e_occur_n2 = name2.count("E")
total_e_occ = e_occurs_n1 + e_occur_n2

total_true = total_t_occ + total_r_occ + total_u_occ + total_e_occ

# LOVE
l_occurs_n1 = name1.count("L")
l_occur_n2 = name2.count("L")
total_l_occ = l_occurs_n1 + l_occur_n2

o_occurs_n1 = name1.count("O")
o_occur_n2 = name2.count("O")
total_o_occ = o_occurs_n1 + o_occur_n2

v_occurs_n1 = name1.count("V")
v_occur_n2 = name2.count("V")
total_v_occ = v_occurs_n1 + v_occur_n2

e2_occurs_n1 = name1.count("E")
e2_occur_n2 = name2.count("E")
total_e2_occ = e2_occurs_n1 + e2_occur_n2

total_love = total_l_occ + total_o_occ + total_v_occ + total_e2_occ

love_score = str(total_true) + str(total_love)

love_score_int = int(love_score)

if (love_score_int < 10) or (love_score_int > 90):
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")
elif (love_score_int >= 40) and (love_score_int <= 50):
    print(f"Your score is {love_score_int}, you are alright together.")
else:
    print(f"Your score is {love_score_int}.")
