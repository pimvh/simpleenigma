#!/usr/bin/env python3
from collections import OrderedDict
import copy
from typing import Text
import string
import time 

from parts import Rotor, StaticRotor, StekkerBrett

class Enigma():
    def __init__(self, rotors : list[Rotor], stekkerbret : StekkerBrett):        
        self.rotors = rotors
        self.stekkerbret = stekkerbret


    def get_state(self) -> list[OrderedDict]:
        return [rotor.dump_settings() for rotor in self.rotors]
    

    def set_state(self, settings) -> None:
        for rotor, setting in zip(self.rotors, settings):
            rotor.set_settings(setting)


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

        for i, current_rotor in enumerate(self.rotors):

            if turn_next:
                # print(f'rotor {i} turned')
                turn_next = current_rotor.turn()
                
            char = current_rotor.get_encoded_char(char)
        
        char = self.stekkerbret.get_encoded_char(char)

        return char
    
    def decode_character(self, char : str):
        ''' parse a single character '''

        char = self.stekkerbret.get_decoded_char(char)

        turn_next = True

        for i, current_rotor in enumerate(self.rotors):

            if turn_next:
                # print(f'rotor {i} turned')
                turn_next = current_rotor.turn()
                
        for i, current_rotor in enumerate(reversed(self.rotors)):
            char = current_rotor.get_decoded_char(char)
    
        return char

    def show_settings(self):
        pass

def main() -> None:

    rotors = []
    stekkerbrett = StekkerBrett()

    for i in range(10):
        rotors.append(Rotor())

    print(rotors[0])

    rotors.append(StaticRotor())

    decoder_rotors = [copy.deepcopy(x) for x in rotors]    
    decoder_stekkerbrett = copy.deepcopy(stekkerbrett)

    enigma = Enigma(rotors, stekkerbrett)
    enigma_decoder = Enigma(decoder_rotors, decoder_stekkerbrett)

    plaintext = '''Hoi dit is enigma'''
    print(f'{plaintext=}')

    encoded = enigma.encode(plaintext)
    print(f'{encoded=}')

    decoded = enigma_decoder.decode(encoded)

    print(f'{decoded=}')
    

if __name__ == "__main__":
    main()

