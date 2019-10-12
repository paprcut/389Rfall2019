# Writeup 6 - Binaries I

Name: *Wyeth Force*
Section: *Section 0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Wyeth Force*

## Assignment Writeup

### Part 1 (50 pts)

Flag: CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

When approaching this homework, I determined by inspection that there were three obstacles to obtaining the flag: 
the check1, 2, and 3 methods located in main.  Each check method would ensure certain conditions had been 
met, and then update the flag.  It's worth mentioning that before reaching the check methods, the program won't allow you 
to proceed unless you provide at least 2 command line arguments.  The first is obviously './crackme', and the second 
(for now) can be whatever you like.

Upon examining the check1 method, I saw noticed that the success of the function was based on a simple string comparison.  
The second command line argument was compared to the string "Oh God".  So in order to pass the first check I had to add 
that string to the input, so I started using './crackme "Oh God"' whenever I wanted to run the binary.

The check2 method was a bit trickier, since the test's success didn't seem at all related to the command line arguments.  
Fortunately Yuval pointed out the use of the 'getenv' function, which referenced a enviromental variable named FOOBAR, 
which was expected to (initially) have the value of "seye ym ".  Later in the same check2 function, though, the value of 
FOOBAR is reversed in a loop, so the final expectation was FOOBAR=" my eyes".  Such a variable did not exist, so all I had 
to do was create it in the current enviroment and I passed the test.

Finally, the check3 method opened a file called 'sesame', and then analyzed a string within it using a switch-like 
statement.  I decoded the expected binary values and found that the expected contents of the 'sesame' file was the string 
" they burn".  So in order to pass the test I created and filled out the necessary file, and I passed the test.

To be perfectly honest, I'm not entirely sure where the flag was stored to begin with.  My best guess is that the flag's 
various components were scattered among the various hashes and tables referenced in the program, and that by continually 
getting the 'updateflag' method to be called, the flag was reassembled.

This assignment was really cool and I would love to see more assembly-related projects in this class.  Big thanks to 
Mitchell for teaching the binaries class really well, and thanks to all the TAs for guiding me through this project.
