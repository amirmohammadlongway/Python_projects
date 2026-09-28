vorood=int(input('1.Manager\n2.Guest\n0.Exit\nselect a number:'))
import dastyar
match vorood:
    case 0:
        print('Exit')
    case 1:
        while True:
            name=input('Enter your name:')
            if name in dastyar.managers:
                while True:
                    password=int(input('Enter your password:'))
                    if dastyar.managers[name]==password:
                        break
                    else:
                        print('Password is not correct!')
                break
            else:
                print('name not defined!')
        while True:
            menu=int(input('MENU:\n1.My Account\n2.display rooms\n3.display guests\n4.budget\n5.add|remove room\n6.edit room\n7.talk to guests\n8.edit budget\n0.exit\nselect a number:'))
            match menu:
                case 0:
                    break
                case 1:
                    print(f'{name}-->{password}')
                case 2:
                    print(dastyar.display_rooms())
                case 3:
                    print(dastyar.display_guests())
                case 4:
                    budget=dastyar.budget()
                    print(budget)
                case 5:
                    q=int(input('1.Add|2.Remove\nselect a number:'))
                    match q:
                        case 1:
                            number_of_room=dastyar.room_counter()
                            if len(number_of_room)==20:
                                print('There is no place to add room!')
                            else:
                                beds=int(input('Enter number of beds:'))
                                type=input('Enter room type(vip|economy):')
                                print(dastyar.add_room(beds,type))
                        case 2:
                            number_of_room=dastyar.room_counter()
                            if len(number_of_room)==0:
                                print('No rooms to remove!')
                            else:
                                room_number=int(input('Enter room number:'))
                                if room_number not in number_of_room:
                                    print(f'No room wtih number{room_number}!')
                                else:
                                    condition=dastyar.condition(room_number)
                                    if condition=='empty':
                                        print(dastyar.remove_room(room_number))
                                    else:
                                        print('we cant remove occupied rooms!')
                case 6:
                    number_of_room=dastyar.room_counter()
                    if len(number_of_room)==0:
                        print('No room to edit!')
                    else:
                        room_number=int(input('Enter room number:'))
                        if room_number not in number_of_room:
                            print(f'Hotel has no room with number {room_number}')
                        else:
                            condition=dastyar.condition(room_number)
                            if condition=='empty':
                                while True:
                                    edits=int(input('1.change beds\n2.change room type\n3.change room price\n0.back\nselect a number:'))
                                    match edits:
                                        case 0:
                                            break
                                        case 1:
                                            bed=int(input('Enter number of beds:'))
                                            print(dastyar.bed_editor(room_number,bed))
                                        case 2:
                                            type=input('Enter room type(vip|economy):')
                                            print(dastyar.type_editor(room_number,type))
                                        case 3:
                                            price=int(input('Enter new price:'))
                                            print(dastyar.price_editor(room_number,price))
                            else:
                                print('This room is already full!')
                case 7:
                    pass
                case 8:
                    q=int(input('1.deposit\n2.withdraw\nselect a number:'))
                    match q:
                        case 1:
                            value=int(input('Enter amount:'))
                            print(dastyar.deposit(value))
                        case 2:
                            value=int(input('Enter amount:'))                       
                            budget=int(dastyar.budget())
                            if value<=budget:
                                print(dastyar.withdraw(value))
                            else:
                                print('not enough money!')
    case 2:
        guests=dastyar.namayesh_mosaferan_log_in()
        name=input('Enter your name:')
        if name in guests:
            while True:
                password=int(input('Enter your password:'))
                if guests[name]['password']==password:
                    break
                else:
                    print('incorrect password!')
        else:
            passwords=dastyar.guests_passwords()
            while True:
                password=int(input('Enter password:'))
                if password not in passwords:
                    break
                else:
                    print('Password not unique!')
            print(dastyar.add_guest(name,password))
        while True:
            menu=int(input('MENU:\n1.My Account\n2.display rooms\n3.Hotel reservation\n4.remove my reserves\n0.Exit\nselect a number:'))
            match menu:
                case 0:
                    break
                case 1:
                  print(dastyar.guest_personality(name,password))
                case 2:
                    print(dastyar.display_rooms_to_guet())
                case 3:
                    room_numbers=dastyar.room_counter()
                    number=int(input('Enter room number:'))
                    if number not in room_numbers:
                        print('NO room with this number!')
                    else:
                        condition=dastyar.condition(number)
                        if condition=='empty':
                            print(dastyar.room_reservation(password,number))
                        else:
                            print('Room is already full!')
                case 4:
                    my_reserves=dastyar.my_reserves(password)
                    if len(my_reserves)==0:
                        print('You have reserved no room!')
                    else:
                        number_of_room=int(input('Enter room number to remove:'))
                        if number_of_room in my_reserves:
                            print(dastyar.canceling(password,number_of_room))
                        else:
                            print('You have not reserved this room!')

                        