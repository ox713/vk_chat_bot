# """vk chat bot"""
import random

group_id = 192665997
token = "e3fcd31773c6d0b4a1e7427347f6a6844ddd1c08749f4045aad69aa891117563a25d81ea7a412eb398f22"
import vk_api
import vk_api.bot_longpoll

class ChatBot:
    def __init__(self, group_id, token):
        self.group_ip = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.long_poll = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_ip)
        self.api = self.vk.get_api()
        self.dialogs = []
        self.storage = ["cola", "vodka", "tarhun"]

    def run(self):
        for event in self.long_poll.listen():
            print("message")
            try:
                self.on_event(event)

            except Exception as err:
                print(err)


    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            #print(event.object.message["text"]) # в новых версиях
            print(event.object.text) # в апи 5.92

            self.answer(event)

        else:
            print("we can't show message")
            print(event.type)

    def answer(self, event):
        if event.object.peer_id not in self.dialogs:
            self.dialogs.append(event.object.peer_id)

            self.api.messages.send(message="Привет, рад познакомиться",
                                   random_id=random.randint(0, 2 * 20),
                                   peer_id=event.object.peer_id)
        else:
            self.api.messages.send(message="Привет",
                               random_id=random.randint(0, 2 * 20),
                               peer_id=event.object.peer_id
                               )
        #if ("напиток", "пить", "кола", "жара")in event.object.text:
        if "напиток" in event.object.text:
            self.api.messages.send(message="Я вижу вам интересны напитки, могу я вам их предложить?",
                                   random_id=random.randint(0, 2 * 20),
                                   peer_id=event.object.peer_id
                                   )
        # if ["да","конечно", "буду рад", "ладно", "ок"] in event.object.text:
        if "да" in event.object.text.lower():
            self.api.messages.send(message=f"Вот наш ассортимент{self.storage}, чего желаете?",
                                   random_id=random.randint(0, 2 * 20),
                                   peer_id=event.object.peer_id
                                   )


if __name__ == "__main__":
    bot = ChatBot(group_id, token)
    bot.run()

