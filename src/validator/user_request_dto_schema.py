from marshmallow import Schema, fields, validates, ValidationError

class UserRequestDtoSchema(Schema):
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    address = fields.Dict(required=True)
    phone = fields.Str(required=True)
    website = fields.Str(required=True)
    company = fields.Dict(required=True)

    @validates('address')
    def validate_address(self, value):
        if not isinstance(value, dict) or not value:
            raise ValidationError('Address must be a non-empty dictionary.')

    @validates('company')
    def validate_company(self, value):
        if not isinstance(value, dict) or not value:
            raise ValidationError('Company must be a non-empty dictionary.')

schema = UserRequestDtoSchema()
data = {
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {"street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough", "zipcode": "92998-3874"},
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {"name": "Romaguera-Crona", "catchPhrase": "Multi-layered client-server neural-net", "bs": "harness real-time e-markets"}
}

try:
    result = schema.load(data)
    print("User request is valid:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)
