def pad_same(input,kernel,stride=1):
    '''calculates the padding for same input and output size
    o = (w-k+2p)/s +1
    '''
    w = input
    k= kernel
    s = stride
    o=w
    p = (o*s - s + k - w)/2
    return int(p)
    
