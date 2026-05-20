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

def dec2bin(n) :
    """fonction convertissant le nombre n en base 2,
    et renvoyant la chaine de caractères correspondante
    >>> dec2bin(0)
    '0'
    >>> dec2bin(1)
    '1'
    >>> dec2bin(3)
    '11'
    >>> dec2bin(8)
    '1000'
    >>> dec2bin(255)
    '11111111'
    """
    if n == 0 :
        return "0"
    base2 =""
    while n != 0 :
        base2 =  str(n%2) + base2
        n = n//2
    return base2


from doctest import testmod

testmod()
