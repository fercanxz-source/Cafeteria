from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            subject = "Cafetería: Nuevo mensaje de contacto"
            message = f"De: {name} <{email}>\n\nMensaje:\n\n{content}"
            from_email = email
            recipient_list = ["admin@lacafeteria.com"]

            try:
                send_mail(subject, message, from_email, recipient_list)
                return redirect(reverse('contact') + "?OK")
            except Exception as e:
                print("EXCEPCIÓN EN SMTP:", e)
                return redirect(reverse('contact') + "?FAIL")
        else:
            # ESTO IMPRIMIRÁ EL ERROR EXACTO EN TU TERMINAL
            print("--- EL FORMULARIO NO ES VÁLIDO ---")
            print(contact_form.errors)

    return render(request, "contact/contact.html", {'form': contact_form})