from core.apis.teachers.schema import UserSchema
from core.libs.helpers import GeneralObject

def test_user_schema_load():
    input_data = {
        'id': 1,
        'username': 'testuser',
        'email': 'testuser@example.com'
    }
    expected = GeneralObject(id=1, username='testuser', email='testuser@example.com')
    result = UserSchema().load(input_data)

    assert isinstance(result, GeneralObject)
    assert result.id == expected.id
    assert result.username == expected.username
    assert result.email == expected.email
