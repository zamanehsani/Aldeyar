from django.db import models

class Bread(models.Model):
    package = models.CharField(max_length=200, null=True, blank=True)
    price   = models.PositiveSmallIntegerField()
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bread"

    def __str__(self):
        return self.package


# this is for Farsi resturant client
class Farsi(models.Model):
    Farsi_package = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.PositiveIntegerField()
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Farsi"
    def __str__(self):
        return self.Farsi_package.package

# this is for BBQ reesturant client
class BBQ(models.Model):
    bbq_package = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.PositiveIntegerField()
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "BBQ"

    def __str__(self):
        return self.bbq_package.package

# this is for Dakhal (nan sold in the store)
class Dakhal(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.PositiveIntegerField()
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Dakhal"
    def __str__(self):
        return self.bread.package


# this is for Dakhal (nan sold in the store)
class Siraj(models.Model):
    bread = models.ForeignKey(Bread, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    price   = models.PositiveIntegerField()
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
    unit_type = models.CharField(max_length=150, null=True, blank=True, choices=options)
    Unit_price = models.DecimalField(max_digits=8, decimal_places=3)
    totol_price = models.DecimalField(max_digits=8, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Expenses"
    
    def __str__(self):
        return self.name

# what the store member eat
class Staff_Expenses(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    totol_price = models.DecimalField(max_digits=8, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Staff Expenses"
    
    def __str__(self):
        return self.name

# what the store member eat
class Staff_Salary(models.Model):
    months = (('January', 'January'),('February', 'February'),('March', 'March'),('April', ' April'), 
              ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'),
              ('October', 'October'), ('November', 'November'), ('December', 'December'))

    name = models.CharField(max_length=300, null=True, blank=True)
    salary = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    month  = models.CharField(max_length=150, null=True, blank=True, choices=months)
    Pay  = models.DecimalField(max_digits=8, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Staff Salary"
    
    def __str__(self):
        return self.name + " - " + self.month

class Rent(models.Model):
    option = (('Shop', 'Shop'), ('Room', 'Room'))
    months = (('January', 'January'),('February', 'February'),('March', 'March'),('April', ' April'), 
              ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'),
              ('October', 'October'), ('November', 'November'), ('December', 'December'))
    rent = models.CharField(max_length=150, null=True, blank=True, choices=option )
    month = models.CharField(max_length=150, null=True, blank=True, choices=months)
    Pay  = models.DecimalField(max_digits=8, decimal_places=3)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Rent"
    
    def __str__(self):
        return self.rent + " - " + self.month