'''Tests the app/utils/unique_id.py module'''

from app.utils.unique_id import UniqueId

def test_unique_id_construction():
    '''Generates multiple UUID obj and test if unique'''
    
    uuid_0 = UniqueId()
    uuid_1 = UniqueId()
    uuid_2 = UniqueId()
    uuid_3 = UniqueId()
    uuid_4 = UniqueId()
    
    assert uuid_0 != uuid_1 != uuid_2 != uuid_3 != uuid4