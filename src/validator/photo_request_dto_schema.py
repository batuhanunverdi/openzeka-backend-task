from marshmallow import Schema, fields, validates, ValidationError

class PhotoRequestDtoSchema(Schema):
    title = fields.Str(required=True)
    url = fields.Str(required=True)
    thumbnailUrl = fields.Str(required=True)
    albumId = fields.Int(required=True)

    @validates('title')
    def validate_title(self, value):
        if not value:
            raise ValidationError('Title cannot be empty or null.')

    @validates('url')
    def validate_url(self, value):
        if not value:
            raise ValidationError('URL cannot be empty or null.')

    @validates('thumbnailUrl')
    def validate_thumbnailUrl(self, value):
        if not value:
            raise ValidationError('Thumbnail URL cannot be empty or null.')

    @validates('albumId')
    def validate_albumId(self, value):
        if value <= 0:
            raise ValidationError('AlbumId must be a positive integer.')

schema = PhotoRequestDtoSchema()
data = {
    "title": "Sample Photo",
    "url": "http://example.com/photo.jpg",
    "thumbnailUrl": "http://example.com/thumbnail.jpg",
    "albumId": 1
}

try:
    result = schema.load(data)
    print("Photo request is valid:", result)
except ValidationError as err:
    print("Validation errors:", err.messages)
