from errbot import BotPlugin, botcmd
import re
import random
#from errbot.utils import get_sender_username

class Emote(BotPlugin):
    """Make Err a bit more emotive"""

    @botcmd
    def give(self, msg, args):
        """Give things"""
        return "/me gives " + args

    @botcmd
    def slap(self, msg, args):
        """Slap things"""
        return "/me slaps " + args + " with a large trout"

    @botcmd
    def say(self, msg, args):
        """Say things"""
        #return args.capitalize()
        return args

    @botcmd
    def say_hello(self, msg, args):
        """Say hello to folks"""
        return "Hello, " + re.sub('^to *', '', args) + '!'

    _dances = (
            'dances a merry jig',
            'dances around the room',
            'happily dances',
            'breaks it down, street style',
            'does the Jitterbug',
            'tap dances across the room',
            'boogies like it\'s 1976',
            'twerks',
            'pops it like it\'s hot',
            'does the Hustle, Travolta-style',
            'elegantly executes an extraordinary exhibition',
            )
    @botcmd
    def dance(self, msg, args):
        """Dance a merry jig!"""
        return "/me " + random.choice(self._dances) + '!'

    _responses_the_bot = (
            'I have a name you know!',
            'Don\'t talk about me like I\'m not here!',
            )
    def callback_message(self, msg):
        if msg.body.lower().find('cookie') != -1:
            self.send(
                msg.frm,
                "Who said cookie? Where is it? Cookie??",
            )
        elif msg.body.lower().find('the bot') != -1:
            self.send(
                msg.frm,
                random.choice(self._responses_the_bot),
            )

