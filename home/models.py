from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField('用户名',max_length=16)
    password = models.CharField('密码',max_length=32)
    email = models.EmailField('邮箱',)
    telephone = models.CharField('电话',max_length=16)
    is_active = models.BooleanField('是否在任',default=True)

    def __str__(self):
        return self.username

class StudentInfo(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)
    # 学生姓名
    name = models.CharField('姓名',max_length=16)
    # 学生年龄
    age = models.IntegerField('年龄',null=True,blank=True)
    # 学生性别
    sex_type = (('male', '男'), ('female', '女'))  #
    sex = models.CharField("性别", choices=sex_type, max_length=16, default='male', blank=True, null=True)
    # 学号
    student_id = models.CharField('学号',max_length=16)
    # 学校
    university = models.CharField('学校',max_length=16)
    # 学院
    college = models.CharField('学院',max_length=16)
    # 专业
    profession = models.CharField('专业',max_length=32)
    # 班级
    student_class = models.CharField('班级',max_length=16)
    # 用户
    user = models.ForeignKey(to=UserInfo,on_delete=models.CASCADE)
    # 注册时间
    register_date = models.DateField('注册时间',auto_now = True)

    class Meta:
        ordering = ['id']
        verbose_name = '学生信息表'
        verbose_name_plural = '学生信息表'

    def __str__(self):
        return self.name

class TeacherInfo(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)
    # 老师姓名
    name = models.CharField('姓名', max_length=16)
    # 老师年龄
    age = models.IntegerField('年龄', null=True, blank=True)
    # 性别
    sex_type = (('male', '男'), ('female', '女'))  #
    sex = models.CharField("性别", choices=sex_type, max_length=16, default='male', blank=True, null=True)
    # 学校
    university = models.CharField('学校',max_length=16)
    # 学院
    college = models.CharField('学院',max_length=16)
    # 专业
    profession = models.CharField('专业',max_length=32)
    # 用户
    user = models.ForeignKey(to=UserInfo, on_delete=models.CASCADE)
    # # 用户名
    # username = models.CharField('用户名',max_length=16)
    # # 密码
    # password = models.CharField('密码',max_length=16)
    # # 电话
    # tel = models.CharField('电话',max_length=16)
    # # 邮箱
    # email = models.EmailField('邮箱',)
    # 注册时间
    register_date = models.DateField('注册时间',auto_now=True)
    # 工号
    teacher_id = models.CharField('工号',max_length=16)

    class Meta:
        ordering = ['id']
        verbose_name = '教师信息表'
        verbose_name_plural = '教师信息表'

    def __str__(self):
        return self.name


#课程信息表
class Course(models.Model):
    #课程名称
    course_name = models.CharField('课程名称',max_length=16)
    #课程图片
    course_img = models.ImageField('课程图片',null=True, blank=True,upload_to= 'course_img')
    #课程老师
    course_teacher = models.ForeignKey(to='TeacherInfo',on_delete=models.CASCADE)
    #学分
    course_credit = models.FloatField('学分',)
    #开课时间
    start_time = models.DateField('开课时间',auto_now=True)
    #结课时间
    end_time = models.DateField('结课时间',auto_now=True)
    #remark
    remark = models.TextField('备注',null=True, blank=True,max_length=200)
    class Meta:
        ordering = ['id']
        verbose_name = '课程信息表'
        verbose_name_plural = '课程信息表'

    def __str__(self):
        return self.course_name

#试卷信息表
class Test_paper(models.Model):
    paper_name = models.CharField('试卷名',max_length=32)
    course_id = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    upload_user = models.ForeignKey(to=UserInfo,on_delete=models.CASCADE)
    upload_time = models.DateField('上传时间',auto_now=True)
    addrs = models.URLField('试卷资料地址',null=True, blank=True)
    remark = models.TextField('备注',null=True, blank=True,max_length=200)
    class Meta:
        ordering = ['id']
        verbose_name = '试卷信息表'
        verbose_name_plural = '试卷信息表'
    def __str__(self):
        return self.paper_name

#公共课真题试卷表
class Public_Test_paper(models.Model):
    paper_name = models.CharField('试卷名', max_length=32)
    years = models.CharField('真题年份',max_length=4)
    type = (('1', '数学一'), ('2', '数学二'),('3','数学三'))  #
    math_type = models.CharField("试卷类型", choices = type, max_length=16, default='1')
    upload_time = models.DateField('上传时间',auto_now_add=True)
    addrs = models.URLField('试卷资料地址',null=True, blank=True)
    remark = models.TextField('备注',null=True, blank=True,max_length=200)
    class Meta:
        ordering = ['id']
        verbose_name = '公共课真题试卷表'
        verbose_name_plural = '公共课真题试卷表'

    def __str__(self):
        return self.paper_name

#专业课真题试卷表
class Pro_Test_paper(models.Model):
    paper_name = models.CharField('试卷名', max_length=32)
    years = models.CharField('真题年份',max_length=4)
    course = models.CharField('真题科目',max_length=16)
    university = models.CharField("真题学校", max_length=16)
    upload_time = models.DateField('上传时间',auto_now_add=True)
    addrs = models.URLField('试卷资料地址',null=True, blank=True)
    remark = models.TextField('备注',null=True, blank=True,max_length=200)
    class Meta:
        ordering = ['id']
        verbose_name = '专业课真题试卷表'
        verbose_name_plural = '专业课真题试卷表'
    def __str__(self):
        return self.paper_name


# 竞赛真题试卷表
class contest_Test_paper(models.Model):
    paper_name = models.CharField('试卷名', max_length=32)
    years = models.CharField('真题年份', max_length=4)
    course = models.CharField('真题科目', max_length=16)
    level = models.CharField("真题级别", max_length=16)
    c_type = models.BooleanField('是否数学专业',default=True)
    contest_address = models.CharField('竞赛地区',max_length=16)
    upload_time = models.DateField('上传时间', auto_now_add=True)
    addrs = models.URLField('试卷资料地址', null=True, blank=True)
    remark = models.TextField('备注', null=True, blank=True, max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = '竞赛真题试卷表'
        verbose_name_plural = '竞赛真题试卷表'
    def __str__(self):
        return self.paper_name

# 视频表
class Video(models.Model):
    course_id = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    video_name = models.CharField('视频名称',max_length=16)
    addrs = models.URLField('视频地址', null=True, blank=True)
    remark = models.TextField('备注', null=True, blank=True, max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = '视频表'
        verbose_name_plural = '视频表'

    def __str__(self):
        return self.video_name

# 公告
class Notice(models.Model):
    course_id = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    Title = models.CharField('公告标题',max_length=32)
    content = models.TextField('公告内容',max_length=500)
    poster = models.ForeignKey(to=UserInfo,on_delete=models.CASCADE)
    post_time = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = '公告'
        verbose_name_plural = '公告'

    def __str__(self):
        return (self.Title +" 发布时间"+ str(self.post_time))

# 课程资料
class CourseData(models.Model):
    course_id = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    type = (('1', 'pdf'), ('2', 'word'))  #
    data_type = models.CharField("资料类型", choices=type, max_length=4, default='1')
    data_name = models.CharField('资料名称',max_length=16)
    content = models.TextField('资料信息',max_length=200)
    upload_user = models.ForeignKey(to=UserInfo, on_delete=models.CASCADE)
    upload_time = models.DateField('上传时间', auto_now_add=True)
    addrs = models.URLField('资料地址', null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '课程资料'
        verbose_name_plural ='课程资料'

    def __str__(self):
        return self.data_name

# 作业
class Homework(models.Model):
    student = models.ForeignKey(to=StudentInfo,on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course,on_delete=models.CASCADE)
    upload_time = models.DateField('上传时间', auto_now_add=True)
    grade = models.FloatField('分数')
    addrs = models.URLField('作业地址', null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = '作业'
        verbose_name_plural = '作业'

    def __str__(self):
        return (self.student +" 上传时间"+ str(self.upload_time))

# 总成绩
class Stu_Grade(models.Model):
    student = models.ForeignKey(to=StudentInfo, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    test_paper = models.ForeignKey(to=Test_paper,on_delete=models.CASCADE)
    grade = models.FloatField('分数',default=0)

    class Meta:
        ordering = ['id']
        verbose_name = '总成绩'
        verbose_name_plural = '总成绩'
    def __str__(self):
        return (self.student +' 成绩'+ self.grade)

# 课程章节
class Course_detial(models.Model):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    video = models.ForeignKey(to=Video,on_delete=models.CASCADE)
    course_detail_name = models.CharField('章节名称',max_length=16)
    chapter = models.CharField('章',max_length=8)
    sector = models.CharField('节',max_length=8)
    remark = models.TextField('备注', null=True, blank=True, max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = '课程章节'
        verbose_name_plural = '课程章节'

    def __str__(self):
        return (self.course + '第' +self.chapter +'章，第'+self.sector+'节')

# 学生选课表
class Stu_Course(models.Model):
    student = models.ForeignKey(to=StudentInfo,on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = '学生选课表'
        verbose_name_plural = '学生选课表'

    def __str__(self):
        return (self.student.name + self.course.course_name)