
# "Sex For Breakfast" is a fictious Jersey pop punk band that serves as a commentary to how homogenous
    # the local and world wide music industry has historically been.
# This is a comedic and satirical piece of a "Basic-Bro-Band."
# Viewers can laugh at the "basic" and not very self aware band while also considering
    # how rock music has historically showcased one narrative.

import random
import twitter

# ___________________________________________________________________________________________________________

# GENERAL TWEETS FROM BAND MEMEBERS
# Sex For Breakfast likes to interact with their fans on social media. It helps them increase
    # interest in their music and promote their shows, music releases, and tours. Sex For Breakfast
    # believes that tweeting their everyday thoughts will 'humanize' them from their rock'n'roll-sex god
    # status and make them more relatable to the normies out there.
# All four band members have access to the band account and they each have different personalities that
    # are apparent in their Tweets. Values will be assigned to each band member and the program will randomly
    # pick which member it will post as.

# Below are Tweets from David. He is very enthusiastic, fame hungry, and is convinced the band will make it
    # big time. Sex For Breakfast IS his life.
def genDavidTweet():
    # DAVID - lead guitar

    DavidSentence1 = ["We love our fans", "One day we're gonna make it", "We love you guys",
    "Last night was siccckkk", "Last night was sickkkk man", "Gig last night was so unreal",
    "So much love out there last night", "We're on a mission to make music our lives", "I just wrote the SICKEST guitar riff",
    "Our fans mean so much to us", "The pit last night was UNREAL", "Our fans give us the best vibessss",
    "Engery was fucking sick last night", "Still coming down from the gig last night"]


    DavidSentence2 = ["You ain't seen the last of us", "Thanks to all you guys out there supporting us",
    "We couldn't do this without you","New music soon", "Workin on our next album", "Can't wait to play there again tho",
    "We have the realest fans out there", "Better see you motherfuckers at the next show",
    "Wish we could take you all on tour with us", "Stay tuned for more new music",
    "Working on our next EP", "Just gotta keep believing in the music", "Shoutout to the best motherfucking fans in the world",
    "Comment below where you want us to play next", "You're NOT gonna wanna miss what we got in store", "RocknRoll, everyone",
    "DM us if you want us to play yoyr venuueee"]

    DavidEndingPunctuation = [".", "!!", "!!!111!!1!", "!!?!", "11!!", "...", "!"]

    DavidFacePunctuation = [ ":D", "XD", ":P", ";P", ":O", ";D", ":-)"]

    FromDavid = ["-David"]

    DavidSentence1 = random.choice(DavidSentence1)
    DavidSentence2 = random.choice(DavidSentence2)
    DavidEndingPunctuation = random.choice(DavidEndingPunctuation)
    DavidFacePunctuation = random.choice(DavidFacePunctuation)
    FromDavid = random.choice(FromDavid)

    DavidTweet = DavidSentence1 + DavidEndingPunctuation + ' ' + DavidSentence2 + DavidEndingPunctuation + ' ' + DavidFacePunctuation + ' ' + FromDavid
    return DavidTweet


# TYLER - vocals, rhythm guitar
# The youngest member of Sex For Breakfast (18 year old senior in high school), he is the
    # angsty, angry teenager that drives the edgy lyrics that makeup the songs. He thinks his mom
    # is a huge bitch and nobody understand what he feels. Music is his only outlet.

def genTylerTweet():

    TylerSentence1 = ["Shit is really fucked in this world", "We live in a messed up world", "We're all alone in this world",
    "Sometimes life just isn't fucking fair", "There's no point in anything", "Fuck everyone, man", "I hate life",
    "My parents are fucking normies", "Fuck normies", "Fuck the posers", "Fuck the corporations", "Fuck my parents",
    "Parents are complete bitches"]

    TylerSentence2 = ["I really channel that anger and put it towards my music", "That's why this guitar and my lyrics are all I got",
    "Can't wait to graduate and just write music all day", "This is the shit that inspires my lyrics", "Jersey fucking suxxx",
    "Just wait till I get out of here", "I just wanna play some songs before I die", "Life of a misfit is hard"]

    TylerEndingPunctuation = [".", "!", "!!!", "..."]

    FromTyler = ["-Tyler"]

    TylerSentence1 = random.choice(TylerSentence1)
    TylerSentence2 =   random.choice(TylerSentence2)
    TylerEndingPunctuation =  random.choice(TylerEndingPunctuation)
    FromTyler = random.choice(FromTyler)

    TylerTweet = TylerSentence1 + TylerEndingPunctuation + ' ' + TylerSentence2 + TylerEndingPunctuation + " " + FromTyler
    return TylerTweet


# JAKE - bass
# Jake is a happy, happy-go-lucky, funloving goofball just along for the ride. He enjoys playing music and being with
    # the band, and wants everyone to be in a good mood.

def genJakeTweet():
    JakeSentence1 = ["Hey friends!", "Sup pals!!", "What's good party people", "Heyooo friends!", "Hey!!!", "Hey hey!",
    "Hey buddies!", "Heeeeeyyy"]

    JakeSentence2 = ["What's your favorite pizza topping?", "What did you guys dream about last night?",
    "Just wanna say I think you're all cuuuuuute.", "Cats or dogs??", "What are you guys doing tonight??",
    "What are your biggest dreams?", "Chinese food or KFC??", "Favorite kind of sandwich??",
    "Has anyone done anything fun recently???", "What should we write our next song about?",
    "Just a friendly reminder that you are beautiful.", "What's your favorite kind of breakfast food?",
    "Gotta favorite sex position?? lolol", "What songs have you guys been listening to this week?",
    "What's everyone's favorite video game??", "Anyone able to get Warped Tour tickets this year??",
    "What do you guys think the next Warped Tour lineup will be??", "I bet the Warped Tour lineup is gonna suck next year",
    "Anyone got fun plans for the weekend???", "What does happiness mean to you?", "What inspires you???",
    "Taylor ham or pork roll??", "Favorite kind of cheese??", "Whatcha gettin into tonight??J"]

    JakeFacePunctuation = [":)", ":-D", ";-D", "XD", ";D", ":P", ";P"]

    JakeFacePunctuation2 = ['<3', '<33333', '<33', ";)", ":-)", ":*" ]

    FromJake = ["-Jake"]

    JakeSentence1 = random.choice(JakeSentence1)
    JakeSentence2 =   random.choice(JakeSentence2)
    JakeFacePunctuation =  random.choice(JakeFacePunctuation)
    FromJake = random.choice(FromJake)
    JakeFacePunctuation2 = random.choice(JakeFacePunctuation2)

    JakeTweet = JakeSentence1 + ' ' + JakeFacePunctuation + ' ' + JakeSentence2 + JakeFacePunctuation2 + ' ' + FromJake
    return JakeTweet

#BRAD - drums
# Brad became the drummer of Sex For Breakfast when he was taught by his longtime friend,
    # David (lead guitar), who "really just needed someone to play drums." Now, he can
    # officially call himself the best drummer in the band.
    # Brad wants fans to know that they should catch him in Sex For Breakfast while they can
    # before a real band discovers his talent and he tours with them

def genBradTweet():

    BradSentence1 = [ "I don't need a big drum kit. I can make a small kit sound huge." "Who thinks we need more drum solos??",
    "Who trynna take drum lessons from me???", "Come watch me play drums hungover today lol.", "I can do with one hand what most drummers need two for.",
    "Just wrote the sickest drum beat", "Yooo which cymbral brand trynna sponsor me??", "I don't play off time, guitarists just can't keep up with me lol.",
    "Yooo still looking for a cymbral brand to sponsor me. HMU.", "Heyooo still trynna book some drum lessons HMU.",
    "I wanna jam with a famous drummer to show them a thing or two lol.", "My sticks only last like one or two songs lol. I'm a beast.",
    "Who trynna give me a drum stick sponsorship??", "I don't play out of time, you just don't understand what I'm doing lol.",
    "I'm off tempo? Nah you're metronome is off tempo lmfoa.", "I'm not gonna play louder cause the sound engineer just has shit mics lol.",
    "My drums are tuned perfectly, not my fault you have bad taste lmfao.", "Who trynna take drum lessons DM me for rates lol."]

    FromBrad = [ "-Brad" ]

    BradSentence1 = random.choice(BradSentence1)
    FromBrad = random.choice(FromBrad)

    BradTweet = BradSentence1 + " " + FromBrad
    return BradTweet

# ___________________________________________________________________________________________________________

# GIG PROMOTION TWEETS
def genPromoTweet():

    Greeting = ["Hey guys", "What's good", "Heyooo", "Yo", "Heyyy", "What's guuuudd", "Hey hey hey", "Yo yo", "Sup homies"]
    #
    Posessives = ["We got", "We have", "Tonight we got", "Tomorrow we have", "There's", "Tomorrow we got"]
    #
    Gig = ["a gig at", "a show at", "one banger of a show at", "a sick lineup at", "a sweeeeet gig at", "a sweet show at",
    "a killer line up at", "a sick show at", "a killerrr gig at", "a fuggin banger at"]

    Location = ["the B'nai Israel Synagogue", "the Denny's parking lot in Westwood", "the Jefferson Township Rec Center Battle of the Bands",
    "the Oakland Farmer's market", "Henry's Hot Dog Joint", "IHOP's Half-Off Senior Sunday Special", "the Jefferson High School Class of '09 Alumni Weekend",
    "Patrick's Pork House", "Daddy Matty's Barbeque", "the Ridgewood High Battle of the Bands", "Murph's Irish Pub", "Bob and Barbara's Burger Palace",
    "Steve's Mom's basement", "Jeff's garage", "Mulligan's Ale and Mead House", "Becky's Biscut Joint", "Harry's Bowl'n'Beer",
    "The Dingo's Den", "The Outhouse Bar", "Tyler's parents' shore house","the Taco Bell in Paterson", "Jimmy's Clam Bar",
    "Rob's Place", "Ted's Tuscan BBQ", "The Inner Eye Smoke Shop", "The Vape Palace off Rout 80", "Biggie's Burgers", "the Hooters parking lot",
    "Gus's Hoagie Shop", "The Metuchen Garlic Festival", "The Trenton Vape Fest", "the Camden Skate Park"]

    Command = ["Come haaaaang", "Come chill with us", "Hear some sick tunes", "Rock out with us", "Hear our new shit",
    "Come hang out", "Come hang out with us", "Come hang and smoke a doobster after", "Let's rock outtttt",
    "Come party with ussss", "Come party and have a good time", "Guuuuud timesss", "Hear those siiccckkkk tunesss"]

    GigEndingPunctuation = ["!!", "!", ".", "!11!!1!", "1!!1!", "!!!", ".", "!!!"]


    Greeting = random.choice(Greeting)
    Posessives = random.choice(Posessives)
    Gig = random.choice(Gig)
    Location = random.choice(Location)
    Command = random.choice(Command)
    GigEndingPunctuation = random.choice(GigEndingPunctuation)


    PromoTweet = Greeting + GigEndingPunctuation + ' ' + Posessives + ' ' + Gig + ' ' + Location +  GigEndingPunctuation + ' ' + Command + GigEndingPunctuation
    return PromoTweet

# ___________________________________________________________________________________________________________
# LYRIC SHARING
# Below will generate random song lyrics 'written' by Sex For Breakfast to share with their fans.
# Topics will include
    #Relationships, cheating, breakups/ex-girlfriends
    #Sex
    #Escaping their town/living situation
    #Self-hatred
    #Hate/anger/angst towards society, parents, school the law etc.

def genLyricTweet():

    Lyric1 = ["I'm breaking down", "I can't think I can't breathe", "I'm born to lose", "I'm stuck in hell",
    "God Must hate me", "You cursed me for eternity", "I hate you", "I can't be saved", "You can't save me",
    "I can't go back home", "Worst day ever", "I feel like the summer is leaving again", "She was a punk queen",
    "I used to love her", "Fuck you", "Fuck me", "Fuck everything", "What's the point", "Tomorrow won't be better",
    "It never gets better", "I am worthless", "Summer plans are gone forever", "I'm just a guy", "I'm just a kid",
    "I don't got a lotta friends", "She was hot but her sister was hotter", "She was a total MILF",
    "Hangin' with my friends","No one can bring us down", "It's not fair", "It's just not fair",
    "You don't know me", "Everything inside me is dead", "Everything is dead", "I'm gonna die", "We're all gonna die",
    "What's the point", "She never loved me", "You never fucking loved me","I'm better without you, girl",
    "I can't live without you, girl", "It started in the summer", "Everyday is the worst day ever",
    "I know it's not fair", "Fuck society", "Society is dead", "The government sucks", "Politics",
    "My life is a nightmare","One day I'll get the hell outta here", "There's no such thing as love",
    "She just keeps spoutin' bullshit", "I'm the misfit everyone hates","These posers just don't understand",
    "Dress me up in what you want me to be", "How could this happen to me", "Sorry I can't be perfect",
    "Sorry I can't be like him", "She's the devil", "Is she the one? Is she forever?", "She fucked my best friend",
    "Started seeing red", "Eyes glued to my stupid fucking phone", "I've got a headache right behind my eyes",
    "Pass me the blunt", "Gimme the joint", "I am rotten inside and out", "I'd rather keep my head down than have a conversation",
    "Hey, Whats that sound?", "I'm Indecisively Indifferent", "Oh here we go again", "Pain isn't something you move on from",
    "Been counted out so many times I lost count"]

    Lyric2 = ["She's got me under her spell again", "You'll see the fire she creates", "Sink into the pit",
    "I already know I'm a fucking disgrace", "Grind my teeth just thinking about you", "I can't be saved",
    "There's no hope for me", "You're just a stranger now", "She's just a stranger now", "I can't escape my body",
    "I'm doing fine without you", "Addicted to your moves", "I'm a sucker for you", "Toying with my head",
    "I'm regretting every word I said", "These pills don't do the trick", "Thought I could make you stay",
    "Shouting the loudest to drown out insanity", "The eyes of the world watch us riot", "Don't hate me",
    "Let's not lose our fucking minds", "Everyone sucks", "There's madness in my mind", "Can't take the pain anymore",
    "Need another drink", "Shouting the loudest to drown out sanity", "Sensory overload", "I just need a break from the world outside my door",
    "I'm not in a good frame of mind", "Shoot up til I'm blind", "It's a trap set up to kill", "I don't wanna be that guy",
    "Not again with all the self-hatred", "Anyone that ever played me", "I tell the truth as I need", "I'm drunk on revenge"]

    Lyric3 = ["And I can't live", "I can't breathe", "And I can't escape", "I can't wake up", "I can't forget about you",
    "I don't wanna forget about her", "She was my fucking life", "But her body drives me crazy",
    "So welcome to my fucked up world","Gonna start diggin my grave", "We're all just a bunch of mannequins",
    "Why can't I just be me?", "Can't trust no one", "And we're all just dying", "And the politicians are rotten",
    "I wear my heart out on my sleave", "So sorry Mom and Dad", "I'm leaving this godforesaken town",
    "The world doesn't understand our struggle, girl", "And we're all alone","Gonna put myself 6 feet under",
    "I'm not okay", "You could cure me", "You are my weakness", "I'm not over you","And I'm over you",
    "I'm gonna build a wall in my narcissistic mind", "I'm not comin back your way no more",
    "The system is broken","Bent over backwards for her again", "If I were you I'd run while you still can",
    "She's the girl of my wet dreams", "And it's really bumming me out", "Cut all the ties to separate you from me",
    "Been warned that you're bad news", "Can you say you feel the same?", "You're just another girl that I built up to burn down",
    "You're worth leaving behind", "She's queen of the open ended", "Did everything mean nothing at all?",
    "All I'm asking for is love", "Woah, woah, Woah", "Yeah, yeah, yeah", "Gotta fill the emptiness inside",
    "We're all fucked now", "Oh my god I can't believe you exist", "And I'm just counting down the seconds til the end",
    "All I've ever done is fuck shit up and creep out all my friends"]

    Lyric1 = random.choice(Lyric1)
    Lyric2 = random.choice(Lyric2)
    Lyric3 = random.choice(Lyric3)

    LyricTweet = "\"" + Lyric1 + "\n" + Lyric2 + "\n" + Lyric3 + "\""
    return LyricTweet

# ___________________________________________________________________________________________________________

tweetType =  random.randint(0,2)
tweet = ""
chooseDude =  random.randint(3,6)


# if the tweetType is 0, it will generate a lyric
if tweetType == 0:
    tweet = genLyricTweet();

# if the tweetType is 1, it will generate a personal tweet
elif tweetType == 1:


    # if the chooseDude is 3, it will generate a David tweet
    if chooseDude == 3:
        tweet = genDavidTweet();

        # if the chooseDude is 4, it will generate a Brad tweet
    elif chooseDude == 4:
            tweet = genBradTweet();

        #if the chooseDude is 5, we will generate a Jake tweet
    elif chooseDude == 5:
            tweet = genJakeTweet();

        # if the chooseDude is 6, we will generate a Jake tweet
    elif chooseDude == 6:
            tweet = genTylerTweet();

    # if the tweetType is two, we will generate a promotional tweet
elif tweetType == 2:
        tweet = genPromoTweet();
print(tweet)


consumer_key = 'PzSJlEwaYFMPAJsAmSLQyuBDb'
consumer_secret = 'uUkrHJyNh39lFh38YGw598IH0aZ3vGxgc0r61nlDLffTr1QSZU'
access_token_key = '1128739908569522177-jVS8HROI8VhionAh5ZOTdYe7qzccBa'
access_token_secret = 'GDD2HHOCp1Zt5SMSBHqfEvZJtb35PapFyl4ylXUxU45A2'

with open('Tweets.txt', 'a') as f:
	f.write(tweet + '\n')

api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)

print('posting tweet...')
try:
    status = api.PostUpdate(tweet)
    print('- success!')
except twitter.TwitterError, e:
    print('- error posting!')
    print(e)
