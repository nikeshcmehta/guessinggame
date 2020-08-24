"""
Guess the secret set to 9
User will input the number. If it matches to 9, message will be displayed "You Win"
If it doesn't match in 3 consecutive attempts, it will message, "You failed"
"""

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("What do you think is the secret number: "))
    guess_count += 1
    if guess == secret_number:
        print(f"You Win")
        break
else:
        print (f"You lose")


to add here is the message that tells the user that they failed
if they could not guess
How do we do that? Well in Python
our while loops can optionally have an else part.
similar to the if statements. Here, so if this condition is true, do this,
otherwise do something else. In this case our if statement doesn't have
an else part. Now, similar to the if statements
Our while loops, our while statements can also have an else part.

So, right at this level we can add an else block, so else colon.

And the code that we write here will get executed if this while loop

completes successfully without an immediate

break. In other words. If the user guesses the

right number, you break this loop, you jump out of it so the code that

we write in the else block will not get executed.

But if the user cannot guess this number, you're never going to break out of

this loop, so this loop will be executed to completion untill

this condition become false. In that case, the code that we write

in the else block will get executed, and this is the perfect opportunity for us

to tell the user hey, you made three guesses but none of them were right.

So, print, sorry you failed.
