from datetime import datetime
from random import randint

from kavenegar import *
from rest_framework import generics

from utilities.exception import exceptions
from utilities.respones import ErrorResponse, SuccessResponse

from ..models import Code, User
from .serializers import (RegisterSerializer, UserUpdateSerializer,
                          UserVerifySerializer)

sms = randint(1000, 9999) // 4


class RegisterWithPhoneNumber(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    throttle_classes = []

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            phone_number = serialized_data.data["phone_number"]
            rand_num = randint(1000, 9999)
            try:
                api = KavenegarAPI(
                    "38502F546846716559723175674E49324A674B2B62654B58724D61314B474777"
                )
                params = {
                    "receptor": "phone_number",
                    "template": "dentino",
                    "token": str(rand_num),
                    "token2": "",
                    "token3": "",
                    "type": "sms",  # sms vs call
                }
                response = api.verify_lookup(params)
                print(response)
            except APIException as e:
                print(e)
            except HTTPException as e:
                print(e)
            code = Code.objects.create(
                number=rand_num,
                expire=datetime.datetime.now() + datetime.timedelta(minutes=10),
                phone=phone_number,
            )
            rand = request.session[code]
            user_phone = request.session[phone_number]
            return SuccessResponse(message=("کد برای شما پیامک شد")).send()
        return ErrorResponse(message=("کد برای شما پیامک شد")).send()


class VerifyUserRegister(generics.CreateAPIView):
    serializer_class = UserVerifySerializer

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            user_phone = request.session["code"]
            code = Code.objects.filter(phone=user_phone).first()
            verify_code = serialized_data.data["verify_code"]
            if verify_code.expire < datetime.datetime.now():
                raise ValueError("Expiration Error, please try again", "danger")

            if code != verify_code:
                raise ValueError("your code is wrong", "danger")
            else:
                user = User.objects.create_user(name=user_phone)
                return SuccessResponse(message=("ثبت نام با موفقیت انجام شد")).send()


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    model = User
    throttle_classes = []

    def patch(self, request):
        try:
            serialize_data = self.get_serializer(
                request.user, data=request.data, partial=True
            )
            if serialize_data.is_valid(raise_exception=True):
                try:
                    self.perform_update(serialize_data)
                except Exception as e:
                    raise e
                serialize_data = self.get_serializer(request.user)
                return SuccessResponse(serialize_data.data).send()

        except exceptions.ValidationError as e:
            return ErrorResponse(message=e.detail, status=e.status_code).send()
        except Exception as e:
            return ErrorResponse(message=str(e)).send()

    def put(self, request):
        try:
            serialize_data = self.get_serializer(request.user, data=request.data)
            if serialize_data.is_valid(raise_exception=True):
                try:
                    self.perform_update(serialize_data)
                except Exception as e:
                    raise e
                serialize_data = self.get_serializer(request.user)
                return SuccessResponse(serialize_data.data).send()

        except exceptions.ValidationError as e:
            return ErrorResponse(message=e.detail, status=e.status_code).send()
        except Exception as e:
            return ErrorResponse(message=str(e)).send()
