##############################################################################
# a215_security_checklist.py
##############################################################################

print("Let's check your security. Answer y or n to each of the questions.")

phish = input("Can you recognize phishing emails? ")
pw = input("Is your password strong? ")
auth = input("Do you use multi-factor authentication? ")
enc = input("Do you know how to encrypt sensitive information? ")
'''
if phish == "y" and pw == "y" and auth == "y" and enc == "y":
    print("You have good security habits.")
else:
    print("You can improve your security habits.")
'''

if phish == "n" or pw == "n" or auth == "n" or enc == "n":
    print("You can improve your security habits.")
else:
    print("You have good security habits.")
    
