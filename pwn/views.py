from django.contrib import messages
from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel,CityModel
from pwn.forms import StateForm,CityForm

def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    sf = StateForm()
    viewstate = StateModel.objects.all()
    return render(request,"pwn/openstate.html",{'state_form':sf,'viewstate':viewstate})

def savestateformredirect(request):
    viewstate = StateModel.objects.all()
    return render(request, 'pwn/openstate.html',{'state_form':StateForm(),'viewstate':viewstate})

# ===========================================================================================
def savestateform(request):
    sf = StateForm(request.POST,request.FILES)
    if sf.is_valid():
        sid = request.POST.get("sid",None)
        if sid:
            spk = StateModel.objects.get(id=sid)
            usf = StateForm(request.POST, request.FILES, instance=spk)

            if usf.is_valid():

                data = usf.save(commit=False)

                data.save()
                messages.success(request, 'State Details Updated')
                return redirect('savestateformredirect')
        else:
            sf.save()
            messages.success(request,'State Details Saved')
            return redirect('savestateformredirect')
    else:
        messages.error(request,'Please Enter Valid Input')
        return redirect('savestateformredirect')

def updatestateform(request,id):
    spk = StateModel.objects.get(id=id)
    if request.method == 'POST':
        print("This is POST")
        sf = StateForm(request.POST or request.FILES,instance=spk)
        if sf.is_valid():
            data = sf.save(commit=False)
            data.save()
            messages.success(request, 'State Details Saved')
            return redirect('state')
        else:
            messages.error(request, 'Please Enter Valid Input')
            return redirect('savestateformredirect')
    else:
        print("This is GET")
        sf = StateForm(instance=spk)
        viewstate = StateModel.objects.all()
        return render(request, 'pwn/openstate.html', {'state_form': sf, 'viewstate': viewstate,"id":id})

def deletestate(request):
    did = request.GET.get("sid")
    # StateModel.objects.filter(id=did).delete()
    # return redirect("savestateformredirect")
    viewstate = StateModel.objects.all()
    return render(request, 'pwn/openstate.html', {'state_form': StateForm(), 'viewstate': viewstate,"confirm":did})


def deleteconfirmYes(request):
    yes_id = request.GET.get("yesid")
    StateModel.objects.filter(id=yes_id).delete()
    return redirect("savestateformredirect")

def deleteconfirmNo(request):
    return redirect("savestateformredirect")

# ==========================================================================================
def openCity(request):
    cf = CityForm()
    viewcity = CityModel.objects.all()
    return render(request,"pwn/opencity.html",{'city_form':cf,'viewcity':viewcity})

def savecityformredirect(request):
    viewcity = CityModel.objects.all()
    return render(request, 'pwn/opencity.html',{'city_form':CityForm(),'viewcity':viewcity})


def savecityform(request):
    cf = CityForm(request.POST, request.FILES)
    if cf.is_valid():
        cf.save()
        messages.success(request, 'City Details Saved')
        return redirect('savecityformredirect')
    else:
        messages.error(request, 'Please Enter Valid Input')
        return redirect('savecityformredirect')


def openCusine(request):
    return render(request,"pwn/opencuisine.html")


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")


