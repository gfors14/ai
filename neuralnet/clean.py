with open('alcoholism_traintest.csv', 'r') as file:

    # holds clean data
    cleanData = []

    col=0 # column titles

    for line in file:

        # skipping column titles
        if(col==0):
            col=1
            continue
            
        row = line.strip().split(',') 
        cleanRow = [] # clean row

        #skipping missing entires instead of filling them in
        if not all(row):
            continue

        # removing rows with -999
        if "-999" in row:
            del row
            continue
        
        # clean
        for val in row[1:]:
            val = int(val)
            if val==1 or val==-1 or val==0:
                cleanRow.append(val)
            elif val<3:
                cleanRow.append(0)
            else:
                cleanRow.append(1)
        cleanData.append(cleanRow)

# copy clean data
with open('cleaned.csv', 'w', newline='') as file:

    for row in cleanData:
        file.write(','.join(map(str, row)) + '\n')