from django.utils import timezone 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.name), filename])



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    washing_amount = models.PositiveIntegerField(default=0)  


    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=255, default='')
    product_name = models.CharField(max_length=255, default='')
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    washing_amount = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f"Order for {self.customer_name}"

class Pay_Pal_Order(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=255, default='')
    product_name = models.CharField(max_length=255, default='')
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PayPal Order for {self.customer_name}"
    

@receiver(post_save, sender=Pay_Pal_Order)
def create_order(sender, instance, created, **kwargs):
    if created:
        # Fetch the corresponding Product based on product_name
        product = Product.objects.filter(name=instance.product_name).first()

        # Get washing_amount from Product if it exists, or default to 0 if not found
        washing_amount = product.washing_amount if product else 0

        # Create an Order with the same data
        Order.objects.create(
            user=User.objects.filter(email=instance.customer_email).first(),
            customer_email=instance.customer_email,
            customer_name=instance.customer_name,
            product_name=instance.product_name,
            total_payment=instance.total_payment,
            order_date=instance.order_date,
            washing_amount=washing_amount,
        )

# Connect the signal
post_save.connect(create_order, sender=Pay_Pal_Order)    

# @receiver(post_save, sender=Pay_Pal_Order)
# def create_order(sender, instance, created, **kwargs):
#     if created:
#         # Create an Order with the same data
#         Order.objects.create(
#             user=User.objects.filter(email=instance.customer_email).first(),
#             customer_email=instance.customer_email,
#             customer_name=instance.customer_name,
#             product_name=instance.product_name,
#             total_payment=instance.total_payment,
#             order_date=instance.order_date,
#             washing_amount = Product.objects.filter(product_name=instance.washing_amount).first(),
#         )

# # Connect the signal
# post_save.connect(create_order, sender=Pay_Pal_Order)
    
    
class WebhookToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)


# class CustomerProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     customer_email = models.EmailField()
#     # Add other fields as needed

#     def __str__(self):
#         return self.customer_email
    
    
# @receiver(post_save, sender=Order)
# def create_or_update_customer_profile(sender, instance, created, **kwargs):
#     if created:
#         # Check if a CustomerProfile already exists for this email
#         customer_profile, created = CustomerProfile.objects.get_or_create(customer_email=instance.customer_email)
        
#         # Update the user reference if it's not already set
#         if customer_profile.user is None:
#             # Find the User based on the email
#             user = User.objects.filter(email=instance.customer_email).first()
#             if user:
#                 customer_profile.user = user
#                 customer_profile.save()




class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)  # Adjust the max length as needed

    def __str__(self):
        return f" User: {self.user.username}"
    
    # class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     purchase_time = models.DateTimeField(default=timezone.now)  # Add this field
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_id = models.CharField(max_length=255, default="")
#     paypal_order_id = models.CharField(max_length=255, blank=True, null=True)  # Add the new field
  

#     def __str__(self):
#         return f"Order #{self.id} by {self.user.username} for {self.product.name}"

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     paypal_order_id = models.CharField(max_length=255, default="")

#     def __str__(self):
#         return f"Order #{self.id} by {self.user.username} for ${self.total_amount}"


  
# class Note(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     body = models.TextField()


  

# class PayPalWebhookEvent(models.Model):
#     event_type = models.CharField(max_length=100)
#     event_id = models.CharField(max_length=100)
#     create_time = models.DateTimeField()    
    

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_info = models.TextField()
#     payment_status = models.CharField(max_length=50)    

# from paypal.standard.forms import PayPalPaymentsForm

# class CustomPayPalPaymentsForm(PayPalPaymentsForm):

#     def get_html_submit_element(self):
#         return """<button type="submit">Continue on PayPal website</button>"""



# class Order(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     customer_email = models.EmailField(default="example@example.com")
#     order_date = models.DateTimeField(default=timezone.now)  # Provide a default value here
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     # Add more fields as needed for your specific use case

#     def __str__(self):
#         return f"Order #{self.id} {self.user.username} for ${self.total_amount}"
