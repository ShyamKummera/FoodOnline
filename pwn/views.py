from django.contrib import messages
from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from pwn.forms import StateForm,CityForm,CuisineForm

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
                messages.error(request, 'State Details not Valid')
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
        sf = StateForm(request.POST,request.FILES,instance=spk)
        if sf.is_valid():
            data = sf.save(commit=False)
            data.save()
            messages.success(request, 'State Details Updated')
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
    viewstate = StateModel.objects.all()
    return render(request, 'pwn/openstate.html', {'state_form': StateForm(), 'viewstate': viewstate,"confirm":did})


def statedeleteconfirmYes(request):
    yes_id = request.GET.get("yesid")
    StateModel.objects.filter(id=yes_id).delete()
    return redirect("savestateformredirect")

def statedeleteconfirmNo(request):
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
    cf = CityForm(request.POST,request.FILES )
    if cf.is_valid():
        cid = request.POST.get("cid",None)
        if cid:
            cpk = CityModel.objects.get(id=cid)
            ucf = CityForm(request.POST,request.FILES,instance=cpk)
            if ucf.is_valid():
                data = ucf.save(commit=False)
                data.save()
                messages.success(request, 'City Details Updated')
                return redirect('savecityformredirect')
            else:
                messages.error(request, 'City Details not Valid')
                return redirect('savecityformredirect')
        else:
            cf.save()
            messages.success(request, 'City Details Saved')
            return redirect('savecityformredirect')
    else:
        messages.error(request, 'Please Enter Valid Input')
        return redirect('savecityformredirect')

def updatecityform(request,id):
    cpk = CityModel.objects.get(id=id)
    if request.method == "POST":
        print("This is POST")
        cf = CityForm(request.POST , request.FILES, instance=cpk)
        if cf.is_valid():
            data = cf.save(commit=False)
            data.save()
            messages.success(request, 'City Details Saved')
            return redirect('city')
        else:
            messages.error(request, 'Please Enter Valid Input')
            return redirect('savecityformredirect')
    else:
        cf = CityForm(instance=cpk)
        viewcity = CityModel.objects.all()
        return render(request, 'pwn/opencity.html',{'city_form': cf, 'viewcity': viewcity, "id": id})

def deletecity(request):
    did = request.GET.get("cid")
    viewcity = CityModel.objects.all()
    return render(request,'pwn/opencity.html', {'city_form': CityForm(), 'viewcity': viewcity,"confirm":did})

def citydeleteconfirmYes(request):
    yes_id = request.GET.get("yesid")
    CityModel.objects.filter(id=yes_id).delete()
    return redirect("savecityformredirect")

def citydeleteconfirmNo(request):
    return redirect("savecityformredirect")
# ==========================================================================================
def openCusine(request):
    cf = CuisineForm()
    viewcuisine = CuisineModel.objects.all()
    return render(request,"pwn/opencuisine.html",{"cuisine_form":cf,'viewcuisine':viewcuisine})

def savecuisineformredirect(request):
    viewcuisine = CuisineModel.objects.all()
    return render(request, 'pwn/opencuisine.html',{'cuisine_form':CuisineForm(),'viewcuisine':viewcuisine})

def savecuisineform(request):
    cfs = CuisineForm(request.POST,request.FILES)
    if cfs.is_valid():
        ucf = request.POST.get("cid",None)
        if ucf:
            cmucf = CuisineModel.objects.get(id=ucf)
            cfv = CuisineForm(request.POST,request.FILES,instance=cmucf)
            if cfv.is_valid():
                same = cfv.save(commit=False)
                same.save()
                messages.success(request,"Cuisine details Updated")
                return redirect("savecuisineformredirect")

        else:
            cfs.save()
            messages.success(request, "Cuisine details saved")
            return redirect("savecuisineformredirect")
    else:
        messages.error(request,"Invalid Details")
        return redirect("savecuisineformredirect")


def updatecuisine(request,pk):
    cmid = CuisineModel.objects.get(id=pk)
    cfiled = CuisineForm(instance=cmid)
    viewcuisine = CuisineModel.objects.all()
    return render(request, 'pwn/opencuisine.html',{'cuisine_form':cfiled,'viewcuisine':viewcuisine,"pk":pk})

def deletecuisine(request):
    did = request.GET.get("cuid")
    viewcuisine = CuisineModel.objects.all()
    return render(request, 'pwn/opencuisine.html', {'cuisine_form': CuisineForm(), 'viewcuisine': viewcuisine, "confirm": did})

def cuisinedeleteconfirmYes(request):
    yes_id = request.GET.get("yesid")
    CuisineModel.objects.filter(id=yes_id).delete()
    return redirect("savecuisineformredirect")

def cuisinedeleteconfirmNo(request):
    return redirect("savecuisineformredirect")
# =========================================================================================
def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")


