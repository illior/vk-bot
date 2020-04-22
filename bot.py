from VkBot import BaseVkBot

class VkBot(BaseVkBot):
	def newMessage(self, event):
		self.sendMessage(event['user_id'], event['message'])

bot = VkBot()