from marshmallow import Schema, fields, validates, ValidationError

class TodoRequestDtoSchema(Schema):
    title = fields.Str(required=True)
    completed = fields.Bool(required=True)
    userId = fields.Int(required=True)

    @validates('title')
    def validate_title(self, value):
        if not value:
            raise ValidationError('Title cannot be empty or null.')

    @validates('userId')
    def validate_userId(self, value):
        if value <= 0:
            raise ValidationError('UserId must be a positive integer.')

schema = TodoRequestDtoSchema()
data = {
    "title": "Finish homework",
    "completed": False,
    "userId": 1
}

try:
    result = schema.load(data)
    print("Todo request is valid:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)
