from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'driver_lunch_cost', 'driver_dinner_cost', 'driver_allowance', 'helper_lunch_cost',
                    'helper_dinner_cost', 'helper_allowance', 'cng_limit_per_km', 'petrol_limit_per_km',  'octane_limit_per_km', 'created_by']
    search_fields = ('name', )
    exclude = ['created_by']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['identity_no', 'vehicle_type',
                    'driver', 'helper', 'user', 'created_by']
    search_fields = ('identity_no', )
    exclude = ['created_by']


class DriverAdmin(admin.ModelAdmin):
    list_display = ['identity_no', 'name', 'salary',
                    'license_expire', 'phone_no', 'vehicle_type', 'created_by']
    search_fields = ('identity_no', )
    exclude = ['created_by']


class HelperAdmin(admin.ModelAdmin):
    list_display = ['identity_no', 'name', 'salary',
                    'phone_no', 'vehicle_type', 'created_by']
    search_fields = ('identity_no', )
    exclude = ['created_by']


class PostKmAllowenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'expense_date', 'vehicle', 'driver',
                    'helper', 'octane_expense', 'petrol_expense', 'cng_expense', 'created_by']
    search_fields = ('id', )
    exclude = ['created_by']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'vehicle', 'driver',
                    'helper', 'octane_expense', 'petrol_expense', 'cng_expense', 'created_by']
    search_fields = ('id', )
    exclude = ['created_by']


class ServiceNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', ]
    search_fields = ('name', )
    exclude = ['created_by']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicle', 'service_name',
                    'expire_date', 'expire_km', 'workshop', 'created_by']
    search_fields = ('vehicle', )
    exclude = ['created_by']


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['post', 'purpose', 'remark', 'total_ammount']
    search_fields = ('post', )
    exclude = ['created_by']


class HolidayAdmin(admin.ModelAdmin):
    list_display = ['day']
    search_fields = ('day', )
    exclude = ['created_by']

class SettingAdmin(admin.ModelAdmin):
    exclude = ['created_by']





admin.site.register(VehicleType, VehicleTypeAdmin)

admin.site.register(Driver, DriverAdmin)

admin.site.register(Helper, HelperAdmin)

admin.site.register(Vehicle, VehicleAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(PostKmAllowence, PostKmAllowenceAdmin)

admin.site.register(Expense, ExpenseAdmin)

admin.site.register(ServiceName, ServiceNameAdmin)

admin.site.register(Service, ServiceAdmin)

admin.site.register(Holiday, HolidayAdmin)

admin.site.register(Setting, SettingAdmin)