import pytest
from unittest.mock import patch
from madlib.madlib import read_template, parse_template, merge, prompt, welcomeMessage

# @pytest.mark.skip("pending")
def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

# @pytest.mark.skip("pending")
def test_welcome_message():
    actual=welcomeMessage()
    expected= "welcom to us !!\nThe program prompts you to input words, and then generates a unique story by inserting these words into a pre-written tale.\nsimply!! run the program from the command line and follow the prompts. Have fun!"
    assert actual == expected

# @pytest.mark.skip("pending")
def test_prompt():
    with patch('builtins.input', side_effect=["majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"]):
        actual = prompt(("majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"))
    expected = (("majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"))
    assert actual == expected





# //////////////original_text_tests//////////////


# @pytest.mark.skip("pending")
def test_read_template_returns_stripped_string():
    actual = read_template("../assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template2():
    actual_stripped, actual_parts = parse_template(
        "Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."
    )
    expected_stripped = "Make Me A Video Game!\n\nI the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {}'s Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find."
    expected_parts = ("Adjective", "Adjective", "A First Name", "Past Tense Verb", "A First Name", "Adjective", "Adjective", "Plural Noun", "Large Animal", "Small Animal", "A Girl's Name", "Adjective", "Plural Noun" , "Adjective", "Plural Noun", "Number 1-50", "First Name", "Number", "Plural Noun", "Number", "Plural Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge2():
    actual = merge("Make Me A Video Game!\n\nI the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {}'s Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.", ("majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"))
    expected="Make Me A Video Game!\n\nI the majestic and purple Scott have colored JB's laughing sister and plan to steal her tickled arrows!\n\nWhat are a gorilla and backpacking butterfly to do? Before you can help Betty, you'll have to collect the silly tests and striped jackets that open up the 44 worlds connected to A Wilson's Lair. There are 3 leaves and 4 swords in the game, along with hundreds of other goodies for you to find."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)