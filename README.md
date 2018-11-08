Energy Dash Boared for stonehill College

# Table of Contents
[Installing Python Requirements](#installing-python-requirements)

[Installing MongoDB](#installing-mongodb)

# Installing Python Requirements
This project requires the following python packages:
beautifulsoup4
pymongo
requests

These packages are listed in requirements.txt and can be installed with the command ```pip install -r requirements.txt```

# Installing MongoDB
If you want to run the application locally you will need to be running an instance of mongo on your local machine

## MacOS
The easiest way to install mongo on mac is to use homebrew.
If you do not have homebrew installed you can do so by executing ```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"``` in your terminal.

The installation for brew will take several minutes.

Once it it installed you can install mongo by typing ```brew install mongodb``` into your terminal.

## Linux

### Ubuntu
```sudo apt-get install mongodb```

## Running Mongo
To start an instance of Mongo to use with the application type ```mongod``` in the terminal.
The default port to access mongo is 27017
