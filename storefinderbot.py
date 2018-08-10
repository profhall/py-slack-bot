from slackclient import SlackClient
import os, time, json
from play import markets
from THD_MD.getMarkets import listMarkets

"""
Psuedocode
#if event is a message, then...
    #if message contains botid
        #if message contains 'directions'
            #ask to what store
            #and the starting destination
            #call getStore func
            #call api & return results

        #if message contains 'help'
            #show menu with example commands

        #if message contains 'markets'
            #call getMarkets func and list markets in pages or scrollable list

        #if message contains 'stores' or 'locations'
            #askk what market
            #call get locations func

"""
#SLACK_VERIFICATION_TOKEN = os.environ['V-TOKEN']
SLACK_BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
slack_client = SlackClient(SLACK_BOT_USER_TOKEN)
mktss = markets()
markets = []
for market in mktss:
    markets.append(next(mktss))

link = '<https://media.makeameme.org/created/that-would-be-3dsosw.jpg|That would be great>'

if slack_client.rtm_connect():
    while True:
        events = slack_client.rtm_read()
        for event in events:
            print('New Event:',event['type'])

            # if event is a message, then...
            if(event['type'] == 'message' and 'text' in event and 'channel' in event ):
                #print(json.dumps(event,indent=2))
                if('bot_id' not in event):
                    print('This is a message from: '+ event['user'])
                    user = event['user']
                print('The message reads "'+ event['text']+ '"')

                channel = event['channel']
                text = event['text']

                if 'that would be great' in text.lower() and link not in text:
                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=link,
                        as_user='true:'
                    )

                # if message contains botID
                if ('UC5ERJZUP' in text ):
                    slack_client.api_call('chat.postMessage',channel=channel,text="you rang <@" + user + ">?",as_user='true:')

                    # if message contains 'directions'
                    if ('directions' in text):
                        # ask to what market store is in


                        slack_client.api_call('chat.postMessage',
                                              channel=channel,
                                              text="What market is the store in <@" + user + ">?",
                                              attachments=  [{
                                                "text": "Choose a game to play",
                                                "fallback": "If you could read this message, you'd be choosing something fun to do right now.",
                                                "color": "#3AA3E3",
                                                "attachment_type": "default",
                                                "callback_id": "game_selection",
                                                "actions": [
                                                    {
                                                        "name": "markets",
                                                        "text": "Which Market",
                                                        "type": "select",
                                                        #markets will go here
                                                        "options": markets
                                                    }
                                                ]
                                              }]
                                              )
                        # call getmarkets and list markets

                        # and the starting destination
                        # call getStore func
                        # call api & return results

        #print('No event:',slack_client.rtm_read())
        time.sleep(1)
else:
	print("Connection failed. Invalid Slack token or bot ID")

