admins={'Amir':'1386'}
def budget():
    with open('budget.txt','r')as file:
        budget=file.readline()
    return int(budget)
def add_car(n,m,p):
    with open('cars.txt','a') as cars:
        cars.write(f'{n}>>{m}>>{p}\n')
    return 'car succesfully added!'
def display_cars():
    with open('cars.txt','r') as file :
        cars=file.readlines()
        c=''
        for car in cars:
            car=car.split('>>')
            c+=f'{car[0]}>>{car[1]}>>{car[2]}'
    return c
def remove_car(n):
    with open('cars.txt','r') as file:
        cars=file.readlines()
        new_cars=[]
        for car in cars:
            if car.split('>>')[0]!=n:
                new_cars.append(car)
    with open('cars.txt','w') as file:
        file.writelines(new_cars)
