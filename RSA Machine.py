#========================================================================================#
#                                                                                        #
#                                    RSA ENCRYPTOR 1.0                                   #
#                                                                                        #
#                                     BY ZACK ZHANG                                      #
#                                                                                        #
#========================================================================================#


#========================================================================================#
#                                     INTRODUCTION                                       #
#========================================================================================#
#This program is written in python 3.7.0. It simulates a basic RSA encryption machine, but
#  with some limitations in the characters it encrypts. Although each allowed character
#  corresponds to only one number, the machine uses a special algorithm to prevent unintended
#  decryption as a Caesar cypher. This algorithm combines the corresponding 2-digit numbers
#  of every two adjacent characters into a 4-digit number before processing the encryption.
#  Thus many different numbers may appear in the coded message, making it difficult
#  to decypher the original text.
#
#The machine offers three modes: setting up the public/private keys, encrypting a message,
#  and decrypting a message.



#========================================================================================#
#                                CONFIGS AND MESSAGES                                    #
#========================================================================================#


#General:
#=========================================================================================

#The variable names (VN) in the program:
VN1,VN2,VN3,VN4,VN5= "p", "q", "n", "e", "d"


#All valid characters in the messages, and their correcponding number codes:
valid_chars = [["a",[91]],["b",[92]],["c",[93]],["d",[94]],["e",[95]],["f",[96]],["g",[97]],
               ["h",[98]],["i",[99]],["j",[10]],["k",[11]],["l",[12]],["m",[13]],["n",[14]],
               ["o",[15]],["p",[16]],["q",[17]],["r",[18]],["s",[19]],["t",[20]],["u",[21]],
               ["v",[22]],["w",[23]],["x",[24]],["y",[25]],["z",[26]],["A",[27]],["B",[28]],
               ["C",[29]],["D",[30]],["E",[31]],["F",[32]],["G",[33]],["H",[34]],["I",[35]],
               ["J",[36]],["K",[37]],["L",[38]],["M",[39]],["N",[40]],["O",[41]],["P",[42]],
               ["Q",[43]],["R",[44]],["S",[45]],["T",[46]],["U",[47]],["V",[48]],["W",[49]],
               ["X",[50]],["Y",[51]],["Z",[52]],["1",[53]],["2",[54]],["3",[55]],["4",[56]],
               ["5",[57]],["6",[58]],["7",[59]],["8",[60]],["9",[61]],["0",[62]],[",",[63]],
               [".",[64]],["?",[65]],["!",[66]],["(",[67]],[")",[68]],["[",[69]],["]",[70]],
               ["{",[71]],["}",[72]],["<",[73]],[">",[74]],["-",[75]],[":",[76]],[";",[77]],
               ["@",[78]],["#",[79]],["$",[80]],["%",[81]],["^",[82]],["&",[83]],["*",[84]],
               ["+",[85]],["_",[86]],['"',[87]],["'",[88]],[" ",[89]]]

#Greeting message:
greeting=\
"""

=========================Welcome to RSA Machine 1.0==============================

This machine will teach you the basics of RSA encryption, and will help you set up
your own RSA system. The name RSA comes from the initials of its creators: Rivest,
Shamir, and Adleman. It is one of the first cryptosystems with public keys, and is
widely used for secure data transmission.
"""

#Prompting the user to choose what to do:
mode_selection=\
"""
   Enter 1 if you would like to set up RSA,
         2 to encrypt your RSA message, or
         3 to decrypt
         : """

#Error message when the user's mode selection is invalid:
invalid_mode_selection="Input invalid. You may only enter 1, 2 or 3."



#Setup mode:
#===========================================================================================

#Message when entering setup mode:
setup_greeting=\
"""

   >>>You have entered setup mode.<<<

To set up your RSA, we begin by choosing two distinct prime numbers. To make sure
your encryption is relative secure, let's use primes with at least three digits."""

#Prompting user to choose primes:
prime_selection="\n   Please choose your {} prime: "

#Messages for invalid prime selections:
invalid_prime_not_number="Input invalid. A prime must be a number."
invalid_prime_not_natural="Input invalid. A prime must be a natural number."
invalid_prime_not_prime= "Input invalid. {} is not a prime."
invalid_prime_too_small= "Input invalid. Please choose a prime that is larger than 100."
invalid_second_prime_duplicate="Your two primes must not be the same."

#Messages after prime selections are successful:
first_prime_chosen="\nYour first prime is {}."

second_prime_chosen="\nYour second prime is {}."

#Messages for variable assignment for the primes chosen:
first_prime_variable_assignment="We will let the variable {} represent this prime."
second_prime_variable_assignment="We will let the variable {} represent this prime."

#Announcing the product of the two primes:
n_value_announcement="\nWe let the variable {} be the product of {} and {}, which is {}."

#Prompting the user to select a number coprime with the product of subtracting 1 from both primes:
e_explanation=\
"""
Now we need to choose a(n) {} value that is between 1 and ({}-1)({}-1), and is coprime
with ({}-1)({}-1)={}, that is, the greatest common divisor of {} and {} is 1."""

e_selection="\n   Enter your desired {} value: "

#Messages for invalid selection of "coprime variable":
invalid_e_not_number="Input invalid. Your {} value must be a number."
invalid_e_not_natural="Input invalid. Your {} value must be a natural number."
invalid_e_not_coprime="Invalid input. Your {} value must be coprime with {}."
invalid_e_bounds="Invalid input. Your {} value must be between 1 and {}."

#Messages after the "coprime variable" is selected:
e_selected="You have chosen your {} value to be {}."

#Announcing the public key:
public_key_announcement="\nYour public key value is ({},{}), or ({},{}). Make this known to the world!"

#Message for solving the congruence to find multiplicative inverse:
congruence_solve=\
"""
Now we solve the congruence for an integer {} such that ({})({}) is
congruent to 1 mod ({}-1)({}-1),or mod {}."""

#Warning the user to keep the private key secret:
private_key_warning="Look around, make sure there is no one spying on you, and then hit enter..."

#Announcing the result of the multiplicative inverse, and the private key:
mult_inv_announcement="The multiplicative inverse of {} is {} in mod {}. This will be your {} value."
private_key_announcement="Your private key value is ({},{}), or ({},{}). SHHH! Don't tell anybody!"

#Finishing the setup for RSA:
setup_end="You have finished setting up your RSA."




#Encryption mode:
#===========================================================================================

#Message at the beginning of the encryption mode:
encryption_greeting=\
"""
   >>>You have entered encryption mode.<<<

Please obtain the public key for the recipient of the message."""

#Prompting the user to enter the public key of the recipient:
key_value_entry="\n   Enter the {} value of the key: "

#Messages for invalid inputs of the public key:
key_invalid_not_number="Input invalid. Your {} value must be a number."
input_invalid_not_natural="Input invalid. Your {} value must be a natural number."

#Announcement after the public key is inputted:
target_public_key_announcement="Your target public key is ({},{})"

#Prompt to input the plain text message:
encrypt_input="Please input your message here: "

#Message containing the encrypted numbers:
coded_message_announcement="Your encoded message is {}."

#Error message when the user tries to encrypt invalid chacaters:
encryption_error=\
"""
Unfortunately the machine does not currently support some of the characters you entered.
The machine currently supports the encryption of all alphanumeric characters, spaces, and
the following special characters:
, . ? ! ( )[ ]{ }< > - : ; @ # $ %" ^ & * + _ " ' """



#Decryption mode:
#===========================================================================================

#Message at the beginning of the decryption mode:

decryption_greeting=\
"""
   >>>You have entered decryption mode.<<<

Please refer to your private key."""

#Prompt for an entry of the encrypted number list:
cypher_entry=\
"""
   Please input your encrypted numbers here in the form of
   a list of numbers,separated by commas: """

#Error message when the encrypted list input is invalid:
cypher_entry_invalid="Your cypher must contain only natural numbers, commas and spaces."

#Message when the drcyphering process is going on:
decyphering_message="\nDecyphering your code..."

#Announcement of the decrypted message
decrypted_message_announcement="If your inputs are correct, your message is: "

#If the decryption fails due to incorrect input:
decryption_fail=\
"""Hmm... the decryption didn't work. Make sure you have entered the correct numbers,
and that the message is encrypted by this machine as well."""




#========================================================================================#
#                                          CODE                                          #
#========================================================================================#


#Returns True if the input, n, is a number, and false otherwise:
def is_number(n):
    try:
        float(n)
        return True
    except:
        
        return False

#Guides the user to enter their private/public keys for de/encryption:
def key_entry():
    e_entered=False
    while e_entered==False:
        e=input (key_value_entry.format("first"))
        if not is_number(e):
            print (key_invalid_not_number.format("first"))
        elif str(e)[-1]==".":
                print (key_invalid_not_number.format("first"))
        else:
            if float(e)!= int(float(e)) or float(e) <= 0:
                print (input_invalid_not_natural.format("first"))
            else:
                e_entered=int(e)
    n_entered=False
    while n_entered==False:
        n=input (key_value_entry.format("second"))
        if not is_number(n):
            print (key_invalid_not_number.format("second"))
        elif str(n)[-1]==".":
                print (key_invalid_not_number.format("second"))
        else:
            if float(n)!= int(float(n)) or float(n) <= 0:
                print (input_invalid_not_natural.format("second"))
            else:
                n_entered=int(n)
    return e_entered, n_entered


#Takes in five variable names and guides the user to set up their RSA:
def setup (variable1, variable2, variable3, variable4, variable5):
    #Choose the two primes for RSA:
    def choose_prime(order):
        # Makes sure the numbers entered are prime:
        def prime_check (item):
            if item <= 1:
                return False
            elif item <= 3:
                return True
            elif item % 2==0 or item % 3==0:
                return False
            else:
                i=5
                while i*i <= item:
                    if item % i==0 or item % (i+2)==0:
                        return False
                        break
                    i+=6
            return True        
        chosen = False
        while chosen == False:
            user_input=input (prime_selection.format(order))
            if not is_number(user_input):
                print (invalid_prime_not_number)
            elif float(user_input)!= int(float(user_input)) or float(user_input) <=0:
                print (invalid_prime_not_natural)
            elif str(user_input)[-1]==".":
                print (invalid_prime_not_number)
            elif not prime_check(int(user_input)):
                print (invalid_prime_not_prime.format(user_input))
            elif int(user_input) < 100:
                print (invalid_prime_too_small)
            else:
                return user_input
                chosen=True
    # Choose a number coprime to the product of when both primes are subtracted 1:
    def choose_e (limit,variable1, variable2, variable4):
        def gcd(a,b):
            while b != 0:
                (a, b) = (b, a % b)
            return a
        e_chosen = False
        print(e_explanation.format(variable4,variable1,variable2,variable1,variable2,\
                                   limit,limit,variable4))
        while e_chosen==False:
            e=input (e_selection.format(variable4))
            if not is_number(e):
                print (invalid_e_not_number.format(variable4))
            elif str(e)[-1]==".":
                print (invalid_e_not_number.format(variable4))
            elif float(e)!= int(float(e)) or float(e) <= 0:
                print (invalid_e_not_natural.format(variable4))
            elif not 1 < int(e) < limit:
                print (invalid_e_bounds.format(variable4,limit))
            elif gcd (int(e), limit) != 1:
                print (invalid_e_not_coprime.format(variable4, limit))
            else:
                print (e_selected.format (variable4,e))
                e_chosen = True
                return e
    #Returns the inverse of input a mod m, or an exception if none is found:
    def modinv(a, m): 
        def pre_modinv(c, d):
            if c == 0:
                return (d, 0, 1)
            else:
                g, y, x = pre_modinv(d % c, c)
                return (g, x - (d // c) * y, y)
        g, x, y = pre_modinv(a, m)
        if g != 1:
            raise Exception('Mod inverse not found.')
        else:
            return x % m
    print (setup_greeting)
    prime_1 = int (choose_prime("first"))
    print (first_prime_chosen.format(prime_1))
    print (first_prime_variable_assignment.format (variable1))
    same_prime=True 
    while same_prime:
        prime_2 = int (choose_prime("second"))
        if prime_2 != prime_1:
            same_prime=False
        else:
            print (invalid_second_prime_duplicate)
    print (second_prime_chosen.format(prime_2))
    print (second_prime_variable_assignment.format (variable2))
    product_value = prime_1 * prime_2
    e_limit=(prime_1-1)*(prime_2-1)
    print (n_value_announcement .format(variable3,variable1,variable2,product_value))
    e_value=int(choose_e (e_limit,variable1, variable2, variable4))
    print (public_key_announcement.format(variable4,variable3,e_value,product_value))
    print (congruence_solve.format (variable5, variable4,variable5,variable1,variable2,e_limit))
    d=modinv(e_value, e_limit)
    print (private_key_warning)
    input()
    print (mult_inv_announcement.format (variable4,d,e_limit,variable5))
    print (private_key_announcement.format(variable5,variable3,d,product_value))
    print(setup_end)


#Guides the user through the encryption process of RSA:
def encrypt ():
    #Matches given code to the valid characters:
    def encode (item):
        for index in valid_chars:
            if index[0]==item:
                return index[1][0]
                break
    #Applies the special algorithm described in the introduction:
    def process_numlist(numlist):
        processed=[]
        start=0
        while len(numlist)-start >= 2:
            processed.append(int(str(numlist[start])+str(numlist[start+1])))
            start+=2
        if len(numlist)-start ==1:
            processed.append(numlist[start])
            start+=1
        return(processed)
                    
    print (encryption_greeting)
    e_value,n_value=key_entry()
    print (target_public_key_announcement.format(e_value,n_value))
    message=input(encrypt_input)
    message_split=list(message)
    try:
        code_list=[]
        for item in message_split:       
            code_list.append(encode(item))
        recoded_list=process_numlist(code_list)
        final_list=[]
        for item in recoded_list:
            cipher=pow(int(item),e_value,n_value)
            final_list.append(cipher)
        print (coded_message_announcement.format(final_list))
    except:
        print (encryption_error)



#Decrypts a message for the user:
def decrypt ():
    #Does a basic check on the entry of the encoded text and will filter out invalid
    #  characters, but will not actually check if the numbers are correct:
    def valid_cypher(cypher):
        validity=True
        for item in cypher:
            if item not in ["1","2","3","4","5","6","7","8","9","0",","," "]:
                validity=False
        return validity
    #Tries to match the input with the valid character list:
    def match (item):
        for index in valid_chars:
            if index[1][0]==item:
                return index[0]
                break            
    print (decryption_greeting)
    d_value,n_value=key_entry()
    cypher_chosen=False
    while cypher_chosen==False:
        cypher=input(cypher_entry)
        if valid_cypher (cypher)==False:
            print(cypher_entry_invalid)
        else:
            cypher_chosen=True
    print (decyphering_message)
    code_list=[x.strip() for x in cypher.split(',')]
    decoded_list=[]
    try:
        for item in code_list:
            decoded=pow(int(item),d_value,n_value)
            if decoded > 999:
                decoded_list.append(match(int(decoded/100)))
                decoded_list.append(match(decoded%100))
            else:
                decoded_list.append(match(decoded))
        try:
            print(decrypted_message_announcement+"\n\n"+"".join(decoded_list))
        except:
            print(decryption_fail)
    except:
        print(decryption_fail)
              
#Main loop for the program:
def RSA ():
    mode_chosen=False
    while mode_chosen==False:
        mode=input (mode_selection)
        if mode not in ["1","2","3"]:
            print (invalid_mode_selection)
        elif mode == "1":
            mode_chosen=True
            setup(VN1,VN2,VN3,VN4,VN5)
        elif mode == "2":
            mode_chosen=True
            encrypt()
        else:
            mode_chosen=True
            decrypt()



print(greeting)
while True:
    RSA()
        
    
