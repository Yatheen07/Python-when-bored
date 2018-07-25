# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:19:00 2018

@author: yatheen!
"""

import smtplib

mail = smtplib.SMTP('smtp.gmail.com',587)

def send_mail(from_email,to_email,mail_body,password):
    mail.ehlo()
    #tls is transport layer security to keep your login credentials safe.
    mail.starttls()
    #login to your mail account
    mail.login(from_email,password)
    #send the mail
    mail.sendmail(from_email,to_email,mail_body)
    print("Mail Sent Succesfully!\n")

def get_input():
    #get required data from the user
    from_email = input("Enter your email address: ")
    to_email = input("Enter receipients email address: ")
    password = input("Enter your password: ")
    content = input("Enter the body of the mail ")
    
    #add subject header to the mail
    mail_body = """From: """+from_email+"""\nTo: """+to_email+"""\nSubject: Test Mail Using Python\n"""+content
    
    #Display the details and get Final Confirmation from the User
    confimationStatus = display_confirmation(from_email,to_email,mail_body,password)
    
    if(confimationStatus):
        send_mail(from_email,to_email,mail_body,password)
    
def display_confirmation(from_email,to_email,mail_body,password):
    print("Mail will be sent from \n\n",from_email," to ",to_email,"\n with the following content\n\n",mail_body)
    if(isConfirmed()):
        print("\nSending Mail...\n")
        return True
        
        
def isConfirmed():
    yes = {'yes','y'}
    no = {'no','n'}

    choice = input("Send Mail Now? yes or no? ").lower()
    if choice in yes:
       return True
    elif choice in no:
       return False
    else:
       print("Please respond with 'yes' or 'no'")


get_input()
mail.close()
