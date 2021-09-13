from collections import OrderedDict
import itertools 
import random 
from .alphabetmapping import AlphabetMapping


class StekkerBrett(AlphabetMapping):

    def __init__(self):
        super().__init__()
        n_of_stekkers = random.randint(1, 9)

        self.mapping = OrderedDict(itertools.islice(self.mapping.items(), n_of_stekkers))
        self.reverse_mapping = OrderedDict(itertools.islice(self.reverse_mapping.items(), n_of_stekkers))
       
    def get_encoded_char(self, key) -> str:
        if not key in self.mapping:
            return key

        return self.mapping.get(key)
    

    def get_decoded_char(self, key) -> str:

        if not key in self.reverse_mapping:
            return key

        return self.reverse_mapping.get(key)
