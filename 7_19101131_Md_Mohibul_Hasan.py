import random

trans=[]
num=int(input("Enter the number of transaction"))
for i in range(num):
    # data=input()
    # if data[0]=='l':
    #     a=data.split(' ')[1]
    #     trans.append(int(a)*-1)
    # elif data[0] =='d':
    #     a=data.split(' ')[1]
    #     trans.append(int(a))
    # else:
    #     print("Wrong input")
    #     break
    n=int(input())
    trans.append(n)
def zero_checker(p1):
    zero=[]
    for i in range(len(p1)):
        zero.append(0)
    if p1 == zero:
        return False
    else:
        return True
        
    
def fitness(arr, pop):    #fitness
    sum= 0
    for i in range(len(arr)):
        sum+=arr[i]*pop[i]
    return abs(sum)
def selection(arr, c1, c2, c3,c4):   #parent selection
    a=[]
    b=[]
    fit1=fitness(arr, c1)
    fit2=fitness(arr, c2)
    fit3=fitness(arr, c3)
    fit4=fitness(arr, c4)
    sortlist=[fit1, fit2, fit3, fit4]
    sortlist.sort()
    for i in range(3):
        if sortlist[0]== fitness(arr, c1):
            a= c1
        elif sortlist[0]== fitness(arr, c2):
            a=c2
        elif sortlist[0]== fitness(arr, c3):
            a=c3
        else:
            a= c4
    for i in range(3):
        if sortlist[1]== fitness(arr, c1):
            b=c1
        elif sortlist[1]== fitness(arr, c2):
            b=c2
        elif sortlist[1]== fitness(arr, c3):
            b=c3
        else:
            b= c4
    return a, b


def chromosome(arr):     #random population
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    for i in range(len(arr)):
        c1.append(random.randrange(-100,100))
        c2.append(random.randrange(-100,100))
        c3.append(random.randrange(-100,100))
        c4.append(random.randrange(-100,100))
    p1=selection(arr, c1, c2, c3, c4)[0]
    p2=selection(arr, c1, c2, c3, c4)[1]
    return p1, p2
def crossover(p1,p2):     #crossover
    half=int(len(p1)/2)
    for i in range(half, len(p1)):
        p1[i],p2[i]=p2[i],p1[i]
    return p1, p2

def mutation(par1,par2):    #mutation
    index=random.randrange(len(par1))
    par1[index]=random.randrange(-100,100)
    index=random.randrange(len(par2))
    par2[index]=random.randrange(-100,100)
    return par1, par2
def ga(arr):                  #Genetic_algorithm Function
     count=0     
     child1= crossover(chromosome(arr)[0], chromosome(arr)[1])[0]
     child2= crossover(chromosome(arr)[0], chromosome(arr)[1])[1]
     child3=mutation(child1, child2)[0]
     child4=mutation(child1, child2)[1]
     for i in range(10000):
         parent1=selection(arr, child1, child2, child3, child4)[0]
         parent2=selection(arr, child1, child2, child3, child4)[1]
         if fitness(arr, parent1)==0 and zero_checker(parent1)== True:
             count+=1
             print(parent1)
             break
         elif fitness(arr, parent2)==0 and zero_checker(parent2)== True:
             count+=1
             print(parent2)
             break
         child1=crossover(parent1, parent2)[0]
         child2=crossover(parent1, parent2)[1]
         child3=mutation(child1, child2)[0]
         child4=mutation(child1, child2)[1]
         if fitness(arr, child1)==0 and zero_checker(child1)== True:
             count+=1
             print(child1)
             break
         elif fitness(arr, child2)==0 and zero_checker(child2)== True :
            count+=1
            print(child2)
            break
         elif fitness(arr, child3)==0 and zero_checker(child3)== True:
            count+=1
            print(child3)
            break
         elif fitness(arr, child4)==0 and zero_checker(child4)== True:
            count+=1
            print(child4)
            break
     if count==0:
        print("-1")
ga(trans)