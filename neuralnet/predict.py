with open('cleaned.csv', 'r') as file:
    currentRow = 0
    testRows = []
    trainRows = []
    lines = file.readlines()

    #8020 split
    for line in lines:
        row = line.strip().split(',')
    
        if currentRow % 5 == 0:
            testRows.append(row)
        else:
            trainRows.append(row)
        
        currentRow += 1
        
step = 0.1
threshold = 4.5
weight = 1.0
rounds = 10

#finds answer location
answer = len(trainRows[1])-1
perceptrons = []

#training
for i in range(rounds):
    if i==0:
        for j in range(len(trainRows[1])-1):
            perceptrons.append(weight)

    trainedPerceptrons = perceptrons.copy()

    for row in trainRows:
        output = 0
        ans = int(row[answer])

        for i in range(len(row)-1):
            output = output + (int(row[i]) * trainedPerceptrons[i])

        if output > threshold:
            predict = 1
        else:
            predict = 0

        if predict == ans:
            continue

        #adjustment based on threshold
        elif predict < ans: #under threshold
            for j in range(len(row)-1):
                if int(row[j]) == 1:
                    newVal = trainedPerceptrons[j] + step
                    trainedPerceptrons[j] = round(newVal,2)
        else: #over threshold
            for j in range(len(row)-1):
                if int(row[j]) == 1:
                    newVal = trainedPerceptrons[j] - step
                    trainedPerceptrons[j] = round(newVal,2)
            
    #check convergence
    if(trainedPerceptrons == perceptrons):
        break
    else:
        perceptrons = trainedPerceptrons.copy()

# starting test
predPos = 0

for test in testRows:
    tOutput = 0
    tAnswer = int(test[answer])

    for n in range(len(test)-1):
        tOutput = tOutput + (int(test[n]) * perceptrons[n])

    if tOutput > threshold:
        predict = 1
    else:
        predict = 0

    if predict == tAnswer:
        predPos += 1
    else:
        continue

# write answers to weights.txt
with open('weights.txt', 'w') as file:
    file.write(str(threshold))
    file.write('\n')

    index = 1
    for p in perceptrons:
        file.write(str(index))
        file.write(". ")
        file.write(str(p))
        file.write('\n')
        index +=1