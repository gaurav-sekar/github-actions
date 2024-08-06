def add(a, b):
    return a + b

def checkMinimumLength(password, minReq):
    if len(password) < minReq:
        return False
    else:
        return True

def reusePassword(newPassword, previousPasswords):
    for index, password in enumerate(previousPasswords):
        previousPasswords[index] = password.lower()
    
    if newPassword.lower() in previousPasswords:
        return True
    else:
        return False



