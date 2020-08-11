import time
from datetime import datetime as dt

hosts_temp="hosts"   #created a dummy host file.
hosts_path="C:\Windows\System32\drivers\etc\hosts"  #actual host file with specified path for windows OS.
redirect="127.0.0.1"       #faulty IP address to redirect the websites and not to orignal IP.
website_list=["www.facebook.com","facebook.com","www.youtube.com","youtube.com","www.instagram.com","instagram.com"]  #list of the websites to be blocked.

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15): #compairing the current time with the set time frame to checck whether we have to block or not.
        print("TIME TO STUDY")                      # if current time lies between the scheduled time, it enter the condition and print.
        with open(hosts_temp,'r+') as file: #command to open host_temp and r+ command is used because we are  reading  and appending at the same time .
            content=file.read()  # saving the content of the host_temp file in a variable named content
            for website in website_list: #checking condition for websites in the website_list 
                if website in content: # if the websites string  are present in the data of content variable i.e. it means that the websites are already blocked.
                    pass # therefore pass the command and dont do anything
                else:
                    file.write(redirect +" "+ website+"\n")    #if the list of website is not present then this write command edits the host file and write the faulty IP address and the name of website to block them

    else: #if the current time does not lies between scheduled time then we have to remove the list of websites from host file to unblock it by accessing the content of the host file and removing only websites name and faulty IP and leaving everything as same as before..

        with open(hosts_temp,'r+') as file: #command to open host_temp and r+ command is used because we are  reading  and appending at the same time .
            content=file.readlines() #instead of read command used previously,  we used readlines  because read will store the host file content in a single string whereas readlines will store each lines of the hosts file as a single string.
            file.seek(0) #takes the cursor at starting of the host file.
            for line in content: #for each line present in content variable
                if not any(website in line for website in website_list): #if no websites name from website_list is present
                    file.write(line) # write that line in the host file..this command will be valid for all the lines except the last lines which has the list of websites.
            file.truncate()     # at last this command deletes whaever is remaining at the current file and downwards.  
        print("TIME TO HAVE SOME FUN") #if the current time does not lies in the scheduled time then print this statement
    time.sleep(5) #run this command for every 5 seconds. for 5 minutes we can do 300 sec.