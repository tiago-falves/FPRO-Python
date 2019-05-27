def reduce_map_filter(args):
    import functools
    if type(args).__name__=="list":
        return args
        
    if args[0]=="map":
        return list(map(args[1],reduce_map_filter(args[2])))
    elif args[0]=="filter":
        return list(filter(args[1],reduce_map_filter(args[2])))
    if args[0]=="reduce":
        return int(functools.reduce(args[1],reduce_map_filter(args[2])))
    
            
