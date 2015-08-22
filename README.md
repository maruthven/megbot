# MegBot
Facebook messenger groups have the ability to reach 100+ unread messages pretty quickly. At that point, you have to make a decision: miss out on the messages and risk missing an awesome discussion, or read every single line and risk oportunity cost. Now you don't have to make that decision! MegBot allows you to automate your Facebook message group summaries.

## Details
MegBot itself is an object that allows you to interface with Facebook messenger through your own account. 

The example, megbotex.py, summarizes the past 50 messages the group said. It does this either every 50 messages, or when someone in the chat group calls it with "@megbot". It also draws attention to whoever you want by responding to your message of "@"xyz with a capitalized version of the word attached to the @.

![](https://scontent.fsnc1-1.fna.fbcdn.net/hphotos-xfp1/v/t1.0-9/11898559_10206907510503212_5645712742133939266_n.jpg?oh=4c25ee4333985aed381cc4b5ac132a2a&oe=567CF17E)

## Usage
To use the example:

python megbotex.py [facebook email] [facebook password] [message ID]

The message ID is located here:
![](https://lh3.googleusercontent.com/brtlx42txPgdHXeg5p_r66ACFLDA2diN9G7Kz_SLbc6zLiCiaoyeyxPx4XpvzEpKyYuvb_kOdXJQKFmiK3psUXa0_ywTbqIuyvRL3CqcVrN46mBWc5ItFJMrX9UHzsVghIT9qefanAT94xOhcvcbdKJHMfPbb8NRa1casKTleU1SmfwqY47r5uLNwLmvoeuoVmpj2yl2xQMXPBxvhnTrUMJLf6LmrMxAsXWXVTGZ8pgWShVv91BHUuKbfG8PmZ8N6X-4WT6vEAoSjqdOCu-wt-k1ml13B7RlV6y9DhEGfyLsIWEdnfQnyMHR4WsU8zDqwe57NSDT7X_HmYsdeTcBdXgp2SLZanyo_UgY4HeA66usPa2f5Na1UCXeOka1BrDjQPQfl130cXjqsZNGIn4E06pxJ4PPeXFzXXGCs3OLgmeGLTTrYaOoYsIVHaxpEt3X7ldesB8vv1ibpHtbahVyoXR_FhTmlXolf-xqiiFETgfz_7b4b1bm-zwlrdWlUGfrR035fw=w1276-h68-no_)

The information in your chat is stored in an array of strings, and therefore does not persist in this example. Please be aware of privacy concerns if you decide to change this feature.

## Contributions
Feel free to send a pull request for added functionality to MegBot or any use cases you want to share. 

## Disclaimer
PM's are private. Therefore, you should have full consent of everyone in your group to opporate MegBot. Please be considerate of others.

## Maintainer
[Megan Ruthven](http://maruthven.com/) ([@maruthven](https://twitter.com/maruthven))
