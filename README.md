# MegBot
Facebook messenger groups have the ability to reach 100+ unread messages pretty quickly. At that point, you have to make a decision: miss out on the messages and risk missing an awesome discussion, or read every single line and risk oportunity cost. Now you don't have to make that decision! MegBot allows you to automate your Facebook message group summaries.

## Details
MegBot itself is an object that allows you to interface with Facebook messenger through your own account. 

The example, megbotex.py, summarizes the past 50 messages the group said. It does this either every 50 messages, or when someone in the chat group calls it with "@megbot". It also draws attention to whoever you want by responding to your message of "@"xyz with a capitalized version of the word attached to the @.

![](https://scontent.fsnc1-1.fna.fbcdn.net/hphotos-xfp1/v/t1.0-9/11898559_10206907510503212_5645712742133939266_n.jpg?oh=4c25ee4333985aed381cc4b5ac132a2a&oe=567CF17E)

## Usage
To use the example:
python megbotex.py [facebook email] [facebook password] [message ID]
The information in your chat is stored in an array of strings, and therefore does not persist in this example. Please be aware of privacy concerns if you decide to change this feature.

## Contributions
Feel free to send a pull request for added functionality to MegBot or any use cases you want to share. 

## Disclaimer
PM's are private, and therefore, you should have full consent of everyone in your group to opporate. Please be considerate of others

## Maintainer
Megan Ruthven ([@maruthven](https://twitter.com/maruthven))
