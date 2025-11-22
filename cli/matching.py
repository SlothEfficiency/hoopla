from functools import reduce

def is_it_a_match(key_words: list, contents: list) -> bool:
    for key_word in key_words:
        for content_piece in contents:
            if key_word in content_piece:
                return True
            
    return False