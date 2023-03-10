

# Create your views here.
from ast import Return
from django.urls import reverse
from django.db.models import Count
import random
from re import template
from sre_constants import SUCCESS
from typing import Generic
from django.shortcuts import  render,HttpResponseRedirect,redirect
from .forms import signupform,loginform1,appliction_form,approve_from,application_id_student,reset_password_form
from django.contrib.auth.models import User
from .models import student_custom,application_model
from django.views import generic
from django.contrib.auth import login
# from django.contrib import messages   
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def make_random_password():
    characters = list('123456789')     
    thepassword = ''
    for x in range(4):
        thepassword += random.choice(characters)
    return thepassword
# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="home.html", context={"register_form":form})
# class register_request(generic.createView):
#     form_class= NewUserForm
#     template_name='home.html'
#     success_url= reverse_lazy('')def
#signup
def register_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=signupform(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('loginform')
        else:
            fm=signupform()
        return render (request=request, template_name="home.html", context={"register_form":fm})
    else:
        n1=request.user

        if n1 in student_custom.objects.filter(Role='Student'):
            return redirect('studentdashbord')
        else:
            return redirect('facultydashbord')
#login 
def loginform(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=loginform1(request.POST)
            if fm.is_valid():
                # uname=fm.cleaned_data['username']
                # email=request.POST.get('email')
                # password=request.POST.get('password')
                Ename=fm.cleaned_data['email']
                upass=fm.cleaned_data['password']
                request.session['email']=Ename
                # if User.objects.filter(email=email).exists():
                #     if User.objects.filter(email=email,password=password).exists():
                #         # request.session['email']=email
                #         return redirect('dashbord')
                #     else:
                #         messages.error(request,'Invalid password')
                # else:
                #     messages.error(request,'Email is not exists')
                user =authenticate(email=Ename,password=upass)
                # print(user)
                # print(student_custom.objects.all())
                if user is not None:
                    if student_custom.objects.filter(email=Ename,Role='Student'):
                    
                        login(request,user)
                        return HttpResponseRedirect('/studentdashbord/')
                    else:
                        login(request,user)
                      
                        return redirect('facultydashbord')
                else:
                    messages.success(request,'Invalid Email and password')
        else:
            fm=loginform1()

        return render(request,'login.html',{'form':fm})
    else:
        # print(request.user)
        n1=request.user

        if n1 in student_custom.objects.filter(Role='Student'):
            return redirect('studentdashbord')
        else:
            return redirect('facultydashbord')

  

def Sdashbord(request):
    if request.user.is_authenticated:
        # if request.method == "POST":
            id=''
            intaial_data={
                'application_id':make_random_password,
                'email':request.user
            }
            form=appliction_form(initial=intaial_data)
            if request.method == "POST":
                id=request.POST.get('application_id')
                uname=request.POST.get('university_name')
                pname=request.POST.get('program_name')
                sname=request.POST.get('study_mode')
                cname=request.POST.get('customer')
                email=request.POST.get('email')
                all=(id,uname,pname,sname,cname)
                setvalue=application_model.objects.filter(email=email)
                setvalu1=len(setvalue)
                print(setvalu1) 
                if setvalu1 >=3:
                    messages.error(request,'You can make 3 attempts so you are no longer eligible to apply')
                else:
                    en=application_model(application_id=id,university_name=uname,program_name=pname,study_mode=sname,customer=cname,email=email,status='')
                    en.save()
                    messages.success(request,'Your application submited succesfully ')
                    data={ 'id':id }
            data={
                'email':request.session.get('email'),
                'form':form,
                'id':id
            }
            return render(request,'studentDashbord.html',data)
        # else:
        #     return redirect('dashbord')
    else:
        return redirect('loginform')
 
def Facultydashbord(request):
    if request.user.is_authenticated:
        a=application_model.objects.all()
        
        
        for student in a:
            # print(student.application_id)
            ntaial_data={
                'id':student.application_id
            }
        
        fm=approve_from(initial=ntaial_data)
        if request.method == "POST":
            # b=request.POST['main_id']   
            # print(b)
            
            # n0=application_model.objects.values(application_id=student.application_id)
            n1=request.POST.get('select')
            print("hjbb",n1)
            # user_id = int(request.POST['main_id'])
            user_id = request.POST.get('sid')
            print(user_id)
            user = application_model.objects.get(application_id=user_id)
            print(user)
            # n1='approved'
            print("------------------")
            if request.POST.get('send1'):
            # en=application_model.objects.get(status=student.application_id)
                n1='Approved'
                en=application_model.objects.get(application_id=user_id)
                en.status=n1
                en.save()
                # return HttpResponseRedirect(reverse("facultydashbord"))
            elif request.POST.get('send2'):
                n1='Disapproved'
                en=application_model.objects.get(application_id=user_id)
                en.status=n1
                en.save()
                # return HttpResponseRedirect(reverse("facultydashbord"))
            
        else:
            print("dscfsdfdf")
        data={
        # 'info':request.all,
        'email':request.session.get('email'),   
        'info':a,
        'from':fm
        }
        return render(request,'facultyDashbord.html',data)
    else:
        return redirect('loginform')

def user_logout(request):
    logout(request)
    return redirect('loginform')

def track_appliction(request):
    a=application_model.objects.filter(email=request.user)
    data={
        'form':application_id_student,
        'info':a,
    }
        
    if request.method == "POST":
        fm=application_id_student()
        if fm.is_valid:
            id=request.POST.get('id')
            print(id)
            if application_model.objects.filter(application_id=id):
                b=application_model.objects.get(application_id=id)
                print( "dedeef",b.status)
                data={'key':b.status}
                if b.status == '':
                    messages.error(request,'Your application stiil pending')
                    return redirect('trackapplication_student')
                elif b.status == 'Disapproved':
                    messages.error(request,'Your application has been Disapproved')
                    return redirect('trackapplication_student')
                elif b.status == 'Approved':
                    messages.success(request,'Your application has been Approved')
                    return redirect('trackapplication_student')
                # else:
                    
                #     return redirect('trackapplication_student')
                    # return render(request,'track_appliction.html')

                # if b.status is not None:
                #     data={'key':b.status}
                #     messages.error(request,'Your application has been ')
                # else:
                #     messages.error(request,'Your application stiil pending')
            else:
                messages.error(request,'Enter a valid application id')
        else:
            pass
    else:
        fm=application_id_student()

    return render(request,'track_appliction.html',data)

def student_dashbord(request):
    if request.user.is_authenticated:
        data={
            'email':request.session.get('email'),
        }
   
        return render(request,'studentdashbord1.html',data)
    else:
        return redirect('loginform')

#change password 
def user_changepassword(request):
    if request.user.is_authenticated:
       
        if request.method == "POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                return redirect("loginform")
        else:
                # return render( request,'changepassword.html',data)
            fm=PasswordChangeForm(user=request.user)
        data={  
            'form1':fm,  
        }
        
        return render( request,'changepassword.html',data)
    else:
        return redirect('loginform')

def PasswordResetView(request):
    fm=reset_password_form()
    return render( request,'password_reset.html',{'form':fm})

def PasswordResetConfirmView(request):
    fm=SetPasswordForm()

    return render( request,'password_reset_form.html',{'form':fm})

@csrf_exempt
def savedata(request):
    # a=application_model.objects.all()
        
        
    # for student in a:
    #     # print(student.application_id)
    #     ntaial_data={
    #         'id':student.application_id
    #     }
    
    # fm=approve_from(initial=ntaial_data)
    if request.method == "POST":
            # b=request.POST['main_id']   
            # print(b)

            # n0=application_model.objects.values(application_id=student.application_id)
            # a=application_model.objects.all()
            # for student in a:
            # # print(student.application_id)
            #     ntaial_data={
            #     'id':student.application_id
            #      }
        
            # fm=approve_from(initial=ntaial_data)
            # n1=request.POST.get('select')
            # print("hjbb",n1)
            # user_id = int(request.POST['main_id'])
            user_id = request.POST.get('sid')
            user_id=user_id

            print("id is",user_id )
            # print(user_id)
            # user = application_model.objects.get(application_id=user_id)
            # print(user)
            # if request.POST.get('send1'):
            #     en=application_model.objects.get(application_id=4821)
            #     en.status='Approved'
            #     en.save()   
            #     data1=en.status
            en=application_model.objects.get(application_id=user_id)
            en.status='Approved'
            en.save()        
            data1=en.status
            # stud=application_model.objects.values()
            # student_data=list(stud)
            return JsonResponse({'status':'Save','data_store1':data1,'user_id':user_id,})
    else:
        return JsonResponse({'status':0 })
@csrf_exempt
def savedata1(request):
    if request.method == "POST":
            user_id = request.POST.get('sid')
            user_id=user_id
            en=application_model.objects.get(application_id=user_id)
            en.status='Disapproved'
            en.save()        
            data1=en.status
            return JsonResponse({'status':'Save','data_store1':data1,'user_id':user_id,})
    else:
        return JsonResponse({'status':0 })


    # if request.method == "POST":
    #         b=request.POST['main_id']   
    #         print(b)
            
    #         # n0=application_model.objects.values(application_id=student.application_id)
    #         n1=request.POST.get('select')
    #         print("hjbb",n1)
    #         user_id = int(request.POST['main_id'])
    #         print(user_id)
    #         user = application_model.objects.get(application_id=user_id)
    #         print(user)
    #         # n1='approved'
    #         print("------------------")
    #         if request.POST.get('send1'):
    #         # en=application_model.objects.get(status=student.application_id)
    #             n1='Approved'
    #             en=application_model.objects.get(application_id=user_id)
    #             en.status=n1
    #             en.save()
    #             # return HttpResponseRedirect(reverse("facultydashbord"))
    #         elif request.POST.get('send2'):
    #             n1='Disapproved'
    #             en=application_model.objects.get(application_id=user_id)
    #             en.status=n1
    #             en.save()

    #         return JsonResponse({'status':'save'})
    # else: 
    #         return JsonResponse({'status':0})   

       


     