Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os, sys, re, telnetlib, pyautogui, openpyxl, datetime, time



import os, sys, re, telnetlib, pyautogui, openpyxl, datetime, time


def telnetting1():

    host = "172.16.20.1"

    port = 23

    tn = telnetlib.Telnet()


    tn.open(host,port)

    tn.write(b'username')

    tn.write(b'password')

    time.sleep(0.25)

    tn.write(b'terminal length 0\n')
    
    #tn.read_until(b'Sec-INTRA-6506>')
    tn.write(b'sh ip int brief gi1/2\n')

    time.sleep(0.25)
    #result = tn.read_until(b'Sec-INTRA-6506>').decode('utf-8')
    result = tn.read_very_eager().decode('utf-8')

    #result = tn.read_very_eager()

    #print(type(result))

    print(result)
    
    res=str(result)

    
    count = 0

    l = res.split("\n")
    li=[]
    for i in l:
        j=i.replace("\r","")
        
        if j != '':
            li.append(j)

    my_str = li[-2]
    global my_list
    my_list = re.split(r'\s+', my_str)
    #print(my_list)
    #print(len(my_list))
    if len(my_list)==7:
        printing_to_excel1()
    else:
        time.sleep(5)
        count = count +1
        if count<5:
            telnetting()
        else:
            pass

    tn.write(b'terminal length 0\n')

    time.sleep(0.10)
    
    #tn.read_until(b'Sec-INTRA-6506>')
    tn.write(b'sh int gi1/2\n')

    time.sleep(0.10)

    result1 = tn.read_very_eager().decode('utf-8')

    s = result1.split('\n')

    global data_input_rate
    global data_output_rate
    global error_rate

    for i in s:
        if '5 minute input'in i:
            data_input_rate = i
            print(i)
        if '5 minute output'in i:
            data_output_rate = i
            print(i)
        if 'input errors' in i:
            error_rate = i
            print(i)

    tn.close()

    printing_to_excel2()

    return my_list
    return data_rate
    return error_rate


def telnetting2():

    host = "172.16.20.3" 
    # ip address of router

    port = 23

    tn = telnetlib.Telnet()


    tn.open(host,port)

    tn.write(b'username')

    tn.write(b'password')

    time.sleep(0.25)

    tn.write(b'terminal length 0\n')
    
    #tn.read_until(b'Sec-INTRA-6506>')
    tn.write(b'sh ip int brief gi2/2\n')

    time.sleep(0.25)
    #result = tn.read_until(b'Sec-INTRA-6506>').decode('utf-8')
    result = tn.read_very_eager().decode('utf-8')

    #result = tn.read_very_eager()

    #print(type(result))

    print(result)
    
    res=str(result)

    
    count = 0

    l = res.split("\n")
    li=[]
    for i in l:
        j=i.replace("\r","")
        
        if j != '':
            li.append(j)

    my_str = li[-2]
    global my_list
    my_list = re.split(r'\s+', my_str)
    #print(my_list)
    #print(len(my_list))
    if len(my_list)==7:
        printing_to_excel1()
    else:
        time.sleep(5)
        count = count +1
        if count<5:
            telnetting()
        else:
            pass

    tn.write(b'terminal length 0\n')

    time.sleep(0.10)
    
    #tn.read_until(b'Sec-INTRA-6506>')
    tn.write(b'sh int gi2/2\n')

    time.sleep(0.10)

    result1 = tn.read_very_eager().decode('utf-8')

    s = result1.split('\n')

    #print(s)

    global data_input_rate
    global data_output_rate
    global error_rate

    for i in s:
        if '5 minute input'in i:
            data_input_rate = i
            print(i)
        if '5 minute output'in i:
            data_output_rate = i
            print(i)
        if 'input errors' in i:
            error_rate = i
            print(i)

    tn.close()

    printing_to_excel2()

    return my_list
    return data_rate
    return error_rate


def printing_to_excel1():

    path ="C:/Users/root/Desktop/GE Links Status.xlsx"

    wb= openpyxl.load_workbook(path)

    ws=wb.active

    r=ws.max_row

    c=ws.max_column
    '''
    for a in range(1,r+1):
        for b in range(1,c+1):
            x=ws.cell(a,b).value
            ws.cell(a,b).value = x
    '''
    for i in range(1,(len(my_list))):
                   ws.cell(r+1,i).value=my_list[i-1]
                   #ws.cell(r+1,i+1).value = datetime.datetime.now()
                   ws.cell(r+1,7).value = datetime.datetime.now()
    wb.save(path)


def printing_to_excel2():

    path ="C:/Users/root/Desktop/GE Links Status.xlsx"

    wb= openpyxl.load_workbook(path)

    ws=wb.active

    r=ws.max_row

    c=ws.max_column

    '''for a in range(1,r+1):
        for b in range(1,c+1):
            x=ws.cell(a,b).value
            ws.cell(a,b).value = x
    '''
    
    ''''
    for i in range(1,(len(my_list))):
                   ws.cell(r+1,i).value=my_list[i-1]
                   #ws.cell(r+1,i+1).value = datetime.datetime.now()
                   ws.cell(r+1,7).value = datetime.datetime.now()
    '''

    ws.cell(r+1,1).value=data_input_rate
    ws.cell(r+2,1).value=data_output_rate
    ws.cell(r+3,1).value=error_rate

    wb.save(path)



telnetting1()
telnetting2()




    

