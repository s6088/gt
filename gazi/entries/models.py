from django.db import models
from django.conf import settings



LICENSE_CATEGORY = (
    ('high', 'Created'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)


SERVICE_TYPE = (
    ('date', 'Date'),
    ('km', 'KM'),
    ('both', 'Both'),
)


class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    driver_lunch_cost = models.DecimalField(decimal_places=2, max_digits=20)
    driver_dinner_cost = models.DecimalField(decimal_places=2, max_digits=20)
    driver_allowance = models.DecimalField(decimal_places=2, max_digits=20)
    helper_lunch_cost = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    helper_dinner_cost = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    helper_allowance = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    petrol_limit_per_km = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    octane_limit_per_km = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    cng_limit_per_km = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  default=True, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Driver(models.Model):
    identity_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2, max_digits=20)
    joining_date = models.DateField( null=True, blank=True)
    license_expire = models.DateField( null=True, blank=True)
    license_category = models.CharField(max_length=50, default='low', choices=LICENSE_CATEGORY, null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  default=True, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.identity_no

class Helper(models.Model):
    identity_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2, max_digits=20)
    joining_date = models.DateField( null=True, blank=True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  default=True, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.identity_no


class Vehicle(models.Model):
    identity_no = models.CharField(max_length=20)
    vehicle_type =  models.ForeignKey(VehicleType, on_delete=models.CASCADE)  
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE, null=True, blank=True)
    body_maker = models.CharField(max_length=100, null=True, blank=True)
    engine_no = models.CharField(max_length=100, null=True, blank=True)
    body_making_date = models.DateField( null=True, blank=True)
    purchase_date = models.DateField( null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    registration_date = models.DateField( null=True, blank=True)
    registration_no = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  default=True, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.identity_no

class PostKmAllowence(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    expense_date = models.DateField( null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE, null=True, blank=True)
    starting_km = models.DecimalField(decimal_places=2, max_digits=20)
    ending_km = models.DecimalField(decimal_places=2, max_digits=20)
    octane_expense = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    petrol_expense = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    cng_expense = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  default=True, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE, null=True, blank=True)
    starting_km = models.DecimalField(decimal_places=2, max_digits=20)
    ending_km = models.DecimalField(decimal_places=2, max_digits=20)
    user = models.CharField(max_length=100, null=True, blank=True)
    started_from = models.CharField(max_length=100, null=True, blank=True)
    destination = models.CharField(max_length=100, null=True, blank=True)
    octane_expense = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    petrol_expense = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    cng_expense = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  default=True, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)

class Expense(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    expense_date = models.DateTimeField( null=True, blank=True)
    purpose = models.CharField(max_length=100)
    memo_no  = models.CharField(max_length=100, null=True, blank=True)
    remark  = models.CharField(max_length=100, null=True, blank=True)
    total_ammount = models.DecimalField(decimal_places=2, max_digits=20)
    expected_ammount = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,  default=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.purpose


class ServiceName(models.Model):
    name =  models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, default='date', choices=SERVICE_TYPE, null=True,   blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,  default=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Setting(models.Model):
    lunch_time_starts = models.TimeField(null=True,  blank=True)
    lunch_time_ends = models.TimeField(null=True,  blank=True)
    dinner_time_starts = models.TimeField(null=True,  blank=True)
    dinner_time_ends = models.TimeField(null=True,  blank=True)
    work_time_starts = models.TimeField(null=True,  blank=True)
    work_time_ends = models.TimeField(null=True,  blank=True)
    minimum_hrs_count_as_say = models.PositiveIntegerField(default=8,null=True,  blank=True)
    days_in_month = models.CharField(max_length=255, null=True,  blank=True)
    company_address = models.CharField(max_length=255,null=True,  blank=True)
    prepared_by = models.CharField(max_length=255, null=True,  blank=True)
    recomended_by = models.CharField(max_length=255, null=True,  blank=True)
    approved_by = models.CharField(max_length=255, null=True,  blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,  default=True, blank=True, on_delete=models.SET_NULL)

    


class Holiday(models.Model):
    day = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=True, on_delete=models.SET_NULL)


class Service(models.Model):
    servicing_date = models.DateTimeField( null=True, blank=True)
    expire_date = models.DateTimeField( null=True, blank=True)
    expire_km = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    service_name = models.ForeignKey(ServiceName, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    workshop = models.CharField(max_length=100, null=True, blank=True)
    service_charge = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)



def save_model(self, request, obj, form, change):
    if not obj.pk:
        obj.added_by = request.user
    super().save_model(request, obj, form, change)
