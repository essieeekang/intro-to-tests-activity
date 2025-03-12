def count_a_letter(sentence, letter):
    if not letter.isalpha():
        return None
    if not sentence or not isinstance(sentence, str):
        return None
    
    sentence = sentence.lower()
    letter = letter.lower()
    
    count = 0
    for char in sentence:
        if char == letter:
            count +=1
    
    return count