from datetime import timezone
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions  import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import  ProductSerializer, UserRegistrationSerializer, OrderSerializer   
# from base.models import Note
from rest_framework import status

from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .serializers import ForgotPasswordSerializer 


# --------------------------------
from django.utils.crypto import get_random_string
from base.models import Product, Order, Pay_Pal_Order

from .serializers import UserSerializer

# ---------------------------------------
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from paypalrestsdk import notifications

from django.utils import timezone
from django.contrib.auth.decorators import login_required





# from django.shortcuts import render
# from .paypal import generate_client_token, create_order, capture_payment

def hello_world(request):
    return HttpResponse("HELLO WORLD")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView) :
    serializer_class= MyTokenObtainPairSerializer  


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)


@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------
# class ForgotPasswordView(APIView):
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 token = get_random_string(length=32)
#                 user.reset_token = token  # Store token in user's profile or temporary table
#                 user.save()

#                 subject = 'Password Reset'
#                 message = f'Click the link to reset your password: http://localhost:3000/reset-password/{token}'

#                 from_email = 'shanilevi88761234@gmail.com'
#                 recipient_list = [email]
#                 send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#                 return Response({'message': 'Email sent with reset instructions.'})
#             except User.DoesNotExist:
#                 return Response({'message': 'No user with that email.'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# def update_washing_amount(request, order_id):
#     try:
#         order = Order.objects.get(id=order_id, user=request.user)
#         new_washing_amount = request.data.get('washing_amount', 0)

#         # Update the washing_amount field
#         order.washing_amount = new_washing_amount
#         order.save()

#         return Response({'message': 'Washing amount updated successfully'}, status=status.HTTP_200_OK)
#     except Order.DoesNotExist:
#         return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['POST'])
# def create_order(request):
#     # Get the payment data from the request
#     payment_data = request.data

#     # Create a new order using the payment data
#     serializer = OrderSerializer(data=payment_data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def create_or_update_order(request, order_id=None):
    if request.method == 'GET':
        try:
            # Try to get the existing order by its ID
            order = Order.objects.get(id=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        # Create a new order using the data from the request
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            # Try to get the existing order by its ID
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the order with the data from the request
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST', 'PUT'])
# def create_or_update_order(request, order_id=None):
#     if request.method == 'POST':
#         # Create a new order using the data from the request
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'PUT':
#         try:
#             # Try to get the existing order by its ID
#             order = Order.objects.get(id=order_id)
#         except Order.DoesNotExist:
#             return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         # Update the order with the data from the request
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['PUT'])
# def update_washing_amount(request, order_id):
#     try:
#         order = Order.objects.get(id=order_id, user=request.user)
#         new_washing_amount = request.data.get('washing_amount', 0)

#         # Update the washing_amount field only
#         serializer = OrderSerializer(order, data={'washing_amount': new_washing_amount}, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Washing amount updated successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Order.DoesNotExist:
#         return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

class UserOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch orders for the authenticated user
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)  # Use your Order serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
    



import json
from decimal import Decimal
from base.models import WebhookToken

@method_decorator(csrf_exempt, name="dispatch")
class ProcessWebhookView(View):
    def post(self, request):
        if "HTTP_PAYPAL_TRANSMISSION_ID" not in request.META:
            return HttpResponseBadRequest()

        auth_algo = request.META['HTTP_PAYPAL_AUTH_ALGO']
        cert_url = request.META['HTTP_PAYPAL_CERT_URL']
        transmission_id = request.META['HTTP_PAYPAL_TRANSMISSION_ID']
        transmission_sig = request.META['HTTP_PAYPAL_TRANSMISSION_SIG']
        transmission_time = request.META['HTTP_PAYPAL_TRANSMISSION_TIME']
        webhook_id = settings.PAYPAL_WEBHOOK_ID
        event_body = request.body.decode(request.encoding or "utf-8")


        valid = notifications.WebhookEvent.verify(
            transmission_id=transmission_id,
            timestamp=transmission_time,
            webhook_id=webhook_id,
            event_body=event_body,
            cert_url=cert_url,
            actual_sig=transmission_sig,
            auth_algo=auth_algo,
        )

        if not valid:
            return HttpResponseBadRequest()

        webhook_event = json.loads(event_body)

        event_type = webhook_event["event_type"]

        CHECKOUT_ORDER_APPROVED = "CHECKOUT.ORDER.APPROVED"

        if event_type == CHECKOUT_ORDER_APPROVED:


            customer_email = webhook_event["resource"]["payer"]["email_address"]
             
            # Extract item details
            purchased_items = webhook_event["resource"]["purchase_units"][0].get("items", [])
            
            # Debugging print to display the entire purchased_items list
            product_name = webhook_event["resource"]["purchase_units"][0].get("description", "")

    # Debugging print to display the entire purchased_items list
            print("Purchased Items:")
            for item in purchased_items:
               print(item)

            # Extract customer name if available
            customer_name = webhook_event["resource"]["payer"]["name"].get("given_name", "")

            # Extract the total payment amount
            total_payment = Decimal(webhook_event["resource"]["purchase_units"][0]["amount"]["value"])

            

            # Debugging prints
            print(f"Customer Email: {customer_email}")
            print(f"Customer Name: {customer_name}")
            print(f"Product Name: {product_name}")
            print(f"Total Payment Amount: {total_payment}")

            # Create and save the Order object with the calculated total_amount and item names
            order = Pay_Pal_Order(
                customer_email=customer_email,
                customer_name=customer_name,
                product_name=product_name, # Join item names into a string
                total_payment=total_payment,  # Store the payment amount as total_amount
                order_date=timezone.now(),
                # You can set the order date here
                # Add other fields as needed for your model
            )
            order.save()

            product_link = "http://localhost:3001/order"
            send_mail(
                subject="Your access",
                message=f"Thank you, {customer_name}, for purchasing the following items: {product_name}. Here is the link: {product_link}",
                from_email="shanilevi88761234@gmail.com",
                recipient_list=[customer_email]
            )

        return HttpResponse()   
    


# import json
# from decimal import Decimal

# @method_decorator(csrf_exempt, name="dispatch")
# class ProcessWebhookView(View):
#     def post(self, request):
#         if "HTTP_PAYPAL_TRANSMISSION_ID" not in request.META:
#             return HttpResponseBadRequest()

#         auth_algo = request.META['HTTP_PAYPAL_AUTH_ALGO']
#         cert_url = request.META['HTTP_PAYPAL_CERT_URL']
#         transmission_id = request.META['HTTP_PAYPAL_TRANSMISSION_ID']
#         transmission_sig = request.META['HTTP_PAYPAL_TRANSMISSION_SIG']
#         transmission_time = request.META['HTTP_PAYPAL_TRANSMISSION_TIME']
#         webhook_id = settings.PAYPAL_WEBHOOK_ID
#         event_body = request.body.decode(request.encoding or "utf-8")

#         valid = notifications.WebhookEvent.verify(
#             transmission_id=transmission_id,
#             timestamp=transmission_time,
#             webhook_id=webhook_id,
#             event_body=event_body,
#             cert_url=cert_url,
#             actual_sig=transmission_sig,
#             auth_algo=auth_algo,
#         )

#         if not valid:
#             return HttpResponseBadRequest()

#         webhook_event = json.loads(event_body)

#         event_type = webhook_event["event_type"]

#         CHECKOUT_ORDER_APPROVED = "CHECKOUT.ORDER.APPROVED"

#         if event_type == CHECKOUT_ORDER_APPROVED:
#             customer_email = webhook_event["resource"]["payer"]["email_address"]
            
#             # Extract item details
#             purchased_items = webhook_event["resource"]["purchase_units"][0].get("items", [])
            
#             # Debugging print to display the entire purchased_items list
#             product_name = webhook_event["resource"]["purchase_units"][0].get("description", "")

#     # Debugging print to display the entire purchased_items list
#             print("Purchased Items:")
#             for item in purchased_items:
#                print(item)

#             # Extract customer name if available
#             customer_name = webhook_event["resource"]["payer"]["name"].get("given_name", "")

#             # Extract the total payment amount
#             total_payment = Decimal(webhook_event["resource"]["purchase_units"][0]["amount"]["value"])


            

#             # Debugging prints
#             print(f"Customer Email: {customer_email}")
#             print(f"Customer Name: {customer_name}")
#             print(f"Product Name: {product_name}")
#             print(f"Total Payment Amount: {total_payment}")

#             # Create and save the Order object with the calculated total_amount and item names
#             order = Order(
#                 customer_email=customer_email,
#                 customer_name=customer_name,
#                 product_name=product_name, # Join item names into a string
#                 total_payment=total_payment,  # Store the payment amount as total_amount
#                 order_date=timezone.now(),
#                 # You can set the order date here
#                 # Add other fields as needed for your model
#             )
#             order.save()

#             product_link = "http://localhost:3001/order"
#             send_mail(
#                 subject="Your access",
#                 message=f"Thank you, {customer_name}, for purchasing the following items: {product_name}. Here is the link: {product_link}",
#                 from_email="shanilevi88761234@gmail.com",
#                 recipient_list=[customer_email]
#             )

#         return HttpResponse()




# Import your Django model that represents webhook event data
# from base.models import PayPalWebhookEvent
# from django.views.decorators.http import require_POST


# @csrf_exempt
# @require_POST
# def paypal_webhook(request):
#     # Parse the JSON data from PayPal
#     data = json.loads(request.body.decode("utf-8"))

#     # Create an instance of the PayPalWebhookEvent model and save it
#     webhook_event = PayPalWebhookEvent(
#         event_type=data.get("event_type"),
#         event_id=data.get("event_id"),
#         create_time=data.get("create_time"),
#         # Add more fields as needed
#     )
#     webhook_event.save()

#     # Retrieve the order related to this webhook event and update its status
#     # Example: order = Order.objects.get(order_number=data["order_number"])
#     # order.is_completed = True
#     # order.save()

#     # Handle other custom logic based on the webhook data
#     # For example, send order confirmations, update inventory, etc.

#     # Return a 200 OK response to PayPal
#     return HttpResponse(status=200)


# from django.shortcuts import render, redirect
# from paypal.standard.forms import PayPalPaymentsForm
# from django.conf import settings
# from django.urls import reverse
# from django.contrib import messages


# def home(request):
#     host=request.get_host()

#     # What you want the button to do.
#     paypal_dict = {
#         "business": settings.PAYPAL_RECEIVER_EMAIL,
#         "amount": "20.00",
#         "item_name": "Product 1",
#         "invoice": 1234,
#         "currency_code": "USD",
#         "notify_url": f'http://{host}{reverse("paypal-ipn")}',
#         "return_url": f'http://{host}{reverse("paypal-return")}' ,
#         "cancel_return": f'http://{host}{reverse("paypal-cancel")}' ,
    
#     }

#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"form": form}
#     return render(request, "home.html", context)


# def paypal_return(request):
#     messages.success(request, 'you successfuly')
#     return redirect('home')


# def paypal_cancel(request):
#     messages.error(request, 'you dont successfuly')
#     return redirect('home')
    
# def render_checkout(request):
#     client_id = "AfbUGtEZE9rX77TgWCDqKGON5e5BuEiPxc5DEudSA88h-_7erNXkaEMruhvbOZtLiV6e1wRmCsr4ENIs"  # Replace with your PayPal client ID
#     try:
#         client_token = generate_client_token()
#         return render(request, 'checkout.html', {'client_id': client_id, 'client_token': client_token})
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# def create_order_view(request):
#     try:
#         order = create_order()
#         return JsonResponse(order)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# def capture_payment_view(request, order_id):
#     try:
#         capture_data = capture_payment(order_id)
#         return JsonResponse(capture_data)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)



# from django.urls import reverse
# from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm

# def home(request):

#     # What you want the button to do.
#     paypal_dict = {
#         "business": "sb-7jvd4726700262@business.example.com",
#         "amount": "1.00",
#         "currency_code": "GBP",
#         "item_name": "book",
#         "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
#         "return": request.build_absolute_uri(reverse('your-return-view')),
#         "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
#         "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#     }

#     # Create the instance.
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"form": form}
#     return render(request, "payment.html", context)


####
# PayPay
####
# from paypalcheckoutsdk.orders import OrdersGetRequest

# from .paypal import PayPalClient


# @login_required
# def payment_complete(request):
#     PPClient = PayPalClient()

#     body = json.loads(request.body)
#     data = body["orderID"]
#     user_id = request.user.id

#     requestorder = OrdersGetRequest(data)
#     response = PPClient.client.execute(requestorder)

#     total_paid = response.result.purchase_units[0].amount.value

#     basket = Basket(request)
#     order = Order.objects.create(
#         user_id=user_id,
#         full_name=response.result.purchase_units[0].shipping.name.full_name,
#         email=response.result.payer.email_address,
#         address1=response.result.purchase_units[0].shipping.address.address_line_1,
#         address2=response.result.purchase_units[0].shipping.address.admin_area_2,
#         postal_code=response.result.purchase_units[0].shipping.address.postal_code,
#         country_code=response.result.purchase_units[0].shipping.address.country_code,
#         total_paid=response.result.purchase_units[0].amount.value,
#         order_key=response.result.id,
#         payment_option="paypal",
#         billing_status=True,
#     )
#     order_id = order.pk

#     for item in basket:
#         OrderItem.objects.create(order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"])

#     return JsonResponse("Payment completed!", safe=False)


# @login_required
# def payment_successful(request):
#     basket = Basket(request)
#     basket.clear()
#     return render(request, "checkout/payment_successful.html", {})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     user = request.user
#     notes = user.note_set.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)



# @api_view(['GET'])
# def get_all_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)  # Use a serializer to convert user data to JSON
#     return Response(serializer.data)

# @api_view(['GET'])
# def get_user_by_id(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = UserSerializer(user)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_order(request):
#     data = request.data
#     data['user'] = request.user.id  # Set the user to the logged-in user
    
#     serializer = OrderSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from .serializers import NoteSerializer
# from base.models import Note



# @api_view(['POST'])
# def postProduct(request):
#     queryset = Product.objects.all()
#     serializer = ProductSerializer

#     def post(self, request, *args, **kwargs):
#         name=request.data['name']
#         cover = request.data['cover']
#         price = request.data['price']
#         Product.objects.create(price=price, cover=cover , name=name)
#         return HttpResponse({'message': 'Book created'}, status=200)

# @api_view(['GET'])
# def getOrders(request, user_id):
#     orders = Order.objects.filter(user_id=user_id)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)




# from django.contrib.auth.hashers import make_password
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import CustomUser

# class UpdatePasswordView(APIView):
#     def post(self, request):
#         reset_token = request.data.get('token')
#         new_password = request.data.get('new_password')

#         try:
#             user = CustomUser.objects.get(reset_token=reset_token)
#             user.set_password(new_password)
#             user.reset_token = None  # Reset the reset token
#             user.save()
            
#             return Response({'message': 'Password updated successfully.'})
#         except CustomUser.DoesNotExist:
#             return Response({'message': 'Invalid reset token.'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#    user = request.user
#    notes = user.note_set.all()
#    seralizer = NoteSerializer(notes, many=True)
#    return Response(seralizer.data)

# views.py
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_str  # Update this import
# from django.contrib.auth import get_user_model
# from django.http import JsonResponse, HttpResponseBadRequest
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# from django.views.decorators.http import require_POST
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import SetPasswordForm
# from base.models import User

# @csrf_exempt
# @require_POST
# def reset_password(request, token):
#     try:
#         # Decode the token to get the user's primary key
#         uid = force_str(urlsafe_base64_decode(token))
#         user = get_object_or_404(User, pk=uid)

#         # Check if the token is valid
#         if not default_token_generator.check_token(user, token):
#             return HttpResponseBadRequest("Invalid token")

#         # Process the password change
#         form = SetPasswordForm(user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, user)  # Update the session to prevent logout
#             return JsonResponse({'message': 'Password reset successful.'})
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
    





from rest_framework import generics, status, viewsets, response

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from . import serializers


# class PasswordReset(generics.GenericAPIView):
#     """
#     Request for Password Reset Link.
#     """

#     serializer_class = serializers.EmailSerializer

#     def post(self, request):
#         """
#         Create token.
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data["email"]
#         user = User.objects.filter(email=email).first()
#         if user:
#             encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
#             token = PasswordResetTokenGenerator().make_token(user)
#             reset_url = reverse(
#                 "reset-password",
#                 kwargs={"encoded_pk": encoded_pk, "token": token},
#             )
#             reset_link = f"localhost:8000{reset_url}"

#             # send the rest_link as mail to the user.

#             return response.Response(
#                 {
#                     "message": 
#                     f"Your password rest link: {reset_link}"
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return response.Response(
#                 {"message": "User doesn't exists"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
        
# class ForgotPasswordView(APIView):
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 token = get_random_string(length=32)
#                 user.reset_token = token  # Store token in user's profile or temporary table
#                 user.save()

#                 subject = 'Password Reset'
#                 message = f'Click the link to reset your password: http://localhost:3000/reset-password/{token}'

#                 from_email = 'shanilevi88761234@gmail.com'
#                 recipient_list = [email]
#                 send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#                 return Response({'message': 'Email sent with reset instructions.'})
#             except User.DoesNotExist:
#                 return Response({'message': 'No user with that email.'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics, status, response
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

class PasswordReset(generics.GenericAPIView):
    """
    Request and Reset Password.
    """

    serializer_class = serializers.EmailSerializer

    def post(self, request):
        """
        Initiate password reset and send reset instructions.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        try:
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)

            # Store the token in the user's profile or temporary table
            user.reset_token = token
            user.save()

            # Generate a reset URL
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )

            # Create the complete reset link
            reset_link = f"http://localhost:3000{reset_url}"

            # Send reset instructions via email
            subject = "Password Reset"
            message = f"Click the link to reset your password: {reset_link}"
            from_email = "shanilevi88761234@gmail.com"  # Replace with your email
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return response.Response(
                {"message": "Email sent with reset instructions."},
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return response.Response(
                {"message": "No user with that email."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = serializers.ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )
    



