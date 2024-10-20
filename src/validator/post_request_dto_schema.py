from marshmallow import Schema, fields, validates, ValidationError

class PostRequestDtoSchema(Schema):
    userId = fields.Int(required=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)

    @validates('title')
    def validate_title(self, value):
        if not value:
            raise ValidationError('Title cannot be empty or null.')

    @validates('body')
    def validate_body(self, value):
        if not value:
            raise ValidationError('Body cannot be empty or null.')

    @validates('userId')
    def validate_userId(self, value):
        if value <= 0:
            raise ValidationError('UserId must be a positive integer.')

schema = PostRequestDtoSchema()
data = {
    "userId": 1,
    "title": "Sample Post Title",
    "body": "This is the body of the post."
}

try:
    result = schema.load(data)
    print("Post request is valid:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)
