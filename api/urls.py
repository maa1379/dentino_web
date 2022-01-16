from django.urls import path

from .views import (
    About_usApiView,
    AddToCart,
    CatDicListApiView,
    CategoryListApiView,
    CityListApiView,
    ClearCartItem,
    ClinicDetailApi,
    ClinicDetailApiView,
    ClinicDoctorListApiView,
    ClinicListApiView,
    ClinicLoginApiView,
    CommonCourseApiView,
    CommonCourseDetailApi,
    CompanyList,
    ComplimentCreateView,
    ComplimentDetail,
    ComplimentListApiView,
    ContactUSApiView,
    DateListApiView,
    DeleteCartItem,
    DeleteReserve,
    DiscountListApiView,
    DoctorDictionaryDetailView,
    DoctorDictionaryListApiView,
    DoctorListApiTest,
    DoctorProfileApi,
    DoctorRetrieveView,
    ExpertiseListApiView,
    FilterListApiView,
    InsuranceLIST,
    ListCart,
    OrderCreate,
    OrderList,
    PrescriptionsLIST,
    PriceList,
    ProductDetail,
    ProductListApiView,
    ProvinceList,
    RegisterWithPhoneNumber,
    ReserveCreateView,
    SliderApiView,
    SubCategoryListAPiView,
    TimeListApiView,
    ToBank,
    UpdateUserView,
    UserProfileApiView,
    UserReferralCodeApiView,
    UserReserveList,
    Verify,
    VerifyUserRegister,
    WinnerApiView,
    ZoneListApiView,
    my_django_view,
    paymentno,
    paymentok,
)

app_name = "api"

urlpatterns = [
    path("order_create/", OrderCreate.as_view(), name="order_create"),
    path("order_create/", OrderCreate.as_view(), name="order_create"),
    path("medical_login/", ClinicLoginApiView.as_view(), name="clinic_login"),
    path("clinic_panel/", ClinicDetailApiView.as_view(), name="clinic_panel"),
    path("prize/", WinnerApiView.as_view(), name="winner_api"),
    path(
        "referral_code/",
        UserReferralCodeApiView.as_view(),
        name="UserReferralCodeApiView",
    ),
    path("sub_category/", SubCategoryListAPiView.as_view(), name="sub_create"),
    path("discount/", DiscountListApiView.as_view(), name="all_discount"),
    path("testing/", paymentok.as_view(), name="order_create"),
    path("but/", paymentno.as_view(), name="order_create"),
    path("dict_category/", CatDicListApiView.as_view(), name="dict_category"),
    path("province_list/", ProvinceList.as_view(), name="province_list"),
    path("city_list/", CityListApiView.as_view(), name="city_list"),
    path("zone_list/", ZoneListApiView.as_view(), name="zone_list"),
    path("clinic_doctor/", ClinicDoctorListApiView.as_view(), name="clinic_doctor"),
    path("delete_cart/", DeleteCartItem.as_view(), name="DeleteCartItem"),
    path(
        "doctordictionarylist/",
        DoctorDictionaryListApiView.as_view(),
        name="doctordictionarylist",
    ),
    path(
        "doctordictionarydetail/",
        DoctorDictionaryDetailView.as_view(),
        name="doctordictionarydetail",
    ),
    path(
        "doctordictionarylist/",
        DoctorDictionaryListApiView.as_view(),
        name="doctordictionarylist",
    ),
    path(
        "doctordictionarydetail/",
        DoctorDictionaryDetailView.as_view(),
        name="doctordictionarydetail",
    ),
    path("bank/", ToBank.as_view(), name="bank"),
    path("verify/", Verify.as_view(), name="bank"),
    path("exertise/", ExpertiseListApiView.as_view(), name="Home"),
    path("time/", TimeListApiView.as_view(), name="list"),
    path("reserve/", ReserveCreateView.as_view(), name="reserve_create"),
    path("update_profile/", UpdateUserView.as_view(), name="update"),
    path("verify_user_register/", VerifyUserRegister.as_view(), name="verify"),
    path("register/", RegisterWithPhoneNumber.as_view(), name="register"),
    path("date_list/", DateListApiView.as_view(), name="date_list"),
    path("doctor_filter/", DoctorListApiTest.as_view(), name="Doctor_filter"),
    path("Prescriptions/", PrescriptionsLIST.as_view(), name="Prescriptions"),
    path("filter_list/", FilterListApiView.as_view(), name="filter_list"),
    path("slider/", SliderApiView.as_view(), name="slider"),
    path("contact_us/", ContactUSApiView.as_view(), name="contact_us"),
    path("about_us/", About_usApiView.as_view(), name="about_us"),
    path("doctorProfile/", DoctorRetrieveView.as_view(), name="doctor_detail"),
    path("insurance/", InsuranceLIST.as_view(), name="insurance_list"),
    path("company/", CompanyList.as_view(), name="company_list"),
    path("price/", PriceList.as_view(), name="price_list"),
    path("common_course/", CommonCourseApiView.as_view(), name="common_course_list"),
    path(
        "common_course_detail/",
        CommonCourseDetailApi.as_view(),
        name="common_course_detail",
    ),
    path("slider/", SliderApiView.as_view(), name="slider_list"),
    path("about_us/", About_usApiView.as_view(), name="about_us"),
    path("contact_us/", ContactUSApiView.as_view(), name="contact_us"),
    path("test/<From>/<To>/<message>", my_django_view, name="test"),
    path("get_profile/", UserProfileApiView.as_view(), name="get_pro"),
    path("clinic_list/", ClinicListApiView.as_view(), name="clinic_list"),
    path("clinic_detail/", ClinicDetailApi.as_view(), name="clinic_detail"),
    path("doctor_profile/", DoctorProfileApi.as_view(), name="doctor_profile"),
    path("reserve_list/", UserReserveList.as_view(), name="reserve_list"),
    path("product_list/", ProductListApiView.as_view(), name="product_list"),
    path("category_list/", CategoryListApiView.as_view(), name="category_list"),
    path("product_detail/", ProductDetail.as_view(), name="product_detail"),
    path("AddToCart/", AddToCart.as_view(), name="AddToCart"),
    path("ListCart/", ListCart.as_view(), name="ListCart"),
    path("ClearCartItem/", ClearCartItem.as_view(), name="ClearCartItem"),
    path(
        "compliment_create/", ComplimentCreateView.as_view(), name="Compliment_Create"
    ),
    path("compliment_detail/", ComplimentDetail.as_view(), name="Compliment_Detail"),
    path("compliment_list/", ComplimentListApiView.as_view(), name="Compliment_list"),
    path("reserve_delete/", DeleteReserve.as_view(), name="DeleteReserve"),
    path("order_list/", OrderList.as_view(), name="order_list"),
    # path("location/", ZoneListApiView.as_view(), name="location"),
]
