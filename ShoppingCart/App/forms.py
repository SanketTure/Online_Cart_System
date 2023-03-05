from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import ProductModel,CustomerModel


class Register(UserCreationForm):
    password1 = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','password']
        
class AddProduct(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['title','desc','price','img']
        labels ={
            'title':'Enter Title',
            'desc':'Enter Description',
            'price':'Enter Price',
            'img':'Select Image',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'img':forms.FileInput(attrs={'class':'form-control'}),
        }
        
class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['name','phoneNo','address']
        labels ={
            'name':'Enter Name',
            'phoneNo':'Enter Phone Number',
            'address':'Enter address',   
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNo':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }