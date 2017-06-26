print ("hello world")
GREETINGS_KEYWORDS = ("hello", "hi", "hey")
GREETINGS_RESPONSE = ["Hello. This is chatbot", "Hello", "How can I help you?"]

def check_for_greeting(sentence)
 for word in sentence.words:
     if word.lower() in GREETINGS_KEYWORDS:
         return random.choice(GREETINGS_RESPONSE)