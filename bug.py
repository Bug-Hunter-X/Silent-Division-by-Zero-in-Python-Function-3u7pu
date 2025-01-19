def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(0, 0)
print(result) #this will give you 0.0 instead of an error, this can lead to unexpected behaviour