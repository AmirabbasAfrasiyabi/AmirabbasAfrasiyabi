from django.db import migrations


def seed_data(apps, schema_editor):
    Profile = apps.get_model('resume', 'Profile')
    Language = apps.get_model('resume', 'Language')
    Education = apps.get_model('resume', 'Education')
    Skill = apps.get_model('resume', 'Skill')
    Experience = apps.get_model('resume', 'Experience')
    Course = apps.get_model('resume', 'Course')
    Project = apps.get_model('resume', 'Project')

    Profile.objects.create(
        full_name='Amirabbas Afrasiabi',
        title='Back-end Developer',
        about_me=(
            'به عنوان یک برنامه‌نویس بک‌اند جونیور و دارای مدرک کارشناسی ارشد مهندسی مکانیک، '
            'علاقه‌ی عمیقی به حل مسائل پیچیده و یادگیری مستمر دارم. تخصص من شامل پایتون، جنگو، '
            'جنگو رست فریمورک و جاوااسکریپت است. توانایی حل مسئله به من کمک می‌کند چالش‌های فنی '
            'پیچیده را با خلاقیت و پشتکار حل کنم و همیشه به دنبال چالش‌های جدید برای تاثیرگذاری مثبت هستم.'
        ),
        email='abb.afrasiyabi@gmail.com',
        phone='0912-091-0309',
        location='Iran',
        github_url='https://github.com/',
        linkedin_url='',
    )

    languages = [
        ('Python', 'PL', 90, 1),
        ('JavaScript', 'PL', 70, 2),
        ('Java', 'PL', 50, 3),
        ('MATLAB', 'PL', 60, 4),
    ]
    for name, ltype, prof, order in languages:
        Language.objects.create(name=name, language_type=ltype, proficiency=prof, order=order)

    Education.objects.create(
        degree='کارشناسی ارشد', field_of_study='مهندسی مکانیک',
        institution='دانشگاه آزاد اسلامی، واحد علوم و تحقیقات',
        start_date='Dec 2020', end_date='Oct 2024', order=1,
    )
    Education.objects.create(
        degree='کارشناسی', field_of_study='مهندسی مکانیک',
        institution='دانشگاه آزاد اسلامی، واحد علوم و تحقیقات',
        start_date='Aug 2016', end_date='Apr 2021', order=2,
    )

    skills = [
        ('Django', 'FW', 1), ('Django REST Framework', 'FW', 2), ('React', 'FW', 3),
        ('Git', 'TL', 1), ('Docker', 'TL', 2), ('Jira', 'TL', 3), ('Trello', 'TL', 4), ('REST API', 'TL', 5),
        ('MySQL', 'DB', 1), ('NoSQL', 'DB', 2), ('PostgreSQL', 'DB', 3),
    ]
    for name, cat, order in skills:
        Skill.objects.create(name=name, category=cat, order=order)

    Experience.objects.create(
        role='Junior Back-end Developer', company='Iranwellness',
        start_date='Apr 2024', end_date='تاکنون',
        description=(
            'توسعه پروژه‌ها با پایتون، جنگو و DRF؛ تبدیل اپلیکیشن‌ها از جاوااسکریپت به پایتون؛ '
            'بهبود کوئری‌های دیتابیس در پلتفرم Iranwellness (صنعت زیبایی و سلامت).'
        ),
        order=1,
    )
    Experience.objects.create(
        role='Intern Back-end Developer', company='Quera',
        start_date='Jan 2024', end_date='Apr 2024',
        description=(
            'کارآموزی بک‌اند در بوت‌کمپ کوئرا، در تیمی ۴ نفره؛ تمرکز بر مفاهیم پایه مهندسی نرم‌افزار، '
            'بهبود طراحی الگوریتم و مدیریت دیتابیس، و استفاده گسترده از Django REST Framework، '
            'قالب‌های جنگو و اصول REST API.'
        ),
        order=2,
    )

    courses = [
        ('بوت‌کمپ کارآموزی مهندسی نرم‌افزار با جنگو', 'Quera', 1),
        ('برنامه‌نویسی با پایتون', 'MFTplus', 2),
        ('Python for Beginners', 'Sololearn', 3),
    ]
    for title, provider, order in courses:
        Course.objects.create(title=title, provider=provider, order=order)

    Project.objects.create(
        title='وبسایت رزومه (این پروژه)',
        description=(
            'یک وبسایت رزومه‌ی داینامیک ساخته‌شده با جنگو که تمام اطلاعات (زبان‌ها، تحصیلات، '
            'توانایی‌ها، سوابق کاری و پروژه‌ها) از طریق پنل ادمین جنگو مدیریت می‌شود.'
        ),
        tech_stack='Django, SQLite, HTML, CSS',
        link='https://github.com/your-username/django-cv-project',
        order=1,
    )


def remove_data(apps, schema_editor):
    for model_name in ['Profile', 'Language', 'Education', 'Skill', 'Experience', 'Course', 'Project']:
        apps.get_model('resume', model_name).objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
