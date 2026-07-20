from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')),
                ('title', models.CharField(help_text='مثال: Back-end Developer', max_length=150, verbose_name='عنوان شغلی')),
                ('about_me', models.TextField(verbose_name='درباره من')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=30, verbose_name='تلفن')),
                ('location', models.CharField(blank=True, max_length=150, verbose_name='محل سکونت')),
                ('github_url', models.URLField(blank=True, verbose_name='لینک گیت‌هاب')),
                ('linkedin_url', models.URLField(blank=True, verbose_name='لینک لینکدین')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='عکس پروفایل')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام زبان')),
                ('language_type', models.CharField(choices=[('PL', 'زبان برنامه‌نویسی'), ('SP', 'زبان خارجی')], default='PL', max_length=2, verbose_name='نوع زبان')),
                ('proficiency', models.PositiveSmallIntegerField(default=70, help_text='عددی بین ۰ تا ۱۰۰', verbose_name='میزان تسلط (٪)')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب نمایش')),
            ],
            options={
                'verbose_name': 'زبان',
                'verbose_name_plural': 'زبان‌ها',
                'ordering': ['order', '-proficiency'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(help_text='مثال: کارشناسی ارشد', max_length=100, verbose_name='مقطع تحصیلی')),
                ('field_of_study', models.CharField(max_length=150, verbose_name='رشته تحصیلی')),
                ('institution', models.CharField(max_length=200, verbose_name='نام دانشگاه/موسسه')),
                ('start_date', models.CharField(help_text='مثال: Aug 2016', max_length=50, verbose_name='تاریخ شروع')),
                ('end_date', models.CharField(help_text='مثال: Apr 2021 یا در حال تحصیل', max_length=50, verbose_name='تاریخ پایان')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب نمایش')),
            ],
            options={
                'verbose_name': 'تحصیلات',
                'verbose_name_plural': 'تحصیلات',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام مهارت')),
                ('category', models.CharField(choices=[('FW', 'فریمورک / کتابخانه'), ('TL', 'ابزار'), ('DB', 'دیتابیس'), ('SF', 'مهارت نرم')], max_length=2, verbose_name='دسته‌بندی')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب نمایش')),
            ],
            options={
                'verbose_name': 'مهارت',
                'verbose_name_plural': 'توانایی‌ها',
                'ordering': ['category', 'order'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150, verbose_name='سمت')),
                ('company', models.CharField(max_length=150, verbose_name='شرکت')),
                ('start_date', models.CharField(max_length=50, verbose_name='تاریخ شروع')),
                ('end_date', models.CharField(help_text='مثال: تاکنون', max_length=50, verbose_name='تاریخ پایان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب نمایش')),
            ],
            options={
                'verbose_name': 'سابقه کاری',
                'verbose_name_plural': 'سوابق کاری',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دوره')),
                ('provider', models.CharField(max_length=150, verbose_name='برگزارکننده')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب نمایش')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره‌ها و گواهینامه‌ها',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان پروژه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('tech_stack', models.CharField(blank=True, help_text='مثال: Django, DRF, PostgreSQL', max_length=250, verbose_name='تکنولوژی‌های استفاده‌شده')),
                ('link', models.URLField(verbose_name='لینک پروژه (گیت‌هاب یا دمو)')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='ترتیب نمایش')),
            ],
            options={
                'verbose_name': 'پروژه',
                'verbose_name_plural': 'پروژه‌ها',
                'ordering': ['order'],
            },
        ),
    ]
