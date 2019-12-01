# Writeup 1 - Web I

Name: *Wyeth Force*
Section: *Section 0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Wyeth Force*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

I gave this website my best shot, but unfortunately I wasn't quite able to get the flag.  I determined that the website's vulnerability was likely to sql injection via the 
URL bar, since there were no other ways the website accepted user input.  On a few of the pages, the end of the URL read '?id=' followed by some number, based on which page 
it was.  I tried following that part of the URL with 'OR 1=1' in an attempt to get the website to dump information, but this was defeated by some sort of filter which I was 
ultimately unable to bypass.  The filter only took issue with 'OR', so I guessed that was probably the command I needed to sneak past it to get the flag.  I tried a lot of the 
filter defeating techniques discussed in class such as encoding the URL or using null bytes, but to no avail.  I also tried to include an empty comment inside the 'OR', but this 
didn't work either.  While I wasn't able to get the flag, I believe I was close.

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

This part of the assignment was tricky.  The first level was easy enough, all I had to do was put a script in the search bar itself that contained 'alert(1)', which got me to the 
next level.

The second part was a little harder, but with the help of the hints I eventually got it.  I was able to exploit the website by putting an image tag in the forum post feature that 
referenced an image that didn't exist.  I caught the error with a 'onerror' that called alert, which ended the level.

Full disclosure, I had to have internet help to pass the rest of the levels.  I realize and accept that I will lose points for this.  

For the third level, the source code allows for someone to insert a .jpg' and then inject another command after it.  In this case, the command was alert(1) within a oneerror, 
which got me through the level.

To solve level 4, you can embed an alert(1) script inside the timer input.

For level 5, an attacker can embed an alert script in the URL.

Level 6 requires that you host a javascript file with the alert script, and then access it via the target website.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
