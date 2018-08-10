from slackclient import SlackClient
import os, time, json

event = [{'type': 'message', 'channel': 'DC5ERK0MV', 'user': 'U9F31JE5Q', 'text': 'Howdy', 'ts': '1524843143.000332', 'source_team': 'T9EG86SC9', 'team': 'T9EG86SC9'}]
#SLACK_VERIFICATION_TOKEN = os.environ['V-TOKEN']
SLACK_BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']


class slackCommunication:
    def __init__(self):
        self.slack_client = SlackClient(SLACK_BOT_USER_TOKEN)
        self.appname = "storefinder"
        self.channels_call = self.slack_client.api_call("channels.list")
        print (self.channels_call['channels'])

    def list_channels(self):
        channels_call = self.slack_client.api_call("channels.list")
        if channels_call.get('ok'):
            print(json.dumps(channels_call['channels'],indent=3))
            return channels_call['channels']
        return None


    def slackConnect(self):
        return self.slack_client.rtm_connect()

    def slackReadRTM(self):
        return self.slack_client.rtm_read()
        """while True:
            print (self.slack_client.rtm_read())
            time.sleep(3)
            """

    def parseSlackInput(self, input, botID):
        botAID = "<@"+botID+">"
        if input and len(input)>0:
            input = input[0]
            if 'text' in input and botAID in input['text']:
                user = input['user']
                message = input['text'].split(botAID)[1].strip(' ')
                channel = input['channel']
                return [str(user), str(message), str(channel)]
            else:
                return [None, None,None]


    def getBotID(self, botUserName):
        api_call = self.slack_client.api_call('users.list')
        users =api_call['members']
        #print (json.dumps(users, indent=2))
        for user in users:
            #Iterates through all users and sees if the userName passed in is one of the users in the channel and returns their id
            if 'name' in user and botUserName in user.get('name') and not user.get('deleted'):
                return user.get('id')


    def writeToSlack(self, chan, mess):
        return self.slack_client.api_call("chat.postMessage", channel=chan, text=mess, as_user=True)

class mainFunc(slackCommunication):
    def __init__(self):
        super(mainFunc, self).__init__()

    def decideWhetherToTakeAction(self, input):
        if input:
            user,message,channel = input
            return self.writeToSlack(channel,message)

    def run(self):
        self.slackConnect()
        BOTID = self.getBotID(self.appname)
        while True:
            self.decideWhetherToTakeAction()
            time.sleep(1)
