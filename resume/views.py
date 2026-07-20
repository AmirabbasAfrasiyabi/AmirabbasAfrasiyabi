from django.shortcuts import render
from .models import Profile, Language, Education, Skill, Experience, Course, Project


def cv_view(request):
    context = {
        'profile': Profile.objects.first(),
        'languages': Language.objects.all(),
        'educations': Education.objects.all(),
        'skills_by_category': {
            'فریمورک / کتابخانه': Skill.objects.filter(category=Skill.SkillCategory.FRAMEWORK),
            'ابزار': Skill.objects.filter(category=Skill.SkillCategory.TOOL),
            'دیتابیس': Skill.objects.filter(category=Skill.SkillCategory.DATABASE),
        },
        'experiences': Experience.objects.all(),
        'courses': Course.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'resume/cv.html', context)
