from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from Agriculture.forms import NewUserForm
from Agriculture.models import Loan, Machinery, Crops, Seeds, Purchase_Crops
from django.template import loader
# Loan request Database Saving Code
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    # return HttpResponse("Home Page")
    return render(request, "index.html")


def login(request):
    return HttpResponse("Login Page")


def main(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return redirect('Dashboard_Owner')
    return render(request, 'main.html')


def main2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return redirect('Dashboard_Partner')
    return render(request, 'main2.html')


def main3(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
            return redirect('Dashboard_Middleman')
    return render(request, 'main3.html')


def new_partner(request):
    signup = NewUserForm()
    if request.method == "POST":
        signup = NewUserForm(request.POST)
        if signup.is_valid():
            signup.save()
            return redirect("Main2")
    dict_signup = {'signup': signup}
    return render(request, 'new_partner.html', dict_signup)


def terms_conditions(request):
    return render(request, 'terms_conditions.html')


def partner_first(request):
    return render(request, 'partner_first.html')


def db_owner(request):
    from datetime import datetime
    loan = None
    if request.method == "POST":
        loan_req = request.POST.get('loan_req')
        prev = loan_req
        date = datetime.now()
        loan = Loan(loan_req=loan_req,
                    date=date)
        loan.save()

    loan_req = Loan.objects.values_list('loan_req')
    loan_req = removespaces(loan_req)
    date = Loan.objects.values_list('date')
    date = removespaces(date)
    status = Loan.objects.values_list('status')

    dict_loan = {'loan_req': loan_req, 'date': date}

    return render(request, 'dashboard_owner.html', dict_loan)



def owner_machinery(request):
    partner_name = Machinery.objects.values_list('partner_name')
    partner_name = removespaces(partner_name)
    machinery_req = Machinery.objects.values_list('machinery')
    machinery_req = removespaces(machinery_req)
    date = Machinery.objects.values_list('date')
    date = removespaces(date)

    if request.method == "POST":
        machinery_name = request.POST.get('p_name')
        rent_price = request.POST.get('p_machinery')
        members = Machinery.objects.filter(machinery=machinery_name)
        for all_members in members:
            all_members.rent = rent_price
            all_members.save()


    rent_lst = Machinery.objects.values_list('rent')
    rent_lst = removespaces(rent_lst)
    dict_machinery_req = {'partner_name': partner_name, 'machinery_req': machinery_req, 'date': date,'rent_machinery':rent_lst}
    return render(request, 'owner_machinery.html', dict_machinery_req)


def owner_seeds(request):
    partner_name = Seeds.objects.values_list('partner_name')
    # print(partner_name)
    partner_name = removespaces(partner_name)
    seed_req = Seeds.objects.values_list('seeds')
    seed_req = removespaces(seed_req)
    date = Seeds.objects.values_list('date')
    date = removespaces(date)
    amount = Seeds.objects.values_list('amount')
    amount = removespaces(amount)

    dict_seeds_req = {'partner_name': partner_name, 'seed_req': seed_req, 'date': date, 'amount': amount}
    return render(request, 'owner_seeds.html', dict_seeds_req)


def owner_crops(request):
    V1 = Purchase_Crops.objects.values_list('crop_name')
    V1 = removespaces(V1)
    V2 = Purchase_Crops.objects.values_list('date')
    V2 = removespaces(V2)
    V3 = Purchase_Crops.objects.values_list('amount_bags')
    V3 = removespaces(V3)
    V4 = Purchase_Crops.objects.values_list('price_crops')
    V4 = removespaces(V4)

    loan = Loan.objects.values_list('loan_req')
    loan = removespaces(loan)
    loan_total = 0
    pur_crops_total = 0
    for i in range(len(V4)):
        if V4[i] is not None:
            pur_crops_total += int(V4[i])

    for i in range(len(loan)):
        if loan[i] is not None:
            loan_total += int(loan[i])
    total_price = pur_crops_total - loan_total

    dict_crops_req = {'crop_name': V1, 'amount_bag': V3, 'date': V2, 'price_bag': V4,
                              'total_price': total_price, 'total_loan_price': loan_total}
    return render(request, 'owner_crops.html', dict_crops_req)


def removespaces(lst):
    res_lst = []
    for i in range(len(lst)):
        res_lst.append(lst[i][0])
        # print(lst[i][0])
    return res_lst


def db_partner(request):
    from datetime import datetime
    machinery = None
    if request.method == "POST":
        partnername = request.POST.get('name')
        machine = request.POST.get('machinery')
        date = datetime.now()
        machinery = Machinery(partner_name=partnername, machinery=machine,
                              date=date)
        machinery.save()

    partner_name = Machinery.objects.values_list('partner_name')
    # print(partner_name)
    partner_name = removespaces(partner_name)
    machinery_req = Machinery.objects.values_list('machinery')
    machinery_req = removespaces(machinery_req)
    date = Machinery.objects.values_list('date')
    date = removespaces(date)

    dict_machinery_req = {'partner_name': partner_name, 'machinery_req': machinery_req, 'date': date}

    return render(request, 'dashboard_partner.html', dict_machinery_req)
    # request.method = None
    return render(request, 'dashboard_partner.html')


def partner_seeds(request):
    from datetime import datetime
    seeds = None
    if request.method == "POST":
        partnername = request.POST.get('name')
        seed = request.POST.get('seeds')
        amount = request.POST.get('amount')
        date = datetime.now()
        # seeds class variable from database(models.py)
        seeds = Seeds(partner_name=partnername, seeds=seed,
                      date=date, amount=amount)
        seeds.save()
    partner_name = Seeds.objects.values_list('partner_name')
    # print(partner_name)
    partner_name = removespaces(partner_name)
    seed_req = Seeds.objects.values_list('seeds')
    seed_req = removespaces(seed_req)
    date = Seeds.objects.values_list('date')
    date = removespaces(date)
    amount = Seeds.objects.values_list('amount')
    amount = removespaces(amount)

    dict_seeds_req = {'partner_name': partner_name, 'seed_req': seed_req, 'date': date, 'amount': amount}

    return render(request, 'partner_seeds.html', dict_seeds_req)



def partner_crops(request):
    from datetime import datetime
    crops = None
    if request.method == "POST":
        partnername = request.POST.get('name')
        crop = request.POST.get('crops')
        amt_bags = request.POST.get('amt_bags')
        date = datetime.now()
        # crops class variable from database(models.py)
        crops = Crops(partner_name=partnername, crops=crop,
                      date=date, amt_bags=amt_bags)
        crops.save()
        partner_name = Crops.objects.values_list('partner_name')
        partner_name = removespaces(partner_name)
        crop_req = Crops.objects.values_list('crops')
        crop_req = removespaces(crop_req)
        date = Crops.objects.values_list('date')
        date = removespaces(date)
        amt_bags = Crops.objects.values_list('amt_bags')
        amt_bags = removespaces(amt_bags)

        dict_crops_req = {'partner_name': partner_name, 'crop_req': crop_req, 'date': date, 'amt_bags': amt_bags}

        return render(request, 'partner_crops.html', dict_crops_req)

    return render(request, 'partner_crops.html')


def db_middleman(request):
    loan_req = Loan.objects.values_list('loan_req')
    loan_req = removespaces(loan_req)
    date = Loan.objects.values_list('date')
    date = removespaces(date)
    status = Loan.objects.values_list('status')
    status = removespaces(status)
    dict_loan = {'loan_req': loan_req, 'date': date, 'loan_status': status}

    return render(request, 'dashboard_middleman.html', dict_loan)


def middleman_crops(request):
    from datetime import datetime
    purchase_crops = None
    if request.method == "POST":
        crop_name = request.POST.get('crops_name')
        price_crops = request.POST.get('crops_price')
        amt_bags = request.POST.get('crops_amount')
        if crop_name != None and price_crops != None and amt_bags != None:
            price_crops = int(amt_bags) * int(price_crops)
            date = datetime.now()
            # crops class variable from database(models.py)
            purchase_crops = Purchase_Crops(crop_name=crop_name, date=date,
                                            price_crops=price_crops, amount_bags=amt_bags)
            purchase_crops.save()
            V1 = Purchase_Crops.objects.values_list('crop_name')
            V1 = removespaces(V1)
            V2 = Purchase_Crops.objects.values_list('date')
            V2 = removespaces(V2)
            V3 = Purchase_Crops.objects.values_list('amount_bags')
            V3 = removespaces(V3)
            V4 = Purchase_Crops.objects.values_list('price_crops')
            V4 = removespaces(V4)
            loan = Loan.objects.values_list('loan_req')
            loan = removespaces(loan)
            loan_total = 0
            pur_crops_total = 0
            for i in range(len(V4)):
                if V4[i] is not None:
                    pur_crops_total += int(V4[i])

            for i in range(len(loan)):
                if loan[i] is not None:
                    loan_total += int(loan[i])

            total_price = pur_crops_total - loan_total

            dict_crops_req = {'crop_name': V1, 'amount_bag': V3, 'date': V2, 'price_bag': V4,
                              'total_price': total_price, 'total_loan_price': loan_total}

        return render(request, 'middleman_crops.html', dict_crops_req)

    return render(request, 'middleman_crops.html')


def new_loan(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        loan = Loan.objects.create(amount=amount, status='Pending')
        return redirect('loan_detail', loan_id=loan.id)
    return render(request, 'owner_dashboard.html')


def loan_detail(request, loan_id):
    loan = Loan.objects.get(id=loan_id)
    return render(request, 'owner_dashboard.html', {'loan': loan})
