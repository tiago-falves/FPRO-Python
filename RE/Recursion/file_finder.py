def file_finder(dirs, file_name):
    if dirs==file_name:
        return file_name
    if type(dirs).__name__=="list":
        for i in dirs[1:]:
            find=file_finder(i,file_name)
            if find!=None:
                return dirs[0]+"/"+find
    return None
#    if file_name in dirs:
#        return str(file_name)
#    else:
#        return dirs[0]+str(file_finder(dirs[1:],file_name))
dirs= ["home",["Documents",[ "FPRO", "lists.txt", "recursion.pdf", "functions" ],[ "Python", "hello_world.py", "readme.md" ],],["Downloads",[ "Movies",[ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],"1.avi", "22", "001.mp4"],],"tmp.txt", "page.html"]

print(file_finder(dirs, 'Documents'))