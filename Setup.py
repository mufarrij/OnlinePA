#! /usr/bin/python2.7

import csv
import os

# Replacing the ? with 0 in datafile
with open('data/datafile.csv', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('?', '0')

with open('data/datafile.csv', 'w') as file:
  file.write(filedata)


# Write train,test data  to a data.csv file
with open("data/datafile.csv","r") as source:
    rdr= csv.reader( source )
    with open("data/data.csv","w") as result:
        wtr= csv.writer( result )
        for r in rdr:
           wtr.writerow( (r[1], r[2], r[3], r[4],r[5], r[6], r[7], r[8],r[9]))

# Write Class labels to different file 
with open("data/datafile.csv","r") as source:
    rdr=csv.reader(source)
    with open("data/labels.csv","w") as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow((r[10]))

# replacing the 2 and 4 with -1 and 1 in class labels
with open('data/labels.csv', 'r') as file:
  filedata = file.read()
  # Replace the target string
  filedata = filedata.replace('2', '-1')
  filedata = filedata.replace('4', '+1')
  # Write the file out again
  with open('data/labels.csv', 'w') as file:
    file.write(filedata)

# seperating train data set and testing data set to seperate files
with open('data/data.csv','r') as source:
     rdr= csv.reader(source)
     with open("data/train_data.csv","w") as result:
         wtr=csv.writer(result)
         head=0
         for r in rdr:
            if(head<466):
             wtr.writerow( (r[0], r[1], r[2], r[3],r[4], r[5], r[6], r[7],r[8]))
             head=head+1
             if head==466:
                break


with open('data/data.csv','r') as source:
     rdr= csv.reader(source)
     with open("data/test_data.csv","w") as result:
         wtr=csv.writer(result)
         head=0
         for r in rdr:
            head=head+1
            if(head>466):
             wtr.writerow( (r[0], r[1], r[2], r[3],r[4], r[5], r[6], r[7],r[8]))
             

#seperating train and test labels to seperate files 

with open('data/labels.csv','r') as source:
     rdr= csv.reader(source)
     with open("data/train_labels.csv","w") as result:
         wtr=csv.writer(result)
         head=0
         for r in rdr:
           if(head<466):
             wtr.writerow(r)
             head=head+1
             if head==466:
                break

with open('data/labels.csv','r') as source:
     rdr= csv.reader(source)
     with open("data/test_labels.csv","w") as result:
         wtr=csv.writer(result)
         head=0
         for r in rdr:
            head=head+1
            if(head>466):
             wtr.writerow(r)

# tearing  down data.csv,labels.csv         
os.remove("data/data.csv")
os.remove("data/labels.csv")




