from chatterbot import ChatBot
from chatterbot.trainers import Trainer
from chatterbot.conversation import Statement, Response
from data_process import process

class ListTrainer(Trainer):
    """
    Allows a chat bot to be trained using a list of strings
    where the list represents a conversation.
    """
    def train(self, conversation):
        """
        Train the chat bot based on the provided list of
        statements that represents a single conversation.
        """
        for conversation_count, text in enumerate(conversation):
            if conversation_count%1000==0:
                print("training %d : "%conversation_count, text[0],"|", text[1])

            statement = self.get_or_create(text[1])
            statement.add_response(Response(text[0]))
            self.storage.update(statement)

# Create a new chat bot named Xiaomi
chatbot = ChatBot('Xiaomi')
chatbot.set_trainer(ListTrainer)

data = process()

chatbot.train(data)

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('我 想 了解 一下 空气 净化器')

print(response)