# """vk chat bot"""
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
        #self.data = vk_api.
            ##groups.getLongPollServer

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
        else:
            print("we can't show message")

    def answer(self):
        pass

if __name__ == "__main__":
    bot = ChatBot(group_id, token)
    bot.run()

