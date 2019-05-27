#3. File Finder

def file_finder(dirs, file_name):
    
    if dirs == file_name:
        return file_name
    
    for elem in dirs[1:]:
        
        finding = file_finder(elem,file_name)
            
        if finding != None:
            return dirs[0] + "/" + finding
     
    return None
    
    