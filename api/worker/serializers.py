from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=(
            '__all__'
            )



class RegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('phone', 'password','first_name','second_name','is_admin','image','id_no','id_img','driving_license_img'
		,'work_license_israel','work_license_type','work_license_expire','imageTest','age','address','pay_per_day'
		,'email')
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	
	def create(self, validated_data):
		user = User.objects.create(
			phone=validated_data['phone'],
			first_name=validated_data['first_name'],
			second_name=validated_data['second_name'],
			image=validated_data['image'],
        	is_admin=validated_data['is_admin'],
			id_no=validated_data['id_no'],
			id_img=validated_data['id_img'],
			driving_license_img=validated_data['driving_license_img'],
			work_license_israel=validated_data['work_license_israel'],
			work_license_type=validated_data['work_license_type'],
			work_license_expire=validated_data['work_license_expire'],
			address=validated_data['address'],
			pay_per_day=validated_data['pay_per_day'],
			email=validated_data['email'],
			age=validated_data['age'],
		)
        
		user.set_password(validated_data['password'])
		user.save()

		return user

	def update(self, instance, validated_data):
		instance.phone = validated_data.get('phone', instance.phone)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.image = validated_data.get('image', instance.image)
		instance.second_name = validated_data.get('second_name', instance.second_name)
		instance.is_admin = validated_data.get('is_admin', instance.is_admin)
		instance.id_no = validated_data.get('id_no', instance.id_no)
		instance.id_img = validated_data.get('id_img', instance.id_img)
		instance.driving_license_img = validated_data.get('driving_license_img', instance.driving_license_img)
		instance.work_license_israel = validated_data.get('work_license_israel', instance.work_license_israel)
		instance.work_license_type = validated_data.get('work_license_type', instance.work_license_type)
		instance.address = validated_data.get('address', instance.address)
		instance.pay_per_day = validated_data.get('pay_per_day', instance.work_license_expire)
		instance.email = validated_data.get('email', instance.email)
		instance.age = validated_data.get('age', instance.age)
		if 'password' in validated_data:
			instance.set_password(validated_data['password'])
		instance.save()
		return instance



class LogoutSerializer(serializers.ModelSerializer):
	model = User
	fields=(
            'first_name','second_name','phone','image',
            )

