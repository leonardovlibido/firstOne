print "You enter a dark room with two doors. Do you go through the door #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a chess piece. What do YOU do?"
    print "1. Take the chess piece."
    print "2. Play chess with the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear flips the chess table, and munches on your face."
    elif bear == "2":
        print "The bear is actually a chess grandmaster, he beats you, and you end up crying"
    else:
        print "You freeze, you little bitch."
elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powerd by a limb of a lamb."
    else:
        print "You crazy"

else:
    print """You made it, you are back to your old life, lucky you, it's back to the same old same old. This is all you wanted when you woke up in that cold dungeon, but somehow you now realize that you shall miss it's charm."""

