from collections import OrderedDict
from itertools import islice, cycle

from .alphabetmapping import AlphabetMapping


class Wheel(AlphabetMapping):
    """ defines a wheel of an enigma machine """
    def __init__(self) -> None:
        super().__init__()
        self.wheelsize = len(self.mapping)
        self.state = 0
        self.full_turns = 0
        self.shift = 1

        self.initial_state = next(iter(self.mapping))


    def get_encoded_char(self, key) -> str:
        return self.mapping.get(key)
    

    def get_decoded_char(self, key) -> str:
        return self.reverse_mapping.get(key)
    

    def get_initial_state(self) -> str:
        return self.initial_state


    def turn(self) -> bool:
        ''' turn the wheel 1 spot, return True when the wheel is fully turned '''
        self.state += self.shift

        self.mapping = OrderedDict(
            (k, v)
            for k, v in zip(self.mapping.keys(), islice(cycle(self.mapping.values()), 1, None))
        )

        self.reverse_mapping = OrderedDict((v, k) for k, v in self.mapping.items())

        encoded = self.mapping.get('a')
        # print(self.mapping.get('a'))
        decoded = self.reverse_mapping.get(encoded)
        # print(self.reverse_mapping.get('n'))
        assert decoded == 'a'

        if self.state > self.wheelsize:
            self.state = 0
            self.full_turns += 1
            return True
        
        return False
        

    def dump_settings(self):
        return self.mapping
    
    def set_settings(self, mapping):
        self.mapping = mapping


class StaticWheel(Wheel):
    """ defines a static wheel of an enigma machine """
    def __init__(self) -> None:
        super().__init__()
    
    def turn(self) -> bool:
        return False

    
