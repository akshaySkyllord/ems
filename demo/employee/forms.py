from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

        label = {
            'password': 'Password'

        }

    # def clean_email(self):
    #     if self.cleaned_data['email'].endsWith('@gmail.com'):
    #         return self.cleaned_data['email']
    #     else:
    #         raise ValidationError("Email is not valid")

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])
        # add() method append the groups
        u.set_password(password)
        u.save()
        return u


