import csv
import codecs
from lxml import html
from contextlib import closing

import itertools
def main():
    arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling=readInCSV()
    print(arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling)
    url = ""
    #print(simple_get(url))
    for (building,ipAdres,enDel,heating,cooling) in itertools.izip_longest(arrOfBuildingNames, arrOfIpAdresses, arrOfEnDel, arrOfHeating, arrOfCooling):



def scrapeWeb():
    session_requests = requests.session()
    login_url = "https://bitbucket.org/account/signin/?next=/"
    result = session_requests.get(login_url)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    result = session_requests.post(login_url,data=payload,headers=dict(referer=login_url))

def readInCSV():
    arrOfBuildingNames = []
    arrOfIpAdresses=[]
    arrOfEnDel=[]
    arrOfHeating=[]
    arrOfCooling=[]

    with open('ACMMeters.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lineCount=0
        for row in csv_reader:
            #print(row)
            #row=str(row)
            if(lineCount==0):
                 print(None)


            else:
                #print(row)
                #print(row[2])
                #rowSplit=row.split(',')

                arrOfBuildingNames.append(row[1])
                arrOfIpAdresses.append(row[2])
                arrOfEnDel.append(row[9])
                arrOfHeating.append(row[7])
                arrOfCooling.append(row[8])


            lineCount+=1
    return arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling



if __name__ == '__main__':
    main()