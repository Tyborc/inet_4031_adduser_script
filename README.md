# inet_4031_adduser_script
INET 4031 Lab 8 Part 2
## Program Description
Program is intended to automate the creation of new users, to include username, password, Last Name, First Name, and any groups they need to be assigned to. 
** AUTOMATED COMMANDS**
1. Adding user without password
- Command: "/usr/sbin/adduser --disabled-password --gecos "Name,,," newusername
- Code:  cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
2. Adding password to User
## User Operation

### Input File Format
1. In the input file to be used in the program each line should be an individual user formatted as follows replacing information between "":
  - "username":"password":"Last_Name":"First_Name":"Group1","Group2"
2. To skip a specific line in the file "#" should be added to the beginning.
  - Ex. -> #UsertoNotInclude:IshouldNotbeHere:LastName:FirstName:Group1
3. If the user does not need to be in a groupd replace any instance with "-"
  - Ex. -> idontgetgroups:noGroups:LastName:FirstName:-

### Command Execution
To run the code in the command line while in the directory where the code is stored enter "./create-users.py < create-users.input"
- create-users.input can be named differently but should be formatted as above.
- If the code fails to run due to inadequate permissions running chmad a+x create-users.py will grant execute permissions.

### 'Dry Run'
