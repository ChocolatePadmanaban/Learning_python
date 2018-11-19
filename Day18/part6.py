#Sending Mail from python

import smtplib

def EmailDef(filename= 'password.txt'):
    l=[]
    with open(filename,mode='r')as File1:
        for i in File1:
            l.append(i.strip())
    email, password = l
    return email, password

def ConnectInternet(email,password):
    # creates SMTP session 
    s = smtplib.SMTP('smtp-mail.outlook.com', 587)  
    # start TLS for security 
    s.starttls()  
    # Authentication 
    s.login(email,password)  
    # message to be sent 
    message = """from:	 <pradeeppadmanaban.c@hcl.com>
    to:	<pradeeppadmanaban7@gmail.com>   
    Subject: Hello

    Hello Pradeep,
        this is a test message

    thank you,
    Pradeep 
    """  
    # sending the mail 
    s.sendmail(email, "pradeeppadmanaban7@gmail.com", message)  
    # terminating the session 
    s.quit() 

if __name__ == '__main__':
    email , password = EmailDef()
    ConnectInternet(email, password)