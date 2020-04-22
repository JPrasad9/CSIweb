from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Other,HomeAppliances,Wearables,SmartPhones,Music,Contact
from math import ceil
from django.core.mail import send_mail
from CSIweb.settings import EMAIL_HOST_USER

import json
# Create your views here.

@login_required
def home(request):
    sproduct = SmartPhones.objects.all()
    wproduct = Wearables.objects.all()
    hproduct = HomeAppliances.objects.all()
    mproduct = Music.objects.all()
    oproduct = Other.objects.all()


    sn = len(sproduct)
    wn = len(wproduct)
    hn = len(hproduct)
    mn = len(mproduct)
    on = len(oproduct)

    sslides = sn//4 + ceil((sn/4) - (sn//4))
    wslides = wn//4 + ceil((wn/4) - (wn//4))
    hslides = hn//4 + ceil((hn/4) - (hn//4))
    mslides = mn//4 + ceil((mn/4) - (mn//4))
    oslides = on//4 + ceil((on/4) - (on//4))

    param = {
            'sproduct': sproduct,
            'wproduct': wproduct,
            'hproduct': hproduct,
            'mproduct': mproduct,
            'oproduct': oproduct,

             'srange': range(1, sslides),
             'wrange': range(1, wslides),
             'hrange': range(1, hslides),
             'mrange': range(1, mslides),
             'orange': range(1, oslides),

             'slides': sslides,
             'wslides': wslides,
             'hslides': hslides,
             'mslides': mslides,
             'oslides': oslides

    }

    return render(request, 'home/index.html',param)

@login_required
def about(request):
    return render(request, 'home/about.html')


@login_required
def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactObj = Contact(name=name, email=email, message=message)
        contactObj.save()
        send_mail(
            'Reply to your Query',
            'Hello our team gadgetbowl is working on your query, we will get back to you as soon as possible',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )


    return render(request, 'home/contact.html')

@login_required
def cart(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        email = request.POST.get('email')

        send_mail(
            'Order places',
            'Hello '+name+' your order has been successfully placed,'
                          +' thank you for spending your valuable time shopping with us',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        mess = 'your order has been placed, you will receive a mail soon'
        return render(request, 'home/cart.html', {'message':mess})
    return render(request, 'home/cart.html')

@login_required
def product(request,pid,cat):
    n=False

    refs = {'sp':SmartPhones, 'hp':HomeAppliances, 'mp':Music, 'wp':Wearables, 'op':Other}
    if(cat=='sp'):
        n=True
    prod=refs[cat].objects.filter(id=pid)[0]
    refid = cat[0]+pid
    return render(request, 'home/product.html',{"prod":prod,"n":n,"refid":refid})



def search(request):
    if request.method == "POST":

        keys = request.POST.get("keyword").split(" ")
        spval = SmartPhones.objects.none()
        wpval = Wearables.objects.none()
        mpval = Music.objects.none()
        hpval = HomeAppliances.objects.none()
        opval = Other.objects.none()

        for i in keys:
            spval = spval | SmartPhones.objects.filter(product_name__icontains=i)
            wpval = wpval| Wearables.objects.filter(product_name__icontains=i)
            mpval = mpval | Music.objects.filter(product_name__icontains=i)
            hpval = hpval | HomeAppliances.objects.filter(product_name__icontains=i)
            opval = opval | Other.objects.filter(product_name__icontains=i)

            param = {
             'spval': spval,
             'wpval': wpval,
             'mpval': mpval,
             'hpval':hpval,
              'opval':opval
             }

        return render(request, 'home/search.html',param)
    return render(request, 'home/search.html' )


def category(request):
    sproduct = SmartPhones.objects.all()
    wproduct = Wearables.objects.all()
    hproduct = HomeAppliances.objects.all()
    mproduct = Music.objects.all()
    oproduct = Other.objects.all()

    param = {
        'sproduct': sproduct,
        'wproduct': wproduct,
        'hproduct': hproduct,
        'mproduct': mproduct,
        'oproduct': oproduct,
    }

    return render(request, 'home/category.html',param)