#  Information From The User

info_list = []

for i in range(5):
    name = input('Enter your name ')
    age = int(input('Enter your age '))
    score = int(input('Enter your score '))
    tpl = (name,age,score)
    info_list.append(tpl)



info_list.sort(key=lambda x:(x[0],x[1],x[2]))

print(info_list)




