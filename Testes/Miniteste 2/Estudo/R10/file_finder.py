def file_finder(dirs, file_name):
    if dirs==file_name:
        return file_name
    else:
        if type(dirs).__name__=="list":
            for i in dirs[1:]:
                find=file_finder(i,file_name)
                if find!=None:
                    return dirs[0]+"/"+ find
            return None

