from slackclient import SlackClient
import os, time, json

#SLACK_VERIFICATION_TOKEN = os.environ['V-TOKEN']
SLACK_BOT_USER_TOKEN = os.environ['BOT_USER_TOKEN']
slack_client = SlackClient(SLACK_BOT_USER_TOKEN)

link = '<https://media.makeameme.org/created/that-would-be-3dsosw.jpg|That would be great>'

if slack_client.rtm_connect():
    while True:
        events = slack_client.rtm_read()
        for event in events:
            print('New Event:',event['type'])
            if(event['type'] == 'message' and 'text' in event and 'channel' in event):
                print('This is a message from: '+ event['user'])
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

        #print('No event:',slack_client.rtm_read())
        time.sleep(1)
else:
	print("Connection failed. Invalid Slack token or bot ID")


#if event is a message, then...
    #if message contains homer or is @homer
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