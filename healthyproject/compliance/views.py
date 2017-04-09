
from django.shortcuts import render, redirect
from django.http import HttpResponse
from compliance.models import Doctor, Patient, Initial
# Create your views here.

def index(request):
    response = render(request,"compliance/index.html")

    if request.method == "POST":
        if request.Get["register_doctor"]:
            response = render(request,"compliance/doctor_Registration.html")
    return response

def doctor_Registration(request):


    if request.method == "POST" :
        doctor = Doctor()
        doctor.name = request.POST.get("doctor-name")
        doctor.password = request.POST.get("doctor-password")
        doctor.specialty = request.POST.get("doctor-specialty")
        #doctor.company = request.POST.get("organization")

        patient_dict = {"default" : ["cold", 15]}
        doctor.save()
        request.session["doc-name"] = doctor.name
        response = render(request,"compliance/doctor_Dashboard.html", {"patient_dict" : patient_dict})
        return response


    response = render(request, "compliance/doctor_Registration.html")
    return response

def doctor_Login(request):
    response = render(request,"compliance/doctor_Login.html")
    if request.method == "POST":
        print "POST LOG"
        doc_name = request.POST.get("doctor-name")
        doc_password = request.POST.get("doctor-password")
        print doc_name
        print doc_password

        for doctor in Doctor.objects.all():
            print doctor.name
            print doctor.password
            request.session["doc-name"] = doctor.name
            if doctor.name == doc_name and doctor.password == doc_password:
                patient_dict = doctor.Patient_list
                response = render(request,"compliance/doctor_Dashboard.html", {"patient_dict" : patient_dict})
                #return redirect("doctor_Dashboard", {"patient_dict" : patient_dict})
                return response


    return response

def doctor_Dashboard(request):
    response = render(request, "compliance/doctor_Dashboard.html")
    return response


def patient_Registration(request):
    if request.method == "POST" :
        patient = Patient()
        patient.name = request.POST.get("Patient-name")
        patient.conditions = request.POST.get("Patient-conditions")
        patient.age = request.POST.get("Patient-age")
        patient.email = request.POST.get("Patient-email")
        #doctor.company = request.POST.get("organization")
        patient.save()

        doc = request.session["doc-name"]
        print doc
        doctor =  Doctor.objects.get_or_create(name = doc)[0]
        #doctor.Patient_list[patient.name] = [patient.conditions, patient.age]
        doctor.Patient_list.update({patient.name : [patient.conditions, patient.age]})
        doctor.save()
        patient_dict =  doctor.Patient_list



        for initial in Initial.objects.all():
            if initial.email == patient.email:
                print "SUCCESS"

                initial.Doctor_list.update({doctor.name : False})
                initial.save()


        response = render(request,"compliance/doctor_Dashboard.html", {"patient_dict": patient_dict})
        return response


    response = render(request, "compliance/patient_Registration.html")
    return response

def initial_Dashboard(request):
    initial_name = request.session["initial-name"]
    print "THIS IS"
    print initial_name

    initial = Initial.objects.get_or_create(name = initial_name)[0]
    initial_feedback = initial.feedback

    response = render(request, "compliance/initial_Dashboard.html", {"initial_name" : initial_name, "initial_feedback" : initial_feedback})
    return response

def initial_Registration(request):
    if request.method == "POST" :
        initial = Initial()
        initial.name = request.POST.get("initial-name")
        initial.password = request.POST.get("initial-password")
        initial.email= request.POST.get("initial-email")
        #doctor.company = request.POST.get("organization")
        initial.save()
        request.session["initial-name"] = initial.name


        return redirect("initial_Dashboard")


    response = render(request, "compliance/initial_Registration.html")
    return response

def patient_Dashboard(request, patient_name): # does not really ever get called
    patient_name = patient_name

    request.session["pat-name"] = patient_name

    patient = Patient.objects.get_or_create(name = patient_name)[0]
    print patient_name
    print patient.conditions
    patient_conditions = patient.conditions


    response = render(request, "compliance/patient_Dashboard.html", {"patient_name" : patient_name, "patient_conditions" : patient_conditions})
    return response




def doctor_feedback(request):
    response = render(request, "compliance/doctor_feedback.html")

    pat = request.session["pat-name"]
    print "THIS IS PAT"
    print pat

    patient = Patient.objects.get_or_create(name = pat)[0]
    print patient.email




    if request.method == "POST":
        category = request.POST["dropdown"]
        feedback = request.POST.get("Patient-feedback")
        print "THIS IS feedback"
        print feedback
        print category

        for initialobject in Initial.objects.all():
            print "checking"
            if initialobject.email == patient.email:
                print "BREAD"

                initialobject.feedback.update({category: feedback })
                initialobject.save()

        if category in patient.feedback:
            print "if"

        #    patient.feedback[category] = " ".join(patient.feedback[category])
            print patient.feedback[category]

            patient.feedback[category] = feedback

            response = render(request, "compliance/patient_Dashboard.html", {"patient_name" : pat, "patient_feedback" : feedback})

            #initial.conditions[category] = list2
        else:
            print "else"
            patient.feedback.update({category: feedback })

            #initial.conditions.update({category : feedback})

        patient.save()
        #initial.save()
        response = render(request, "compliance/patient_Dashboard.html", {"patient_name" : pat, "patient_feedback" : patient.feedback})

    return response
