def fight(heroes,villain):
    for i in heroes:
        if i["category"]==villain["category"]:
            if i["health"]>=villain["health"]:
                return "{} defeated the villain and now has a score of {}".format(i["name"],i["score"]+1)
            else:
                villain["health"]=villain["health"]-i["health"]/2
    return "{} prevailed with {}HP left".format(villain["name"],villain["health"])