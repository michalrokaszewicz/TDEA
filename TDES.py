from Crypto.Cipher import DES
import time

key1 = b'abcdefgh'
key2 = b'98712346'
key3 = b'zxvbkigt'

cipher1 = DES.new(key1, DES.MODE_ECB)
cipher2 = DES.new(key2, DES.MODE_ECB)
cipher3 = DES.new(key3, DES.MODE_ECB)

en_time = 0.0
de_time = 0.0

filepath = "C:\\Users\\micha\\ADW\\Crypto\\input.txt"
f = open(filepath, "rb")
t0 = time.time()
msg = cipher1.encrypt(f.read())
msg = cipher2.decrypt(msg)
msg = cipher3.encrypt(msg)
en_time += time.time() - t0

t1 = time.time()
msg = cipher3.decrypt(msg)
msg = cipher2.encrypt(msg)
msg = cipher1.decrypt(msg)
de_time += time.time() - t1

print("end")
print("encrypt time: ", en_time)
print("decrypt time: ", de_time)


