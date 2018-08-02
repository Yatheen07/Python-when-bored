# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:57:32 2018

@author: kmy07
"""

import numpy as np
import webbrowser as wb
import time

def openMyTab(browser,sites_list):
    firefox = 'D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
    wb.register('firefox', None,wb.BackgroundBrowser(firefox),1)

    opera = 'C:\\Program Files\\Opera\\launcher.exe'
    wb.register('opera', None,wb.BackgroundBrowser(opera),1)
    
    chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    wb.register('chrome',None,wb.BackgroundBrowser(chrome),1)
    
    print(browser)
    for i in sites_list:
        wb.get(browser).open_new_tab(i)
        time.sleep(1)

def generate_list(file,browser):
    sites_list = []
    for i in file:
        i = i.replace('\n','')
        sites_list.append(str(i))
    openMyTab(browser,sites_list)



programming = open('./machine_learning_and_programming.txt','r')
communications = open('./communications.txt','r')
entertainment = open('./entertainment.txt','r')



generate_list(programming,'chrome')
generate_list(communications,'opera')
generate_list(entertainment,'firefox')
