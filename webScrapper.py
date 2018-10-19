import csv
import codecs
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
def main():
    arrOfBuildingNames,arrOfIpAdresses=readInCSV()
    print(arrOfIpAdresses,arrOfIpAdresses)
    url = "https://www.google.com/"
    print(simple_get(url))
    #SCRAPE WEB HERE

def readInCSV():
    arrOfBuildingNames = []
    arrOfIpAdresses=[]
    with open('Meter_IP_addresses.csv',mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lineCount=0
        for row in csv_reader:
            print(row)
            #row=str(row)
            if(lineCount==0):
                print(row)

            else:
                #print(row)
                #print(row[0])
                #rowSplit=row.split(',')

                arrOfBuildingNames.append(row[1])
                arrOfIpAdresses.append( row[2])

            lineCount+=1
    return arrOfIpAdresses,arrOfBuildingNames
def simple_get(url):

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):

    print(e)


if __name__ == '__main__':
    main()