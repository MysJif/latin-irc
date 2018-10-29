from googletrans import Translator
import sys
import irc.bot
import requests
import string

all_normal_characters = string.printable
translator = Translator()
class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.token = token
        self.channel = '#' + channel

        #Create connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print(translator.translate('Connecting to ' + server + ' on port ' + str(port) + '...', dest='la').text)
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)

    def on_welcome(self, c, e):
        print(translator.translate('Joining ' + self.channel, dest='la').text)

        #request capabilities
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        text = e.arguments[0]
        try:
            translation = translator.translate(text, dest='la')
            print(e.source.split('!')[0] + ': ' + translation.text)
        except:
            print(e.source.split('!')[0] + ': ' + text)
        return

def main():
    username  = sys.argv[1]
    token     = sys.argv[2]
    channel   = sys.argv[3]

    bot = TwitchBot(username, token, channel)
    bot.start()

if __name__ == "__main__":
    main()
