while True:
    try:
        ch=int(input('Select your charactor(1.customer|2.manager):'))
        if ch not in [1,2]:
            raise ValueError('select 1 or 2')
    except Exception as e:
        print(e)
    else:
        break
match ch:
    case 2:
        import manager
        while True:
            while True:
                try:
                    nam=input('Enter your name:')
                    if not nam.isalpha():
                        raise ValueError('Dont use numbers!')
                except Exception as E:
                    print(E)
                else:
                    break
            if nam in manager.admins:
                while True:
                    while True:
                        try:
                            ramz=input('Enter your password:')
                            if len(ramz)!=4:
                                raise ValueError('password must contain 4 charactors!')
                        except Exception as E:
                            print(E)
                        else:
                            break
                    if manager.admins[nam]==ramz:
                        break
                    else:
                        print('password not correct!')
                break
            else:
                print('name not defined!')
        while True:
            men=int(input('MENU:\n1.My Account\n2.Gallery budget\n3.Display cars\n4.Add|Remove car\n0.Exit\nselect a number:'))
            match men:
                case 1:
                    print(f'{nam}-->{manager.admins[nam]}')
                case 2:
                    print(manager.budget())
                case 4:
                    operation_type=int(input('1.add\n2.remove\nselect a number:'))
                    match operation_type:
                        case 1:
                            nam=input('car name:')
                            model=int(input('car model:'))
                            price=int(input('car value:'))
                            print(manager.add_car(nam,model,price))
                        case 2:
                            nam=input('car name:')
                            print(manager.remove_car(nam))
                case 3:
                    print(manager.display_cars())
                case 0:
                    break
    case 1:
        import manager
        with open('cars.txt','r') as file:
            cars=file.readlines()
            for car in cars:
                car=car.split('>>')[2]
        while True:
            men=int(input('MENU:\n1.Display cars\n2.Deal\n0.Exit\nselect a number:'))
            match men:
                case 1:
                   print(manager.display_cars())
                case 2:
                    deal=int(input('1.buy\n2.sell\nchoose deal type:'))
                    match deal:
                        case 1:
                            with open('budget.txt','r') as file:
                                budget=file.readline()
                            nam=input('car name:')
                            with open('cars.txt','r') as file:
                                cars=file.readlines()
                                for car in cars:
                                    d=car.split('>>')
                                    if d[0]==nam:
                                        price=int(d[2])
                                        break
                                budget=int(budget)+price
                            with open('budget.txt','w') as file:
                                file.write(str(budget))
                            print(manager.remove_car(nam))
                        case 2:
                            import manager
                            nam=input('car name:')
                            model=int(input('car model:'))
                            price=int(input('car price:'))
                            with open('budget.txt','r') as file:
                                budget=file.readline()
                            if int(budget)>price:
                                manager.add_car(nam,model,price*1.1)
                                budget=int(budget)-price
                                print('we bought your car')
                                with open('budget.txt','w') as file:
                                    file.write(str(budget))
                            else:
                                print('sorry we cant pay this amount!')
                case 0:
                    break