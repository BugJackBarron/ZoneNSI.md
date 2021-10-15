def bin2dec(x) :
    """fonction convertissant le nombre (x)_2 en base 10
>>> bin2dec('0')
0
>>> bin2dec('1')
1
>>> bin2dec('11')
3
>>> bin2dec('1000')
8
>>> bin2dec('11111111')
255
    """
    dec = 0
    for i in range(len(x)):
        if x[i] == "1" :
            dec = dec + 2**(len(x)-1-i)
    return dec

from doctest import testmod

testmod()
