from django import forms
from django.forms import ModelForm,widgets
from .models import Apply_for_job,Register,Job_det
        
        
class ApplyNowForm(forms.ModelForm):
    error_css_class='error-field'
    required_css_class='required-field'    
    class Meta:
        model=Apply_for_job
      
        fields=['name','email','sclass','year','company_name','class10clgname','class10per','class12clgname','class12per','job_post','resume']
        #label={'class10clgname':'High School Name(10)','class10per':'Percentage','class12clgname':'Senior Secondry School Name(12)','class12per':'Percentage','resume':'Resume'}
    
    
class RegisterForm_ApplyForJob(forms.ModelForm):
    error_css_class='error-field'
    required_css_class='required-field'
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','readonly':'readonly'}))
    #pno=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),label='Phone No')
    sclass=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),label='Class')
    year=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}))
    #date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','readonly':'readonly'}),label='Date')
    class Meta:
        model = Apply_for_job
        fields = ['name','email','sclass','year']
    
class RegisterForm(forms.ModelForm):
    error_css_class='error-field'
    required_css_class='required-field'
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    pno=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sclass=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    year=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Register
        fields = ['name','email','pno','sclass','year']
        
class AddStudentForm(forms.ModelForm):
    error_css_class='error-field'
    required_css_class='required-field'
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    pno=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sclass=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    year=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','id':'datepicker'}))
    class Meta:
        model = Register
        fields = ['name','email','pno','sclass','year','date']
        
class JobDetForm(forms.ModelForm):
    error_css_class='error-field'
    required_css_class='required-field'
    company_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Company_email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    job_post=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    vacancy=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    salary=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_date_toapply=forms.CharField(widget=forms.DateInput(attrs={'class':'form-control','id':'datepicker'}))
    class Meta:
        model = Job_det
        fields = ['company_name','Company_email','job_post','vacancy','salary','location','last_date_toapply']