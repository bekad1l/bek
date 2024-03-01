#Python regex
import re

def match_a_followed_by_zero_or_more_b(text):
    pattern = r'ab*'
    return re.findall(pattern, text)

def match_a_followed_by_two_to_three_b(text):
    pattern = r'ab{2,3}'
    return re.findall(pattern, text)

def find_sequences_of_lowercase_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

def find_sequences_of_one_uppercase_followed_by_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

def match_a_followed_by_anything_ending_in_b(text):
    pattern = r'a.*?b$'
    return re.findall(pattern, text)

def replace_spaces_commas_dots_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

def snake_case_to_camel_case(text):
    words = text.split('_')
    return ''.join(word.capitalize() for word in words)

def split_string_at_uppercase_letters(text):
    pattern = r'[A-Z][a-z]*'
    return re.findall(pattern, text)

def insert_spaces_between_words_starting_with_capital_letters(text):
    pattern = r'([A-Z][a-z]+)'
    return re.sub(pattern, r' \1', text).strip()

def camel_case_to_snake_case(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return '_'.join(re.split(pattern, text)).lower()

# Test cases
test_string = "ab abbbb acbcab abc abcb aabbcc"
print("Matches for 'a' followed by zero or more 'b's:", match_a_followed_by_zero_or_more_b(test_string))
print("Matches for 'a' followed by two to three 'b's:", match_a_followed_by_two_to_three_b(test_string))
print("Sequences of lowercase letters joined with an underscore:", find_sequences_of_lowercase_with_underscore(test_string))
print("Sequences of one uppercase letter followed by lowercase letters:", find_sequences_of_one_uppercase_followed_by_lowercase(test_string))
print("Matches for 'a' followed by anything, ending in 'b':", match_a_followed_by_anything_ending_in_b(test_string))
print("After replacing spaces, commas, and dots with colons:", replace_spaces_commas_dots_with_colon(test_string))
print("Camel case to snake case:", snake_case_to_camel_case("snake_case_string"))
print("Splitting string at uppercase letters:", split_string_at_uppercase_letters("CamelCaseString"))
print("Inserting spaces between words starting with capital letters:", insert_spaces_between_words_starting_with_capital_letters("CamelCaseString"))
print("Camel case to snake case:", camel_case_to_snake_case("CamelCaseString"))
