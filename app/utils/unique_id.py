'''
Module:         unique_id.py
Description:    Defines the `UniqueId` class that generates and stores UUID
Author:         Charles Morman
'''


from uuid import uuid4


class UniqueId:
    '''Responsible for generating and storing UUID upon construction'''

    def __init__(self):
        self.id_value = self.generate_id()

    def generate_id(self):
        '''
        Use `uuid4` to generate a unique id; separate func for later updates
        if needed
        '''
        return str(uuid4())

    def __str__(self):
        return str(self.id_value)
