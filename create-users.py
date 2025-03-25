#!/usr/bin/python3

# INET4031
# Josh Haataja
# 3-23-25
# 3-25-25

#Answers will be commented next to code. 
import os    #Imports OS module allowing for I/O functions including file reading and writing
import re    #Imports regular expressions to ensure functionality without needing most up to date python
import sys   #Imports sys module allowing for more efficient I/O and command line arguments

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #REPLACE THIS COMMENT - this "regular expression" is searching for the presence of a character - what is it and why?
        #The important part is WHY it is looking for a particular characer - what is that character being used for?
        match = re.match("^#",line) #Checking for the presence of the '#' Character 

        #REPLACE THIS COMMENT - why is the code doing this?
        fields = line.strip().split(':')         #Takes a single 
        
        # The following IF statement checks if there is a '#' beginning a line or if the length of fields which it the individual lines from the is not equal to 5.
        # If either of the checks is true then the continue skips the remaining code in the loop.
        if match or len(fields) != 5:
            continue

        #REPLACE THIS COMMENT - what is the purpose of the next three lines. How does it relate to what is stored in the passwd file?
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #REPLACE THIS COMMENT - why is this split being done?
        groups = fields[4].split(',')

        #REPLACE THIS COMMENT - what is the point of this print statement?
        print("==> Creating account for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

        #REPLACE THIS COMMENT - what is the point of this print statement?
        print("==> Setting the password for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain. You'll need to lookup what these linux commands do.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

        for group in groups:
            #REPLACE THIS COMMENT with one that answers "What is this IF statement looking for and why? If group !='-' what happens?"
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
