
def ipV4(inStr):

    vals = inStr.split('.')
    return_value = True
    if len(vals) != 4:
        return_value = False
    else:
        for value in  vals:
            intValue = int(value)
            if intValue >= 0 and intValue <= 255 and len(value) == len(str(intValue)):
                pass
            else:
                return_value = False
                break

    return return_value

assert ipV4("172.16.254.1") == True
assert ipV4("172.16.256.1") == False
assert ipV4("172.16.254.01") == False
