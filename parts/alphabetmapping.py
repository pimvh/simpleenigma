from collections import OrderedDict
import random
import string

class AlphabetMapping():
    ''' implements a mapping of the alphabet for one letter to another '''

    def __init__(self) -> None:
        
        input_alpabet = [x for x in string.ascii_lowercase]
        random.shuffle(input_alpabet)
        output_alphabet = [x for x in string.ascii_lowercase]
        random.shuffle(output_alphabet)

        self.mapping : OrderedDict = OrderedDict()
        self.reverse_mapping : OrderedDict = OrderedDict()

        for key, value in zip(input_alpabet, output_alphabet):
            self.mapping.update({key : value})
            self.reverse_mapping.update({value : key})

        encoded = self.mapping.get('a')
        decoded = self.reverse_mapping.get(encoded)
        assert decoded == 'a'

    def show(self) -> None:
        ''' display the alphabet mapping of this wheel '''
        print(self)

    def __str__(self) -> str:
        out = ''
        for key, value in self.mapping.items():
            out += str(key) + ' --> ' + str(value) + '\n'
        
        return out