from ipaddress import *
k = 0

ip = ip_address("192.214.116.184")

for mask in range(33):
    net = ip_network(f"192.214.116.184/{mask}", 0)
    if f"{int(net[0]):032b}".count("1") % 5 == 0:
        if net[0] < ip < net[-1]:
            k += 1
print(k)
