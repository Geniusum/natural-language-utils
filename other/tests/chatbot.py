import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by NLTK.",]
    ],
    [
        r"how are you?",
        ["I'm a chatbot, so I'm always functioning as expected.",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Good to know that you're %1", "How can I assist you today?",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am just a program, so I exist everywhere.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. Goodbye!"]
    ],
]


class ChatBot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def start_chat(self):
        print("Hi, I'm a chatbot. Type something to start a conversation. Type 'quit' to end the chat.")
        self.chat.converse()

if __name__ == "__main__":
    chatbot = ChatBot(pairs)
    chatbot.start_chat()