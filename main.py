import copy
import math

def floatArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = float(arr[i][j])
def powerSigma(arr):
    sigma = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sigma += (arr[i][j]**2)
    sigma = math.sqrt(sigma)
    return sigma
def normalize(arr):
    sigma = powerSigma(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = (arr[i][j]/sigma)
def distance(normalizedArr, normalUnnormalIdeal):
    distance = []
    for i in range(len(normalizedArr)):
        sigma = 0
        for j in range(len(normalizedArr[0])):
            sigma += ((normalizedArr[i][j]-normalUnnormalIdeal)**2)
        sigma = math.sqrt(sigma)
        distance.append(sigma)
    return distance
def normalizeIdeal(Ideal, unnormalizedArr):
    return (Ideal/powerSigma(unnormalizedArr))
#LINMAP Function
def LINMAP(CSVArr, IdealPoint):
    normalizedArr = copy.deepcopy(CSVArr)
    IdealPoint = normalizeIdeal(IdealPoint, normalizedArr)
    normalize(normalizedArr)
    dplus = distance(normalizedArr, IdealPoint)
    print("LINMAP Point index is {i}".format(i = dplus.index(min(dplus))))
    print("LINMAP Point is {i}".format(i = CSVArr[dplus.index(min(dplus))]))


print("Enter Path of CSV file:")
path = input()
print("Enter Ideal Point:")
IdealPoint = float(input())
print("Enter nonIdeal Point:")
nonIdealPoint = float(input())

CSVFile = []
with open(path, "r") as f:
    for i in f:
        CSVFile.append(i.replace(",", " ").split())
    floatArray(CSVFile)
LINMAP(CSVFile, IdealPoint)

