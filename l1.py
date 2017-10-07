import subprocess
import re
import shlex

lspci_out = subprocess.Popen(shlex.split('lspci -vmm'), stdout=subprocess.PIPE)
temp_vendors = subprocess.Popen(shlex.split('grep Vendor: '), stdin=lspci_out.stdout, stdout=subprocess.PIPE)
vendors = subprocess.Popen(shlex.split('grep -v SVendor: '), stdin=temp_vendors.stdout, stdout=subprocess.PIPE)
vendors_out = vendors.communicate()
test1 = vendors_out[0].decode().split('\n')
lspci_out = subprocess.Popen(shlex.split('lspci -vmm'), stdout=subprocess.PIPE)
temp_devices = subprocess.Popen(shlex.split('grep Device: '), stdin=lspci_out.stdout, stdout=subprocess.PIPE)
devices = subprocess.Popen(shlex.split('grep -v SDevice: '), stdin=temp_devices.stdout, stdout=subprocess.PIPE)
devices_out = devices.communicate()
test2 = devices_out[0].decode().split('\n')
i = 0
while i < test1.__len__() - 1:
    print(test1[i] + "\t\t" + test2[i])
    i += 1
