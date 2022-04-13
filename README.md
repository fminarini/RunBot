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
I'll leave the link to telegram's official documentation on this topic: https://core.telegram.org/bots.

# Required Libraries
This small project relies on https://python-telegram-bot.readthedocs.io/en/stable/index.html, which can be installed via `pip`.

# Prepare to launch your own RunBot
The logic of the bot is kept in a separate class (runbot.py). Just a single edit is required on this file:

- Substitute "\<PLACE-YOUR-OWN-TOKEN-HERE\>" with the Token produced by BotFather 

  (i.e. "\<PLACE-YOUR-OWN-TOKEN-HERE\>" --> "token")

Then you should place runbot.py in a folder within your current working directory:

- For instance, if I work in directory X, I will make X/some_name and then place runbot.py into X/some_name.

This will allow you to import the class in ideally any python script with the syntax `from folder_name import runbot as alias_you_like`

# Launching script
the launcher can be as simple as the following:

  ```python
  #launcher.py
  from Runbot import runbot as bot

  run_bot = bot.Runbot()
  run_bot.Launch()
  ```
and then you can run it either with the classic `python3 launcher.py &` to keep it in the background or with the `nohup` feature if you want to avoid the service to be hung up.

# What can I do with it
Once you started the "back-end" logic of the bot, you should open the bot on your phone (or, equivalently, on telegram web) and type `/help` to list all available commands.
Right now, the bot has two main features, `/monit` and `/push`:

- **/monit** _PID_ triggers the monitoring on the specified Process ID. To retrieve the PID of a running python script, for instance, you can `import os` and then add a `print(os.getpid())` at the beginning of the script.

so if your script has PID=12345, then writing `/monit 12345` in the chat will trigger the monitor feature of the bot.

- **/push** _filename_ triggers the upload of the specified file in the bot chat-room (the file needs to be in the current working path and have exactly the name we provided to the command.

so, if our program writes some output to a `logfile.txt`, if we write `/push logfile.txt` we will see it uploaded in the chat.

- **publish** _filename_ triggers the upload of the specified picture in the bot chat-room (the picture needs to be in the current working path and have exactly the name we provided to the command.

