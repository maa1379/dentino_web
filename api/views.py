import random
from datetime import timedelta
from decimal import Decimal

# from django.http import HttpRespone
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from django_filters import rest_framework as filters
from kavenegar import *
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from zeep import Client

import api.ser
import doctor.models
import partial.models
from account.models import Code, Profile
from cart.cart import Cart
from clinic.models import Clinic, Winner
from commoncourse.models import Common_Course
from config.models import About_Us, Contact_Us, Slider
from doctor.api.serailizers import DoctorSer, VisitTimeSerializer
from doctor.models import (Discount, Doctor, DoctorDate, Expertise, Insurance,
                           VisitTime)
from location.models import City, Province, Zone
from order.models import Order, OrderItem
from partial.models import (Company, Complaint, DoctorDictionary,
                            Prescriptions, Price)
from reservation.models import Reservation
from shop.models import Category, Product
from utilities.respones import ErrorResponse, SuccessResponse
from .filters import DoctorFilter
from .ser import (About_usSerializer, AddToCartSerializer,
                  CategoryListSerializer, CitySerializer, ClinicSerializer,
                  ClinicShortSeralizer, CommonDetailSerializer,
                  CommonListSerializer, CompanySerializer,
                  ComplimentSerializer, ContactUsSerializer,
                  DeleteCartItemSerializer, DictCategorySer,
                  DiscountListSerializer, DoctorDictionarySerializer,
                  DoctorProfileSerializer, DoctorSerializer,
                  ExpertiseSerializer, InsuranceSerializer,
                  OrderDetailSerializer, OrderListSerializer, OrderSerializer,
                  PrescriptionsSerializer, ProductDetailSerializer,
                  ProductListSerializer, ProvinceSerializer,
                  RegisterSerializer, RseSerializer, SliderSerializer, TimeSer,
                  UserProfile, UserReservationSerializer, UserUpdateSerializer,
                  UserVerifySerializer)


def UniqueGenerator(length=8):
    source = "0123456789"
    result = ""
    for _ in range(length):
        result += source[random.randint(0, length)]
    return result


class CoustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [settings.APP_SCHEME, "http", "https"]


from django.conf import settings
# from zeep import Client
from django.http import HttpResponsePermanentRedirect


class CoustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [settings.APP_SCHEME, "http", "https"]


class DiscountListApiView(GenericAPIView):
    serializer_class = DiscountListSerializer

    def get(self, request):
        instance = Discount.objects.all()
        ser_data = self.serializer_class(instance, many=True).data
        return SuccessResponse(data=ser_data, status=201).send()


class ComplimentCreateView(GenericAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplimentSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.POST)
        if serialized_data.is_valid(raise_exception=True):
            text = serialized_data.validated_data["text"]
            user = self.request.user.id
            clinic = self.request.POST.get("clinic_id")
            doctor = self.request.POST.get("doctor_id")
            Complaint.objects.create(
                text=text, user_id=user, clinic_id=clinic, doctor_id=doctor
            )
            return SuccessResponse(data="success").send()

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)


class ComplimentListApiView(generics.ListAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplimentSerializer


class ComplimentDetail(GenericAPIView):
    serializer_class = ComplimentSerializer

    def get(self, request):
        id = self.request.POST.get("id")
        try:
            queryset = Complaint.objects.get(id=id)
            serializer = self.serializer_class(queryset).data
            return SuccessResponse({"compliment": serializer}).send()
        except Exception as e:
            return ErrorResponse(
                message=f"{e}", status=status.HTTP_404_NOT_FOUND
            ).send()


class ProvinceList(GenericAPIView):
    serializer_class = ProvinceSerializer
    model = Province

    def get(self, request):
        try:
            queryset = self.model.objects.all()
            ser_data = self.serializer_class(queryset, many=True).data
            return SuccessResponse({"province": ser_data}).send()
        except Exception as e:
            return ErrorResponse(
                message=f"{e}", status=status.HTTP_404_NOT_FOUND
            ).send()


class CityListApiView(GenericAPIView):
    serializer_class = CitySerializer
    model = City

    def post(self, request):
        province = request.POST.get("province")
        try:
            queryset = self.model.objects.filter(province__name=province)
            ser_data = self.serializer_class(queryset, many=True).data
            return SuccessResponse({"city": ser_data}).send()
        except Exception as e:
            return ErrorResponse(
                message=f"{e}", status=status.HTTP_404_NOT_FOUND
            ).send()


class ZoneListApiView(generics.ListAPIView):
    serializer_class = api.ser.ZoneListSerializer
    model = Zone

    def post(self, request):
        city = request.POST.get("city")
        try:
            queryst = self.model.objects.filter(city__name=city)
            serialized_data = self.serializer_class(queryst, many=True).data
            return SuccessResponse(data=serialized_data, many=True).send()
        except Exception as e:
            return ErrorResponse(
                message=f"{e}", status=status.HTTP_404_NOT_FOUND
            ).send()


class ExpertiseListApiView(generics.ListAPIView):
    serializer_class = ExpertiseSerializer
    model = Expertise

    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = DoctorFilter
    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialized_data = self.serializer_class(instance, many=True).data
            return SuccessResponse(data=serialized_data).send()
        except:
            return ErrorResponse(message="failed").send()

    def post(self, request, *args, **kwargs):
        # id=request.POST.get("pk")
        pk = request.POST.get("pk")
        try:
            instance = Doctor.objects.filter(expertise=pk)
            serialize_data = DoctorSer(instance, many=True).data
            # name = VisitTime.objects.filter(doctor=pk)
            # date = VisitTimeSerializer(name, many=True).data
            tempe_data = {
                "doctor_list": serialize_data,
                # "date_list": date,
            }
            return SuccessResponse(data=tempe_data).send()
        except Expertise.DoesNotExist as e:
            return ErrorResponse(message="Instance does not Found.", status=404).send()


class DateListApiView(generics.ListAPIView):
    def post(self, request, *args, **kwargs):
        doctor = request.POST.get("doctor_id")
        try:
            instance = VisitTime.objects.filter(doctor=doctor)
            ser_data = VisitTimeSerializer(instance, many=True).data
            return SuccessResponse(data={"data_list": ser_data}, status=201).send()
        except Exception as e:
            return ErrorResponse(
                message=f"{e}", status=status.HTTP_404_NOT_FOUND
            ).send()


# class ExpertiseListApiView(generics.ListAPIView):
#     queryset = Expertise.objects.all()
#     serializer_class = ExpertiseSerializer

# class DoctorListApiView(generics.ListAPIView):
#
#     def get(self, request, *args, **kwargs):
#         # id=request.POST.get("pk")
#         pk = request.POST.get("id")
#         try:
#             instance = Doctor.objects.filter(id=pk)
#             serialize_data = DoctorSer(instance, many=True).data
#             name = VisitTime.objects.filter(doctor=pk)
#             date = VisitTimeSerializer(name, many=True).data
#             tempe_data = {
#                 "doctor_list": serialize_data,
#                 "date_list": date,
#             }
#             return SuccessResponse(data=tempe_data).send()
#         except Expertise.DoesNotExist as e:
#             return ErrorResponse(message='Instance does not Found.', status=404).send()
from .ser import TimelistSer


class TimeListApiView(generics.ListAPIView):
    serializer_class = VisitTimeSerializer
    queryset = VisitTime.objects.all()

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("doctor_id")
        doctor = Doctor.objects.get(id=pk)
        visit_time_date = request.POST.get("date_id")
        vistime = VisitTime.objects.get(id=visit_time_date)
        ali = VisitTime.objects.all().values_list("id")
        print(ali)
        try:
            instance = VisitTime.objects.get(doctor=pk, id=visit_time_date)
            my_database = []
            my_list = []
            a = instance.start_time
            b = instance.finish_time
            check = DoctorDate.objects.filter(doctor=doctor, date=visit_time_date)
            print(check)
            if check.count() == 0:
                while True:
                    # if elyas:
                    a = a + timedelta(minutes=30)
                    my_list.append(
                        str(a.time().replace(hour=a.hour, minute=a.minute, second=00))[
                        :5
                        ]
                    )
                    name = DoctorDate.objects.create(
                        doctor=doctor,
                        date=vistime,
                        name=str(
                            a.time().replace(hour=a.hour, minute=a.minute, second=00)
                        )[:5],
                    )
                    if a >= b:
                        break

                a = instance.start_time2
                b = instance.finish_time2
                while True:
                    a = a + timedelta(minutes=30)
                    my_list.append(
                        str(a.time().replace(hour=a.hour, minute=a.minute, second=00))[
                        :5
                        ]
                    )
                    DoctorDate.objects.create(
                        doctor=doctor,
                        date=vistime,
                        name=str(
                            a.time().replace(hour=a.hour, minute=a.minute, second=00)
                        )[:5],
                    )
                    if a >= b:
                        # my_list.append(pk)
                        # my_list.append(id)
                        break

            saved = TimelistSer(instance=check, many=True).data
            for item in saved:
                my_list.append(str(item).removesuffix("name"))
            ser_data = TimeSer(instance).data
            temp_data = {
                "data": ser_data,
                "my_list": my_list,
                # "check": my_database,
            }
            return SuccessResponse(data=temp_data).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}", status=404).send()


class ReserveCreateView(generics.CreateAPIView):
    queryset = Reservation
    serializer_class = RseSerializer

    def perform_create(self, serializer):
        doctor_id = (self.request.POST.get("doctor_id"),)
        day = self.request.POST.get("day")
        DoctorDate.objects.get(doctor=doctor_id, day=day, name=day)
        DoctorDate.delete()
        serializer.save(
            day=self.request.POST.get("day"),
            time=self.request.POST.get("time"),
            doctor_id=doctor_id,
            user=self.request.user,
        )


sms = random.randint(1000, 9999) // 4


class RegisterWithPhoneNumber(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            phone_number = serialized_data.data["phone_number"]
            rand_num = random.randint(1000, 9999)
            api = KavenegarAPI(
                "38502F546846716559723175674E49324A674B2B62654B58724D61314B474777"
            )
            params = {
                "receptor": phone_number,
                "template": "dentino",
                "token": str(rand_num),
                "token2": "",
                "token3": "",
                "type": "sms",  # sms vs call
            }
            code = Code(number=str(rand_num), phone_number=phone_number)
            code.save()
            api.verify_lookup(params)
            return Response(data="send", status=201)


class VerifyUserRegister(GenericAPIView):
    serializer_class = UserVerifySerializer

    def post(self, request, *args, **kwargs):
        phone_number = request.POST.get("phone_number")
        ser_data = self.serializer_class(data=request.data)
        if ser_data.is_valid(raise_exception=True):
            code = Code.objects.filter(phone_number=phone_number).last()
            verify_code = ser_data.data["verify_code"]
            my_code = code.number
            if my_code == verify_code:
                user = User.objects.filter(username=phone_number).last()
                if user:
                    token = RefreshToken.for_user(user)
                    auth = True
                    data = {
                        "refresh": str(token),
                        "access": str(token.access_token),
                        "registerd": str(auth),
                    }
                else:
                    user = User.objects.create_user(
                        username=phone_number, password="1234"
                    )
                    token = RefreshToken.for_user(user)
                    auth = False
                    data = {
                        "refresh": str(token),
                        "access": str(token.access_token),
                        "registerd": str(auth),
                    }

                    # return HttpResponseRedirect("api:get_pro")
                return Response(status=201, data={"data": data})
            return Response(status=300)


from rest_framework_simplejwt.backends import TokenBackend


class UserProfileApiView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfile

    def get(self, request, *args, **kwargs):
        # token = self.request.META.get("HTTP_AUTHORIZATION", " ").split(" ")[1]
        # data = {"token": token}
        # valid_data = TokenBackend(algorithm="HS256").decode(token, verify=False)
        # user = valid_data["user_id"]
        # try:
        user = request.user
        por = Profile.objects.get(user=user)
        if por.national_code:
            ser_data = self.serializer_class(instance=por).data
            return SuccessResponse(data=ser_data, status=201).send()
        else:
            return ErrorResponse(message="is blank", status=410).send()


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def put(self, request, *args, **kwargs):
        token = self.request.META.get("HTTP_AUTHORIZATION", " ").split(" ")[1]
        data = {"token": token}
        valid_data = TokenBackend(algorithm="HS256").decode(token, verify=False)
        user = valid_data["user_id"]
        profile = Profile.objects.get(user=user)
        serialized_data = self.serializer_class(
            instance=profile, data=request.POST, partial=True
        )
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return SuccessResponse(data=serialized_data.data).send()

    # def perform_update(self, serializer):
    # return serializer.save(profile.is_done=True)


class DoctorListApiTest(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DoctorFilter

    def post(self, request, *args, **kwargs):
        expertise = request.POST.get("expertise_id")
        insurance = request.POST.get("insurance")
        clinic = request.POST.get("clinic_type")
        region = request.POST.get("zone")
        city = request.POST.get("city")
        # province=request.POST.get("province")
        if city and not region:
            query_set = Doctor.objects.filter(expertise=expertise, clinic__location__city__name=city)
        else:
            query_set = Doctor.objects.filter(expertise=expertise, clinic__location__name=region)

        # query_set = Doctor.objects.filter(
        # expertise=expertise, clinic__location__name=region
        # )

        if insurance and clinic:
            query_set = query_set.filter(insurance=insurance, clinic__type=clinic)
        if clinic and not insurance or None:
            query_set = query_set.filter(clinic__type=clinic)
        if insurance and not clinic:
            query_set = query_set.filter(insurance=insurance)
        ser_data = DoctorSer(query_set, many=True).data
        return SuccessResponse(data=ser_data, status=201).send()


class UserReferralCodeApiView(GenericAPIView):
    def get(self, request):
        return SuccessResponse(data=request.user.profile.referral_code).send()


#
# class DoctorListApiTest(generics.ListAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = DoctorFilter
#
#     def post(self, request, *args, **kwargs):
#         expertise = request.POST.get("expertise_id")
#         insurance = request.POST.get("insurance")
#         clinic = request.POST.get("clinic")
#         region = request.POST.get("location")
#         query_set = Doctor.objects.filter(expertise=expertise)
#         if insurance and clinic or None:
#             query_set = query_set.filter(insurance=insurance, clinic=clinic)
#             # query_set = Doctor.objects.filter(clinic=clinic, insurance=insurance)
#         if insurance and region and not clinic or None:
#             clinic = Clinic.objects.filter(location=region)
#             query_set = query_set.filter(insurance=insurance, clinic=clinic)
#             # query_set = Doctor.objects.filter(insurance=insurance)
#         if insurance and not region and not clinic or None:
#             query_set = query_set.filter(insurance=insurance)
#         if clinic and not insurance or None:
#             query_set = query_set.filter(clinic=clinic)
#         if region and not clinic and not insurance or None:
#             clinic = Clinic.objects.filter(location__id=region)
#             query_set = Doctor.objects.filter(clinic=clinic)
#
#         ser_data = DoctorSer(query_set, many=True).data
#         return SuccessResponse(data=ser_data, status=201).send()


class PrescriptionsLIST(generics.ListAPIView):
    model = Prescriptions
    serializer_class = PrescriptionsSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialized_data = self.serializer_class(instance, many=True).data
            return SuccessResponse(data=serialized_data).send()
        except:
            return ErrorResponse(message="failed").send()


class PriceList(generics.ListAPIView):
    model = Price
    serializer_class = PrescriptionsSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialized_data = self.serializer_class(instance, many=True).data
            return SuccessResponse(data=serialized_data).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}").send()


class InsuranceLIST(generics.ListAPIView):
    model = doctor.models.Insurance
    serializer_class = InsuranceSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialized_data = self.serializer_class(instance, many=True).data
            return SuccessResponse(data=serialized_data).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}").send()


class DeleteReserve(GenericAPIView):
    serializer_class = UserReservationSerializer
    model = Reservation

    def post(self, request, *args, **kwargs):
        id = request.POST.get("reserve_id")
        try:
            reserve = Reservation.objects.get(id=id)

            # reserve_time=reserve.time
            # reserve_date=reserve.day
            reserve_doctor = reserve.doctor.id
            print(reserve_doctor)
            doctor = Doctor.objects.get(id=reserve_doctor)
            reserve_date = reserve.day
            print(reserve_date)
            date = VisitTime.objects.get(id=1)
            # reserve_day = reserve.hour
            # hour = int(reserve_hour[0:2])
            # minutes = int(reserve_hour[3:5])
            # year=datetime.datetime.now().year
            # month=datetime.datetime.now().month

            # print(year)
            # print(month)
            # print(datetime.datetime.now())
            # reserved_time=datetime.datetime(year,month,hour,minutes)
            # print(f"{reserved_time} reserved time")

            # total=now_time=reserved_time
            # total=int(total)
            # reserved_time3=str(reserved_time+timedelta(hours=3))
            # print("*"*99)
            # now=str(datetime.datetime.now().hour)
            #
            # print(reserved_time3)
            # print(now)
            # if len(now) <1:
            #     "0"+now
            #     print()
            # print(reserved_time3[11:13])
            # if reserved_time3[11:13] > now[0:2]:
            #     pass
            # if total>3:
            reserve.delete()
            DoctorDate.objects.create(doctor=doctor, date=date, name=reserve.time)
            return SuccessResponse(data="نوبت شما با موفقیت حذف شد", status=201).send()
        except:
            return ErrorResponse(message="نمیتوان لغو کرذ", status=202).send()

    # except self.model.DoesNotExist:
    #     return ErrorResponse(message="نوبتی وجود ندارد").send()

    # if reserve_hour >
    # # if reserve_hour
    # print(reserve_day)
    # print(reserve_hour)

    # date=datetime.datetime(year=reserve_day[0:2],day=reserve_day[0])
    # print(reserve1)
    # print(reserve2)


class CompanyList(generics.ListAPIView):
    model = Company
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialized_data = self.serializer_class(instance, many=True).data
            return SuccessResponse(data=serialized_data).send()
        except:
            return ErrorResponse(message="failed").send()


class FilterListApiView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # try:
        insurance = Insurance.objects.all()
        insurance_ser = InsuranceSerializer(insurance, many=True).data
        clinic = Clinic.objects.all()
        clinic_ser = ClinicShortSeralizer(clinic, many=True).data
        temp_data = {
            "insurance": insurance_ser,
            "clinic": clinic_ser,
        }
        return SuccessResponse(data=temp_data, status=201).send()

    # except:
    #     return ErrorResponse(message="failed").send()


#


class About_usApiView(generics.ListAPIView):
    serializer_class = About_usSerializer
    model = About_Us

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.first()
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}").send()


class ContactUSApiView(generics.ListAPIView):
    serializer_class = ContactUsSerializer
    model = Contact_Us

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.first()
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}").send()


class SliderApiView(generics.ListAPIView):
    serializer_class = SliderSerializer
    model = Slider

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}").send()


class DoctorRetrieveView(GenericAPIView):
    serializer_class = DoctorSerializer
    model = Doctor

    def get(self, request, *args, **kwargs):
        id = request.POST.get("doctor_id")
        try:
            instance = self.model.objects.get(id=id)
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(serialize_data).send()
        except Exception as e:
            return ErrorResponse(message=f"{e}").send()


class CommonCourseApiView(generics.ListAPIView):
    serializer_class = CommonListSerializer
    model = Common_Course

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed.", status=404).send()


class ClinicListApiView(generics.ListAPIView):
    serializer_class = ClinicSerializer
    model = Clinic

    def get(self, request, *args, **kwargs):
        # try:
        instance = self.model.objects.all()
        serialize_data = self.get_serializer(instance, many=True).data
        return SuccessResponse(data=serialize_data, status=201).send()

    # except:
    #     return ErrorResponse(message="failed.", status=404).send()


class ClinicDoctorListApiView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    model = Doctor

    def post(self, request, *args, **kwargs):
        clinic = request.POST.get("clinic_id")
        try:
            instance = self.model.objects.filter(clinic=clinic)
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except Exception as e:
            return ErrorResponse(f"{e}", status=410)


class ClinicDetailApi(generics.ListAPIView):
    serializer_class = ClinicSerializer
    model = Clinic
    queryset = Clinic.objects.all()

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        try:
            instance = self.model.objects.get(id=id)
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed").send()


class DoctorProfileApi(generics.ListAPIView):
    serializer_class = DoctorProfileSerializer
    model = Doctor
    queryset = Doctor.objects.all()

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        try:
            instance = self.model.objects.get(id=id)
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed").send()


class CommonCourseDetailApi(generics.ListAPIView):
    serializer_class = CommonDetailSerializer
    model = Common_Course
    queryset = Common_Course.objects.all()

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        try:
            instance = self.model.objects.get(id=id)
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed").send()


class ProductListApiView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    model = Product

    def post(self, request, *args, **kwargs):
        try:
            category_id = request.POST.get("category_id")
            instance = self.model.objects.filter(category=category_id)
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed.", status=404).send()


class OrderCreate(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            address = serializer.data["address"]
            name = serializer.data["name"]
            family = serializer.data["family"]
            code = serializer.data["code"]
            email = serializer.data["email"]
            user = request.user
            carts = Cart.carts(user.id)
            if carts == []:
                content = {"error": "carts are empty."}
                return ErrorResponse(content, status=status.HTTP_400_BAD_REQUEST).send()
            total_price = 0
            for cart in carts:
                total_price += float(cart["product_price"])
            order = Order.objects.create(
                user=user,
                price=total_price,
                paid=False,
                address=address,
                name=name,
                family=family,
                code=code,
                email=email,
            )
            for cart in carts:
                OrderItem.objects.create(
                    product=Product.objects.get(id=cart["product_id"]),
                    order=order,
                )
            Cart.delete_all_carts(user.id)
            content = {"order_id": order.id}
            return SuccessResponse(data=content, status=status.HTTP_201_CREATED).send()

        return ErrorResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        ).send()


class CategoryListApiView(GenericAPIView):
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        instance = Category.objects.filter(parent__isnull=True)
        serialize_data = self.get_serializer(instance, many=True).data
        return SuccessResponse(data=serialize_data, status=201).send()


class WinnerApiView(GenericAPIView):
    def post(self, request):
        try:
            clinic= get_object_or_404(Clinic, name=request.POST.get("clinic"))
            expertise = request.POST.get("expertise")
            Winner.objects.create(
                user=request.user,
                clinic=clinic,
                expertise=expertise
            )
            user_profile = get_object_or_404(Profile, user=request.user)
            user_profile.referral_code = UniqueGenerator()
            user_profile.save()
            return SuccessResponse(data="created", status=201).send()
        except Exception as e:
            return ErrorResponse(message=e, status=420).send()


class SubCategoryListAPiView(GenericAPIView):
    serializer_class = CategoryListSerializer

    def post(self, request, *args, **kwargs):
        try:
            parent_id = request.POST.get("parent_id")
            instance = Category.objects.filter(parent_id=parent_id)
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed.", status=404).send()


class CatDicListApiView(generics.ListAPIView):
    serializer_class = DictCategorySer
    model = partial.models.DoctorDictionaryCategory

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed.", status=404).send()


class DoctorDictionaryListApiView(GenericAPIView):
    serializer_class = DoctorDictionarySerializer
    model = DoctorDictionary

    def post(self, request, *args, **kwargs):
        id = request.POST.get("category_id")
        try:
            instance = self.model.objects.filter(category_id=id)
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except Exception as e:
            return ErrorResponse(message=e, status=404).send()


class DoctorDictionaryDetailView(GenericAPIView):
    serializer_class = DoctorDictionarySerializer
    model = DoctorDictionary

    def post(self, request, *args, **kwargs):
        try:
            id = request.POST.get("id")
            instance = self.model.objects.filter(id=id)
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed.", status=404).send()


from django.shortcuts import render

from clinic.models import Test


def my_django_view(request):
    From = request.GET.get("From")
    To = request.GET.get("To")
    message = request.GET.get("message")
    Test.objects.create(From=From, message=message, To="asdfasdf")

    # r = requests.get(f'https://dentino.app/api/test?from=@{From}&to=@{To}&message=@{message}').json()
    # print()
    #
    # if r.status_code == 200:
    #     print(r)
    #     return HttpResponse('Yay, it worked')
    context = {"from": From, "To": To, "message": message}
    return render(request, "test.html", context=context)


class UserReserveList(GenericAPIView):
    serializer_class = UserReservationSerializer
    model = Reservation

    def get(self, request, *args, **kwargs):
        try:
            user = request.user.id
            instance = self.model.objects.filter(user=user)
            serialize_data = self.get_serializer(instance, many=True).data
            return SuccessResponse(data=serialize_data, status=201).send()
        except:
            return ErrorResponse(message="failed").send()


# class ProductDetail(GenericAPIView):
#     serializer_class = ProductDetailSerializer
#
#     def post(self, request, *args, **kwargs):
#
#         id = self.request.POST.get("id")
#         try:
#             queryset = Product.objects.get(id=id)
#             ser_data = self.serializer_class(queryset,many=True).data
#             return SuccessResponse(data=ser_data,status=201).send()
#
#         except Exception as e:
#             return ErrorResponse(message=e,status=400).send()


class ProductDetail(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    model = Product

    def post(self, request, *args, **kwargs):
        id = request.POST.get("id")
        try:
            instance = self.model.objects.get(id=id)
            serialize_data = self.get_serializer(instance).data
            return SuccessResponse(serialize_data).send()
        except:
            return ErrorResponse(message="Instance does not Found.", status=401).send()


from rest_framework.permissions import AllowAny


class paymentno(View):
    def get(self, request, *args, **kwargs):
        return render(request, "paymentno.html", {"re": settings.FRONT_END_URL})


class AddToCart(generics.GenericAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                product_id = serializer.data["product_id"]
                quantity = serializer.data["quantity"]

                product = Product.objects.get(id=product_id)
                Cart.add_to_cart(
                    user_id=request.user.id,
                    product_id=product.id,
                    product_image=str(product.image.url),
                    product_price=str(Decimal(product.price) * quantity),
                    product_quantity=quantity,
                    product__name=product.name,
                )
                content = {"success": "add to cart."}
                return SuccessResponse(content, status=status.HTTP_200_OK).send()

                # except Product.DoesNotExist:
                # content = {"error": "Product matching query does not exist."}
                # return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except:
            return ErrorResponse(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            ).send()


class DeleteCartItem(generics.GenericAPIView):
    serializer_class = DeleteCartItemSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            row_id = serializer.data["row_id"]
            Cart.delete_cart(request.user.id, row_id)
            content = {"success": "delete cart."}
            return SuccessResponse(content, status=201).send()
        else:
            return ErrorResponse(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            ).send()


class ClearCartItem(generics.GenericAPIView):
    def get(self, request):
        Cart.delete_all_carts(self.request.user.id)
        content = {"success": "clear cart."}
        return SuccessResponse(content, status=status.HTTP_204_NO_CONTENT).send()


class ListCart(generics.GenericAPIView):
    def get(self, request):
        total_price = 0
        items = Cart.carts(request.user.id)
        for item in items:
            total_price += float(item["product_price"])

        return SuccessResponse(
            {"items": items, "total_price": total_price}, status=status.HTTP_200_OK
        ).send()


# from zeep import Client


def create_custom_uuid():
    try:
        max_id = Order.objects.latest("pk").id
    except Order.DoesNotExist:
        max_id = 1
    my_id = "{}{:08d}".format("ODR", max_id if max_id is not None else 1)
    return my_id


MERCHANT = "a7388921-07b1-463a-93ab-ef2472eca1ee"
client = Client("https://www.zarinpal.com/pg/services/WebGate/wsdl")
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = "email@example.com"  # Optional
mobile = "09123456789"  # Optional
CallbackURL = (
    "https://dentino.app/api/verify/"  # Important: need to edit for realy server.
)


class ToBank(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        order_id = request.POST.get("order_id")
        try:
            order = Order.objects.get(pk=order_id)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

        amount = 1000
        result = client.service.PaymentRequest(
            MERCHANT, amount, description, email, mobile, CallbackURL
        )
        if result.Status == 100:
            authority = str(result.Authority)
            order.authority = authority
            order.save()
            print(authority)
            print(result)
            return SuccessResponse(
                data="https://www.zarinpal.com/pg/StartPay/" + str(result.Authority)
            ).send()

        else:
            content = {"detail": str(result.Status)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


from django.views.generic import View


# return HttpResponseRedirect(redirect_to=f'{star_pay_url}{authority}')


class Verify(GenericAPIView):
    def get(self, request):
        if request.GET.get("Status") == "OK":
            authority = request.GET["Authority"]
            order = Order.objects.get(authority=authority)
            amount = 1000
            result = client.service.PaymentVerification(MERCHANT, authority, amount)
            if result.Status == 100:
                order.paid = True
                order.save()
                return redirect("payment_ok")
            else:
                order.delete()
                return redirect("payment_no")
        else:
            return redirect("payment_no")


class paymentok(View):
    def get(self, request, *args, **kwargs):
        return render(request, "paymentok.html")


class paymentno(View):
    def get(self, request, *args, **kwargs):
        return render(request, "paymentno.html")


class OrderList(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = OrderListSerializer

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = self.serializer_class(orders, many=True).data
        return SuccessResponse(serializer, status=status.HTTP_200_OK).send()


class OrderDetail(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = OrderDetailSerializer

    def get(self, request):
        try:
            pk = request.POST.get("pk")
            queryset = Order.objects.get(user=request.user, pk=pk)
            serializer = self.serializer_class(instance=queryset).data
            return SuccessResponse(serializer, status=status.HTTP_200_OK).send()

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
