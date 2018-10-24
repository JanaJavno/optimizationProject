#
budget = 70

class Candidate:
    def __init__(self, name, minSalary, level):
        self.name = name
        self.minSalary = minSalary
        self.level = level

candidates = []

candidateDetails, candidateAmount = '', 0
with open('input.txt', 'r+', encoding='utf8') as fileinput:
    for line in fileinput:
        line = line.strip('}{\n')
        candidateDetails = line.split(', ')
        candidates.append(Candidate(candidateDetails[0], int(int(candidateDetails[1].strip('минимальная зарплата'))/100),
                                    int(candidateDetails[2].strip('навык уровня'))))
        candidateAmount += 1

a = [[-1 for x in range(budget + 1)] for y in range(candidateAmount + 1)]

def findMax(k, s):
    if k == 0:
        a[k][s] = 0
        return 0
    if s == 0:
        a[k][s] = 0
        return 0
    a[k-1][s] = a[k-1][s] if a[k-1][s] != -1 else findMax(k - 1, s)
    if s-candidates[k - 1].minSalary >= 0:
        a[k-1][s-candidates[k - 1].minSalary] = a[k-1][s-candidates[k - 1].minSalary] \
            if a[k-1][s-candidates[k - 1].minSalary] != -1 else findMax(k - 1, s-candidates[k - 1].minSalary)
        return max(a[k-1][s], a[k-1][s-candidates[k - 1].minSalary] + candidates[k - 1].level)
    else:
        return a[k-1][s]


with open("output.txt", "w") as fileoutput:
    fileoutput.write(str(findMax(candidateAmount, budget)) + '\n')
    indexes = [None]*candidateAmount
    for i in range(candidateAmount, 0, -1):
        if findMax(i, budget) == findMax(i - 1, budget):
            indexes[i - 1] = 0
        else:
            indexes[i - 1] = 1
            budget -= candidates[i - 1].minSalary
    fileoutput.write(str(indexes))