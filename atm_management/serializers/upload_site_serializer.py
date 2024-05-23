from rest_framework import serializers


class SiteDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    site_id = serializers.CharField(allow_blank=False, allow_null=False)
    address_line_1 = serializers.CharField(default=None, allow_blank=True, allow_null=True)
    address_line_2 = serializers.CharField(default=None, allow_blank=True, allow_null=True)
    city = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    state = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    phone_number = serializers.CharField(default=None, allow_blank=True, allow_null=True)
    email = serializers.EmailField(default=None, allow_blank=True, allow_null=True)
    pincode = serializers.CharField(required=True)

    def validate_phone_number(self, ph):
        try:
            ph_str = str(int(ph.replace(".0", "")))
            if len(ph_str) == 10:
                return ph_str
            else:
                raise serializers.ValidationError(f"Incorrect Phone Number Format {ph}")
        except Exception as e:
            raise serializers.ValidationError(f"Incorrect Phone Number Format {ph}")

    def validate_pincode(self, pincode):
        try:
            pincode_str = str(int(pincode.replace(".0", "")))
            if len(pincode_str) == 6:
                return pincode_str
            else:
                raise serializers.ValidationError(f"Incorrect Pincode Format {pincode}")
        except Exception as e:
            raise serializers.ValidationError(f"Incorrect Pincode Format {pincode}")
        
    
    def validate_site_id(self, site_id):
        try:
            site_id_str = str(int(site_id.replace(".0", "")))
            if len(site_id_str) <= 12:
                return site_id_str
            else:
                raise serializers.ValidationError(f"Incorrect Pincode Format {site_id}")
        except Exception as e:
            raise serializers.ValidationError(f"Incorrect Pincode Format {site_id}")
