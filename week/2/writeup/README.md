# Writeup 2 - OSINT

Name: *Wyeth Force*
Section: *Section 0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Wyeth Force*

## Assignment Writeup

### Part 1 (45 pts)

1.  I determined that ejnorman84's real name is Eric Norman.  I found this on his instagram account, which I discovered via methods discussed in question 3.
 
2.  Eric works for a power and energy company called Wattsamp Energy.  Their website url is wattsamp.net

3.  The first thing I did was locate Eric's Reddit and Instagram accounts, both of which were under the given username ejnorman84.  I found these social media accounts using username
finding tools that I got from osintframework.com.  His Reddit account seemed to indicate that he lived in Texas, and his instagram account informed me where he worked.  I believe I was
able to determine his address from running 'whois' on his company's website via Kali terminal, which gave me the address 1300 Adabel Drive, El Paso, TX 79835.  'whois' also informed me
that Eric's email address is ejnorman84@gmail.com, and that his phone number is 202-656-2837.

4.  I only found 1 IP address, which was the one associated with his company's website.  The address is 157.230.179.99.  DNS tools like dnstrails and dnsdumpster didn't yield any new
information besides a bonus flag, which I list in question 8.  I determined the IP address using 'whois'.

5.  Unfortunately I was unable to find any hidden files or directories on the wattsamp.net website.

6.  I used nmap to find open ports on the website.  I determined that ports 22 and 80 were both open and running ssh and http respectively, but these were not the relevent open ports.  With 
TA assistance I was able to find another open port, number 1337.  I was unable to determine what service was running behind it, only that it was unfiltered.

7.  I determined that the web server is running Ubuntu with Apache.  This was determined using an online tool I found at browserSPY.dk.

8.  Yes, I found 4 bonus flags.  The first bonus flag I found was on one of Eric Norman's instagram posts, in the bottom of the frame.  It's text was \*CMSC389R-{Looking_Closely_Pays}.
The next flag I found was in the 'inspect element' of the wattsamp.net homepage, the text being \*CMSC389R-{html_h@x0r_lulz}.  The third bonus flag I found was in the wattsamp.net's
robots.txt file, which read \*CMSC389R-{n0_indexing_pls}.  The fourth and final bonus flag I found was via dnsdumpster, which revealed \*CMSC389R-{Do_you_N0T_See_this} in TXT records for 
wattsamp.net.  I apologize I couldn't figure out how to attach screenshots of the flags, I hope to do so for future assignments as I get the hang of MarkDown.

### Part 2 (75 pts)

I was eventually able to get my python script to work for this situation, but it was admittedly slow.  I guessed correctly from my OSINT that the username was ejnorman84, and with my 
slow-moving stub.py script I eventually found that the password was 'hello1'.  My stub.py file should be in my writeup directory on GitHub.  Big thanks to the TA's for help with the script. 

The main thought process behind my script was as follows.  Per the TA suggestions, the majority of my script was a big 'for' loop that connected to the server via a socket, then received
whatever the server was sending/asking for, which was the captcha to start.  I processed the captcha line and performed whatever operations were necessary, then sent back the answer via
the socket.  I then entered the username and the first line from the password wordlist.  If this entry failed, I moved back to the beginning of the loop and iterated one line down the 
password wordlist.  This would continue until I found a successful password, which in this case was 'hello1'.

The biggest problem I faced with the script was that it took so long.  I had to execute numerous time.sleep(1) calls, which made it so that iterating through a single password took about
10 seconds.  Considering that the wordlist was over a million elements, this was definitely a big problem.  If the correct password hadn't been very early in the file I would have been in 
big trouble.  A possible solution to this issue may have been multi-threading, but fortunately I didn't have to explore any alternatives.

Once I had access to the server, I found the 'flag.txt' file in the '~/home' directory.  The main flag is CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}.
