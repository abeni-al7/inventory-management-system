from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)
        if request and request.method != 'POST':
            fields.pop('password', None)
        return fields
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
