# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:55:46 2019

@author: Gustavo
"""

def grep(pattern, files_list, flags=''):
    result=""
    files= open(files_list[0])
    file=files.readlines()
    fl=file[:]   
    flag=flags.split(" ")
    if "-i" in flag:
        for i in range(len(fl)):
            fl[i]=fl[i].lower()
        pattern = pattern.lower()
    if "-l" in flag:
        if pattern in "".join(fl):
            result+= files_list[0]+"\n"
    if "-c" in flag:
        count=0
        for i in fl:
            if pattern in i:
                count+=1
        result+=files_list[0]+":"+str(count)+"\n"

    if "-x" in flag:
        for i in range(len(fl)):
            if fl[i]==pattern+"\n":
                result+=files_list[0]+":"+str(i+1)+":"+file[i]
    if "-v" in flag:
        for i in range(len(fl)):
            if pattern not in fl[i]:
                result+=files_list[0]+":"+str(i+1)+":"+file[i]
    
    if flags=="-i" or flags=="":
        for i in range(len(fl)):
            if pattern in fl[i]:
                result+=files_list[0]+":"+str(i+1)+":"+file[i]
    files.close()
    if len(files_list)==1:
        return result
    else:
        return result + grep(pattern, files_list[1:], flags)
    
        
        
        
#print(grep('Hello', ['file1g.txt', 'file2g.txt'], ''))
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i'))   
#print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -x'))
#print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -v'))
#print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -l'))
print(grep('Hello', ['file1g.txt', 'file2g.txt'], '-i -c'))
print(grep('Hellooo', ['file1g.txt', 'file2g.txt'], ''))