def to_english(n):
    units=["","one","two","three","four","five","six","seven","eight","nine"]
    tens=["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    hundreds=["hundred"]
    tenths=["eleven","twelve","thirteen","fourteen","fifteen","sisteen","seventeen","eighteen","nineteen"]
    if n>99 and n<=999:
        value=n//100
        print(units[value],hundreds[0],'and ',end='')
        value1=n%100
        if value1>=11 and value1<=19:
            print(tenths[value1-11],' ',end='')
        else:
            value3=value1//10
            if value3==0:
                print('',end='')
            else:
                print(tens[value3-1],' ',end='')
            value2=value1%10
            if value2==0:
                print('',end='')
            else:
                print (units[value2],' ',end='')  
    elif n>9 and n<100:
        if n>10 and n<20:
            print(tenths[n-11],' ',end='')
        else:
            value2=n//10
            print(tens[value2-1],' ',end='')
            value1=n%10
            if value1==0:
                print('',end='')
            else:
                print(units[value1],' ',end='')
    elif n>=0 and n<=9:
        print(units[n])
    else:
        print('Please enter number below 1000')
