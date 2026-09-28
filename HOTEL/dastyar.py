managers={'Amir':123456,'Maedeh':654321}
def display_rooms():
    with open('rooms.txt') as file:
        rooms=file.readlines()
    res=''
    if len(rooms)==0:
        res='No rooms to display'
    else:
        for room in rooms:
            if room!=' ' and room!='\n':
                room=room.split('>>')
                res+=f'room number:{room[0]},number of beds:{room[1]},room type:{room[2]},room condition:{room[3]},room price:{room[4]}'
    return res
def display_guests():
    with open('guests.txt') as file:
        guests=file.readlines()
    if len(guests)==0:
        return 'No guests to display!'
    else:
        res=''
        for guest in guests:
            guest=guest.split('>>')
            res+=f'name:{guest[0]},password:{guest[1]},history:{guest[2]}'
        return res
def budget():
    with open('budget.txt') as file:
        budget=file.readlines()
    res=''
    if len(budget)==0:
        res='0'
    else:
        for b in budget:
            res+=b
    return res   
def room_counter():
    with open('rooms.txt') as file:
        rooms=file.readlines()
    rooms1=[]
    for room in rooms:
        if room!=' ' and room!='\n':
            rooms1.append(int(room.split('>>')[0]))
    return rooms1
def add_room(bed,type):
    with open('rooms.txt','r') as file:
        rooms=file.readlines()
    numbers=[]
    for room in rooms:
        numbers.append(room.split('>>')[0])
    import random
    while True:
        password=random.randint(1,21)
        if password not in numbers:
            break
    with open('rooms.txt','a') as file:
        if type=='vip':
            price=150
            file.write(f'{password}>>{bed}>>{type}>>empty>>{bed*price}\n')
        elif type=='economy':
            price=75
            file.write(f'{password}>>{bed}>>{type}>>empty>>{bed*price}\n')
    return 'Adition successful!'
def remove_room(number):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    edited=[]
    for room in rooms:
        if room!='\n' and room!='':
            if int(room.split('>>')[0])!=number:
                edited.append(room)
    with open('rooms.txt','w') as file:
        file.writelines(edited)
    return 'Deletion successful!'
def condition(number):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    res=''
    for room in rooms:
        if int(room.split('>>')[0])==number:
            res+=room.split('>>')[3]
    return res
def bed_editor(number,bed):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    edited=[]
    for room in rooms:
        if int(room.split('>>')[0])!=number:
            edited.append(room)
        else:
            if room.split('>>')[2]=='vip':
                edited.append(f'{room.split('>>')[0]}>>{bed}>>{room.split('>>')[2]}>>{room.split('>>')[3]}>>{bed*150}')
            else:
                edited.append(f'{room.split('>>')[0]}>>{bed}>>{room.split('>>')[2]}>>{room.split('>>')[3]}>>{bed*75}') 
    with open('rooms.txt','w') as file:
        file.writelines(edited)
    return f'number of beds in room {number} changed!'
def type_editor(number,type):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    edited=[]
    for room in  rooms:
        room=room.split('>>')
        if int(room[0])!=number:
            edited.append(room)
        else:
            if type=='vip':
                edited.append(f'{room[0]}>>{room[1]}>>{type}>>{room[3]}>>{int(room[1])*150}')
            else:
                 edited.append(f'{room[0]}>>{room[1]}>>{type}>>{room[3]}>>{int(room[1])*75}')
    with open('rooms.txt','w') as file:
        file.writelines(edited)
    return f'room {number} type changed!'
def price_editor(number,price):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    edited=[]
    for room in rooms:
        room=room.split('>>')
        if int(room[0])!=number:
            edited.append(room)
        else:
            edited.append(f'{room[0]}>>{room[1]}>>{room[2]}>>{room[3]}>>{int(room[1])*price}')
    with open('rooms.txt','w') as file:
        file.writelines(edited)
    return f'price of room {number} updated!'
def deposit(amount):
    with open('budget.txt') as file:
        budget=file.readlines()
    new_budget=''
    for money in budget:
        new_budget=int(money)+amount
    with open('budget','w') as file:
        file.write(str(new_budget))
    return 'operation succesful!'
def withdraw(amount):
    with open('budget.txt') as file:
        budget=file.readlines()
    new_budget=''
    for money in budget:
        money=int(money)
        new_budget=money-amount
    with open('budget.txt','w') as file:
        file.write(str(new_budget))
    return 'operation successfull!'
def namayesh_mosaferan_log_in():
    with open('guests.txt') as file:
        guests=file.readlines()
    namayesh={}
    for guest in guests:
        guest=guest.split('>>')
        namayesh[guest[0]]={'password':int(guest[1]),'history':guest[2]}
    return namayesh
def add_guest(name,password):
    with open('guests.txt','a') as file:
        file.write(f'{name}>>{password}>>[]\n')
    return 'Your name has added!'
def guests_passwords():
    with open('guests.txt') as file:
        guests=file.readlines()
    passwords=[]
    for guest in guests:
        passwords.append(int(guest.split('>>')[1]))
    return passwords
def guest_personality(name,password):
    import ast
    with open('guests.txt') as file:
        guests=file.readlines()
    res=''
    for guest in guests:
        guest=guest.split('>>')
        if guest[0]==name:
            if int(guest[1])==password:
                history=ast.literal_eval(guest[2])
                res+=f'{guest[0]}>>{guest[1]}>>{history}'
    return res
def display_rooms_to_guet():
    with open('rooms.txt') as file:
        rooms=file.readlines()
    res=''
    for room in rooms:
        room=room.split('>>')
        if room[3]=='empty':
            res+=f'room number:{room[0]}>>number of beds:{room[1]}>>type:{room[2]}>>{room[3]}>>price:{room[4]}'
    return res
def room_reservation(password,number):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    selected_room=[]
    new_rooms=[]
    for room in rooms:
        if int(room.split('>>')[0])!=number:
            new_rooms.append(room)
        else:
            new_rooms.append(f"{room.split('>>')[0]}>>{room.split('>>')[1]}>>{room.split('>>')[2]}>>full>>{room.split('>>')[-1]}")
            selected_room.append(room)
    with open('rooms.txt','w') as file:
        file.writelines(new_rooms)
    price=0
    updated_guets=[]
    for i in selected_room:
        price=int(i.split('>>')[-1])
    new_price=0
    with open('budget.txt') as file:
        budget=file.read()
        if budget=='':
            budget=0
        else:
            budget=int(budget)
        new_price=price+budget
        new_price=str(new_price)
    with open('budget.txt','w') as file:
        file.write(new_price)
    with open('guests.txt') as file:
        guests=file.readlines()
        for guest in guests:
            if int(guest.split('>>')[1])!=password:
                updated_guets.append(guest)
            else:
                import ast
                history=list(ast.literal_eval(guest.split('>>')[-1]))
                history.append(number)
                updated_guets.append(f"{guest.split('>>')[0]}>>{guest.split('>>')[1]}>>{history}\n")
    with open('guests.txt','w') as file:
        file.writelines(updated_guets)
    return 'operation successful!'
def my_reserves(password):
    with open('guests.txt') as file:
        guests=file.readlines()
    import ast
    for guet in guests:
        if int(guet.split('>>')[1])==password:
            History=list(ast.literal_eval(guet.split('>>')[-1]))
    return History   
def canceling(password,number):
    with open('rooms.txt') as file:
        rooms=file.readlines()
    emptied=[]
    edited=[]
    for room in rooms:
        if int(room.split('>>')[0])!=number:
            edited.append(room)
        else:
            emptied.append(room)
            edited.append(f'{room.split('>>')[0]}>>{room.split('>>')[1]}>>{room.split('>>')[2]}>>empty>>{room.split('>>')[-1]}\n')
    with open('rooms.txt','w') as file:
        file.writelines(edited)
    with open('guests.txt') as file:
        guests=file.readlines()
    new_edited=[]
    import ast
    for guest in guests:
        if int(guest.split('>>')[1])!=password:
            new_edited.append(guest)
        else:
            history=list(ast.literal_eval(guest.split('>>')[-1]))
            history.remove(number)
            new_edited.append(f'{guest.split('>>')[0]}>>{guest.split('>>')[1]}>>{history}\n')
    with open('guests.txt','w') as file:
        file.writelines(new_edited)
    with open('budget.txt') as file:
        budget=file.read()
    if budget==' ':
        budget=0
    else:
        budget=int(budget)
    price=0
    for value in emptied:
        value=value.split('>>')[-1]
    price=int(value)//2
    budget=budget-price
    with open('budget.txt','w') as file:
        file.write(str(budget))
    return 'Done!'
