# Operational Security and Social Engineering

## Homework 3 Writeup

**Name: Wyeth Force	Section: 0101**

### Part 1

Since the necessary information all pertains to Eric’s mother, it would probably be best if I were to directly contact his mother directly and to create a pretext with her.  To do this, 
though, I would first need to get her phone number from Eric.  In order to accomplish this, I would call Eric posing as an administrator from his own company, Wattsamp.  I would create the 
pretext that Wattsamp is updating emergency contact information for all employees in case of medical emergency.  I would ask for emergency contact information from Eric until we got to 
his mom.  Once I have his mother’s number, I can reach out to her and create another pretext.

When calling Eric’s mother, I would pose as an employee of her bank (I would find out what bank via OSINT).  I would inform her that some suspicious purchases were just made using her card, and that I would like to ask her 
some questions about her recent transaction history.  First I would ask her to login to her online account.  I would ask if she saw the purchase in question on her statement (she would 
not see anything suspicious, of course).  Upon her stating she can’t see anything out of the ordinary, I would ask what browser she is using to view her account.  No matter her answer I 
would state that users of that specific browser often have issues viewing our website, and then move on.  If she tries a different browser and still doesn’t see the fake charge, I would 
feign confusion, then suggest that our fraud team had stopped the charge from going through until we had spoken to her, which is why she isn’t seeing it.  I would then ask for 
her basic account information, then ask for her ATM pin in order to verify that I was speaking to the correct person.  I would then ask for more information regarding her security 
questions, such as her maiden name, city of birth, and the name of her first pet.  In order to make these questions less suspicious, I would ask for other information between these 
questions, such as 'do you know of any way your account may have been compromised' or something along those lines.  There’s a small chance that she has set up these kind of security 
questions and wouldn’t be confused by my asking for this information, but in the event that she becomes suspicious I would aim to create self-doubt.  If she says that she never set up 
those kind of questions on her account, I would feign confusion and ask if she was sure about that.  If she doesn’t budge I would state that the protections are in fact on her account, 
and then suggest that possibly her account has been hacked or otherwise compromised.  I would then assert that I need this information, and hopefully get her to budge.  I would then 
conclude the call by asking her about the fake charges to her card, and then satisfy her by stating that we would remove the charges from her statement.  By the conclusion of this call I 
will have gathered all necessary information.


### Part 2

The first suggestion I would make to Eric would be to strengthen both his username and password combination.  First of all, it seems very unwise to use the same username on social media and your server’s backend login.  Had he only had a different username I likely would not have gotten into the server.  Secondly, ‘hello1’ is a very weak password, largely because of its length.  I would recommend that Eric use a secure password generator, such as https://passwordsgenerator.net/, or at least come up with a password longer than 6 characters.  I would also suggest that he change his password every few months, if possible.  The truth is that this attack would have almost certainly been foiled had Eric only had a stronger username/password combo.
Another area I would suggest strengthening would be that of the server’s ‘Captcha’.  The current security on the website is super predictable and can easily be scripted.  I would personally recommend that the server admin change it to some sort of text-base question chosen from a bank of possible questions.  The questions should differ to the point that it would be impossible for a script to easily understand and answer the questions.  For example, one questions could be “Combine the words stop and light: stoplight”, and another could be something like “Three eggs plus two eggs makes how many eggs: five”.  Questions like this are easily understood by humans but cannot be automated by scripts without tremendous difficulty.
My final recommendation for Eric and Wattsamp would be to secure the open ports on their server using a firewall.  I personally have limited knowledge about how firewalls work, but from the reading I did online (https://www.networkworld.com/article/3191513/securing-risky-network-ports.html), it seems that admins can use a firewall to prevent people from accessing the open ports from outside the server’s local network.  This would prevent attackers from remotely accessing the servers.  There would still be the danger of attackers getting onto the local network, but hopefully Wattsamp’s physical security would be able to prevent that.

