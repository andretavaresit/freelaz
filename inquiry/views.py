from django.shortcuts import render, redirect
from django.contrib import messages
from .models import inquiry
from django.core.mail import send_mail
from listing.models import Listing

def inquirys(request):
    print('entrei inquiry')
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        owner_mail = request.POST['owner_mail']
        owner_id = request.POST['owner_id']
        
    
        if request.user.is_authenticated:
            print('print aqui')
            user_id  = request.user.id
            has_inquired = inquiry.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_inquired:
                messages.error(request, 'Você já entrou em contato com o proprietário')
                return redirect('/listing/'+listing_id+'/')


            listing_anuncio = Listing(id=listing_id)
            inquirys1 = inquiry(listing=listing, listing_id=listing_id,anuncio = listing_anuncio, name=name, email=email, phone=phone,
                             message=message, user_id=user_id, owner_id=owner_id)
            inquirys1.save()
            print('passei save inquiry')
            send_mail(
                'Mensagem sobre o anúncio "'+ listing+'"',
                'Você recebeu uma mensagem para '+ listing +
                ' - Faça login no seu painel para obter mais informações',
                'andretavares16@gmail.com',
                [owner_mail],
                fail_silently=False
            )
            messages.success(request, "Sua mensagem foi enviada, o proprietário da postagem entrará em contato com você o mais rápido possível")
            return redirect('/listing/'+listing_id+'/')