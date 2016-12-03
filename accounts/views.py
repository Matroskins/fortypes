from django.db.transaction import atomic
from rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response

from invite.models import Invite
from invite.serializers import InviteCodeRegisterSerializer


class InviteCodeRegisterView(RegisterView):
    serializer_class = InviteCodeRegisterSerializer

    @atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        password = request.data.pop('password')[0]
        request.data['password1'] = password
        request.data['password2'] = password
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        invite = Invite.objects.get(code=request.data['invite_code'], used=False)
        invite.used = True
        invite.user_who_used = user
        invite.save()

        return Response(self.get_response_data(user), status=status.HTTP_201_CREATED, headers=headers)
