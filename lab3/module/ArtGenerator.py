import art

class ArtGenerator:
    default_font = 'xcourb'
    @staticmethod
    def text_to_art(text, font=default_font):
        return art.text2art(text, font)
    
    @staticmethod
    def get_fonts():
        return art.font_list()
        