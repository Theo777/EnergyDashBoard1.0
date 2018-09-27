import csv

def main():
    arrOfBuildingNames,arrOfIpAdresses=readInCSV()
    #SCRAPE WEB HERE

def readInCSV():
    arrOfBuildingNames = []
    arrOfIpAdresses=[]
    with open('Meter_IP_addresses.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

    return arrOfIpAdresses,arrOfBuildingNames

if __name__ == '__main__':
    main()