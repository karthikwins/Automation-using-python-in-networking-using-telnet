Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os, sys, re, telnetlib, pyautogui, openpyxl, datetime, time


def telnetting():

    host = "ip address"

    port = 23

    tn = telnetlib.Telnet()


    tn.open(host,port)

    tn.write(b'username')

    tn.write(b'password')

    time.sleep(0.25)

    
    tn.write(b'sh ip int brief gi2/2\n')

    time.sleep(0.25)
    
    result = tn.read_very_eager().decode('utf-8')

    print(result)
    
    res=str(result)

    tn.close()

    l = res.split("\n")
    li=[]
    for i in l:
        j=i.replace("\r","")
        
        if j != '':
            li.append(j)

    my_str = li[-2]
    global my_list
    my_list = re.split(r'\s+', my_str)

        if len(my_list)==7:
        printing_to_excel()
    else:
        time.sleep(5)
        telnetting()
    return my_list


def printing_to_excel():

    path ="C:\\Users\\root\\Desktop\\demo.xlsx"

    wb= openpyxl.load_workbook(path)

    ws=wb.active

    r=ws.max_row

    c=ws.max_column

    for a in range(1,r+1):
        for b in range(1,c+1):
            x=ws.cell(a,b).value
            ws.cell(a,b).value = x

    for i in range(1,(len(my_list))):
                   ws.cell(r+1,i).value=my_list[i-1]
                   ws.cell(r+1,i+1).value = datetime.datetime.now()
                
    wb.save(path)



telnetting()