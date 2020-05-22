# frs.gov.cz_app_status

This set of scripts (appStatus) can be interesting for those people who live in Czech Republic as foreigners.

## Overview

As a foreigner in Czech Republic, you should periodically apply a request for your residence prolongation at the Ministry of Interior.

In old days, the results were published on site in an xls file. Now, there is a specific form for that.

appStatus takes as an input numbers of application requests, opens a browser, fills parameters in a form and returns results of applied requests.

It is writen in Python and uses Selenium web driver to automate this task.

It runs under Windows, Linux and MacOS.

It supports Chrome, FireFox and Safari web browsers.

## Getting Started

* Install Python3.7 x64

    <code>http://pytyhon.org</code>

*  Install virtualenv Python module

    <code>python3.7 -m pip install virtualenv</code>
    
    Note, sometimes you should in stall pip itself. On Ubuntu-based systems:
    
    <code>sudo apt install python-pip</code>
  
* Clone repository

  <code>git clone https://github.com/avsokol/frs.gov.cz_app_status.git</code>

* Create virtual environment

  <code>cd ./frs.gov.cz_app_status.git</code>

  <code>python3 -m virtualenv venv</code>

* Activate the virtual environment

  <code>source ./venv/bin/activate</code>

* Install required Python modules, run:

  <code>python3 -m pip install -r requirements.txt</code>

* Set PYTHONPATH
  
  <code>export PYTHONPATH=~/frs.gov.cz_app_status.git</code>

* Fill input data

    Fill you application numbers in file:
    <code>resources/input_data.txt</code>
    
    Each line should contain one application number, like:
    
    <code>OAM-0xxxx-y/DP-2019</code><br>
    <code>OAM-0xxxx/DP-2019</code><br>
    <code>OAM-xxxxx/ZM-2019</code>

* Decide which browser you will use

    You can choose among 3 most popular browsers: Chrome, FireFox and Safari (under MacOS only).
    Note, that chrome requires Chrome browser installed on your system and to be the same version.

    Chrome and FireFox allows running in a **headless** mode - this is the default option. Safari doesn't have such possibility.
    
    **headless** mode means that browser will run without any graphic interface, like in a command line.

* Run Application

    Here is the example how to run application with FireFox browser:
    
    <code>./venv/bin/python ./lib/firefox_engine.py</code>
 
* Take a look at results you get

    Results will be shown in a console and in a file:
    
    <code>resources/output_data.txt</code>
