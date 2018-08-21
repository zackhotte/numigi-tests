def ninety_nine_bottles_of_beer():
    return ''.join([generate_lyrics(i) for i in reversed(range(100))])


def generate_lyrics(num):
    if type(num) != int:
        raise TypeError("Parameter must be of type 'int'. You entered " + num + " of type " + type(num))

    lyrics = "{} {} of beer on the wall, {} {} of beer.\n" \
             "Take one down and pass it around, {} {} of beer on the wall.\n"
    singular = "bottle"
    plural = "bottles"

    if num > 1:
        if (num - 1) == 1:
            return lyrics.format(num, plural, num, plural, num - 1, singular)
        else:
            return lyrics.format(num, plural, num, plural, num - 1, plural)

    if num == 1:
        return lyrics.format(1, singular, 1, singular, "no more", plural)

    if num == 0:
        # No more beers, return the last two sentences of the song
        return "No more bottles of beer on the wall, no more bottles of beer.\n" \
               "Go to the store and buy some more, 99 bottles of beer on the wall."

    if num < 0:
        raise ValueError("You cannot have less than 0 beers, even having 0 is not enough beer")
