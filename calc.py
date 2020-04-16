import math


def pmean(data):
    print('data: ', data)
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    mean = sum(data) / len(data)

    return mean


def mode(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    n = len(data)
    getMode = {}

    for l in data:
        getMode[l] = getMode.get(l, 0) + 1

    maxValue = max(list(getMode.values()))
    modeValue = [a for a, v in getMode.items() if v == maxValue]

    if len(modeValue) == n:
        return 0
    else:
        return modeValue[0]


def median(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    listLength = len(data)
    sortedList = sorted(data)
    index = (listLength - 1) // 2
    if (listLength % 2):
        return sortedList[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0


def stddev(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]
    # CSVlues are supposed to be the values that are given
    u = 0
    #This is the Mean
    Top = 0
    # This is the top half of the equation
    Set = 0
    # This the bottom half of the equation
    Ans = 0
    # This is the Answer
    u = sum(data)/len(data)

    for i in data:
        Top +=(i-u)**2

    Set = Top/len(data)

    Ans = math.sqrt(Set)

    return Ans

def variance(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    mean = sum(data) / len(data)
    populationProportion = 1 / len(data)
    print('populationProportion: ', populationProportion)
    if populationProportion != 0:
        varianceOfPopulation = sum((xi - mean) ** 2 for xi in data) / populationProportion
    else:
        varianceOfPopulation = 0

    return varianceOfPopulation

def zscore(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    mean = sum(data) / len(data)
    std = math.sqrt(sum([(val - mean)**2 for val in data])/(len(data) - 1))
    scores = []
    for num in data:
        # calculates the z-score of each number in the dataset
        zScore = (num - mean)/std
        scores.append(zScore)
    return scores

def popcorcoeff(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    # data.pop()

    halfOfLength = int((len(data)) / 2)
    endOfList = int(len(data))
    dataX = data[halfOfLength:endOfList]
    print('dataX: ', dataX)

    print('len(data): ', len(data))

    dataY = data[0:halfOfLength]
    print('dataY: ', dataY)

    Ex = sum(dataX)
    Ey = sum(dataY)
    Exy = 0
    Ex2 = 0
    Ey2 = 0
    n = len(dataX)

    if n != len(dataY):
        cake ='The two data sets that you have entered do not have the same number of numbers.'
        return 0
    else:
        for i in range(len(dataX)):
            Exy += dataX[i]* dataY[i]
            Ex2 += dataX[i] ** 2
            Ey2 += dataY[i] ** 2

        Top = 0
        Top = (n*Exy) - (Ex*Ey)
        Bottom = 0
        Bottom = math.sqrt((n*Ex2-Ex**2)* (n*Ey2-Ey**2))
        ans = Top/Bottom
        return ans

def confint(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    confidence = .95
    n = len(data)
    m = sum(data) / n
    std = math.sqrt(sum([(val - m)**2 for val in data])/(len(data) - 1))
    std_err = std / math.sqrt(n)
    t = m / std_err
    h = std_err * t * float(1 + confidence) / float((n - 1) + 2)

    start = m + h
    end = m - h

    return start, end

def pvar(data):
    data = [elem for elem in data if elem.strip()]
    i = 0
    while i < len(data):
        if data[i] == ',':
            data.remove(data[i])
        else:
            i += 1
    data = [float(s) for s in data]

    mean = sum(data) / len(data)

    variance = sum((xi - mean) ** 2 for xi in data) / len(data)
    return variance

def sin(data):
    data = int(data)
    return(math.sin(data))

def cos(data):
    data = int(data)
    return(math.cos(data))

def tan(data):
    data = int(data)
    return(math.tan(data))