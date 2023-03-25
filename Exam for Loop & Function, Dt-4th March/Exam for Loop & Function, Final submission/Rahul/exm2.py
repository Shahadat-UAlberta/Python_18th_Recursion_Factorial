def unique_list (x):
    y = []
    for value in x:
        if value not in y:
            y.append(value)
    return y
print(unique_list([1,2,3,3,3,3,4,5]))