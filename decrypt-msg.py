# Decrypt Message

# Messages consist of lowercase latin letters only, 
# and every word is encrypted separately as follows:

# Convert every letter to its ASCII value. 
# Add 1 to the first letter, 
# and then for every letter from the second one to the last one, 
# add the value of the previous letter. 
# Subtract 26 from every letter until it is in the range of 
# lowercase letters a-z in ASCII. 
# Convert the values back to letters.

# For instance, to encrypt the word “crime”

# Decrypted message:  c   r   i   m   e
#             Step 1: 99  114 105 109 101
#             Step 2: 100 214 319 428 529
#             Step 3: 100 110 111 116 113
# Encrypted message:  d   n   o   t   q

# Write a function named decrypt(word) that receives a string that consists of 
# small latin letters only, and returns the decrypted word.


def decrypt(word):
    msg = ""
    initial_ascii = 1
    
    for i in range(len(word)):
        final_ascii = ord(word[i])
        final_ascii -= initial_ascii
        
        while final_ascii < 97:
            final_ascii += 26
      
        initial_ascii += final_ascii
        msg += chr(final_ascii)
      
    return msg