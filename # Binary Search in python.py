
msg = ["H", "e", "l", "l", "o", "S", "t", "u", "d", "e", "n", "t"]
str1 = []; 
str2 = []
cnt1 = 0; cnt2 = 0
print ("Rail Fence - Encryption\n\n")
print ("Plain Text: HelloStudent\n\n")

for i in range(len(msg)):
    if (i % 2 == 0):
        message = msg[i]
        str1.append(message)      
        cnt1+= 1
    else :
        message = msg[i]
        str2.append(message)
        cnt2 += 1
	
print ("Cipher Text:", str1, str2)
