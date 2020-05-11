from django import forms


class registered(forms.Form):
    username = forms.CharField(
        label='Enter Your Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'mobile'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )


class login(forms.Form):
    username = forms.CharField(
        label='Enter Your Username/mobile',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username/mobile'
            }
        )
    )
    password = forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
