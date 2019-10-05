# Writeup 2 - Pentesting

Name: *Wyeth Force*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Wyeth Force*

## Assignment Writeup

### Part 1 (45 pts)

Thanks to the helpful link from the TAs, I guessed that I should first check to see if I could mess with Eric's
service just by giving the server some made-up input and then trying to include something malicious afterwards.  So I 
connected to his server using the 'nc wattsamp.net 1337' command given on the homepage.  The server then asks for an ip 
address, and after ~2 seconds of waiting it ends the session.  I guessed (correctly, I think) that the server was reading
the input directly in without at all considering what it entailed, which is a clear vulnerability.  So I used the
input '1; ls' to view the contents of the server, and then ran '1; cd home; ls' to find a file named 'flag.txt'.  Finally
I just ran '1; cd home; cat flag.txt' to get the flag, which was CMSC389R-{p1ng_as_a_$erv1c3}.

As far as recommendations for Eric to improve security, I have a few ideas, most of which revolve around monitoring the 
the input for his ping command.  I think the simplest way to combat basics attacks like this is to establish a list of 
illegal characters (like the semicolon) which might enable someone to perform a basic injection attack like the one 
I performed.  Even a simple defensive measure like this would have completely disarmed me.  Another idea I had was to 
search the input for a number of illegal substrings and block input that contains them.  For example, maybe substrings 
like 'ls' and 'cd' could be added to the list of illegals, so that any attempt to inject these linux commands would be 
rejected.  Finally, one website I looked at (https://portswigger.net/web-security/os-command-injection) recommends 
avoiding this kind of server functionality in general.  This particular site recommends finding an alternative way to 
implement the ip ping functionality, preferably in a way that doesn't leave the server vulnerable to such a simple attack.

### Part 2 (55 pts)

I'm not too familiar with python, so I modelled this code as much as possible after my stub.py code from week 2.  I chose 
to implement a shell (and each following inner-shell) with a while loop mixed in with a little recursion.  For every 
command given, I attempt to recognize whether it's one of the commands I have to run locally (help, quit, exit, etc) 
using string comparisons.  If it's none of the 'local' commands, I then use the socket to send the command to Eric's 
server, where it will run whatever it entails.  Whenever a command is executed on Eric's server I always output the result.
My shell doesn't really have to worry about bad commands because they would be unrecognized and therefore sent out to 
the wattsamp.net server, which would return back it's own 'invalid command' error.

Key areas where I failed to meet project requirements were with the multi-line functionality and the pull command.  For
the life of me I couldn't figure out how to break up the commands across lines, so that you could call 'cd home' on one 
line and then just type 'ls' and be shown the contents of the 'home' directory.  As my shell is currently implemented, all 
commands have to be entered in the same line, which is obviously not ideal.  Also, I couldn't figure out how to implement 
the 'pull' functionality.  I found a command online that may have worked ('scp'), but it seemed like you needed the 
username and password of the local machine, so what worked on my computer wouldn't have worked on the TA's computers.  In 
the end, I was unable to implement either of those features.  For future I'll try to start assignments earlier so I can go 
to office hours with these questions.
