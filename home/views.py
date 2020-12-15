from django.shortcuts import render,HttpResponse,redirect
from home import models
from django import forms
import re
from django.core.exceptions import ValidationError
# Create your views here.
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length = 16,
        min_length = 3,
        label='用户名',
        widget=forms.widgets.TextInput(attrs={'class':'username','autocomplete':'off','placeholder':'用户名'}),
        error_messages={
            'required':'用户名不能为空',
            'max_length':'用户名长度不能大于16位',
            'min_length':'用户名长度不能小于3位',
        }
    )
    password = forms.CharField(
        max_length=16,
        min_length=3,
        label='密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'autocomplete': 'off', 'placeholder': '输入密码','oncontextmenu':"return false",'onpaste':'false'}),
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码长度不能大于16位',
            'min_length': '密码长度不能小于3位',
        }
    )
    r_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'autocomplete': 'off', 'placeholder': '再次输入密码', 'oncontextmenu': "return false",'onpaste': 'return false'}),
        error_messages={
            'required':'确认密码不能为空',
        }
    )
    def clean(self):
        values = self.cleaned_data
        passwoed= values.get('password')
        r_passwoed= values.get('r_password')
        if passwoed == r_passwoed:
            return values
        else:
            self.add_error('两次输入密码不一致')

    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.TextInput(attrs={'placeholder': "输入邮箱地址", 'oncontextmenu': "return false", 'type': 'email',
                                              'onpaste': "return false"}),
        error_messages={
            'isvalid': '邮箱格式不对',
            'required': '邮箱不能为空',
        }
    )
    telephone = forms.CharField(
        label='电话',
        widget=forms.widgets.TextInput(attrs={'placeholder': "输入手机号码", 'autocomplete': "off"}),
        error_messages={
            'required': '手机号不能为空',
        },
        validators=[mobile_validate]
    )


class AddinfoForm(forms.Form):
    name = forms.CharField(
        max_length = 8,
        min_length = 2,
        label='姓名',
        widget=forms.widgets.TextInput(attrs={'class':'username','autocomplete':'off','placeholder':'姓名'}),
        error_messages={
            'required':'姓名不能为空',
            'max_length':'姓名长度不能大于8位',
            'min_length':'姓名长度不能小于2位',
        }
    )
    age = forms.IntegerField(
        label='年龄',
        widget=forms.widgets.TextInput(attrs={'class': 'username', 'autocomplete': 'off', 'placeholder': '输入年龄','oncontextmenu':"return false",'onpaste':'false'}),
        error_messages={
            'required': '年龄不能为空',
        }
    )

    sex = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'autocomplete': 'off', 'placeholder': '再次输入密码', 'oncontextmenu': "return false",'onpaste': 'return false'}),
        error_messages={
            'required':'确认密码不能为空',
        }
    )
    def clean(self):
        values = self.cleaned_data
        passwoed= values.get('password')
        r_passwoed= values.get('r_password')
        if passwoed == r_passwoed:
            return values
        else:
            self.add_error('两次输入密码不一致')

    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.TextInput(attrs={'placeholder': "输入邮箱地址", 'oncontextmenu': "return false", 'type': 'email',
                                              'onpaste': "return false"}),
        error_messages={
            'isvalid': '邮箱格式不对',
            'required': '邮箱不能为空',
        }
    )
    telephone = forms.CharField(
        label='电话',
        widget=forms.widgets.TextInput(attrs={'placeholder': "输入手机号码", 'autocomplete': "off"}),
        error_messages={
            'required': '手机号不能为空',
        },
        validators=[mobile_validate]
    )

def register(request):
    if request.method == 'GET':
        register_form_obj = RegisterForm()
        return render(request,'regist.html',{'register_form_obj':register_form_obj})
    else:
        register_form_obj = RegisterForm(request.POST)
        if register_form_obj.is_valid():
            register_form_obj.cleaned_data.pop('r_password')
            models.UserInfo.objects.create(**register_form_obj.cleaned_data)
            return redirect('login')
        else:
            return render(request,'regist.html',{'register_form_obj':register_form_obj})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(username=username,password=password).first()
        if user_obj:
            request.session['user_id'] = user_obj.id
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'用户名或密码错误'})

def home(request):
    # user_obj = models.UserInfo.objects.filter(id = request.session.get('user_id')).first()
    if request.method == 'GET':
        cou_obj = models.Course.objects.all()
        paper_obj= models.Public_Test_paper.objects.all()
        data_obj = models.CourseData.objects.all()
        return render(request, 'home.html', {'cou_obj': cou_obj, 'user_obj': request.user_obj})
    else:
        # print(request.POST.get('want_to_learn'))
        # return HttpResponse('OK')
        return search(request)


def about(request):
    if request.method == "GET":
        return render(request, 'about.html',{'user_obj':request.user_obj})
    else:
        return search(request)

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return search(request)

def single_course(request):
    if request.method == 'GET':
        return render(request, 'single_course.html',{'user_obj':request.user_obj})
    else:
        return search(request)


def video(request):
    if request.method == 'GET':
        return render(request, 'video_play.html',{'user_obj':request.user_obj})
    else:
        return search(request)

class StuForm(forms.ModelForm):
    class Meta:
        model = models.StudentInfo
        fields = '__all__'
        exclude = ['user']
        error_messages = {
            'name': {'required': '不能为空'},
            'age': {'required': '不能为空'},
            'student_id': {'required': '不能为空'},
            'university': {'required': '不能为空'},
            'college': {'required': '不能为空'},
            'profession': {'required': '不能为空'},
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        from multiselectfield.forms.fields import MultiSelectFormField
        from django.forms.fields import TypedChoiceField
        for field_name, field in self.fields.items():
            print(field.widget)
            if not isinstance(field, MultiSelectFormField):
                field.widget.attrs.update({'class': 'form-control'})

def add_edit_stuinfo(request,sid =None):

    label = '编辑客户' if sid else '添加客户'
    stu_obj = models.StudentInfo.objects.filter(pk=sid).first()
    if request.method == 'GET':
        stu_obj_form = StuForm(instance=stu_obj)
        return render(request,'addinfo.html',{'stu_obj_form':stu_obj_form,'label':label,'user_obj':request.user_obj})
    else:
        if search(request) == 0:
            stu_obj_form = StuForm(request.POST,instance=stu_obj)
            if stu_obj_form.is_valid():
                models.StudentInfo.objects.create(
                    **stu_obj_form.cleaned_data,
                    user_id=request.session.get('user_id')
                )
                return redirect('home')
            else:
                return render(request, 'addinfo.html', {'stu_obj_form': stu_obj_form, 'label': label,'user_obj':request.user_obj})

        else:
            return search(request)

class TeaForm(forms.ModelForm):
    class Meta:
        model = models.TeacherInfo
        fields = '__all__'
        exclude = ['user']
        error_messages = {
            'name': {'required': '不能为空'},
            'age': {'required': '不能为空'},
            'teacher_id': {'required': '不能为空'},
            'university': {'required': '不能为空'},
            'college': {'required': '不能为空'},
            'profession': {'required': '不能为空'},
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        from multiselectfield.forms.fields import MultiSelectFormField
        from django.forms.fields import TypedChoiceField
        for field_name, field in self.fields.items():
            print(field_name,field)
            if not isinstance(field, MultiSelectFormField):
                field.widget.attrs.update({'class': 'form-control'})

def add_edit_teainfo(request,sid =None):

    label = '编辑客户' if sid else '添加客户'
    tea_obj = models.TeacherInfo.objects.filter(pk=sid).first()
    if request.method == 'GET':
        tea_obj_form = TeaForm(instance=tea_obj)
        return render(request,'addinfo.html',{'tea_obj_form':tea_obj_form,'label':label,'user_obj':request.user_obj})
    else:
        if search(request) == 0:
            tea_obj_form = TeaForm(request.POST,instance=tea_obj)
            if tea_obj_form.is_valid():
                models.TeacherInfo.objects.create(
                    **tea_obj_form.cleaned_data,
                    user_id=request.session.get('user_id')
                )
                # print(tea_obj_form.cleaned_data)
                # a = models.UserInfo.objects.filter(id = request.session.get('user_id'))
                # tea_obj_form.cleaned_data.update({'user': '<UserInfo: zhangwz>'})
                # tea_obj_form.save()
                return redirect('home')
            else:
                return render(request, 'addinfo.html', {'tea_obj_form': tea_obj_form, 'label': label,'user_obj':request.user_obj})
        else:
            return search(request)

def choise_course(request):
    if request.method == 'GET':
        if models.StudentInfo.objects.filter(user_id=request.session.get('user_id')).first():
            cou_obj = models.Course.objects.all()
            return render(request,'choise_course.html',{'cou_obj':cou_obj,'user_obj':request.user_obj})
        else:
            return redirect('jump')
    else:
        if search(request) == 0:
            choised = request.POST.get('choise_course')
            models.Stu_Course.objects.create(
                student=models.StudentInfo.objects.filter(id=request.session.get('user_id')).first(),
                course=models.Course.objects.filter(course_name=choised).first()
            )
            return redirect('home')
        else:
            return search(request)

def mycourse(request):
    if request.method == 'GET':
        my_course_obj = models.Course.objects.filter(stu_course__student__id=request.session.get('user_id'))
        return render(request,'mycourse.html',{'user_obj':request.user_obj,'my_course_obj':my_course_obj})
    else:
        return search(request)

def allcourse(request):
    if request.method =="GET":
        all_course = models.Course.objects.all()
        return render(request, 'allcourse.html', {'user_obj': request.user_obj, 'all_course': all_course})
    else:
        return search(request)

def jump(request):
    return render(request,'jump.html',{'user_obj':request.user_obj})


def search(request):
        keyword = request.POST.get('want_to_learn')
        if keyword is None:
            return 0
        else:
            course_obj = models.Course.objects.filter(course_name__contains=keyword)
            pro_test_paper_obj = models.Pro_Test_paper.objects.filter(paper_name__contains=keyword)
            pub_test_paper_obj = models.Public_Test_paper.objects.filter(paper_name__contains=keyword)
            coursedata_obj = models.CourseData.objects.filter(data_name__contains=keyword)
            return render(request,'search.html',{'course_obj':course_obj,'pro_test_paper_obj':pro_test_paper_obj,'pub_test_paper_obj':pub_test_paper_obj,'coursedata_obj':coursedata_obj,'user_obj':request.user_obj})
