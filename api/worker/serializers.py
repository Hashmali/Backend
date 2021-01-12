from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            'first_name','second_name','phone','image','id'
            )



class RegistrationSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ('phone', 'password', 'password2','first_name','second_name','is_admin','image')
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
           	 raise serializers.ValidationError({"password": "Password fields didn't match."})

		return attrs

	def create(self, validated_data):
		user = User.objects.create(
			phone=validated_data['phone'],
			image=validated_data['image'],
			first_name=validated_data['first_name'],
			second_name=validated_data['second_name'],
        	is_admin=validated_data['is_admin']
		)
        
		user.set_password(validated_data['password'])
		user.save()

		return user




class LogoutSerializer(serializers.ModelSerializer):
	model = User
	fields=(
            'first_name','second_name','phone','image',
            )

