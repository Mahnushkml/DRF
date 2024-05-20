from rest_framework import serializers
from .models import Assets

class AssetsSerializer(serializers.ModelSerializer):
    """Serializes for assets"""

    class Meta:
        model = Assets
        fields = ('id', 'ip', 'management_category', 'network_category', 'group_user', 'group_owner', 'responsible_employee', 'physical_location', 'hostname','service', 'sub_service', 'access_type', 'device_type', 'device_model', 'os', 'unpatchable', 'ref_num', 'description', 'siem_log')
