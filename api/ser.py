from django.contrib.auth import get_user_model
from django.utils.html import format_html
from rest_framework import serializers

from account.models import Profile
from clinic.models import Clinic
from commoncourse.models import Common_Course
from config.models import About_Us, Contact_Us, Slider
from doctor.models import Discount, Doctor, Expertise, Insurance, VisitTime
from location.models import City, Province, Zone
from partial.models import (
    Company,
    Complaint,
    DoctorDictionary,
    DoctorDictionaryCategory,
    Prescriptions,
    Price,
)
from shop.models import Category, Product

user = get_user_model()


class ClinicRegister(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class DiscountListSerializer(serializers.ModelSerializer):
    clinic_name = serializers.SerializerMethodField()
    expertise_name = serializers.SerializerMethodField()

    class Meta:
        model = Discount
        fields = ("clinic_name", "percent", "expertise_name")

    def get_clinic_name(self, obj):
        return obj.clinic.name

    def get_expertise_name(self, obj):
        return obj.expertise.title


class DiscountCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ("percent", "expertise")


class DiscountClinicSerializer(serializers.ModelSerializer):
    clinic_name = serializers.SerializerMethodField()
    expertise_name = serializers.SerializerMethodField()

    class Meta:
        model = Discount
        fields = ("clinic_name", "expertise_name")

    def get_clinic_name(self, obj):
        return obj.clinic.name

    def get_expertise_name(self, obj):
        return obj.expertise.title


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ("name", "id")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("province", "name", "id")


class ZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ("city", "name", "id")


class DoctorDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDictionary
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "icon", "id")


class ComplimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ("text",)


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class DeleteCartItemSerializer(serializers.Serializer):
    row_id = serializers.CharField(max_length=150)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "image",
            "category",
            "sell",
            "discount_percent",
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "price",
            "image",
            "image",
            "image2",
            "image3",
            "image4",
            "description",
            "created",
            "phone_number",
            "address",
            "category",
            "id",
            "discount_percent",
        )


class DictCategorySer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDictionaryCategory
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "id")


class CommonListSerializer(serializers.ModelSerializer):
    # obj_video=serializers.SerializerMethodField()
    class Meta:
        model = Common_Course
        fields = "__all__"


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        depth = 1


class CommonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common_Course
        fields = "__all__"


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ("title", "id", "image")


# class ExpertiseSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     id = serializers.IntegerField()
#     image = serializers.ImageField(use_url=True)


class DoctorListSerializers(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ("id", "full_name", "expertise", "clinic", "image", "star_count")

    def get_star_count(self, obj):
        return obj.star / 5


class VisitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitTime
        fields = ("id", "date", "doctor")


class TimeSer(serializers.ModelSerializer):
    class Meta:
        model = VisitTime
        fields = "__all__"

    #
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['doctor'] = DoctorTest(instance.doctor).data
    #     return response

    # def to_representation(self, obj):
    #     data = super().to_representation(obj)
    #     return data


# class ExpertiseDetailSerializer():
#    doctor_list=
#    class Meta:
#       model=Expertise
#       fields=("")


class Test(serializers.Serializer):
    time = serializers.DateTimeField()


from rest_framework import serializers

from reservation.models import Reservation


class RseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "name",
            "family",
            "phone_number",
            "national_code",
        )


from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11)


class UserVerifySerializer(serializers.Serializer):
    verify_code = serializers.CharField()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("name", "family", "national_code")


class UserProfile(serializers.ModelSerializer):
    invited_user_count = serializers.ReadOnlyField()
    user_score = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = (
            "name",
            "family",
            "national_code",
            "is_done",
            "invite_code",
            "referral_code",
            "invited_user_count",
            "user_score",
        )


class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = "__all__"


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ("name", "image", "id")


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ("title", "price")


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("title", "id")


class ClinicSerializer(serializers.ModelSerializer):
    companies = serializers.SerializerMethodField()
    zone_name = serializers.SerializerMethodField()
    insurances = serializers.SerializerMethodField()
    clinic_description = serializers.SerializerMethodField()
    clinic_discount = serializers.SerializerMethodField()

    class Meta:
        model = Clinic

        fields = (
            "name",
            "logo",
            "address",
            "instagram",
            "phone_number",
            "clinic_description",
            "image1",
            "image2",
            "image3",
            "location",
            "type",
            "insurances",
            "zone_name",
            "companies",
            "insurances",
            "id",
            "clinic_discount",
        )

        # fields = (
        #     "name",
        #     "logo",
        #     "address",
        #     "instagram",
        #     "phone_number",
        #     "clinic_description",
        #     "image1",
        #     "image2",
        #     "image3",
        #     "location",
        #     "type",
        #     "insurances",
        #     "zone_name",
        #     "companies",
        #     "insurances",
        # )

    def get_clinic_description(self, obj):
        return format_html(obj.description)

    def get_companies(self, obj):
        return CompanySerializer(obj.company.all(), many=True).data

    def get_insurances(self, obj):
        insurance = Insurance.objects.filter(doctor__clinic=obj)
        return InsuranceSerializer(insurance, many=True).data

    def get_zone_name(self, obj):
        return obj.location.name

    def get_clinic_discount(self, obj):
        discount = Discount.objects.filter(clinic=obj)
        return DiscountClinicSerializer(discount, many=True).data


class ClinicPanelSerializer(serializers.ModelSerializer):
    companies_number = serializers.SerializerMethodField()
    # insurances_number = serializers.SerializerMethodField()
    clinic_discount_number = serializers.SerializerMethodField()
    doctor_number = serializers.SerializerMethodField()
    reservtion_number = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = (
            "name",
            "companies_number",
            "clinic_discount_number",
            "doctor_number",
            "reservtion_number",
        )

    def get_companies_number(self, obj):
        return obj.company.all().count()

    def get_reservtion_number(self, obj):
        return Reservation.objects.filter(doctor__clinic=obj).count()

    def get_doctor_number(self, obj):
        return obj.discount.all().count()

    #
    # def get_insurances_number(self, obj):
    #     return obj.doctor.insurance.all().count()

    def get_clinic_discount_number(self, obj):
        return obj.discount.all().count()


class ClinicShortSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ("id", "name", "type")


class TimelistSer(serializers.Serializer):
    name = serializers.CharField(max_length=125)


class About_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Slider
        fields = "__all__"

    def get_picture(self, obj):
        return obj.picture.url


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        depth = 1


class clinicLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()


# class UserSerializer(serializers.Serializer):
#     name = serializers.CharField(min_length=3, max_length=30, required=False)
#     family = serializers.CharField(min_length=3, max_length=30, required=False)
#     birthday = serializers.CharField(max_length=200, required=False, validators=[utilities.check_file_exist])
#     facebook = serializers.ReadOnlyField()
#     linkedin = serializers.ReadOnlyField()
#     twitter = serializers.ReadOnlyField()
#     nick_name = serializers.SlugField(max_length=150)
#     biography = serializers.CharField(max_length=2000, min_length=10, required=False)
#     admin_of_company = serializers.ReadOnlyField()
#
#     def update(self, instance, validated_data):
#         nick_name = validated_data.get('nick_name')
#         instance.profile.nick_name = nick_name
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.profile.profile_image = validated_data.get('profile_image', instance.profile.profile_image)
#         instance.profile.biography = validated_data.get('biography', instance.profile.biography)
#         instance.save()
#         return instance
class UserReservationSerializer(serializers.ModelSerializer):
#     dr_cl = serializers.SerializerMethodField()
    dr_cl_name = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
#     doctor_id = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            "id",
            "name",
            "family",
            "phone_number",
            "national_code",
            "user",
            "day",
            "time",
            "created",
#             "dr_cl",
            "dr_cl_name",
            "doctor_name",
#             "doctor_id",
        )

#     def get_dr_cl(self, obj):
#         doctor_clinic = Clinic.objects.filter(name=obj.doctor.clinic.name)
#         return ClinicSerializer(doctor_clinic).data

    def get_dr_cl_name(self, obj):
        return obj.doctor.clinic.name

    def get_doctor_name(self, obj):
        return obj.doctor.full_name

#     def get_doctor_id(self, obj):
#         return object.doctor


from rest_framework import serializers

from order.models import Order, OrderItem


class CompareAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)


class OrderUpdateRemittance(serializers.Serializer):
    image = serializers.ImageField()
    pk = serializers.IntegerField()


class OrderAdvertisingSerializer(serializers.ModelSerializer):
    advertising_id = serializers.IntegerField()
    proposal_provider_id = serializers.IntegerField()

    class Meta:
        model = Order
        exclude = [
            "size",
            "color",
            "is_advertising",
            "user",
            "email",
            "create",
            "update",
            "paid",
            "total_price",
            "accepted",
            "posted",
            "order_code",
            "provider",
            "authority",
        ]


class OrderSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=125)
    family = serializers.CharField(max_length=125)
    email = serializers.EmailField(max_length=125)
    code = serializers.CharField(max_length=250)


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        exclude = ["user"]

    def get_products(self, obj):
        result = OrderItem.objects.filter(order_id=obj)
        return OrderItemSerializer(instance=result, many=True).data


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def get_product(self, obj):
        result = obj.product
        # return ProductsOrderCartSerializer(instance=result).data


class ClinicDetailSerializer(serializers.ModelSerializer):
    clinic_doctor_count = serializers.SerializerMethodField()
    clinic_discount_count = serializers.SerializerMethodField()
    expertise_count = serializers.SerializerMethodField()
    clinic_reserve_count = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = (
            "name",
            "clinic_doctor_count",
            "clinic_discount_count",
            "expertise_count",
            "clinic_reserve_count",
        )

    def get_clinic_doctor_count(self, obj):
        return Doctor.objects.filter(clinic=obj).count()

    def get_clinic_discount_count(self, obj):
        return Discount.objects.filter(clinic=obj).count()

    def get_expertise_count(self, obj):
        return Expertise.objects.filter(doctor__clinic=obj).count()

    def get_clinic_reserve_count(self, obj):
        return Reservation.objects.filter(doctor__clinic=obj).count()


from drf_extra_fields.fields import Base64ImageField


class DoctorCreateSerializer(serializers.ModelSerializer):
    expertise = serializers.CharField()
    insurance = serializers.CharField()
    clinic = serializers.CharField()
    profile = Base64ImageField()
    parvaneh_tebabat = Base64ImageField()
    ID_photo = Base64ImageField()

    class Meta:
        model = Doctor
        fields = (
            "name",
            "family",
            "national_code",
            "phone_number",
            "ID_photo",
            "profile",
            "medical_code",
            "insurance",
            "expertise",
            "bio",
            "age",
            "parvaneh_tebabat",
            "clinic"
        )

        # def create(self, validated_data):
        #     clinic = validated_data.pop('clinic', None)
        #     insurance=validated_data.pop('insurance',None)
        #     expertise=validated_data.pop('expertise',None)
        # # Create relations
        #     for cli in clinic:
        #         Doctor.clinic.add(Clinic.objects.get(id=cli), **validated_data)
        #     return clinic
        #
        #     for insu in insurance:
        #         Doctor.insurance.add(Insurance.objects.get(id=insu),**validated_data)
        #     return insurance
        #
        #     for exp in expertise:
        #         Doctor.expertise.add(Expertise.objects.get(id=exp),**validated_data)
        #     return expertise
