ip_addrs = input("IP address:")

def defang(ip :str) -> str: 
# Easy method of using built in replace function 
#    return ip.replace(".", "[.]")
# Can also use string manipulation 
    sub = ''
    for ch in ip:
        if ch == ".":
            sub += "[.]"
        else:
            sub += ch
    return sub
# testing solution
print("Defanged:", defang(ip_addrs))

exit()