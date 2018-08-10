#from slack_bot import *

import pytest


input = [
    {'type': 'message',
     'user': 'U9F31JE5Q',
     'text': '<@UC5ERJZUP> hi',
     'client_msg_id': '1cd27c97-0daf-4402-a4f2-537312910078',
     'team': 'T9EG86SC9',
     'channel': 'DC5ERK0MV',
     'event_ts': '1533842753.000293',
     'ts': '1533842753.000293'}
]

@pytest.fixture
#Whaqt is pytest fixture
#@pytest.mark.skip()
def slackCommunication():
    from slack_botClass import slackCommunication
    return slackCommunication()

@pytest.fixture
def mainFunc():
    from slack_botClass import mainFunc
    return mainFunc()

#@pytest.mark.skip()
def test_slackConnect(slackCommunication):
    print (slackCommunication.slackConnect())
    #assert slackCommunication.slackConnect() == True

#@pytest.mark.skip()
def test_parseSlackInput(slackCommunication):
    assert slackCommunication.parseSlackInput(input, 'UC5ERJZUP') == ["U9F31JE5Q", "hi", 'DC5ERK0MV']

#Give Bot Id
#@pytest.mark.skip()
def test_getBotID(slackCommunication):

    assert slackCommunication.getBotID('storefinder') == 'UC5ERJZUP'

#@pytest.mark.skip()
def test_writeToSlack(slackCommunication):
    assert slackCommunication.writeToSlack('DC5ERK0MV', "Testing write to slack")['ok']==True

#@pytest.mark.skip()
def test_slackReadRTM(slackCommunication):
    slackCommunication.slackConnect()
    print (slackCommunication.slackReadRTM())

def test_decideWhetherToTakeAction_Message(mainFunc):
    input = ["U9F31JE5Q", "hi", 'DC5ERK0MV']
    assert mainFunc.decideWhetherToTakeAction(input)

def test_decideWhetherToTakeAction_None(mainFunc):
    input = [None, None,None]
    assert mainFunc.decideWhetherToTakeAction(input)


#pytest -v -s test_slack_bot.py
