from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from datetime import datetime
from  home.models import Register,User
from  home.models import Job_det,Apply_for_job,ShortlistedCand
#from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,AddStudentForm,JobDetForm,ApplyNowForm,RegisterForm_ApplyForJob
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import datetime

# Create your views here.
def index(request):
    index=Job_det.objects.all()
    return render(request, 'index.html',{'index': index})

def about(request):
     return HttpResponse("this is abt page")

def services(request):
    return HttpResponse("this is service page")

def contact(request):
    return HttpResponse("this is contact page")

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        pno=request.POST.get('pno')
        sclass=request.POST.get('sclass')
        year=request.POST.get('year')
        passw=request.POST.get('passw')
        c_pass=request.POST.get('c_pass')
        
        
        
        if len(name)>30:
            messages.error(request,"Username must be greater than 30 characters")
            return redirect('register')
        if len(pno)==12:
            messages.error(request,"Phone number should be of 10 digits only")
            return redirect('register')
        # if len(name)>30:
        #     messages.error(request,"Username must be greater than 30 characters")
        #     return redirect('register')
        if not username.isalnum():
            messages.error(request,"Name must be alpha numeric")
            return redirect('register')
        if passw!=c_pass:
            messages.error(request,"Passwords do not match")
            return redirect('register')
        #regex = ^[\w!#$%&'*+/=?^`{|}~-]+(?:\.[\w!#$%&'*+/=?`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+(?:\.ox\.ac\.uk)$`
        user = Register.objects.create(username=username,name=name,email=email,pno=pno,sclass=sclass,year=year,passw=passw,date=datetime.date.today())
        myuser=User.objects.create_user(username,email,passw)
        user.save()
        myuser.save()
        messages.success(request,"Account created successfully")
        return render(request,'register.html')
   
    return render(request,'register.html')
    
 
def handlelogin(request):
    if request.method=="POST":
       username = request.POST['username']
       password= request.POST['password']
       user = authenticate(username=username, password=password)
       if user is not None:
            login(request, user)
            
            messages.success(request,"Succcessfully Logged In")
            return redirect('index')
       else:
         messages.error(request,"Invalid Credentials, Please try again")
         return redirect('handlelogin')
    return render(request,'handlelogin.html')

def adminUpdateComp(request,id):
    if request.method == 'POST':
        comp_det= Job_det.objects.get(id=id)
        form = JobDetForm(request.POST, instance = comp_det)
        if form.is_valid():
            form.save()
            messages.success(request,"Company details updated successfully")
            return redirect('admin/admin_manageComp/admincompany_det')
    else:
        comp_det= Job_det.objects.get(id=id)
        form=JobDetForm(instance=comp_det)
    context={'form':form}
    return render(request,'admin/admin_manageComp/adminUpdateComp.html', context)

def applynowform(request,id):
    if request.user.is_authenticated:
        comp_det=Job_det.objects.get(id=id)    
        user_det=Register.objects.get(username=request.user.username)
        if comp_det.vacancy>0: 
            if  comp_det.last_date_toapply>datetime.date.today():
               
                if request.method=="POST":
                    
                        comp_det=Job_det.objects.get(id=id)     
                        user_det=Register.objects.get(username=request.user.username)
                        
                        # form = Apply_for_job.objects.create(name=name,email=email,sclass=sclass,year=year,company_name=company_name,class10clgname=class10clgname,class10per=class10per,class12clgname=class12clgname,class12per=class12per,job_post=job_post,resume=resume)
                        form=ApplyNowForm(request.POST,request.FILES)
                        comp_det.vacancy=comp_det.vacancy-1
                        comp_det.save()
                        form.save()
                        
                        #form1.save()
                            
                        
                        messages.success(request,"Applied successfully for the job")
                        return redirect('index')
                else:
                    comp_det=Job_det.objects.get(id=id)
                    user_det=Register.objects.get(username=request.user.username)
                    #user_det=Register.objects.get(username=Register.username)
                    #{"name": cand_det.name,"company_name":cand_det.company_name,"job_post":cand_det.job_post}
                    #form=ApplyNowForm(instance=user_det)
                                                                                                                                                                                                                                                                                                                                                              
                    context={'user_det':user_det,'comp_det':comp_det}
                    return render(request,'applynowform.html',context)
            else:
               messages.error(request,"Sorry!!! The Job you are looking for is no more available.")
               return redirect('index')
           
        else:
            messages.error(request,"No vacancy available, Better luck next time ")
            return redirect('index')
   
    messages.error(request,"Please login before Applying") 
    return render(request,'index.html')
   
def logout_user(request):
    logout(request)
    messages.success(request,"Logged out successfully") 
    return redirect('index')

def studDashboard(request):
    return render(request, 'stud_dashboard.html')

def admin_login(request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
               login(request, user)
               return redirect('/dashboard')
            else:
               messages.error(request,"Invalid Credentials, Please try again")
               return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
           
        return render(request,'admin/admin_login.html')
     
     
def dashboard(request):
    sdet_count=Register.objects.all().count()
    jobdet_count=Job_det.objects.all().count()
    applied_cand_count=Apply_for_job.objects.all().count()
    shortlisted_cand_count=ShortlistedCand.objects.all().count()
    return render(request, 'dashboard.html',{'sdet_count': sdet_count,'jobdet_count':jobdet_count,'applied_cand_count':applied_cand_count,'shortlisted_cand_count':shortlisted_cand_count})

def adminstud_det(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        sdet = Register.objects.filter(name__icontains=q)
        sdet_c= Register.objects.filter(name__icontains=q).count()
        if sdet_c==0:
            
            return render(request,'admin/admin_manageStud/norecordpresent.html',{'q':q})
        else:
            context = {'sdet':sdet}
            return render(request, 'admin/admin_manageStud/adminstud_det.html', context)
    else:
        sdet=Register.objects.all()
        return render(request,'admin/admin_manageStud/adminstud_det.html',{'sdet':sdet})
    

def admin_header(request):
    return render(request,'admin/admin_header.html')

def adminUpdateStud(request,id):
    if request.method == 'POST':
        stud= Register.objects.get(id=id)
        form = RegisterForm(request.POST, instance = stud)
        if form.is_valid():
            form.save()
            messages.success(request,"Student details updated successfully")
            return redirect('admin/admin_manageStud/adminstud_det')
    else:
        stud= Register.objects.get(id=id)
        form=RegisterForm(instance=stud)
    context={'form':form}
    return render(request, 'admin/admin_manageStud/admin_updateStud.html', context)
    
def adminAddStud(request):
    if request.method=="POST":
        form=AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Added successfully")
            return redirect('admin/admin_manageStud/adminstud_det')
    else:
        form=AddStudentForm()
    return render(request,'admin/admin_manageStud/admin_addrecord.html',{'form':form})

def deleteStudRecord(request, id):
    if request.method=="POST":
        stud= Register.objects.get(id=id)
        if stud.delete():
            messages.error(request,"Student record deleted successfully")
            return redirect('admin/admin_manageStud/adminstud_det')
    return render(request,'admin/admin_manageStud/admin_deleteStudRecord.html')
      
      
def adminComp_det(request):
    comp_det=Job_det.objects.all()
    return render(request,'admin/admin_manageComp/admincompany_det',{'comp_det':comp_det})

def adminUpdateComp(request,id):
    if request.method == 'POST':
        comp_det= Job_det.objects.get(id=id)
        form = JobDetForm(request.POST, instance = comp_det)
        if form.is_valid():
            form.save()
            messages.success(request,"Company details updated successfully")
            return redirect('admin/admin_manageComp/admincompany_det')
    else:
        comp_det= Job_det.objects.get(id=id)
        form=JobDetForm(instance=comp_det)
    context={'form':form}
    return render(request,'admin/admin_manageComp/adminUpdateComp.html', context)

def adminAddComp(request):
    if request.method=="POST":
        form = JobDetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Company Details Added successfully")
            return redirect('admin/admin_manageComp/admincompany_det')
    else:
        form=JobDetForm()
    return render(request,'admin/admin_manageComp/adminAddComp.html',{'form':form})

def deleteCompRecord(request, id):
    if request.method=="POST":
        comp_det= Job_det.objects.get(id=id)
        if comp_det.delete():
            messages.error(request,"Company record deleted successfully")
            return redirect('admin/admin_manageComp/admincompany_det')
    return render(request,'admin/admin_manageComp/adminRemoveComp.html')

def admin_logout(request):
    logout(request)
    messages.success(request,"Logged out successfully") 
    return redirect('index')
      
      
def appliedcandidates(request):
     if request.user.is_authenticated:
        if request.method=="POST":
            fdate=request.POST.get('fdate')
            tdate=request.POST.get('tdate')
            cand_det2=Apply_for_job.objects.filter(date__gte=fdate,date__lte=tdate)
            cand_det2_count=Apply_for_job.objects.filter(date__gte=fdate,date__lte=tdate).count()
            if cand_det2_count==0:
                 return render(request,'admin/admin_manageStud/nrecpfordate.html',{'fdate':fdate,'tdate':tdate})
            return render(request,'admin/admin_manageStud/appliedcandidates.html',{'cand_det2':cand_det2,'fdate':fdate,'tdate':tdate})
        if 'comp_wise' in request.GET:
            comp_wise = request.GET.get('comp_wise')
            cand_det2=Apply_for_job.objects.filter(company_name__icontains=comp_wise)
            return render(request,'admin/admin_manageStud/appliedcandidates.html',{'cand_det2':cand_det2})
        cand_det2=Apply_for_job.objects.all()
        return render(request,'admin/admin_manageStud/appliedcandidates.html',{'cand_det2':cand_det2})
    
def suretoselectcand(request,id):
    cand_det= Apply_for_job.objects.get(id=id)
    return render(request,'admin/admin_manageStud/suretoselectcand.html',{'cand_det':cand_det})
    
def select_cand(request,id):
    if request.method== 'POST':
       
        name=request.POST.get('name')
        email=request.POST.get('email')
        sclass=request.POST.get('sclass')
        year=request.POST.get('year')
        company_name=request.POST.get('company_name')
        job_post=request.POST.get('job_post')
        resume=request.POST.get('resume')
        status=request.POST.get('status')
        cand_det= Apply_for_job.objects.get(id=id)
        if cand_det.status=="Selected":
            messages.error(request,"Candidate is already selected")
        else:
            cand_det.status="Selected"
            cand_det.save()
            s_cand = ShortlistedCand.objects.create(name=cand_det.name,email=cand_det.email,sclass=cand_det.sclass,year=cand_det.year,company_name=cand_det.company_name,job_post=cand_det.job_post,resume=cand_det.resume,status=cand_det.status)
            s_cand.save()
            cand_det2= Apply_for_job.objects.all()
            context=({"name": cand_det.name,"company_name":cand_det.company_name,"job_post":cand_det.job_post})
            html_content=render_to_string("admin/email_template.html",context)
            text_content=strip_tags(html_content)
            
            email=EmailMultiAlternatives(
                'Job Offer Letter',
                text_content,
                settings.EMAIL_HOST_USER,
                [cand_det.email],
                
            )
            email.attach_alternative(html_content,"text/html")
            email.send()
            messages.success(request,"Candidate Shortlisted Successsfully")
            return render(request,'admin/admin_manageStud/appliedcandidates.html',{'cand_det2':cand_det2})
        cand_det2= Apply_for_job.objects.all()
        return render(request,'admin/admin_manageStud/appliedcandidates.html',{'cand_det2':cand_det2})
    else:
        cand_det= Apply_for_job.objects.get(id=id)   
    return render(request,'admin/admin_manageStud/suretoselectcand.html')

def shortlisted_cand(request):
    cand_det=ShortlistedCand.objects.all()
    return render(request,'admin/admin_manageStud/shortlistedCand.html',{'cand_det':cand_det})

def del_shortlistedCand(request,id):
    if request.method=="POST":
        s_cand= ShortlistedCand.objects.get(id=id)
        if s_cand.delete():
            messages.error(request,"Candidates removed successfully")
            return redirect('admin/admin_manageStud/shortlistedCand')
    return render(request,'admin/admin_manageStud/admin_deleteShortlistedCand.html')

def reject_cand(request,id):
    if request.method== 'POST':
        cand_det= Apply_for_job.objects.get(id=id)
        cand_det.status="Rejected"
        cand_det.save()
        messages.error(request,"Candidate Rejected Successsfully")
        cand_det2= Apply_for_job.objects.all()
        return render(request,'admin/admin_manageStud/appliedcandidates.html',{'cand_det2':cand_det2})
    else:
        cand_det= Apply_for_job.objects.get(id=id)   
    return render(request,'admin/admin_manageStud/suretoremove_appCand.html')


# def send_mail_tocomp(request):
#     return render(request,"admin/sendMailToComp.html")