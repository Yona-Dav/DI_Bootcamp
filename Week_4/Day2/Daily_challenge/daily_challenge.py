from datetime import date

print(date.today())
bday = input('Enter you birthday , format DD/MM/YYYY')

bday_year = bday[6:]
bday_day = bday[:2]
bday_month = bday[3:5]

today_year = date.today().year
today_day = date.today().day
today_month = date.today().month

age = int()
if int(bday_month) < today_month:
    age = today_year - int(bday_year)
elif int(bday_month) == today_month:
    if int(bday_day)<=today_day:
        age = today_year - int(bday_year)
    else:
        age = today_year - int(bday_year) -1
else:
    age = today_year -1 - int(bday_year)

print(age)

candles = str(age)[-1]
candles = int(candles)
print(type(candles))


if candles%2==0:
    x = (11-candles)/2
    a = ' '*5 + '_'*(int(x))+"i"*candles+'_'*(int(x)+1)+' '*5 
else:
    y = (11-candles)/2
    a = ' '*5 + '_'*(int(y))+"i"*candles+'_'*(int(y))+' '*5 

# a = ' '*5 + '_'*11+' '*5
b = ' '*3 +"|"+':'+'H'+':'+'a'+':'+'p'+":"+'p'+":"+'y'+':'+'|'+ ' '*3
d = ' '+'_'*2+"|"+'_'*11+"|"+'_'*2+" "
e = "|"+"^"*17+"|"
f = "|"+':'+'B'+':'+'i'+':'+'r'+":"+'t'+":"+'h'+':'+'d'+':'+'a'+':'+'y'+':'+'|'
g = "|"+" "*17+"|"
h = "~"*19


year = int(bday_year)
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} is a leap year')
            print( a,"\n",b,"\n",d,'\n',e,'\n',f,'\n',g,'\n',h )
            print( a,"\n",b,"\n",d,'\n',e,'\n',f,'\n',g,'\n',h )
        else:
            print(f'{year} is not a leap year')
            print( a,"\n",b,"\n",d,'\n',e,'\n',f,'\n',g,'\n',h )
    else:
        print(f'{year} is a leap year')
        print( a,"\n",b,"\n",d,'\n',e,'\n',f,'\n',g,'\n',h )
        print( a,"\n",b,"\n",d,'\n',e,'\n',f,'\n',g,'\n',h )
else:
    print(f'{year} is not a leap year')
    print( a,"\n",b,"\n",d,'\n',e,'\n',f,'\n',g,'\n',h )


