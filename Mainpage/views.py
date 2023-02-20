from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import MasterPackages, CustomerData, Review
from .forms import ImageForm
import datetime
from datetime import date

# Create your views here.

def Homepages(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("pass")
        cpass = request.POST.get("cpass")
        if password == cpass:
            myuser = User.objects.create_user(email,mobile,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            user = authenticate(username = email,password = password)
            login(request,user)
            messages.success(request,"You are Logged in successfully")
            return redirect("/profile/")
        else:
            messages.warning(request,"Password is not matched ")
            return redirect("/password/")
    highlighted_packages = MasterPackages.objects.filter(package_event = "Highlighted Events").all()
    Snow_packages = MasterPackages.objects.filter(package_event = "Snow Events").all()
    Weekends_packages = MasterPackages.objects.filter(package_event = "Weekend Events").all()
    Summer_packages = MasterPackages.objects.filter(package_event = "Summer Events").all()
    return render(request, "Mainpage/index.html",{"highlighted_packages":highlighted_packages,"Snow_packages":Snow_packages,"Weekends_packages":Weekends_packages,"Summer_packages":Summer_packages})

def Aboutpage(request):
    return render(request, 'Mainpage/about.html')

def Eventpage(request):
    Events = MasterPackages.objects.filter(package_event = "Events").all()
    return render(request,'Mainpage/events.html',{'Events':Events})

def Teampage(request):
    return render(request,'Mainpage/team.html')

def Contactpage(request):
    return render(request,"Mainpage/contact.html")

def Profile_page(request):
    form = ImageForm()
    user = request.user
    allow = 0
    if CustomerData.objects.filter(customer_email = user.username).all().exists():
        allow = 1
        profile_data = CustomerData.objects.all()
        return render(request,'Mainpage/profile.html',{"form":form,"allow":allow,"profile_data":profile_data})
    else:
        allow = 0
        profile_data = CustomerData()
        if request.method == "POST":
            if len(request.FILES) != 0:
                profile_data.customer_img = request.FILES['customer_img']
            full_name = user.first_name
            last_name = user.last_name
            profile_data.customer_id = user.id
            profile_data.customer_fname = full_name
            profile_data.customer_lname = last_name
            profile_data.customer_address = request.POST.get("address")
            profile_data.customer_mobile = user.email
            profile_data.customer_email = user.username
            profile_data.customer_gender = request.POST.get("gender")
            profile_data.customer_dob = request.POST.get("dob")
            profile_data.save()
            return redirect("/profile/")
    return render(request,'Mainpage/profile.html',{"form":form,"allow":allow})

def Event_detail(request,id):
    user = request.user
    event_id = id
    allow  = 0
    package_data = MasterPackages.objects.filter(id = event_id).all()
    reviews_data = Review.objects.filter(event_id = event_id).all().values()
    review_list = []
    for i in reviews_data:
        review_dic = {}
        review_dic["id"] = i['id']
        review_dic["customer_id"] = i["customer_id"]
        str = ""
        for j in range(i["stars"]):
            str = str + "a"
        review_dic["stars"] = str
        review_dic["reviewer_name"] = i["reviewer_name"]
        review_dic["review_text"] = i["review_text"]
        review_list.append(review_dic)
    if CustomerData.objects.filter(customer_email = user.username).all().exists():
        allow = 1
    else:
        allow = 0
    return render(request,"Mainpage/event_detail.html",{"allow":allow,"review_list":review_list,"package_data":package_data})

def edit_profile(request):
    profile_data = CustomerData()
    form = ImageForm()
    user  = request.user
    if request.method == "POST":
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        CustomerData.objects.filter(customer_email = user).update(customer_dob = dob)
        CustomerData.objects.filter(customer_email = user).update(customer_fname = first_name)
        CustomerData.objects.filter(customer_email = user).update(customer_lname = last_name)
        CustomerData.objects.filter(customer_email = user).update(customer_address = address)
        CustomerData.objects.filter(customer_email = user).update(customer_gender = gender)
        return redirect("/profile/")
    return render(request,"Mainpage/edit_profile.html",{"form":form})

def Review_page(request):
    user = request.user
    reviews = Review()
    if CustomerData.objects.filter(customer_email = user.username).all().exists():
        if request.method == "POST":
            review = request.POST.get("review")
            result = request.POST.get("result")
            event_id = request.POST.get("event_id")
            reviews.event_id = event_id
            reviews.customer_id = user.id
            reviews.stars = result
            reviews.review_text = review
            reviews.reviewer_name = user.first_name
            reviews.save()
            return redirect("/event-detail/{}".format(event_id))
    else:
        messages.warning(request,"Please First complete Profile")
    return redirect("/event-detail/")

def logout_page(request):
    logout(request)
    return redirect("/")