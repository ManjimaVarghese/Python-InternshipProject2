

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import DoctorUpload

from .forms import  DataFormNew
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404

from .forms import CreateUserForm,CreateUserFormNew,CreateUserFormNewOne


from .models import userForm,User,userFormnew,userFormadmin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required





from django.contrib import messages
def newpatient(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            age = form.cleaned_data['age']
            mobile = form.cleaned_data['mobile']
            gender = form.cleaned_data['gender']
            disease = form.cleaned_data['disease']
            doctor = form.cleaned_data['doctor']
            user = form.save()
            userForm.objects.create(user = user, fullname = fullname, age = age,mobile=mobile,gender=gender,disease=disease,doctor=doctor)
            login(request, user)
            msg = 'Registration Completed, Go To Signin Page'
            return render(request, 'hosapp/newpatient.html', {'msg': msg,'form': form})
    else:
        form = CreateUserForm()
    return render(request, 'hosapp/newpatient.html', {'form': form})


# def newpatient(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)

#         if form.is_valid():
#             fullname = form.cleaned_data['fullname']
#             age = form.cleaned_data['age']
#             mobile = form.cleaned_data['mobile']
#             gender = form.cleaned_data['gender']
#             disease = form.cleaned_data['disease']
#             doctor = form.cleaned_data['doctor']
#             user = form.save()
#             userForm.objects.create(user = user, fullname = fullname, age = age,mobile=mobile,gender=gender,disease=disease,doctor=doctor)
#             login(request, user)
#             msg = 'Registration Completed, Go To Signin Page'
#             return render(request, 'hosapp/newpatient.html', {'msg': msg,'form': form})
#     else:
#         form = CreateUserForm()
#     return render(request, 'hosapp/newpatient.html', {'form': form})



    
def entry(request):

    return render(request, 'hosapp/entry.html')



    
def patiententrypage(request):
    return render(request, 'hosapp/patiententrypage.html')




    
def patiententrynew(request):
    return render(request, 'hosapp/patiententrynew.html')


    
def patientedit(request):
 

    data = userForm.objects.filter(user_id=request.user.id).get()
    return render(request, 'hosapp/patientedit.html', {'datas': data})


def loginpatient(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username'] = username
            if user is not None:
                print(user.id)
                login(request, user)
                request.session['id'] = user.id
                return redirect(patientedit)
            else:
                try:
                    userForm.objects.get(username=username)
                    return render(request, 'hosapp/newpatient.html', {'form': form})
                except userForm.DoesNotExist:
                    messages.error(request, 'User does not exist')
    else:
        form = AuthenticationForm()
    return render(request, 'hosapp/loginpatient.html', {'form': form})


def delete(request, user_id):
    
        new= userForm.objects.filter(user_id=user_id).get()
        new.delete()
   
        return redirect('loginpatient')


def deletedr(request, user_id):
    
        new= DoctorUpload.objects.filter(user_id=user_id).get()
        new.delete()
   
        return redirect('logindoctor')


def edit(request,user_id):
    instance = get_object_or_404(userForm,user_id=user_id)
    form = CreateUserForm(instance=instance)
    # user_data = userForm.objects.filter(user_id=user_id).values('fullname', 'mobile', 'age','gender','disease','doctor')
    return render(request,'hosapp/newpatient.html',{'form':form,'instance':instance})


def ptnsignout(request):
    if 'username' in request.session:
        del request.session['username']
    
    logout(request)
    return redirect('loginpatient')


@login_required

def changepassptn(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginpatient)
        else:
            return render(request,'hosapp/changepassptn.html',{'form':form})          
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'hosapp/changepassptn.html',{'form':form})


def update(request,id=None):
     if request.method == 'POST':
        if id is not None:
            instance = userForm.objects.get(id=id)
            form=CreateUserForm(request.POST,instance=instance)
            if form.is_valid():
                 fullname = form.cleaned_data['fullname']
                 age = form.cleaned_data['age']
                 mobile = form.cleaned_data['mobile']
                 gender = form.cleaned_data['gender']
                 disease = form.cleaned_data['disease']
                 doctor = form.cleaned_data['doctor']
                 form.save()
                 userForm.objects.update( fullname = fullname, age = age,mobile=mobile,gender=gender,disease=disease,doctor=doctor)
                 msg = 'updated'
                 return redirect('entry')
          
          
            else:
                return render(request,'hosapp/newpatient.html',{'form':form})
        else:
            return redirect('patientedit')
     else:
        return render(request,'hosapp/newpatient.html',{'form':form})
     
    

     
     


# def save(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form=CreateUserForm()
#             data_value=userForm.objects.all()
#             return render(request,'hosapp/patientedit.html',{'datas':data_value})
#         else:
#              return render(request,'hosapp/newpatient.html',{'form':form})
        
#     else:
#          return render(request,'hosapp/newpatient.html',{'form':form})
    





def newdoctor(request):
    if request.method == 'POST':
        form = CreateUserFormNew(request.POST)

        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            department = form.cleaned_data['department']
            mobile = form.cleaned_data['mobile']
            user = form.save()
            userFormnew.objects.create(user = user, fullname = fullname,department=department,mobile=mobile)
            login(request, user)
            msg = 'Registration Completed, Go To Signin Page'
            return render(request, 'hosapp/newdoctor.html', {'msg': msg,'form': form})
    else:
        form = CreateUserFormNew()
    return render(request, 'hosapp/newdoctor.html', {'form': form})




def logindoctor(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username'] = username
            if user is not None:
                print(user.id)
                login(request, user)
                request.session['id'] = user.id
                return redirect(doctoredit)
            else:
                try:
                    userForm.objects.get(username=username)
                    return render(request, 'hosapp/newdoctor.html', {'form': form})
                except userForm.DoesNotExist:
                    messages.error(request, 'User does not exist')
    else:
        form = AuthenticationForm()
    return render(request, 'hosapp/logindoctor.html', {'form': form})



     


def doctoredit(request):
 

    data = userFormnew.objects.filter(user_id=request.user.id).get()
    return render(request, 'hosapp/doctoredit.html', {'datas': data})
    







def drsignout(request):
    if 'username' in request.session:
        del request.session['username']
    
    logout(request)
    return redirect('logindoctor')


@login_required

def drchangepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(logindoctor)
        else:
            return render(request,'hosapp/drchangepass.html',{'form':form})          
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'hosapp/drchangepass.html',{'form':form})


def viewpatientdetails(request):
 
  
    username = request.session.get('username')
    datas = userForm.objects.filter(doctor__exact=username)
    return render(request, 'hosapp/viewpatientdetails.html', {'datas': datas})


def viewpresptn(request):
    user_id = request.session.get('id')
    datas = DoctorUpload.objects.filter(id=user_id)
    return render(request, 'hosapp/viewpresptn.html', {'datas': datas})
           






def loginptnfpres(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username'] = username
            if user is not None:
                print(user.id)
                login(request, user)
                request.session['id'] = user.id
                
                # Get the data of the logged-in user
                datas = DoctorUpload.objects.filter(Patient_name__exact=username)
                
                # Redirect to the viewpresptn.html page with the data
                return render(request, 'hosapp/viewpresptn.html', {'datas': datas})
    else:
        form = AuthenticationForm()
        
    return render(request, 'hosapp/loginptnfpres.html', {'form': form})





def drloginvptn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username'] = username
            if user is not None:
                print(user.id)
                login(request, user)
                request.session['id'] = user.id
                
                # Get the data of the logged-in user
                datas = userForm.objects.filter(doctor__exact=username)
                
                # Redirect to the viewpresptn.html page with the data
                return render(request, 'hosapp/viewpatientdetails.html', {'datas': datas})
    else:
        form = AuthenticationForm()
        
    return render(request, 'hosapp/drloginvptn.html', {'form': form})




def druploadpres(request):
    if request.method == 'POST':
        form = DataFormNew(request.POST,request.FILES)

        if form.is_valid():
            
            Patient_name = form.cleaned_data['Patient_name']
            profile = form.cleaned_data['profile']
            form.save()
           
            # DoctorUpload.objects.create(Dr_name = Dr_name, Patient_name = Patient_name,profile = profile)
            
            form.instance.Patient_name = Patient_name
            form.instance.profile = profile
            msg = 'Registration Completed, Go To Signin Page'
            return render(request, 'hosapp/druploadpres.html', {'msg': msg,'form': form})
    else:
        form = DataFormNew()
    return render(request, 'hosapp/druploadpres.html', {'form': form})




def viewptnupdetails(request):
    datas=userForm.objects.all()
    return render(request,'hosapp/viewptnupdetails.html',{'datas':datas})
def viewdrupdetails(request):

    datas=DoctorUpload.objects.all()
    return render(request,'hosapp/viewdrupdetails.html',{'datas':datas})

def adminviews(request):

    return render(request,'hosapp/adminviews.html')



def adminlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            request.session['username'] = username
            if user is not None:
                print(user.id)
                login(request, user)
                request.session['id'] = user.id
                return redirect(adminviews)
            else:
                try:
                    userForm.objects.get(username=username)
                    return render(request, 'hosapp/adminlogin.html', {'form': form})
                except userForm.DoesNotExist:
                    messages.error(request, 'User does not exist')
    else:
        form = AuthenticationForm()
    return render(request, 'hosapp/adminlogin.html', {'form': form})





def newadmin(request):
    if request.method == 'POST':
        form = CreateUserFormNewOne(request.POST)

        if form.is_valid():
            user = form.save()
            userFormadmin.objects.create(user = user)
            login(request, user)
            msg = 'Registration Completed, Go To Signin Page'
            return render(request, 'hosapp/newadmin.html', {'msg': msg,'form': form})
    else:
        form = CreateUserFormNewOne()
    return render(request, 'hosapp/newadmin.html', {'form': form})





def adminpage(request):
 


    return render(request, 'hosapp/adminpage.html')





def adminviews(request):
    
    return render(request,'hosapp/adminviews.html')