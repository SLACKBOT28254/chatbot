import slackclient, time

# delay in seconds before checking for new events 
SOCKET_DELAY = 1
# slackbot environment variables SETTING YOUR VARIABLES THAT YOU NEED
SLACKBOT_NAME = "task1"
SLACKBOT_TOKEN = ""
SLACKBOT_ID = "U5ZCRAQFL"

# Create client which allows us to interact with SLACK API 
CLIENT = slackclient.SlackClient(SLACKBOT_TOKEN)

# Mock function which always returns true
def is_for_me(event):
    # TODO Implement later
    return True

def handle_message(message, user, channel):
    # TODO Implement later
    print('Handling Message: ' + str(message))
    print('User: ' + str(user))
    print('Channel: ' + str(channel))

    post_message(message='Hello', channel=channel)

def post_message(message, channel):
    CLIENT.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)

def is_hi(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens for g in ['hello', 'bonjour', 'hey', 'hi', 'sup', 'morning', 'hola', 'ohai', 'yo'])

def run():
    if CLIENT.rtm_connect():
        print('[.] Slackbot is ON...')
        while True:
            event_list = CLIENT.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print('Event: ' + str(event))
                    print('Name: ' + str(event.get('name')))
                    if True:
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY) 
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()
