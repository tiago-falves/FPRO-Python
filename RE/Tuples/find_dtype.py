def  find_dtype(atuple, data_type):
    tup=()
    for i in atuple:
        if type(i).__name__==data_type:
            tup+=(i,)
    return tup
