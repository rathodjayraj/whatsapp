
from whatsapp_app.views.files_import import * 


##############################  login && logout  ##############################

def logins(request):
    try:
        if request.method == "POST":
            username= request.POST['username']
            password= request.POST['password']
            # user_type= request.POST['user_type']
            user = auth.authenticate(username =username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['username']=username
                messages.success(request,"Successfully authenticated as Admin")
                return redirect("dashboard")
            else:
                messages.info(request,"Invalid Username or Password")
                return redirect("logins")
        else:
            return render(request,"adminTemplate/login.html")

    except Exception as e:
        print("This error is login --->: ",e)
        return render(request,'404.html')
    



def logoutpage(request):
    try:
        logout(request)
        return redirect("login")
    except Exception as e:
        print("This error is logoutpage --->: ",e)
        return render(request,'404.html')


##############################  forget  ##############################


def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP




def send_mails(request):
    global otp
    if request.method=="POST":
        try:  
           a=request.POST['id']
        except:
            a=''
        if a!='':
            otps=request.POST['otp']
            id=request.POST['id']
            if(otp==otps):
                return render(request,'adminTemplate/login_user.html',{"id":id,"state":"set_pwd"})
            else:   
                return render(request,'adminTemplate/login_user.html' ,{"state":"otp","msg":"Otp is not correct"})
        else:
            email=request.POST['email']
            try:
                user=User.objects.get(email=email)
            except Exception as e:
                user=[]
            if(user!=[]):
                otp=generateOTP()
                send_mail('OTP request',f'{otp}',settings.EMAIL_HOST_USER,[email])
                return render(request,'adminTemplate/login_user.html' ,{"id":user.id ,"state":"otp"})
            else:
                messages.info(request,"email is not exist")
                return render(request,'adminTemplate/login_user.html')
    else:
        return render(request,'adminTemplate/login_user.html')



def set_pwd(request):
    if request.method=="POST":
        pwd=request.POST['pwd']
        con_pwd=request.POST['con_pwd']
        id=request.POST['id']
        if(pwd==con_pwd):
            user=User.objects.get(id=id)
            user.set_password(pwd)
            user.save()
            return redirect('login')
    else:
        print('ggggggggggg')
    
    


def check_otp(request):
    if request.method=="POST":
        otps=request.POST['otp']
        id=request.POST['id']

        if(otp==otps):
            return render(request,'adminTemplate/login_user.html',{"id":id,"state":"set_pwd"})
        else:
            return HttpResponse('error')



##############################  profile  ##############################


def profile_page(request):


    return render(request,'adminTemplate/profile.html')

def profile(request):
    try:
        if request.method == 'POST':
            id=request.POST.get('upid')
            user=User.objects.get(id=id)
            user.username = request.POST.get('un')

            if(request.POST['pa'] == "*****" ):
                pass
            else:
                user.set_password(request.POST['pa'])

            user.first_name = request.POST.get('fn')
            user.last_name = request.POST.get('ln')
            user.email = request.POST.get('em')
            user.save()
            return redirect('dashboardpage')
    except Exception as e:
        print("This error is profile --->: ",e)
        return render(request, '404.html')
    

