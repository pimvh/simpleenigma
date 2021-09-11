#!/usr/bin/env python3
from collections import OrderedDict
import copy
from typing import Text
import string
import time 

from parts import Wheel, StaticWheel

class Enigma():
    def __init__(self, wheels : list[Wheel]):        
        self.wheels = wheels


    def get_state(self) -> list[OrderedDict]:
        return [wheel.dump_settings() for wheel in self.wheels]
    

    def set_state(self, settings) -> None:
        for wheel, setting in zip(self.wheels, settings):
            wheel.set_settings(setting)


    def encode(self, text_to_encode : Text) -> Text:
        print('encoding text...')

        result = ''        

        char_map = {' ' : 'x',
                    '?' : 'qq',
                    '.' : 'dot',
                    '/' : 'slash',
                    ',' : 'comma',}

        for c, char in enumerate(text_to_encode):
            
            if c % 4 == 0 and not c == 0:
                result += ' '

            if char in char_map:
                chars = char_map.get(char, '')
                
                for ch in chars:
                    result += self.encode_character(ch)
                continue

            char = char.lower()

            if not char in string.ascii_lowercase:
                continue
            
            result += self.encode_character(char)

        return result        
    
    def decode(self, text_to_decode : Text) -> Text:
        print('decoding text...')  

        result = ''

        for c, char in enumerate(text_to_decode.replace(' ', '')):
            result += self.decode_character(char)

        return result


    def encode_character(self, char : str):
        ''' parse a single character '''

        turn_next = True

        for i, current_wheel in enumerate(self.wheels):

            if turn_next:
                # print(f'wheel {i} turned')
                turn_next = current_wheel.turn()
                
            char = current_wheel.get_encoded_char(char)
        
        return char
    
    def decode_character(self, char : str):
        ''' parse a single character '''

        turn_next = True

        for i, current_wheel in enumerate(self.wheels):

            if turn_next:
                # print(f'wheel {i} turned')
                turn_next = current_wheel.turn()
                
        for i, current_wheel in enumerate(reversed(self.wheels)):
            char = current_wheel.get_decoded_char(char)
    
        return char

    def show_settings(self):
        pass

def main() -> None:

    wheels = []

    for i in range(10):
        wheels.append(Wheel())

    decoder_wheels = [copy.deepcopy(x) for x in wheels]    

    enigma = Enigma(wheels)
    enigma_decoder = Enigma(decoder_wheels)

    # plaintext = 'test'
    plaintext = '''I've tried my hand a simple Enigma encoder/decoder. I think it works.'''
    print(f'{plaintext=}')

    encoded = enigma.encode(plaintext)
    print(f'{encoded=}')

    decoded = enigma_decoder.decode(encoded)

    print(f'{decoded=}')
    

if __name__ == "__main__":
    main()

