from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def result(request):
    number_list = []
    random_list = []
    countEq = 0
 
    '''for i in range(1, 7):
        numName.append('number' + str(i))'''

    for i in range(6):
        number_list.append(int(request.GET['number'+ str(i+1)]))
        random_list.append(random.randint(1, 45))

    for i in range(6):
        if number_list[i] == random_list[i]:
            countEq += 1

    return render(request, 'result.html', {'number_list': number_list, 'random_list': random_list, 'count': countEq}) 