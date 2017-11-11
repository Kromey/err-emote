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
    def poke(self, msg, args):
        """Poke people"""
        return "/me poke poke poke"

    @botcmd
    def say(self, msg, args):
        """Say things"""
        #return args.capitalize()
        return args

    @botcmd
    def say_hello(self, msg, args):
        """Say hello to folks"""
        return "Hello, " + re.sub('^to *', '', args) + '!'

    @botcmd(hidden=True)
    def say_hi(self, msg, args):
        """Say hi to folks"""
        return "Hi, " + re.sub('^to *', '', args) + '!'

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

    _jokes = (
            ('Did you hear about the guy whose whole left side was cut off? He\'s all right now.',),
            ("I'm reading a book about anti-gravity. It's impossible to put down.",),
            ("I wondered why the baseball was getting bigger. Then it hit me.",),
            ("It's not that the man did not know how to juggle, he just didn't have the balls to do it.",),
            ("I'm glad I know sign language, it's pretty handy.",),
            ("My friend's bakery burned down last night. Now his business is toast.",),
            ("Why did the cookie cry? It was feeling crumby.",),
            ("I used to be a banker, but I lost interest.",),
            ("A drum and a symbol fall off a cliff",),
            ("Why do seagulls fly over the sea? Because they aren't bay-gulls!",),
            ("Why did the fireman wear red, white, and blue suspenders? To hold his pants up.",),
            ("Why didn't the crab share his food? Because crabs are territorial animals, that don't share anything.",),
            ("Why was the javascript developer sad? Because he didn't Node how to Express himself.",),
            ("What do I look like? A JOKE MACHINE!?",),
            ("How did the hipster burn the roof of his mouth? He ate the pizza before it was cool.",),
            ("Why is it hard to make puns for kleptomaniacs? They are always taking things literally.",),
            ("Why do mermaid wear sea-shells? Because b-shells are too small.",),
            ("I'm a humorless, cold hearted, machine.",),
            ("Two fish in a tank. One looks to the other and says 'Can you even drive this thing???'",),
            ("Two fish swim down a river, and hit a wall. One says: 'Dam!'",),
            ("What's funnier than a monkey dancing with an elephant? Two monkeys dancing with an elephant.",),
            ("How did Darth Vader know what Luke was getting for Christmas? He felt his presents.",),
            ("What's red and bad for your teeth? A Brick.",),
            ("What's orange and sounds like a parrot? A Carrot.",),
            ("What do you call a cow with no legs? Ground beef",),
            ("Two guys walk into a bar. You'd think the second one would have noticed.",),
            ("What is a centipedes's favorite Beatle song?  I want to hold your hand, hand, hand, hand...",),
            ("What do you call a chicken crossing the road? Poultry in moton. ",),
            ("Did you hear about the Mexican train killer?  He had locomotives",),
            ("What do you call a fake noodle?  An impasta",),
            ("How many tickles does it take to tickle an octupus? Ten-tickles!",),
            ("At the rate law schools are turning them out, by 2050 there will be more lawyers than humans.",),
            )
    @botcmd
    def joke(self, msg, args):
        return random.choice(self._jokes)[0]

    _emotes = (
            (re.compile(r'\bcookie\b'), ('Who said cookie?', 'Someone has cookies??', 'Can I please have the cookie?')),
            (re.compile(r'\bthe bot\b'), ('I have a name you know!', 'Don\'t talk about me like I\'m not here!')),
            (re.compile(r'(^/me cr(y|ies)|:\'\()'), ('Aw don\'t be sad!', 'Don\'t cry!')),
            )
    def callback_message(self, msg):
        try:
            reply = msg.frm.room
        except AttributeError:
            reply = msg.frm

        message = msg.body.lower()
        for emote in self._emotes:
            if emote[0].search(message):
                self.send(
                        reply,
                        random.choice(emote[1]),
                        )

