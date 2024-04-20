from marshmallow import EXCLUDE, post_load, Schema, fields
from core.libs.helpers import GeneralObject


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(required=True, allow_none=False)
    username = fields.String(allow_none=False)
    email = fields.String(allow_none=False)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return GeneralObject(**data_dict)