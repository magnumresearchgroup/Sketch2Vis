import random
from random import randint
from english_words import english_words_set

class RandomDataGenerator():
    def __init__(self):
        pass

    def get_random_string(self, length=4,

                          ):
        return ' '.join(random.sample(english_words_set, length) )

    def get_int(self, low, high):
        return randint(low, high)

    def get_int_list(self, length, low=0, high=100):
        return [randint(low, high) for _ in range(length)]

    def get_choice(self, l):
        return random.choice(l)

    def get_random_string_list(self, list_length, word_length=4):
        return [self.get_random_string(length=word_length) for _ in range(list_length)]

    def get_random_hd_font(self):
        fonts_list = [
         'Indie Flower',
         'Dancing Script',
         'Pacifico',
         'Shadows Into Light',
         'Amatic SC',
         'Caveat',
         'Permanent Marker',
         'Courgette',
         'Satisfy',
         'Great Vibes',
         'Kalam',
         'Kaushan Script',
         'Sacramento',
         'Cookie',
         'Gloria Hallelujah',
         'Damion',
         'Patrick Hand',
         'Handlee',
         'Humor Sans'
        ]
        return random.choice(fonts_list)