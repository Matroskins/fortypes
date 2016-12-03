import factory
from invite.models import Invite


class InviteFactory(factory.django.DjangoModelFactory):
    code = 'INVTCD'

    class Meta:
        model = Invite
