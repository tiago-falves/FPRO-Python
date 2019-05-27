def find_dtype(atuple, data_type):
    s=()
    for i in atuple:
        if type(i).__name__==data_type:
            s+=(i,)
    return s
