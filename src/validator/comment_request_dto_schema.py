from marshmallow import Schema, fields, validates, ValidationError

class CommentRequestDtoSchema(Schema):
    postId = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    body = fields.Str(required=True)

    @validates('postId')
    def validate_postId(self, value):
        if value <= 0:
            raise ValidationError('PostId must be a positive integer.')

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise ValidationError('Name cannot be empty or null.')

    @validates('email')
    def validate_email(self, value):
        if not value:
            raise ValidationError('Email cannot be empty or null.')

    @validates('body')
    def validate_body(self, value):
        if not value:
            raise ValidationError('Body cannot be empty or null.')

schema = CommentRequestDtoSchema()
data = {
    "postId": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "body": "This is a comment."
}

try:
    result = schema.load(data)
    print("Comment request is valid:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)
