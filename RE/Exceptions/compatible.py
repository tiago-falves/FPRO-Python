def compatible(A,B):
    try:
        assert len(A[0])==len(B),"A and B cannot be multiplied"
    except AssertionError as error:
        return error
    else:
        return "A and B can be multiplied"
