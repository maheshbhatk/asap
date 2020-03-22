import csv
from collections import Counter
import os
timeslot_1=[];
timeslot=[];
waitingslot=[];
done=[];

with open('graph.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(row)
        if(row[5]=='0'):
            timeslot_1.append(row)
        else:
            continue
    #print(timeslot_1);
    print('In time slot 1,these operations are done:')
    for i in timeslot_1:
        done.append(i[0])
        print(i[0])
        
print('In the next time slot,these operations are done')        
with open('graph.csv') as csv_file:
    printing=[]
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(row)
       
        if(row[5]=='1'):
            input1=row[2];
            input2=row[3];
            for i in timeslot_1:
                if(input1==i[4] or input2==i[4]):
                    printing.append(row[0]);
                    timeslot.append(row)

    printing=(list(dict.fromkeys(printing)))
    for i in printing:
        print(i)
        
with open('graph.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if(row[5]=='1'):
            if row in timeslot:
                continue
            else:
                waitingslot.append(row)
    #print(waitingslot)
    
    while(len(waitingslot)!=0):
        printing=[];
        print('Next time slot,these operations are done')
        y=-1;
        for i in waitingslot:
            y=y+1
            input1=i[1];
            input2=i[2];
            for row in timeslot:
                if(input1==row[4] or input2==row[4]):
                    printing.append(i[0])
                    timeslot.append(i)
                    del(waitingslot[y])
                    break;
        
        printing=(list(dict.fromkeys(printing)))
        for i in printing:
            print(i)
#ASAP DONE
#writing the verilog.v file below
inputs=[];          #the inputs in the verilog module
outputs=[];         #the outputs in the verilog module

with open('graph.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    num = Counter(i for j in csv_reader for i in j) 
    dup = [k for k, v in num.items() if v > 1]
    
with open('graph.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        inputs.append(row[2])
        inputs.append(row[3])
        outputs.append(row[4])
    inputs=(list(set(inputs)-set(dup)));
    inputs.sort()
    #for i in inputs:
     #   print(i)
    outputs1=(list(set(outputs)-set(dup)));
    outputs1.sort()
    #for i in outputs:
     #   print(i)
        
file1 = open("verilog.v","w+")

file1.write("module(input ")
for item in inputs:
        file1.write("%s" % item)
        file1.write(",")
file1.write("output ")
for item in outputs1:
        file1.write("%s" % item)
        file1.write(",")
file1.seek(0,2)
file1.seek(file1.tell() - 1, 0)
file1.truncate()
file1.write(");\n")
#module declaration done

with open('graph.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if((row[1])=='MUL'):
            file1.write('assign '+ row[4] + '=' + row[2] +'*' +row[3]+';\n')
        elif((row[1])=='ADD'):
            file1.write('assign '+ row[4] + '=' + row[2] +'+' +row[3]+';\n')
        else:
            file1.write('assign '+ row[4] + '=' + row[2] +'-' +row[3]+';\n')
            
file1.write('endmodule;')

file1.close()
