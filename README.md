# RunBot
Python-powered Telegram bot for monitoring the status of running scripts in a linux system.

_Disclaimer: This is a "for fun" project that will be updated in my spare time. Since I don't have a CS background, I'm fully aware that my code might not be the most optimized or professional one. Suggestions for improvements will always be more than welcome._

# Concept
This bot stems from the idea that sometimes scripts require a lot of time to compile and/or run. In those cases, you'd typically like to keep yourself in proximity of your personal PC as you want to see the beautiful result of your hard work or, alternatively, cry in despair as errors multiply. 

But sometimes keeping a physical eye on your terminal is not easy: for instance, if you have to attend a meeting, it is not professional to open the lid of your laptop every 10 seconds to check if everything is working as expected :)

What if you could run your errands while keeping in touch with your code? What if you could receive in real-time the result of computations as a log file and read it on your phone after leaving the office?

That is the reason I've created this logic in python: Run my code, do something else in the meantime, neglect nothing.

# Create your own Telegram Bot
There are a lot of guides online. Since the procedure is quite standard, all of them are almost equivalent.
I'll leave the link to telegram's official documentation on this topic: https://core.telegram.org/bots

# Prepare to launch your own RunBot
The logic of the bot is kept in a separate class (runbot.py). Just a single edit is required on this file:

- Substitute "\<YOUR-BOT-TOKEN-HERE\>" with the Token produced by BotFather (i.e. "\<YOUR-BOT-TOKEN-HERE\>" --> "token")

Then you should place runbot.py in a folder within your current working directory:

- For instance, if I work in directory X, I will make X/some_name and then place runbot.py into X/some_name.

This will allow you to import the class in ideally any python script

# Launching script
the launcher can be as simple as the following launcher.py:

  ```python
  from Runbot import runbot as bot

  run_bot = bot.Runbot()
  run_bot.Launch()
  ```
and then you can run it either with the classic `python3 launcher.py &` to keep it in the background or with the `nohup` feature if you want to avoid the service to be hung up.
