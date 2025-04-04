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
		
#	Sets the new variables equal to specific indexes in the Fields array this is each section that us broken up in the line.strip().split(';') command 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

#	A user may need to be added to multiple groups. 
        groups = fields[4].split(',')

       
#	The print statement is akin to a troubleshooting printout in code allowing the user to see what is being added as the account user name. 
        print("==> Creating account for %s..." % (username))
      
#	Runs the add user command through the import OS commands without setting password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

#	The first time it running the code would be good to print the contents of 'cmd'. If uncommented os.system(cmd) will attempt to run the command in cmd on the machine.
#       print cmd
        os.system(cmd)

#	Same as the line for the account creation is shows that the password is being set for a specific user so that the person running the code knows who it is set for and can track what has happened
        print("==> Setting the password for %s..." % (username))
        #Sets the password of the priorly created user 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        
        
#	The first time that this code is run it would be beneficial to just print out what the cmd would be to ensure it is working. The os.system(cmd) statement will run 'cmd' as a command in the machine. 
#       print cmd
        os.system(cmd)

        for group in groups:
#		The IF statment is checking for sections of the group field that are not '-' which indicates no groups. If the group is not '-' then the code should add a user to that group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
#	        print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
