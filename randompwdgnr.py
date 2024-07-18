import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
symbols="!@#$%^&*()_+><.]}{[';:"

for password in range(0,5):
     all_chars=lower+upper+digits+symbols
     length=int(input("Enter the lenght of the password that you want : "))
     password="".join(random.sample(all_chars,length))
     print("Generate password : ",password)
