import copy
import math

def floatArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = float(arr[i][j])
def powerSigma(arr):
    sigma = []
    for i in range(len(arr[0])):
        sigma.append(0)
        for j in range(len(arr)):
            sigma[i] += (arr[j][i]**2)
        sigma[i] = math.sqrt(sigma[i])
    return sigma
def normalize(arr):
    sigma = powerSigma(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = (arr[i][j]/sigma[j])
def distance(normalizedArr, normalUnnormalIdeal):
    distance = []
    for i in range(len(normalizedArr)):
        sigma = 0
        for j in range(len(normalizedArr[0])):
            sigma += ((normalizedArr[i][j]-normalUnnormalIdeal[j])**2)
        sigma = math.sqrt(sigma)
        distance.append(sigma)
    return distance
def normalizeIdeal(Ideal, unnormalizedArr):
    for i in range(len(Ideal)):
        Ideal[i] = (Ideal[i]/powerSigma(unnoramlizedArr)[i])
    return Ideal
#LINMAP Function
def LINMAP(CSVArr, IdealPoints):
    normalizedArr = copy.deepcopy(CSVArr)
    IdealPoints = normalizeIdeal(IdealPoints, normalizedArr)
    normalize(normalizedArr)
    dplus = distance(normalizedArr, IdealPoints)
    print("LINMAP Point index is {i}".format(i = dplus.index(min(dplus))))
    print("LINMAP Point is {i}".format(i = CSVArr[dplus.index(min(dplus))]))


print("Enter Path of CSV file:")
path = input()
print("Enter Ideal Point:")
IdealPoints = float(input())
print("Enter nonIdeal Point:")
nonIdealPoints = float(input())

CSVFile = []
with open(path, "r") as f:
    for i in f:
        CSVFile.append(i.replace(",", " ").split())
    floatArray(CSVFile)
LINMAP(CSVFile, IdealPoints)

