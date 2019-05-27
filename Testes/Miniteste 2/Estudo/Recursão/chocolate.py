def countMaxChoco(money, price, wrap): 
    if wrap<2:
        return 
    chocolates=money//price
    
    def count_wraps(chocolates,wrap):
        if wrap<2:
            return chocolates
        
        return count_wraps(chocolates+chocolates//wrap,wrap)
    return count_wraps(chocolates,wrap)
        
