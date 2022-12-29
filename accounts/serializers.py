from rest_framework import serializers 
from accounts.models import CustomUser



class StaffsignupSerializer(serializers.ModelSerializer):
	# track=TrackSerializer(many=True)
	class Meta:
		fields=['email', 'first_name', 'last_name','password']
		model=CustomUser
		extra_kwargs={'is_instructor':{'read_only':True},'is_staff':{'read_only':True},'password':{'write_only':True}}

	def create(self, validated_data):
		user=CustomUser(
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],

			)
		user.set_password(validated_data['password'])

		user.save()
		return user

class LoginSerializer(serializers.Serializer):
	email=serializers.EmailField(max_length=30, min_length=5, allow_blank=False)
	password=serializers.CharField(max_length=30, min_length=5, allow_blank=False, trim_whitespace=True)