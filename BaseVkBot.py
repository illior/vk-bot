from os import environ
from vk_api import VkApi, longpoll
from random import randint

class BaseVkBot:
	token = ''
	api_v = ''
	vk = None
	longPoll = None
	
	def __init__(self):
		self.loadEnv()

		self.token = environ['token']
		self.api_v = environ['api_v']

		self.vk = VkApi(token = self.token)
		self.longPoll = longpoll.VkLongPoll(self.vk)

	def run(self):
		for event in self.longPoll.listen():
			if event.type == longpoll.VkEventType.MESSAGE_NEW and event.to_me:
				self.newMessage({'user_id': event.user_id, 'message': event.text})

	def loadEnv(self):
		try:
			file = open('.env', 'r')

			for line in file:
				line = line.rstrip()

				temp = line.split('=')

				environ[temp[0]] = temp[1]
		except FileNotFoundError as e:
			print('File .env not exists')
			exit()

	def sendMessage(self, user_id, message):
		random_id = randint(1, 10000000)
		self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

	def newMessage(self, event):
		pass


