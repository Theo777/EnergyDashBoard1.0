import csv
import mechanize
import time
import codecs
from pyquery import PyQuery
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from contextlib import closing
#import urllib2
import itertools
def main():
    arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling=readInCSV()
    #print(arrOfBuildingNames,arrOfIpAdresses,arrOfEnDel,arrOfHeating,arrOfCooling)
    url = ""
    #print(simple_get(url))
    #for ipAdres in arrOfIpAdresses:
    print(scrapeWeb("10.150.2.72"))


def scrapeWeb(ipAdress):
    sess = webdriver.Chrome()
    sess.get("http://"+ipAdress+"/obix/config/Drivers/ObixNetwork/exports/EnergyDelivered_ASC/")
    element=sess.find_element_by_id('username')

    element.send_keys('energy')
    element1 = sess.find_element_by_id('password')
    print(element1.id)
    element1.send_keys('meters')
    #print(sess.page_source)
    butt=sess.find_element_by_id('submitButton')

    butt.click()
    num=sess.page_source

    time.sleep(10)
    print (num)
    print(sess.page_source)
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