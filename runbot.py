from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import os
import psutil
import time


class Runbot:
	
	def __init__(self):
		self.updater = Updater("<PLACE-YOUR-OWN-TOKEN-HERE>", use_context=True)
		
	
	def Start(self, 
	          update: Update, 
		  context: CallbackContext):
		
		update.message.reply_text("Welcome to RunBot, type /help for a list of available features")
	
	
	def Help(self, 
	         update: Update,  
		 context: CallbackContext):
			
		update.message.reply_text("""/start for live message, /monit <PID> to monitor a specific PID, 
							  /push to upload in this chat a copy of the indicated file""")
	
	
	def Monitor(self, 
	            update: Update,
		    context: CallbackContext):
		
		PID = int(context.args[0])
		update.message.reply_text("Ok, I will watch {} with great interest".format(PID))
		t0 = time.time()
		while True:
			if psutil.pid_exists(PID):
				continue
			else:
				t1 = time.time()
				update.message.reply_text("looks like your PID finished! took {} seconds".format(t1-t0))
				break


	def PushDoc(self,
		    update: Update,
		    context: CallbackContext):
	
		doc_name = os.getcwd()+'/'+ str(context.args[0])
		with open(doc_name, "rb") as docs:
			context.bot.send_document(update.message.chat_id, document=docs, filename=str(context.args[0]))

	def Launch(self):
		
		self.updater.dispatcher.add_handler(CommandHandler('start', self.Start))
		self.updater.dispatcher.add_handler(CommandHandler('help', self.Help))
		self.updater.dispatcher.add_handler(CommandHandler('monit', self.Monitor))
		self.updater.dispatcher.add_handler(CommandHandler('push', self.PushDoc))

		self.updater.start_polling()
