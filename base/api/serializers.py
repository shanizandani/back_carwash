from rest_framework.serializers import ModelSerializer
from base.models import Product, Order, Transaction
from django.contrib.auth.models import User 
from rest_framework import serializers

# -----------------------------------------


# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


# ------------------------------------------------------------------

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'price')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'cover', 'washing_amount']


# class OrderSerializer(serializers.ModelSerializer):
#     # Add any additional fields or customization here
#     class Meta:
#         model = Order
#         fields = ['id', 'user', 'product', 'order_date', 'total_amount', 'payment_id', 'product_name']   
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] 


# from base.models import Note


# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'

from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode


class EmailSerializer(serializers.Serializer):
    """
    Reset Password Email Request Serializer.
    """

    email = serializers.EmailField()

    class Meta:
        fields = ("email",)



class ResetPasswordSerializer(serializers.Serializer):
    """
    Reset Password Serializer.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data
