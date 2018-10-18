import csv

def main():
    arrOfBuildingNames,arrOfIpAdresses=readInCSV()
    print(arrOfIpAdresses,arrOfIpAdresses)
    #SCRAPE WEB HERE

def readInCSV():
    arrOfBuildingNames = []
    arrOfIpAdresses=[]
    with open('Meter_IP_addresses.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lineCount=0
        for row in csv_reader:
            #print(row)
            row=str(row)
            if(lineCount==0):
                print(row)

            else:
                print(row)
                #rowSplit=row.split(',')

                arrOfBuildingNames[lineCount-1]=row[1]
                arrOfIpAdresses[lineCount - 1] = row[2]

            lineCount+=1
    return arrOfIpAdresses,arrOfBuildingNames

if __name__ == '__main__':
    main()