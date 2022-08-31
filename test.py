ex1 = "45385593107843568"

def fake_bin(x):
    for i in range(len(x)):
        if x[i] < '5':
            x = x.replace(x[i], "0", 1)
        else:
            x = x.replace(x[i], "1", 1)
    return x

fake_bin(ex1)