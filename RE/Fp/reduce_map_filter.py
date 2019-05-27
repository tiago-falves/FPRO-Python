def reduce_map_filter(args):
    from functools import reduce
    
    if type(args[2]).__name__=="tuple":
        largs=list(args)
        largs[2]=reduce_map_filter(args[2])
        return reduce_map_filter(largs)
    elif type(args[2]).__name__=="int":
        return reduce_map_filter(args)
    else:
        if args[0]=="map":
            return list(map(args[1],args[2]))
        elif args[0]=="filter":
            return list(filter(args[1],args[2]))
        else:
            return reduce(args[1],args[2])
