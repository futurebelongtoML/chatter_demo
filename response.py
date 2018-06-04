from chatterbot import ChatBot
import jieba

# Create a new chat bot named Xiaomi
chatbot = ChatBot('Xiaomi',
    storage_adapter={
        'import_path': 'chatterbot.storage.SQLStorageAdapter',
        'database_name': 'db.sqlite3'
    },
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ])

print("Example: ")
# Get a response to the input text 'I would like to book a flight.'
print('我想了解一下空气净化器')
response = chatbot.get_response('我 想 了解 一下 空气 净化器')
print('response: ', response)

while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        question = input("question: ")
        response = chatbot.get_response(" ".join(jieba.cut(question)))
        #print(" ".join(jieba.cut(question)))
        print('response: ', response)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break