import help
users=help.users()
print('WelCome')
q=input('Do you have account(y/n)?')
match q:
    case 'n':
        while True:
            name=input('Choose a name for your self:')
            if name in users:
                print('Your name is not unique!')
            else:
                print(help.add(name))
                break
    case 'y':
        while True:
            name=input('Enter your name:')

            if name in users:
                while True:
                    password=int(input('Enter your password:'))
                    
                    if users[name]==password:
                        break
                    else:
                        print('Incorrect password!')
                break
            else:
                print('You are not defined!')
while True:
    nam=name
    selection=int(input('1.car dealership\n2.real estate dealership\n3.bank\n0.exit\nselect a number:'))
    match selection:
        case 0:
            break
        case 1:
            while True:
                options=int(input('1.Add advertisement\n2.Remove advertisement\n3.Show ads\n4.purchase\n0.exit\nselect a number:'))
                match options:
                    case 0:
                        break
                    case 1:
                        name=input('car name:')
                        model=int(input('car model:'))
                        price=int(input('car price:'))
                        print(help.add_ads(name,model,price,nam))
                    case 2:
                       history=help.my_history(nam)
                       if len(history)==0:
                           print('You have no ads to remove!') 
                       else:
                           code1=int(input('Enter ads code:'))
                           print(history)
                           if code1 not in history:
                               print('NO ads with this code!')
                           else:
                              print(help.ads_remover(code1,nam)) 
                    case 3:
                        print(help.car_ads_display())  
                    case 4:
                        codes=help.codes()
                        if len(codes)!=0:
                            code=int(input('Enter car code:'))
                            if code in codes:
                                print(help.purchasing_car(nam,code))
                            else:
                                print('No ads with this code!')
                        else:
                            print('No car for sale!')
        case 2:
            while True:
                menu=int(input('MENU:\n1.Add advertisment\n2.Remove advertisment\n3.Display advertisments\n4.purchase\n0.exit\nselect a number:'))                    
                match menu:
                    case 0:
                        break
                    case 1:
                       type=input('Enter your buliding type:')
                       location=input('Enter the location of building:')
                       area=int(input('Enter the area of your building:'))
                       price=int(input('Enter the value:'))
                       print(help.add_real_estate(type,location,area,price,nam))
                    case 2:
                        histories=help.my_history_estate(nam)
                        if len(histories)==0:
                            print('You have no ads to remove!')
                        else:
                            code=int(input('Enter ads code:'))
                            if code not in histories:
                                print('No ads with this code!')
                            else:
                                print(help.ads_remover_estate(code,nam))
                    case 3:
                        print(help.estate_ads_display())
                    case 4:
                        codesq=help.all_estates()
                        if len(codesq)==0:
                            print('No estate available!')
                        else:
                            codeq=int(input('Enter code:'))
                            if codeq in codesq:
                                print(help.purchasing_estate(nam,codeq))
                            else:
                                print('No ads with this code!')