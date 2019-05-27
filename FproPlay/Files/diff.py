def diff(filename1, filename2):
    with open(filename1,"r") as file1,open(filename2,"r") as file2:
        all_lines1=file1.readlines()
        all_lines2=file2.readlines()
        s=""
        for i in all_lines1:
            if i not in all_lines2:
                s+="- "+i          
            else:
                a=i
                
        for i in all_lines2:
            if i not in all_lines1:
                s+="+ "+i   
    return s.strip()
print(diff("file1d.txt", "file2d.txt"))