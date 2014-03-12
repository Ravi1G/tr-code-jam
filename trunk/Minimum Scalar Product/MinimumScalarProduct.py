with open('A-large-practice.in', 'r') as inputFile:
    with open('output.txt' ,'w') as outputFile:
        caseCount = int(inputFile.readline())
        print("Case Count : " + str(caseCount))

        for i in range(1, caseCount+1):
            #print("Case : " + str(i))

            vectorItems = int(inputFile.readline())
            #print("Items Count : " + str(vectorItems))

            vector1 = sorted([int(x) for x in inputFile.readline().split()])
            vector2 = sorted([int(x) for x in inputFile.readline().split()], reverse=True)
            pairs = zip(vector1, vector2)
            products = [x[0]*x[1] for x in pairs]
            scalarProduct = sum(products)

            #print (scalarProduct)
            outputFile.write("Case #" + str(i) + ": " + str(scalarProduct) + "\n")
