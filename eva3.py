aclNum = int(input(" Cual es el numero de ACL ? "))
if aclNum >= 1 and aclNum <= 99:
    print("Esta ACL es estandard de IPv4 ")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL extendida de IPv4 ")
else:
    print("Esta no es una ACL correspondiente a una lista de acceso")