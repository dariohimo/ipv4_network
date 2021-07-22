import ipaddress
""" ################
####__ @dariohimo github """
"""#################     """
print(f"========================================")
print(f"Con digitar la ip y la mascara de red")
print(f"averigue su mascara,broadcast,wilcard")


print(f"y direcciones utilizables")
print(f"========================================")
net_1 = input(f"Digite su ip y mascara \n")
net_2= ipaddress.ip_interface(net_1)
net_3 = net_2.network

print(f"\nip digitada: {net_2} ")
print(f"\nIpversion: Ipv_{net_3.version} Red: {net_3} ")
print(f"mascara: {net_2.netmask} ")
print(f"broadcast: {net_3.broadcast_address}")
print(f"Wilcard: {net_2.hostmask}")
print(f"direcciones: {net_3.num_addresses} ")
print(f"Numero de hosts utilizables: {net_3.num_addresses -2 } ")
print(f"rango de ip: {net_3[1]} hasta {net_3[-2]}")
