################################################################################
# This program uses the python module hashlib to hash a files content.
# The hashes can be compared to see if two or more files have the same content.
################################################################################
import hashlib

# Asks the user for file path and disired hashing algorithm.
xinput = raw_input('Enter the absolute path to the file to be hashed \n: ')
hashinput = raw_input(' MD5    [1] \n SHA1   [2] \n SHA224 [3] \n SHA256 [4] \n SHA384 [5] \n SHA512 [6] \n Number :')
try:
    if hashinput == '1':

	    # Reads users file in binary so that more then just text files can be hashed.
        file = open(xinput,"rb")

        # Puts users file into a string.
        fString = file.read()

        # Hashs the string using hashlib module.
        xhash = hashlib.md5(fString).hexdigest()

        # prints out the algorithms type and hash value.
        print('\nMD5')
        print xhash

     # More of the same four more times.  
    elif hashinput == '2':
        file = open(xinput,"rb")
        fString = file.read()
        xhash = hashlib.sha1(fString).hexdigest()
        print('\nSHA1')
        print xhash
    elif hashinput == '3':
        file = open(xinput,"rb")
        fString = file.read()
        xhash = hashlib.sha224(fString).hexdigest()
        print('\nSHA224')
        print xhash
    elif hashinput == '4':
        file = open(xinput,"rb")
        fString = file.read()
        xhash = hashlib.sha256(fString).hexdigest()
        print('\nSHA256')
        print xhash
    elif hashinput == '5':
        file = open(xinput,"rb")
        fString = file.read()
        xhash = hashlib.sha384(fString).hexdigest()
        print('\nSHA384')
        print xhash
    elif hashinput == '6':
        file = open(xinput,"rb")
        fString = file.read()
        xhash = hashlib.sha512(fString).hexdigest()
        print('\nSHA512')
        print xhash
    else:

    # If a invalid number is chosen let the user know.	
        print("\nNot a valid algorithm option!") 

    # If the file can not be found let the user know.
except IOError:
    print "\nCould not find the file, check your path and/or filename!"