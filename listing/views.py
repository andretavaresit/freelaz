from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from .choices import price_choices, category_choices, state_choices
from django.contrib.auth.decorators import login_required
from .forms import ListingForm, UpdateForm
from django.core.mail import send_mail

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings  = paginator.get_page(page)
    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, pk):
    rate=False
    favourite = False
    listing = get_object_or_404(Listing, pk=pk)

    if request.user.is_authenticated:
        favourites = str(request.user.favourites)
        rate_listing = str(request.user.rate_listing)
        favourites = favourites.split(',')
        rate_listing = rate_listing.split(',')
        if request.method== "POST":
            if 'favourite_val' in request.POST:
                favourite_val = request.POST['favourite_val']
                if favourite_val == 'unfavourite':
                    if str(pk) in favourites:
                        favourites.remove(str(pk))
                if favourite_val == 'favourite':
                    if str(pk) not in favourites:
                        favourites.append(str(pk))
                request.user.favourites = ','.join(favourites)
                request.user.save()

            if 'my_rating' in request.POST:
                my_rating = request.POST['my_rating']
                if int(my_rating)>10 or int(my_rating)<0:
                    messages.error(request,'Please enter a value from 0-10')
                elif str(pk) not in rate_listing:
                    if listing.total_rating:
                        listing.total_rating += int(request.POST['my_rating'])
                        listing.no_of_rating +=1
                    else:
                        listing.total_rating = int(request.POST['my_rating'])
                        listing.no_of_rating = 1
                    rate_listing.append(str(pk))
                    request.user.rate_listing = ','.join(rate_listing)
                    request.user.save()
                    listing.save()
                    if int(my_rating)<5:
                        print('entrei if')
                        owner_mail = request.POST['owner_mail']
                        title = request.POST['listing']
                        send_mail(
                            'Mensagem sobre o anúncio "'+ title+'"',
                            'Seu anúncio '+ title +
                            ' foi avaliado abaixo de nossas regras de diretrizes, você tem 1 semana para melhorar a avaliação ou seu anúncio será removido de nossa plataforma.',
                            'andretavares16@gmail.com',
                            [owner_mail],
                            fail_silently=False
                        )
                        
                        messages.success(request, "Sua avaliação gerou um avíso ao dono do Anúncio, caso o mesmo nao melhore, terá seu anúncio removido.")
                        print('passei avaliação')
                    else:
                        print('nao entrei if')
        
        if str(pk) in favourites:
            favourite=True
        if str(pk) not in rate_listing:
            rate = True
    current_rating = 0
    if listing.no_of_rating:
        current_rating = listing.total_rating/listing.no_of_rating
    context = {
        'listing': listing,
        'favourite':favourite,
        'rate': rate,
        'current_rating': current_rating

    }
    return render(request, 'listings/listing.html', context)

def search(request):
    query_set = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(title__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category__iexact=category)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set = query_set.filter(state__iexact=state)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)
    context = {
        'query_set': query_set,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'category_choices': category_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

@login_required
def create(request):
    
    
    context = {
    'state_choices': state_choices,
    'category_choices': category_choices
        }
    if request.method=='GET':
        print('GET')
    else:
        print('POST')
        photo_main = request.POST.get('foto-principal')
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')

        data_agora = datetime.now()
        data_agora = data_agora.strftime('%Y/%m/%d')
        data_agora = str(data_agora)

        Listing.objects.create(photo_main='photos/'+data_agora+'/'+photo_main,owner=request.user,title=titulo,category=categoria,address=endereco,city=cidade,state=estado,zipcode=cep,description=descricao,price=preco)
    return render(request,'listings/create.html',context)
    


@login_required
def update(request, pk):
    print('entrei função')
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)
    print('entrei passei get object')
    context = {
        'form': UpdateForm(instance=listing),
        'update': True,
        'pk': pk
    }
    print('entrei passei context')
    if request.method=="POST":
        print('entrei passei REQUEST')
        photo_main = request.POST.get('foto-principal')
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')

        data_agora = datetime.now()
        data_agora = data_agora.strftime('%Y/%m/%d')
        data_agora = str(data_agora)

        Listing.objects.filter(pk=pk).update(photo_main='photos/'+data_agora+'/'+photo_main,owner=request.user,title=titulo,category=categoria,address=endereco,city=cidade,state=estado,zipcode=cep,description=descricao,price=preco)
        return redirect('dashboard')

    else:
        print('entrei NAO passei REQUEST')
        print('LISTING: '+str(listing.__dict__))
        context = {
        'state_choices': state_choices,
        'category_choices': category_choices,
        'listing': listing   
        }
        return render(request, 'listings/update.html', context)

@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing,pk=pk)
    print(str(listing.__dict__))
    listing.delete()
    return redirect('dashboard')