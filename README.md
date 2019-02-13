Energy Dash Boared for stonehill College

# Table of Contents
[Installing Python Requirements](#installing-python-requirements)  
[Installing MongoDB](#installing-mongodb)  
[Running MongoDB](#running-mongodb)

# Installing Python Requirements
This project requires the following python packages:  
beautifulsoup4  
pymongo  
requests

These packages are listed in requirements.txt and can be installed with the command ```pip install -r requirements.txt```
## (Optional) Using a Virtual Environment
If you wish to keep these projects requirements along with their versioning separate from your other libraries
you may install the requirements with in a virtual environment

### Anaconda/Miniconda
To create an environment with these tools type ```conda create --name myenv```
Activate the environment with  

Linux or Mac ```conda activate myenv```  
Windows ```activate myenv```

Once you are inside the environment type ```conda install --file requirements.txt```
If you use Anaconda/Miniconda your virtual environment will not take up space in the repository

# Installing MongoDB
If you want to run the application locally you will need to be running an instance of mongo on your local machine

## MacOS
The easiest way to install mongo on mac is to use homebrew.
If you do not have homebrew installed you can do so by executing ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``` in your terminal.

The installation for brew will take several minutes.

Once it it installed you can install mongo by typing ```brew install mongodb``` into your terminal.

## Linux

### Ubuntu
```sudo apt-get install mongodb mongodb-server```
### Fedora
```sudo dnf install mongodb mongodb-server```

## Running MongoDB
### MacOS
To start an instance of Mongo to use with the application type ```mongod``` in the terminal.
The default port to access mongo is 27017
### Linux
```sudo service mongodb start``` and ```sudo service mongodb stop```
