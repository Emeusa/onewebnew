from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("user most have an email address.")
        if not username:
            raise ValueError("user most have a username.")
        user = self.model(
            email       = self.normalize_email(email),
            username    = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email     = self.normalize_email(email),
            username  = username,
            password  = password
        )
        user.is_admin = True
        user.is_staff = True 
        user.is_superuser = True
        user.save(using=self._db)
        return user






class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email", max_length=50, unique=True)
    username        = models.CharField(max_length=50, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    hide_email      = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
        

    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True




class AoneEducational(models.Model):
    
    males    = "Male"
    females  = "Female"
    gender_choices = {males:"Male", females:"Female"}

    blind      = "bl"
    deaf       = "de"
    dumb       = "dm"
    albino     = "al"
    others     = "ot"
    no_con       = "ne"
    condition   =  {blind:"Blind", deaf:"Deaf", dumb:"Dumb", albino:"Albino", others:"Others", no_con:"None"}

    positive = "ye"
    negetive = "nn"
    pos_ne = {positive:"Yes", negetive:"No"}



    married = "Married"
    divorced = "Divorced"
    single   = "Single"
    marital_stat = {married:"Married", divorced:"Divorced", single:"Single"}


    abia         = "Abia State"
    adamawa      = "Adamawa State"
    akwa_ibom    = "Akwa Ibom State"
    anambra      = "Anambra State"
    bauchi       = "Bauchi State"
    bayelsa      = "Bayelsa State"
    benue        = "Benue State"
    borno        = "Borno State"
    cross_river  = "Cross River State"
    delta        = "Delta State"
    ebonyi       = "Ebonyi State"
    edo          = "Edo State"
    ekiti        = "Ekiti State"
    enugu        = "Enugu State"
    gombe        = "Gombe State"
    imo          = "Imo State"
    jigawa       = "Jigawa State"
    kaduna       = "Kaduna State"
    kano         = "Kano State"
    kastina      = "Kastina State"
    kebbi        = "Kebbi State"
    kogi         = "Kogi State"
    kwara        = "Kwara State"
    lagos        = "Lagos State"
    nasarawa     = "Nasarawa State"
    niger        = "Niger State"
    ogun         = "Ogun State"
    ondo         = "Ondo State"
    osun         = "Osun State"
    oyo          = "Oyo State"
    plateau      = "Plateau State"
    rivers       = "Rivers State"
    sokoto       = "Sokoto State"
    taraba       = "Taraba State"
    yobe         = "Yobe State"
    zamfara      = "Zamfara State"
    abuja        = "FCT Abuja"

    states_ch = { abia:"Abia State", adamawa:"Adamawa State", akwa_ibom:"Akwa Ibom State", anambra:"Anambra State", bauchi:"Bauchi State", bayelsa:"Bayelsa State", benue:"Benue State", borno:"Borno State",  cross_river:"Cross River State", delta:"Delta State", ebonyi:"Ebonyi State", edo:"Edo State", ekiti:"Ekiti State", enugu:"Enugu State", gombe:"Gombe State", imo:"Imo State", jigawa:"Jigawa State", kaduna:"Kaduna State", kano:"Kano State", kastina:"Kastina State", kebbi:"Kebbi State", kogi:"Kogi State", kwara:"Kwara State", lagos:"Lagos State", nasarawa:"Nasarawa State", niger:"Niger State", ogun:"Ogun State", ondo:"Ondo State", osun:"Osun State", oyo:"Oyo State", plateau:"Plateau State", rivers:"Rivers State", sokoto:"Sokoto State", taraba:"Taraba State", yobe:"Yobe State", zamfara:"Zamfara State", abuja:"FCT Abuja"}



    Use_of_English_Language         = "Use of English Language"
    english_language                = "English Language"
    Mathematics                     = "Mathematics"
    Physics                         = "Physics"             
    Chemistry                       = "Chemistry"
    Computer_Studies                = "Computer Studies"
    Physical_Health_Education       = "Physical Health Education"
    Literature_in_English           = "Literature in English"
    Home_Economics                  = "Home Economics"
    civic_education                 = "Civic Education"
    History                         = "History"
    Hausa                           = "Hausa"
    Government                      = "Government"
    Geography                       = "Geography"
    Economics                       = "Economics"
    Christain_Religious_Education   = "Christain Religious Education"
    Commerce                        = "Commerce"
    Biology                         = "Biology"
    Agricultural_Science            = "Agricultural Science"
    Accounting                      = "Accounting"
    French                          = "French"
    Arabic                          = "Arabic"
    Yoruba                          = "Yoruba"


    sub_choices = {Use_of_English_Language:"Use of English Language", english_language:"English Language", Mathematics:"Mathematics", Physics:"Physics", Chemistry:"Chemistry", Computer_Studies:"Computer Studies", Physical_Health_Education:"Physical Health Education", Literature_in_English:"Literature in English", Home_Economics:"Home Economics", History:"History", Hausa:"Hausa", Government:"Government", Geography:"Geography", Economics:"Economics", Christain_Religious_Education:"Christain Religious Education", Commerce:"Commerce", Biology:"Biology", Agricultural_Science:"Agricultural Science", Accounting:"Accounting", French:"French", Arabic:"Arabic", Yoruba:"Yoruba", civic_education:"Civic Education"}

    aone    = "A1"
    btwo    = "B2"
    bthree  = "B3"
    cfour   = "C4"
    cfive   = "C5"
    csix    = "C6"
    dseven  = "D7"
    eeight  = "E8"
    fnine   = "F9"

    grade_choices = {aone:"A1", btwo:"B2", bthree:"B3", cfour:"C4", cfive:"C5", csix:"C6", dseven:"D7", eeight:"E8", fnine:"F9"}

    waec    = "WAEC"
    neco    = "NECO"
    nabteb  = "NABTEB"
    jamb    = "JAMB"
    jupeb   = "JUPEB"
    ijmb    = "IJMB"
    gce     = "GCE"
    oth     = "Others"

    exam_type = {waec:"WAEC", neco:"NECO", nabteb:"NABTEB", jamb:"JAMB", jupeb:"JUPEB", ijmb:"IJMB", gce:"GCE", oth:"Others"}
    alevel = {}

    school    = "SCHOOL"
    private   = "PRIVATE"

    school_choice = {school:"SCHOOL", private:"PRIVATE"}

    def nation():
        return "Nigeria"


    owner               =         models.ForeignKey(Account, on_delete=models.CASCADE, related_name="formowner", null=True)
    profile_code        =         models.BigIntegerField(verbose_name="Profile Code", null=True, blank=True)
    last_name           =         models.CharField(max_length=250, verbose_name="Surname")
    first_name          =         models.CharField(max_length=250, verbose_name="First Name")
    middle_name         =         models.CharField(max_length=250, verbose_name="Middle Name")
    date_of_birth       =         models.DateField(verbose_name="Date of Birth", auto_now=False, auto_now_add=False)
    gender              =         models.CharField(max_length=200, choices=gender_choices, verbose_name="Gender")
    genotype            =         models.CharField(verbose_name="Genotype", max_length=250,)
    b_group             =         models.CharField(verbose_name="Blood Group", max_length=250,)
    marital             =         models.CharField(max_length=200, choices=marital_stat, verbose_name="Marital Status")
    madien_name         =         models.CharField(max_length=250, null=True, blank=True, verbose_name="Madien Name (if Married)")
    email               =         models.EmailField(verbose_name="Email")
    contact_add         =         models.CharField(max_length=250, verbose_name="Contact Address")
    nin                 =         models.BigIntegerField(verbose_name="NIN")
    mobile_number       =         models.BigIntegerField(verbose_name="Mobile Number")
    nationality         =         models.CharField("Nationality", max_length=250, default=nation)
    state_of_origin     =         models.CharField(max_length=50, choices=states_ch, verbose_name="State of Origin")
    local_gov           =         models.CharField("L.G.A", max_length=250)
    parent_name         =         models.CharField("Parent Name", max_length=250)
    occupation          =         models.CharField("Occupation", max_length=250)
    office_add          =         models.CharField("Office Address", max_length=250)
    phone_no            =         models.BigIntegerField(verbose_name="Parent Phone Number")
    parent_mail         =         models.EmailField(verbose_name="Parent Email Address")
    alevel_pro          =         models.CharField(max_length=200, verbose_name="Exams Type", choices=exam_type, default=False)
    prefered_ex_state   =         models.CharField(max_length=50, choices=states_ch, verbose_name="Prefered state of exam", blank=True, null=True)
    exam_town           =         models.CharField("Exams Town", max_length=250, blank=True, null=True)
    first_choices       =         models.CharField("first Institution", max_length=250)
    programme_one       =         models.CharField("Programme of study", max_length=250)
    second_choices      =         models.CharField("second Institution", max_length=250)
    programme_two       =         models.CharField("Programme of study", max_length=250)
    utme_sub_one        =         models.CharField(max_length=200, choices=sub_choices, verbose_name="UTME subject 1", blank=True, null=True)
    utme_sub_two        =         models.CharField(max_length=200, choices=sub_choices, verbose_name="UTME subject 2", blank=True, null=True)
    utme_sub_three      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="UTME subject 3", blank=True, null=True)
    utme_sub_four       =         models.CharField(max_length=200, choices=sub_choices, verbose_name="UTME subject 4", blank=True, null=True)
    name_of_sec         =         models.CharField("Name of Secondary School Attended", max_length=250)
    exam_type           =         models.CharField(max_length=200, choices=exam_type, verbose_name="Exam type")
    reg_mode            =         models.CharField(max_length=200, choices=school_choice, verbose_name="how did you register for examination", blank=True, null=True)
    yr_of_exam          =         models.IntegerField(verbose_name="Exam Year", blank=True, null=True)
    serial_no           =         models.BigIntegerField(verbose_name="Serial Number", blank=True, null=True)
    pin_no              =         models.BigIntegerField(verbose_name="Pin", blank=True, null=True)
    exam_no             =         models.BigIntegerField(verbose_name="Exam Number", blank=True, null=True)
    num_of_sit          =         models.IntegerField(verbose_name="Number of Sittings", blank=True, null=True, default=1,
        validators=[
            MaxValueValidator(2),
            MinValueValidator(1)
        ])

    olevel_sub_one      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 1")
    grade1              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_two      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 2")
    grade2              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_three    =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 3")
    grade3              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_four     =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 4")
    grade4              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_five     =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 5")
    grade5              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_six      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 6")
    grade6              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_sev      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 7")
    grade7              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_eig      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 8")
    grade8              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)

    olevel_sub_nin      =         models.CharField(max_length=200, choices=sub_choices, verbose_name="O'Level Subject 9")
    grade9              =         models.CharField(max_length=200, choices=grade_choices, verbose_name="grade", blank=True, null=True)


    class Meta:
        ordering = ("-last_name", "-first_name", "-middle_name")
        verbose_name_plural = "A1 Educational Form"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
