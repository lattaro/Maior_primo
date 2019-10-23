def maior_primo(x):
    j = x - 1
    while j > 1:
        if x % j != 0:
            j = j - 1
            
        else:
            x = x - 1
            j = x - 2
            
    return (x)



