from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.core.files.storage import default_storage as storage

def upload_location(instance, filename):
    return 'profiles/{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField("tell me about yourself",null=True, blank=True)
    phone = models.PositiveIntegerField("what is your phone?",null=True, blank=True)
    address = models.CharField("where do you live?",max_length=500,null=True, blank=True)
    photo = models.ImageField("Upload a square picture of yourself.",default='default.png', upload_to = upload_location, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.photo.path)
    #     if img.height > 400 or img.width > 400:
    #         output_size = (400,400)
    #         img.thumbnail(output_size)
    #         img.save(user.photo.path)
    #         print("your photo was large, so we resized and saved")

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile')

class Bread(models.Model):
    package = models.CharField(max_length=200, null=True, blank=True)
    price   = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name_plural = "Bread"

    def __str__(self):
        return self.package
    
    def get_absolute_url(self):
        return reverse('bread')

# this is the model for all orders in cluding seraj, farsi ...
class Sale(models.Model):
    user    = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    bread   = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity= models.PositiveSmallIntegerField()
    cleint  = models.CharField(max_length=200, null=True, blank=True)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sale"
    def __str__(self):
        return '%s %s' % (self.bread, self.quantity)

    def get_absolute_url(self):
        return reverse('sale')

# this is for Farsi resturant client
class Farsi(models.Model):
    Farsi_package = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Farsi"
    def __str__(self):
        return self.Farsi_package.package

# this is for BBQ reesturant client
class BBQ(models.Model):
    bbq_package = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "BBQ"

    def __str__(self):
        return self.bbq_package.package

# this is for Dakhal (nan sold in the store)
class Dakhal(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Dakhal"
    def __str__(self):
        return self.bread.package

# this is for Dakhal (nan sold in the store)
class Siraj(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Siraj"

    def __str__(self):
        return self.bread.package

# for the expenses of the store (what you spend for store)
class Expenses(models.Model):
    options = (('Piece', 'Piece'),('KG', 'KG'),('Liter', 'Liter'),('Gallon', ' Gallon'), ('Package', 'Package'))
    name = models.CharField(max_length=300, null=True, blank=True)
    quantity = models.SmallIntegerField()
    unit_type = models.CharField(max_length=150, null=True, blank=True, default="Piece", choices=options)
    Unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    totol_price = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = "Expenses"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('expense')

# what the store member eat
class Staff_Expenses(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    totol_price = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = "Staff Expenses"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('staff_expense')

# what the store member eat
class Staff_Salary(models.Model):
    months = (('January', 'January'),('February', 'February'),('March', 'March'),('April', ' April'), 
              ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'),
              ('October', 'October'), ('November', 'November'), ('December', 'December'))

    pay_by  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name    = models.CharField(max_length=300, null=True, blank=True)
    salary  = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    month   = models.CharField(max_length=150, null=True, blank=True, choices=months)
    Pay     = models.DecimalField(max_digits=10, decimal_places=3)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Staff Salary"
    
    def __str__(self):
        return self.name + " - " + self.month
    
    def get_absolute_url(self):
        return reverse('salary')

class Rent(models.Model):
    option = (('Shop', 'Shop'), ('Room', 'Room'))
    months = (('January', 'January'),('February', 'February'),('March', 'March'),('April', ' April'), 
              ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'),
              ('October', 'October'), ('November', 'November'), ('December', 'December'))
    rent = models.CharField(max_length=150, null=True, blank=True, choices=option )
    month = models.CharField(max_length=150, null=True, blank=True, choices=months)
    Pay  = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Rent"
    
    def __str__(self):
        return self.rent + " - " + self.month
    
    def get_absolute_url(self):
        return reverse('rent')