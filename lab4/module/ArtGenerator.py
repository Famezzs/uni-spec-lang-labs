from module.InputScanner import InputScanner

class ArtGenerator:
    def __init__(self, letters_and_art, elements_in_letter_array, default_symbol):
        self.letters_and_art = letters_and_art
        self.elements_in_letter_array = elements_in_letter_array
        self.default_symbol = default_symbol

    def __create_art_array(self):
        art_array = []
        for _ in range(self.elements_in_letter_array):
            art_array.append('')
        return art_array

    def __fill_in_art_array(self, art_array, text):
        for letter in text.lower():
            for i in range(self.elements_in_letter_array):
                art_array[i] += self.letters_and_art[letter][i] + ' '
        return art_array
    
    def __art_array_to_string(self, art_array):
        result = ''
        for i in range(self.elements_in_letter_array):
            result += art_array[i] + '\n'
        return result
    
    def __replace_character_in_art_string(self, art_string: str, character):
        if InputScanner.input_empty(character) == False and character != self.default_symbol:
            art_string = art_string.replace(self.default_symbol, character)
        return art_string

    def text_to_art(self, text, character = ''):
        art_array = self.__fill_in_art_array(self.__create_art_array(), text) 
        art_string = self.__art_array_to_string(art_array)
        return self.__replace_character_in_art_string(art_string, character)