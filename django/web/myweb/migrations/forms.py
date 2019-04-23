from django import forms
from django.contrib.auth import authenticate


 class UserLoginForm(forms.Form):
     username = forms.CharField()
     password = forms.CharField(widget=forms.PasswordInput)

     def clean(self,args,*kwargs):
    username=self.cleaned_data.get('username')
    password=self.cleaned_data.get('password')


    if username and password:

        user= authenticate(username=username, password=password)
        if not user:
            raise forms.validationError('Sorry user does not exist')
        if not user.check_password(password):
            raise forms.validationError('Check Password, it is not correct')
        if not user.is_active:
            raise forms.validationError('This user is not active')
        return super(UserLoginForm,self).clean(args,*kwargs)


class UserRegisterForm(forms.ModelForm):
  email = forms.EmailField(label='Email Adderess')
  email2 = forms.EmailField(label='Confirm email')
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
      model = User
      fields = [
          'username',
          'email'
          'email2'
          'password'
          ]

      def clean_email(self):
          email = self.cleaned_data.get('email')
          email2 = self.cleaned_data.get('email2')
          if email is email2:
              raise forms.ValidationError('emails not match')
          email_qs = User.objects.filter(email=email1)
          if email_qs.exits():
              raise forms.ValidationError(
                  "This email is alredy being used"
              )
          return email


