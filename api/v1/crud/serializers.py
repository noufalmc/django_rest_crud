from rest_framework import serializers

from crud.models import BloodData


class BloodDataSerializer(serializers.ModelSerializer):
    blood_group_name = serializers.ModelSerializer(read_only=True, required=False)

    class Meta:
        model = BloodData
        fields = ('id', 'first_name', 'last_name', 'blood_group_name', 'blood_group',
                  'mobile_number', 'address', 'created_at', 'profile_pic', 'willing_to_donate',
                  'updated_at', 'is_deleted')

    def get_blood_group_name(self, instance):
        if instance:
            return instance.blood_group.blood_group
        else:
            return ""
