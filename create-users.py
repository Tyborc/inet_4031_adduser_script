#!/usr/bin/python3

# INET4031
# Josh Haataja
# 3-23-25
# 3-25-25

#Answers will be commented above code. 
import os    #Imports OS module allowing for I/O functions including file reading and writing
import re    #Imports regular expressions to ensure functionality without needing most up to date python
import sys   #Imports sys module allowing for more efficient I/O and command line arguments

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        
        #Checking for the presence of the '#' Character indicating a line to skip 
        match = re.match("^#",line)  
        
 #Takes a single line and splits it by the ':' character.
        fields = line.strip().split(':')        
        
        # The following IF statement checks if there is a '#' beginning a line or if the length of fields which it the individual lines from the is not equal to 5.
        # If either of the checks is true then the continue skips the remaining code in the loop.
        if match or len(fields) != 5:
            continue

        # Sets the new variables equal to specific indexes in the Fields array this is each section that us broken up in the line.strip().split(';') command 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #A user may need to be added to multiple groups. 
        groups = fields[4].split(',')

        #REPLACE THIS COMMENT - what is the point of this print statement?
        # The print statement is akin to a troubleshooting printout in code allowing the user to see what is being added as the account user name. 
        print("==> Creating account for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

        #Same as the line for the account creation is shows that the password is being set for a specific user so that the person running the code knows who it is set for and can track what has happened
        print("==> Setting the password for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain. You'll need to lookup what these linux commands do.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #print cmd
        #os.system(cmd)

        for group in groups:
            #REPLACE THIS COMMENT with one that answers "What is this IF statement looking for and why? If group !='-' what happens?"
            #The IF statment is checking for sections of the group field that are not '-' which indicates no groups. If the group is not '-' then the code should add a user to that group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
