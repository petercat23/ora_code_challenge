from rest_framework import serializers


class SessionsTypeSerializer(serializers.Serializer):

    type = serializers.CharField(required=True)

    def validate_type(self, value):
        if value != "sessions":
            raise serializers.ValidationError("Request `type` of `sessions`")
        return value


class DataSerializer(serializers.Serializer):

    data = SessionsTypeSerializer(required=True)


class SessionsSerializer(serializers.Serializer):

    pass
