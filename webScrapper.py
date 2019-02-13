import csv
import time
from selenium import webdriver
from model.MeterReading import MeterReading
from model.MeterReading import MeterReading
from contextlib import closing

def main():
    arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling=readInCSV()
    #print(arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling)
    url = ""
    #print(simple_get(url))
    timStamp=time.clock()
    arrOfMeterReadings=[]
    arrOfID,arrOfVals=scrapeWeb()
    i=0
    for item in arrOfID:

        if item in arrOfEnDel:

            tempName=arrOfBuildingNames[arrOfEnDel.index(item)]
            tempValue=arrOfVals[i]
            tempTimeStamp=timStamp
            tempMeter = MeterReading(tempName,tempValue,tempTimeStamp)
            arrOfMeterReadings.append(tempMeter)
        i+=1

    return arrOfMeterReadings


def scrapeWeb():
    sess = webdriver.Chrome()
    sess.get("http://10.150.2.72/obix/config/Drivers/ObixNetwork/exports/")
    element=sess.find_element_by_id('username')

    element.send_keys('energy')
    element1 = sess.find_element_by_id('password')
    print(element1.id)
    element1.send_keys('meters')
    #print(sess.page_source)
    butt=sess.find_element_by_id('submitButton')

    butt.click()
    num=sess.page_source

    time.sleep(1)
    #print (num)
    pagesourseString = sess.page_source
    #print(pagesourseString)
    arrOfValues=[]
    arrOfEnergyDel=[]
    i=0

    while True:
        if i==0:
            print("HERE")
            splitString = pagesourseString.find('body')
            pagesourseString = pagesourseString[splitString + 5:]
        elif i==1:
            print("HERE")
            splitString = pagesourseString.find('display')
            pagesourseString = pagesourseString[splitString + 5:]
        else:

            splitString=pagesourseString.find('EnergyDelivered')
            #print(splitString)
            if splitString==-1:
                break
            pagesourseString=pagesourseString[splitString:]
            #print(pagesourseString)
            #SystemExit
            splitString=pagesourseString.find('\"')
            arrOfEnergyDel.append(pagesourseString[:splitString])
            splitString = pagesourseString.find('display')
            print(pagesourseString)

            pagesourseString = pagesourseString[splitString + 58:]
            temp =pagesourseString.find('\"')
            #print(pagesourseString)
            arrOfValues.append(pagesourseString[:temp])
            throwOut=pagesourseString.find('display')
            pagesourseString=pagesourseString[throwOut+2:]
        i+=1
    print(arrOfValues)
    print(arrOfEnergyDel)
    return (arrOfEnergyDel,arrOfValues)


    #br = mechanize.Browser()
    ##print("http://"+ipAdress+"/obix/config/Drivers/ObixNetwork/exports/EnergyDelivered_ASC/")
    #try:
    #payload = {'username': 'energy', 'password': 'meters'}
    #url="http://"+ipAdress+"/obix/config/Drivers/ObixNetwork/exports/EnergyDelivered_ASC/"
    #r =requests.(url,payload)
    #print (r.text)
    #except:
        #return False
def readInCSV():
    arrOfBuildingNames = []
    arrOfIpAdresses=[]
    arrOfEnDel=[]
    arrOfHeating=[]
    arrOfCooling=[]

    with open('Meter_IP_addresses.CSV',mode='r') as csv_file:
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