from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields=('username','email','password1','password2')


    def __str__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.field['username'].label="Account ID"
        self.field['email'].label="Email Address"
