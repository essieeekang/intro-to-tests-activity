from main import count_a_letter
import pytest

# def test_demo_one():
#     num_1 = 8
#     num_2 = 9

#     result = num_1 + num_2

#     assert result == 17

# def test_demo_two():
#     num_1 = 18
#     num_2 = 24

#     result = num_1 + num_2

#     assert result == 42
# Delete the demo tests and add your tests here 

def test_hello_world_o_count():
    sentence = "Hello World!"
    letter = "o"

    result = count_a_letter(sentence,letter)
    assert result == 2

def test_hello_world_z_count():
    sentence = "Hello World!"
    letter = "z"

    result = count_a_letter(sentence,letter)
    assert result == 0

def test_hello_world_F_count():
    sentence = "Hello World!"
    letter = "F"

    result = count_a_letter(sentence,letter)
    assert result == 0

def test_hello_world_special_char_count():
    sentence = "Hello World!"
    letter = "!"

    result = count_a_letter(sentence,letter)
    assert result == None

def test_hello_world_num_char_count():
    sentence = "Hello World!"
    letter = "123"

    result = count_a_letter(sentence,letter)
    assert result == None

def test_hello_world_h_count():
    sentence = "Hello World 2349857"
    letter = "h"

    result = count_a_letter(sentence,letter)
    assert result == 1

def test_hello_world_H_count():
    sentence = "Hello World 78273648"
    letter = "H"

    result = count_a_letter(sentence,letter)
    assert result == 1

def test_sentence_is_int():
    sentence = 123
    letter = "a"

    result = count_a_letter(sentence, letter)
    assert result == None