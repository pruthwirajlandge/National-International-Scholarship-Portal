from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import permissions,authentication,parsers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserModel
from .serializers import UserSerializer, GetUserSerializer
from verify_email.email_handler import send_verification_email
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password


FIELD_NOT_EMPTY = "field should not be empty."
BAD_REQUEST = status.HTTP_400_BAD_REQUEST
CREATE_REQUEST = status.HTTP_201_CREATED
GET_REQUEST = status.HTTP_200_OK
USER_EXIST = "with the given credentials already exist."
USER_NOT_EXIST = "with the given credentials does not exist."
HOURS = ' hours!'

def validate_user_input(request_data):
    required_fields = ['email', 'first_name', 'last_name', 'password', 'phone_number', 'address']
    for field in required_fields:
        if not request_data.get(field, '').strip() or len(request_data.get(field)) <= 0:
            return False, f'{field.capitalize()} should not be empty.'
    return True, 'Success'

class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ["first_name","last_name","email","password","phone_number","address","profile_picture"]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
@parser_classes([parsers.MultiPartParser, parsers.FormParser])
def create_profile(request):
    try:
        request_data = request.data
        is_valid, error = validate_user_input(request_data)
        if not is_valid:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        email = request_data.get('email', '').strip()
        first_name = request_data.get('first_name', '').strip()
        last_name = request_data.get('last_name', '').strip()
        password = request_data.get('password', '').strip()
        phone_number = request_data.get('phone_number')
        address = request_data.get('address', '').strip()
        profile_picture = request.FILES.getlist('profile_picture')
        validate_password(password, user=email, password_validators=None)
        
        user_data = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email': email,
            'password': make_password(password),
            "phone_number": ('+91' + phone_number) if phone_number.split('+91')[0] != '+91' else phone_number,
            "address": address,
        }
        
        form = UserForm(data=user_data, files=request.FILES)
        if form.is_valid():
            form.save()
            inactive_user = send_verification_email(request, form)
            print(inactive_user)
            return Response("User Successfully Created!", status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class Me(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            user = UserModel.objects.filter(id=request.auth.user.pk).order_by('id')
            serializer = GetUserSerializer(instance=user, many=True)
            return Response(serializer.data, status=GET_REQUEST)
        except Exception as e:
            return Response(str(e), status=BAD_REQUEST)
