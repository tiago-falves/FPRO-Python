def interleave(f1,f2):
    s=""
    with open(f1,"r") as file1, open(f2,"r") as file2:
        all_lines1=file1.readlines()
        all_lines2=file2.readlines()
        for i in range(min(len(all_lines1),len(all_lines2))):
            s+=all_lines1[i]+all_lines2[i]
    return s
                
