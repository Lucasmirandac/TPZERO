import math

with open('exemplo100.txt', 'r') as myfile:
    data = myfile.readlines()
notes = []
names = []

for x in data:
    notes.append(int(x.split(",")[1])) #Separating the int part of the file
    names.append(x.split(",")[0]) # separating the name of the student

def minmax_note (names,notes):
    major = 0 # seeting max as min for algorithm logic
    temp = 0
    min = 100 # setting min as max for the algorithm logic
    namesmax = []
    namesmin = []

    for x in notes:
        if x >= major:                   #Catch the maximum value and the position of this max to define the person who has taken this grade#
            major = x
            imax = temp
        if x <= min:                     #Catch the minimum value and the position of this min to define the person who has taken this grade#
            min = x
            imin = temp
        temp +=1
    #Procurando o valor na lista, pego a posição em que ele se encontra e adiciono o nome ao vetor

    temp = 0
    for n in notes:
        if  n == major:
            namesmax.append(names[temp])
        if n == min:
            namesmin.append(names[temp])
        temp +=1



    print("The biggest grade is: {} from {}".format(major,namesmax))
    print('The lowest grade is {} from {}'.format(min,namesmin))

def avg(notes):
    sum = 0
    n = len(notes)

    for x in notes:
        sum = sum+x

    avgnote = sum/n

    return avgnote

def std_deviation (avg, notes):
    avg_std_deviation = avg(notes)
    length = len(notes)
    numerator = 0
    for x in notes:
        float(x)
        numerator = numerator + math.pow(x-avg_std_deviation, 2)

    stand_deviation = raiz = math.pow(numerator/length, 1/2)

    return stand_deviation

def histogram (notes):

    printtimes = [0] * 10 #This variabel count the number of numbers on the range
    i = 0
    notes.sort()
    for n in notes:
        if n > 0 and n < 10:
            printtimes[0] += 1
        if n > 9 and n < 20:
            printtimes[1] += 1
        if n > 19 and n < 30:
            printtimes[2] += 1
        if n > 29 and n < 40:
            printtimes[3] += 1
        if n > 39 and n < 50:
            printtimes[4] += 1
        if n > 49 and n < 60:
            printtimes[5] += 1
        if n > 59 and n < 70:
            printtimes[6] += 1
        if n > 69 and n < 80:
            printtimes[7] += 1
        if n > 79 and n < 90:
            printtimes[8] += 1
        if n > 89 and n <= 100:
            printtimes[9] += 1

    LengthMax = max(printtimes)+1
    print('Histrogram:\n\nY:')

    for n in range(LengthMax):
        print(LengthMax, end='')
        for p in range(0,10):
            if  LengthMax <= printtimes[p]:
                print("\t", end='')
                print("*", end='')
            else:
                print("\t", end='')
            i+=1
        print('\n', end='')
        LengthMax = LengthMax - 1

    print('X:\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9', end='')

def GreaterThanAvg(notes):
    average = avg(notes)
    greater = 0
    for n in notes:
        if n>average:
            greater +=1
    print("{} Students have grades above the average".format(greater))

minmax_note(names,notes)
average=avg(notes)
print(round(average,2))
stand_deviation = std_deviation(avg,notes)
print(round(stand_deviation,2))
GreaterThanAvg(notes)
histogram(notes)

