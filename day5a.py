#day 5 practice
st_score = input("Input a list of student scores ").split(",")
print(st_score)
print(type(st_score))
for n in range(0, len(st_score)):
    st_score[n] = int(st_score[n])
print(st_score)