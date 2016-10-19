#!/usr/bin/python

# The crypt library is used to hash and encrypt data
import passlib

# This is a stand-in password dictionary to guess from, later we will replace this with a file
#
# passwordList = ["password", "Password", "PASSWORD", "P@$$W0rd", "Passwerd", "WordPass", "WordPress", "pass", "word", "password1", "password123"]



def main():
passwordList = open(password.lst, -r)
print(passwordList)
    # Open the fake shadow file and iterate over each line in it
    for shadowLine in open("ex4_3_data.txt"):
        # Take the line, strip all the whitespace off, split it on ":" and return the first two items assigning them to "username" and "fullhash" respectively
        username, fullhash = shadowLine.strip().split(":")[:2]
        # The salt is the first two fields of the fullhash, but we need to retain the $signs when we extract the salt
        salt = "$".join(fullhash.split("$")[:3])
        # We will store the cracked password here, if it is still blank we will know we didn't find the password
        crackedPassword = None
        # Iterate over every password in our dictionary
        for password in passwordList:
            # Hash the password from the dictionary with the salt from the shadowfile, and compare it to the fullhash from the shadow file
            if crypt.crypt(password, salt) == fullhash:
                # Success! We found the password
                crackedPassword = password
                # Exit the for loop, we have the password, we don't need to try any other words
                break
        if not crackedPassword == None:
            # Print the cracked password
            print username + " : " + crackedPassword
        else:
            # Turns out we couldn't crack the password, just complain about it here
            print "Could not find password for: " + username

if __name__ == "__main__":
    main()
