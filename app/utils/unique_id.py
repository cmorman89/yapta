'''
Module:         unique_id.py
Description:    Defines the `UniqueId` class that generates and stores UUID
Author:         Charles Morman
'''


from uuid import uuid4, UUID


class UniqueId:
    '''Responsible for generating and storing UUID upon construction'''

    def __init__(self):
        self.id_value = self.generate_id()

    @staticmethod
    def generate_id():
        '''
        Use `uuid4` to generate a unique id; separate func for later updates
        if needed
        '''
        return str(uuid4())

    def __str__(self):
        return self.id_value
