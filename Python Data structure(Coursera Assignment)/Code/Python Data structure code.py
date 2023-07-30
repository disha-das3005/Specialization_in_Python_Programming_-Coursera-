#!/usr/bin/env python
# coding: utf-8

# In[1]:



#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
x=text.find('0.8475')
y=text[x:x+6]
print(float(y))


# In[ ]:



#Write a program that prompts for a file name, then opens that file and reads through the file, 
#and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

fh = input("Enter file name: ")
try:
   fh = open(fname)
except:
    print('file not found:error')
    quit()
    
text=fh.read()
res=text.upper()
print(res.rstrip())


# In[ ]:



#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values 
#and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number

average = total/count
print("Average spam confidence:",average)


# In[ ]:



#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method
#The program should build a list of words. For each word on each line check to see if the word is already in the list
#and if not append it to the list. When the program completes, sort 
#and print the resulting words in python sort() order as shown in the desired output.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word_split = line.split()
    for word in word_split:
       if word not in lst:
           lst.append(word)
       else:
          continue

print(sorted(lst))


# In[ ]:



# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
#they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to 
#find the most prolific committer.

fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)


# In[ ]:



#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)


# In[ ]:




