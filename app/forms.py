from django.forms import ModelForm

from app.models import Poll


class CreatePoll(ModelForm):
    class Meta:
        model = Poll
        exclude = ['option1_count', 'option2_count', 'option3_count']