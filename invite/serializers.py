from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from invite.models import Invite


class InviteCodeRegisterSerializer(RegisterSerializer):
    invite_code = serializers.CharField(required=True)

    def validate_invite_code(self, invite_code):
        if Invite.objects.filter(code=invite_code, used=False).exists():
            return invite_code
        else:
            raise serializers.ValidationError("Wrong invite code")
