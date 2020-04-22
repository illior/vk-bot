from BaseVkBot import BaseVkBot

class VkBot(BaseVkBot):
	def newMessage(self, event):
		response = self.vk.method('users.get', {'user_ids': event['user_id']})
		
		name_user = response[0]['first_name']

		self.sendMessage(event['user_id'], 'Привет ' + name_user)
