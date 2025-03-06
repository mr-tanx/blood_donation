
from .models import donor, recipient
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import donor
from django.http import HttpResponse, JsonResponse
from .models import donor
from django.views.decorators.csrf import csrf_exempt

def adminhome(request):
    return render(request,"adminhome.html")

def logout(request):
    return render(request,"index.html")

def donor_view(request):  # Renamed from 'donor' to 'donor_view'
    return render(request,"donor.html")

def recipient_view(request):  # Renamed from 'recipient' to 'recipient_view'
    return render(request,"recipient.html")

def donoradd(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        email = request.POST['email']
        blood_group = request.POST['bloodgroup']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']

        donor_obj = donor(full_name=full_name, email=email, blood_group=blood_group, age=age, gender=gender, address=address)
        donor.save()
        return render(request, 'succesfull.html')

    return render(request, 'donor.html')


def recipientadd(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        email = request.POST['email']
        blood_group = request.POST['bloodgroup']
        urgency_level = request.POST['urgency']
        hospital_name = request.POST['hospital']
        hospital_address = request.POST['address']

        recipient_obj = recipient(FULL_NAME=full_name, EMAIL=email, BLOOD_GROUP=blood_group, urgency_level=urgency_level, hospital_name=hospital_name, hospital_address=hospital_address)
        recipient_obj.save()  # Fixed the call to save the recipient object
        return render(request, 'succesfull.html')
    return render(request, 'recipient.html')
def crud(request):
    return render(request,"crud.html")

@csrf_exempt
def add_donor(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        donor_obj = donor(full_name=full_name, age=age)
        donor_obj.save()
        return HttpResponse("Donor added successfully.")
    return HttpResponse("This is the Add Donor page.")

@csrf_exempt
def delete_donor(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        donor.objects.filter(age=age).delete()
        return HttpResponse("Donor deleted successfully.")
    return HttpResponse("This is the Delete Donor page.")

@csrf_exempt
def update_donor(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        new_full_name = request.POST.get('new_full_name')
        donor_obj = donor.objects.get(age=age)
        donor_obj.full_name = new_full_name
        donor_obj.save()
        return HttpResponse("Donor updated successfully.")
    return HttpResponse("This is the Update Donor page.")

@csrf_exempt
def search_donor(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        donor_obj = donor.objects.filter(age=age).first()
        if donor_obj:
            return JsonResponse({'full_name': donor_obj.full_name, 'age': donor_obj.age})
        else:
            return JsonResponse({'message': 'Donor not found'})
    return HttpResponse("This is the Search Donor page.")
