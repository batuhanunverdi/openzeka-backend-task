from marshmallow import Schema, fields, validates, ValidationError

class AlbumRequestDtoSchema(Schema):
    userId = fields.Int(required=True)
    title = fields.Str(required=True)

    @validates('userId')
    def validate_userId(self, value):
        if value <= 0:
            raise ValidationError('UserId must be a positive integer.')

    @validates('title')
    def validate_title(self, value):
        if not value:
            raise ValidationError('Title cannot be empty or null.')

schema = AlbumRequestDtoSchema()
data = {
    "userId": 1,
    "title": "My Album"
}

try:
    result = schema.load(data)
    print("Album request is valid:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)
