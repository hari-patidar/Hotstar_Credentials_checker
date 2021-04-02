# Hotstar_Credentials_checker

This was a basic selenium web testing script that basically takes input from the text file given with and provides output if the credentials are usefull or not.

I had an file that contains the hotstar credentials which were fake. But just to learn some selenium testing i made this script. So the file of credentials is also given here.

The program takes email Id and Password from the file which also contains lots of other text and uses it on the hotstar website and try logging in and performs two or three steps if it fails.

Features contains:
 If the email is connected with the phone number then hotstar asks for the otp which we cannot get, so it neglects.
 
 Also if the Email and Password are wrong when passed in it just rejects that too.
 
 And finally if the we are logged in it saves the email and password in new file which will be crated in the same directory in which the program is present.
 
 
 But the flaw of the program is it only works with the file which i used and it cannot be used with any other file. And i am working to improve it that it can be used with any file that is being passed with it.
