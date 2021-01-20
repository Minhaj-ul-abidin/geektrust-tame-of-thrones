
class Cipher:
    @staticmethod
    def decrypt(cipher_message,key): 
        result = "" 
        key = key%26 #Ensuring key is always between 0-25
        rev_key = 26-key
        for i in range(len(cipher_message)): 
            char = cipher_message[i] 
            # decrypt uppercase characters as characters are always upper case
            result += chr((ord(char) + rev_key-65) % 26 + 65)         
        return result