def users():
    carbar={}
    with open('users.txt') as file:
        users=file.readlines()
    for user in users:
        if user!='\n':
            user=user.split('>>')
            carbar[user[0]]=int(user[1])
    return carbar
def add(name):
    with open('users.txt') as file:
        users=file.readlines()
    passwords=[]
    for user in users:
        if user!='\n':
            user=user.split('>>')
            passwords.append(int(user[1]))
    import random
    while True:
        password=random.randint(1000,10000)
        if password not in passwords:
            break
    with open('users.txt','a') as file1:
        file1.write(f'{name}>>{password}>>0>>{[]}\n')
    return f'You Are added\nyour name:{name}\npassword:{password}'
def add_ads(name,model,price,seller):
    with open('cars.txt') as file:
        cars=file.readlines()
    codes=[]
    for car in cars :
        if car!='\n':
            car=car.split('>>')
            codes.append(car[0])
    import random
    while True:
        code=random.randint(100,1000)
        if code not in codes:
            break
    with open('cars.txt','a') as file:
        file.write(f'{code}>>{name}>>{model}>>{price}>>{seller}\n')
    with open('users.txt') as file:
        users=file.readlines()
    res=[]
    for use in users:
        if use!='\n':
            use=use.split('>>')
            if use[0]!=seller:
                res.append(f'{use[0]}>>{use[1]}>>{use[2]}>>{use[3]}')
            else:
                import ast
                histories=list(ast.literal_eval(use[3]))
                histories.append(int(code))
                res.append(f'{seller}>>{use[1]}>>{use[2]}>>{histories}\n')
    with open('users.txt','w') as file:
        file.writelines(res)
    return 'your ads has added!'
def my_history(name):
    with open('users.txt') as file:
        users=file.readlines()
    for user in users:
        if user!='\n':
            if user.split('>>')[0]==name:
                import ast
                on_sales=list(ast.literal_eval(user.split('>>')[-1]))
                on_sell=[]
                for i in on_sales:
                    if len(str(i))==3:
                        on_sell.append(int(i))
    return on_sell
def ads_remover(code=str,name=str):
    with open('users.txt') as file:
        users=file.readlines()
    edited_user=[]
    for user in users:
        if user!='\n':
            if user.split('>>')[0]!=name:
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{user.split('>>')[2]}>>{user.split('>>')[3]}')    
            else:
                import ast
                on_sales=list(ast.literal_eval(user.split('>>')[-1]))
                print(on_sales)
                on_sales.remove(code)
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{user.split('>>')[2]}>>{on_sales}') 
    with open('users.txt','w') as file:
        file.writelines(edited_user)
    with open('cars.txt') as file:
        cars=file.readlines()
    new=[]
    for car in cars:
        if car!='\n':
            if code!=int(car.split('>>')[0]):
                new.append(car)  
    with open('cars.txt','w') as file:
        file.writelines(new)
    return 'Your Ads has removed'
def car_ads_display():
    with open('cars.txt') as file:
        cars=file.readlines()
    res=''
    for car in cars:
        if car!='\n':
            car=car.split('>>')
            res+=f'{car[0]}>>{car[1]}>>{car[2]}>>{car[3]}>>{car[4]}'
    if len(res)==0:
        r='No ads to display!'
    else:
        r=res
    return r
def purchasing_car(name0,code):
    with open('cars.txt') as file:
        cars=file.readlines()
    name=''
    value=0
    ram=0
    edited_car=[]
    for car in cars:
        if car!='\n':
            if code!=int(car.split('>>')[0]):
                edited_car.append(car)  
            else:
                ram=int(car.split('>>')[0])
                value=int(car.split(">>")[3])
                name=car.split('>>')[-1].split('\n')[0]
    with open('cars.txt','w') as file:
        file.writelines(edited_car)
    with open('users.txt') as file:
        users=file.readlines()
    edited_user=[]
    for user in users:
        if user!='\n':
            if user.split('>>')[0]!=name:
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{user.split('>>')[2]}>>{user.split('>>')[3]}\n')    
            else:
                import ast
                on_sales=(ast.literal_eval(user.split('>>')[-1]))
                on_sales.remove(ram)
                amount=value+int(user.split('>>')[2])
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{amount}>>{on_sales}\n') 
    with open('users.txt','w') as file:
        file.writelines(edited_user)    
    with open('users.txt') as file:
        users1=file.readlines()
    rewrited=[]
    for user1 in users1:
        if user1!='\n':
            if user1.split('>>')[0]!=name0:
                rewrited.append(user1)
            else:
                user1=user1.split('>>')
                user1[2]=int(user1[2])
                amount=user1[2]-value
                rewrited.append(f'{user1[0]}>>{user1[1]}>>{amount}>>{user1[-1]}')
    with open('users.txt','w') as file2:
        file2.writelines(rewrited)
    return 'Car purchase!'           
def codes():
    with open('cars.txt') as file:
        cars=file.readlines()
    res=[]
    for car in cars:
      if car!='\n':
          car=car.split('>>')
          res.append(int(car[0]))
    return res
def add_real_estate(type,location,area,price,seller):
    with open('realestate.txt') as file:
        estates=file.readlines()
    codes=[]
    for estate in estates:
        if estate!='\n':
            estate=estate.split('>>')
            codes.append(estate[0])
    import random
    while True:
        code=random.randint(1000,10000)
        if code not in codes:
            break
    with open('realestate.txt','a') as file:
        file.write(f'{code}>>{type}>>{location}>>{area}>>{price}>>{seller}\n')
    with open('users.txt') as file:
        users=file.readlines()
    edited=[]
    for user in users:
        if user!='\n':
            user=user.split('>>')
            if user[0]!=seller:
                edited.append(f'{user[0]}>>{user[1]}>>{user[2]}>>{user[-1]}')
            else:
                import ast
                history=list(ast.literal_eval(user[-1]))
                history.append(code)
                edited.append(f'{user[0]}>>{user[1]}>>{user[2]}>>{history}\n')
    with open('users.txt','w') as file1:
        file1.writelines(edited)
    return 'Your advertisment added!'
def my_history_estate(name):
    with open('users.txt') as file:
        users=file.readlines()
    for user in users:
        if user!='\n':
            if user.split('>>')[0]==name:
                import ast
                on_sales=list(ast.literal_eval(user.split('>>')[-1]))
                on_sell=[]
                for i in on_sales:
                    if len(str(i))==4:
                        on_sell.append(int(i))
    return on_sales  
def ads_remover_estate(code=str,name=str):
    with open('users.txt') as file:
        users=file.readlines()
    edited_user=[]
    for user in users:
        if user!='\n':
            if user.split('>>')[0]!=name:
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{user.split('>>')[2]}>>{user.split('>>')[3]}')    
            else:
                import ast
                on_sales=list(ast.literal_eval(user.split('>>')[-1]))
                print(on_sales)
                on_sales.remove(code)
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{user.split('>>')[2]}>>{on_sales}\n') 
    with open('users.txt','w') as file:
        file.writelines(edited_user)
    with open('realestate.txt') as file:
        estates=file.readlines()
    new=[]
    for estate in estates:
        if estate!='\n':
            if code!=int(estate.split('>>')[0]):
                new.append(estate)  
    with open('realestate.txt','w') as file:
        file.writelines(new)
    return 'Your Ads has removed'
def estate_ads_display():
    with open('realestate.txt') as file:
        estates=file.readlines()
    res=''
    for estate in estates:
        if estate!='\n':
            estate=estate.split('>>')
            res+=f'{estate[0]}>>{estate[1]}>>{estate[2]}>>{estate[3]}>>{estate[4]}>>{estate[5]}'
    if len(res)==0:
        r='No ads to display!'
    else:
        r=res
    return r
def purchasing_estate(name0,code0):
    with open('realestate.txt') as file:
        estates=file.readlines()
    name=''
    value=0
    ram=0
    edited_estate=[]
    for estate in estates:
        code=int(code0)
        if estate!='\n':
            if code!=int(estate.split('>>')[0]):
                edited_estate.append(estate)  
            else:
                ram=int(estate.split('>>')[0])
                value=int(estate.split(">>")[4])
                name=estate.split('>>')[-1].split('\n')[0]
    with open('realestate.txt','w') as file:
        file.writelines(edited_estate)
    with open('users.txt') as file:
        users=file.readlines()
    edited_user=[]
    for user in users:
        if user!='\n':
            if user.split('>>')[0]!=name:
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{user.split('>>')[2]}>>{user.split('>>')[3]}\n')    
            else:
                import ast
                on_sales=(ast.literal_eval(user.split('>>')[-1]))
                on_sales.remove(ram)
                amount=value+int(user.split('>>')[2])
                edited_user.append(f'{user.split('>>')[0]}>>{user.split('>>')[1]}>>{amount}>>{on_sales}\n') 
    with open('users.txt','w') as file:
        file.writelines(edited_user)    
    with open('users.txt') as file:
        users1=file.readlines()
    rewrited=[]
    for user1 in users1:
        if user1!='\n':
            if user1.split('>>')[0]!=name0:
                rewrited.append(user1)
            else:
                user1=user1.split('>>')
                user1[2]=int(user1[2])
                amount=user1[2]-value
                rewrited.append(f'{user1[0]}>>{user1[1]}>>{amount}>>{user1[-1].split('\n')[0]}\n')
    with open('users.txt','w') as file2:
        file2.writelines(rewrited)
    return 'Estate purchase!'
def all_estates():
    with open('realestate.txt') as file:
        estates=file.readlines()
    codes=[]
    for estate in estates:
        if estate!='\n':
            estate=estate.split('>>')
            codes.append(int(estate[0]))
    return codes
 