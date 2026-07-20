from django.db import models


class Profile(models.Model):
    """بخش بیوگرافی و اطلاعات تماس (Singleton - فقط یک رکورد باید وجود داشته باشد)"""
    full_name = models.CharField('نام و نام خانوادگی', max_length=150)
    title = models.CharField('عنوان شغلی', max_length=150, help_text='مثال: Back-end Developer')
    about_me = models.TextField('درباره من')
    email = models.EmailField('ایمیل')
    phone = models.CharField('تلفن', max_length=30)
    location = models.CharField('محل سکونت', max_length=150, blank=True)
    github_url = models.URLField('لینک گیت‌هاب', blank=True)
    linkedin_url = models.URLField('لینک لینکدین', blank=True)
    photo = models.ImageField('عکس پروفایل', upload_to='profile/', blank=True, null=True)

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل'

    def __str__(self):
        return self.full_name


class Language(models.Model):
    """زبان‌های برنامه‌نویسی / زبان‌های خارجی"""

    class LanguageType(models.TextChoices):
        PROGRAMMING = 'PL', 'زبان برنامه‌نویسی'
        SPOKEN = 'SP', 'زبان خارجی'

    name = models.CharField('نام زبان', max_length=100)
    language_type = models.CharField(
        'نوع زبان', max_length=2, choices=LanguageType.choices, default=LanguageType.PROGRAMMING
    )
    proficiency = models.PositiveSmallIntegerField(
        'میزان تسلط (٪)', default=70, help_text='عددی بین ۰ تا ۱۰۰'
    )
    order = models.PositiveSmallIntegerField('ترتیب نمایش', default=0)

    class Meta:
        verbose_name = 'زبان'
        verbose_name_plural = 'زبان‌ها'
        ordering = ['order', '-proficiency']

    def __str__(self):
        return self.name


class Education(models.Model):
    """بخش تحصیلات"""
    degree = models.CharField('مقطع تحصیلی', max_length=100, help_text='مثال: کارشناسی ارشد')
    field_of_study = models.CharField('رشته تحصیلی', max_length=150)
    institution = models.CharField('نام دانشگاه/موسسه', max_length=200)
    start_date = models.CharField('تاریخ شروع', max_length=50, help_text='مثال: Aug 2016')
    end_date = models.CharField('تاریخ پایان', max_length=50, help_text='مثال: Apr 2021 یا در حال تحصیل')
    order = models.PositiveSmallIntegerField('ترتیب نمایش', default=0)

    class Meta:
        verbose_name = 'تحصیلات'
        verbose_name_plural = 'تحصیلات'
        ordering = ['order']

    def __str__(self):
        return f'{self.degree} - {self.field_of_study}'


class Skill(models.Model):
    """بخش توانایی‌ها (فریمورک‌ها، ابزارها، دیتابیس‌ها و ...)"""

    class SkillCategory(models.TextChoices):
        FRAMEWORK = 'FW', 'فریمورک / کتابخانه'
        TOOL = 'TL', 'ابزار'
        DATABASE = 'DB', 'دیتابیس'
        SOFT = 'SF', 'مهارت نرم'

    name = models.CharField('نام مهارت', max_length=100)
    category = models.CharField('دسته‌بندی', max_length=2, choices=SkillCategory.choices)
    order = models.PositiveSmallIntegerField('ترتیب نمایش', default=0)

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'توانایی‌ها'
        ordering = ['category', 'order']

    def __str__(self):
        return self.name


class Experience(models.Model):
    """بخش سوابق کاری (تکمیلی)"""
    role = models.CharField('سمت', max_length=150)
    company = models.CharField('شرکت', max_length=150)
    start_date = models.CharField('تاریخ شروع', max_length=50)
    end_date = models.CharField('تاریخ پایان', max_length=50, help_text='مثال: تاکنون')
    description = models.TextField('توضیحات')
    order = models.PositiveSmallIntegerField('ترتیب نمایش', default=0)

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سوابق کاری'
        ordering = ['order']

    def __str__(self):
        return f'{self.role} @ {self.company}'


class Course(models.Model):
    """بخش دوره‌ها و گواهینامه‌ها (تکمیلی)"""
    title = models.CharField('عنوان دوره', max_length=200)
    provider = models.CharField('برگزارکننده', max_length=150)
    order = models.PositiveSmallIntegerField('ترتیب نمایش', default=0)

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره‌ها و گواهینامه‌ها'
        ordering = ['order']

    def __str__(self):
        return self.title


class Project(models.Model):
    """بخش پروژه‌ها"""
    title = models.CharField('عنوان پروژه', max_length=200)
    description = models.TextField('توضیحات')
    tech_stack = models.CharField('تکنولوژی‌های استفاده‌شده', max_length=250, blank=True,
                                   help_text='مثال: Django, DRF, PostgreSQL')
    link = models.URLField('لینک پروژه (گیت‌هاب یا دمو)')
    order = models.PositiveSmallIntegerField('ترتیب نمایش', default=0)

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'
        ordering = ['order']

    def __str__(self):
        return self.title
