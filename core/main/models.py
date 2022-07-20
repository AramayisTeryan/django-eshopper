from django.db import models

# Create your models here.
class HomeCarusel(models.Model):
    name1 = models.CharField('Carusel name', max_length=30)
    name2 = models.CharField('Carusel name', max_length=60)
    about = models.TextField('Carusel about')
    img1 = models.ImageField('Carusel image', upload_to='media')
    img2 = models.ImageField('Carusel image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeCarusel'
        verbose_name_plural = 'HomeCarusels'

class HomeCategory(models.Model):
    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeCategory'
        verbose_name_plural = 'HomeCategories'

class HomeSubCategory(models.Model):
    homecategory = models.ForeignKey(HomeCategory, on_delete=models.CASCADE, related_name='subcateg')
    name = models.CharField('SubCategory name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeSubCategory'
        verbose_name_plural = 'HomeSubCategories'


class HomeBrand(models.Model):
    name = models.CharField('Brand name', max_length=30)
    count = models.IntegerField('Brand count', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeBrand'
        verbose_name_plural = 'HomeBrands'


class HomeFeatureItem(models.Model):
    price = models.CharField('Item price', max_length=20)
    about = models.TextField('Item about')
    img = models.ImageField('Item image', upload_to='media', null=True)
    

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = 'HomeFeatureItem'
        verbose_name_plural = 'HomeFeatureItems'

class HomeRec(models.Model):
    price = models.CharField('Rec price', max_length=20)
    about = models.TextField('Rec about')
    img = models.ImageField('Rec image', upload_to='media')

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = 'HomeRec'
        verbose_name_plural = 'HomeRecs'



class HomeBlog(models.Model):
    name2 = models.CharField('HomeBlog name2', max_length=50, null=True)
    img = models.ImageField('HomeBlog image', upload_to='media', null=True)
    about1 = models.TextField('HomeBlog about1', null=True)
    about2 = models.TextField('HomeBlog about2', null=True)

    def _str_(self):
        return self.name2

    class Meta:
        verbose_name = 'HomeBlog'
        verbose_name_plural = 'HomeBlogs'


class HeadBlog(models.Model):
    name1 = models.CharField('HeadBlog name1', max_length=30)

    def _str_(self):
        return self.name1

    class Meta:
        verbose_name = 'HeadBlog'
        verbose_name_plural = 'HeadBlogs'


class HeadFooter(models.Model):
    name = models.CharField('HeadFooter name', max_length=30)
    about = models.TextField('HeadFooter about')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'HeadFooter'
        verbose_name_plural = 'HeadFooters'


class Circle(models.Model):
    name = models.CharField('Circle name', max_length=30)
    img = models.ImageField('Circle image', upload_to='media')
    about = models.TextField('Circle about')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'Circle'
        verbose_name_plural = 'Circles'


class Map(models.Model):
    name = models.CharField('Map name', max_length=30)
    img = models.ImageField('Map image', upload_to='media')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'Map'
        verbose_name_plural = 'Maps'


class BlogSingle(models.Model):
    name1 = models.CharField('BlogSingle name1', max_length=30)
    name2 = models.CharField('BlogSingle name2', max_length=50)
    img = models.ImageField('BlogSingle image', upload_to='media')
    about1 = models.TextField('BlogSingle about1')
    about2 = models.TextField('BlogSingle about2')

    def _str_(self):
        return self.name1

    class Meta:
        verbose_name = 'BlogSingle'
        verbose_name_plural = 'BlogSingles'



class BlogDavis(models.Model):
    name = models.CharField('BlogDavis name', max_length=20)
    about = models.TextField('BlogDavis about')
    img = models.ImageField('BlogDavis image', upload_to='media')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'BlogDavis'
        verbose_name_plural = 'BlogsDavis'


class BlogJanis(models.Model):
    about = models.TextField('BlogJanis about')
    img = models.ImageField('BlogJanis image', upload_to='media')

    def _str_(self):
        return self.about

    class Meta:
        verbose_name = 'BlogeJanis'
        verbose_name_plural = 'BlogsJanis'


class HomeContact(models.Model):
    name = models.CharField('HomeContact name', max_length=30)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'HomeContact'
        verbose_name_plural = 'HomeContacts'


class ShippingBlog(models.Model):
    name = models.CharField('ShippingBlog name', max_length=50, blank=True)
    img = models.ImageField('ShippingBlog image', upload_to='media')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'ShippingBlog'
        verbose_name_plural = 'ShippingBlogs'



class ErrorBlog(models.Model):
    name = models.CharField('ErrorBlog name', max_length=50)
    img = models.ImageField('ErrorBlog image', upload_to='media')
    about = models.TextField('ErrorBlog about')

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'ErrorBlog'
        verbose_name_plural = 'ErrorBlogs'



class ShopperLogo(models.Model):
    img = models.ImageField('ShopperLogo image', upload_to='media')

    def _str_(self):
        return self.img

    class Meta:
        verbose_name = 'ShopperLogo'
        verbose_name_plural = 'ShopperLogos'


class HomeCart(models.Model):
    name1 = models.CharField('HomeCart name1', max_length=30)
    name2 = models.CharField('HomeCart name2', max_length=30)
    img = models.ImageField('HomeCart image', upload_to='media')
    about1 = models.TextField('HomeCart about1')
    about2 = models.TextField('HomeCart about2')

    def _str_(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeCart'
        verbose_name_plural = 'HomeCarts'


    
    
