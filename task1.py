import os
import slackclient

SLACKBOT_NAME = "task1"
SLACKBOT_TOKEN = "xoxb-203433364530-aCWblZmFrmB8YkqPhn18GNfs"
SLACKBOT_ID = "U5ZCRAQFL"

CLIENT = slackclient.SlackClient(SLACKBOT_TOKEN)

print (SLACKBOT_NAME)
print (SLACKBOT_TOKEN)

IS_OKAY = CLIENT.api_call("users.list").get("ok")

print (IS_OKAY)

if (IS_OKAY):
    for user in CLIENT.api_call("users.list"). get("members"):
        if user.get("name") == SLACKBOT_NAME:
            print (user.get("id"))

print (SLACKBOT_ID)
