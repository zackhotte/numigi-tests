import pytest
import requests
from bs4 import BeautifulSoup

from numigi_tests import ninety_nine_bottles_of_beer, generate_lyrics


def get_song_lyrics():
    res = requests.get("http://www.99-bottles-of-beer.net/lyrics.html")
    soup = BeautifulSoup(res.text, "html.parser")
    lyrics = soup.find(id="main").find_all("p")
    return ''.join([parse_lyrics(line) for line in lyrics])


def parse_lyrics(line):
    line = line.text.split('.')
    return line[0].strip() + '.\n' + line[1].strip() + '.\n'


def test_lyric_generator_when_beer_is_one():
    lyric = "1 bottle of beer on the wall, 1 bottle of beer.\n" \
            "Take one down and pass it around, no more bottles of beer on the wall.\n"
    assert lyric == generate_lyrics(1)


def test_lyric_generator_when_beer_is_more_than_one():
    lyric = "11 bottles of beer on the wall, 11 bottles of beer.\n" \
            "Take one down and pass it around, 10 bottles of beer on the wall.\n"
    assert lyric == generate_lyrics(11)


def test_lyric_generator_throws_error_when_less_than_zero():
    with pytest.raises(ValueError):
        generate_lyrics(-5)


def test_that_lyrics_match():
    expected = get_song_lyrics().split("\n")
    actual = ninety_nine_bottles_of_beer().split("\n")
    for idx, line in enumerate(actual):
        assert expected[idx] == line
