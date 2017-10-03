from django import forms
from django.contrib.auth import login,logout,get_user_model,authenticate

User = get_user_model()


class UserSignupForm(forms.ModelForm):
	repeat_email = forms.EmailField(label='Confirm email')
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','repeat_email','password']

	def clean_repeat_email(self):
		email = self.cleaned_data.get('email')
		repeat_email = self.cleaned_data.get('repeat_email')
		if email != repeat_email:
			raise forms.ValidationError('Your emails do not match.')
		email_exists = User.objects.filter(email=email)
		if email_exists:
			raise forms.ValidationError('This email address is already registered with another account')
		return email


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("The password entered is incorrect")
			if not user.is_active:
				raise forms.ValidationError("This user is not active")
		return super(UserLoginForm,self).clean(*args,**kwargs)


