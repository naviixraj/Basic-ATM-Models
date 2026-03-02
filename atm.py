import otp
pin=1724
bal=10000000000
u_pin=int(input('Please enter your four digit pin :'))
if u_pin==pin:
    try:
        g_otp=(otp.generate_otp())
        print(f'Generated Otp: {g_otp}')
        m_otp=(int(input('Enter the otp: ')))
        if m_otp==g_otp:
            while True:
                print('----Welcome to our bank----')
                print("1.check Balance ")
                print('2.Amount Deposite')
                print('3.Amount Withdrawal')
                print('4.Exit')
                a=int(input('Tell us what you want: '))
                if a==1:
                   print(f'The Balance you had {bal}')
                elif a==2:
                   dep=int(input('enter the amount you have to deposite:'))
                   bal=bal+dep
                   print(f'The amount after deposite {bal}')
                elif a==3:
                    wit=int(input('enter the amount of withdrawal: '))
                    if wit<bal:
                        bal-=wit
                        print(f'The withdrawal amount is: {wit}')
                        print(f'The available balance is: {bal}')
                    else:
                        print('The unavailable balance')
                elif a==4:
                    print("----Thanking you----")
                    break
        else:
            print('Invalid otp, please enter the valid otp')
    except:
        print('value error,Please enter valid balance')
else :
    print('"Invalid pin, Unable to process"') 



