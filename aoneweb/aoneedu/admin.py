from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Account, AoneEducational

# Register your models here.


admin.site.site_header = "A1 EDUCATIONAL ADMINISTRATION DASHBOARD"
admin.site.site_title = "A1 ADMIN"

class AccountAdmin(UserAdmin):
    list_display = ("email", "username", "date_joined", "last_login", "is_admin", "is_staff")
    search_fields = ("email", "username")
    readonly_fields = ("id", "date_joined", "last_login")


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class AoneAdminManager(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    list_display_links = ('last_name', 'first_name', 'middle_name')
    ordering = ["last_name", "first_name", "middle_name"]
    fields = ['owner',('last_name', 'first_name', 'middle_name'), 'date_of_birth', 'gender', 'genotype', 'b_group', 'marital', 'madien_name', 'email', 'contact_add', 'nin', 'mobile_number', 'nationality', 'state_of_origin', 'local_gov', 'parent_name', 'occupation', 'office_add', 'phone_no', 'parent_mail', 'alevel_pro', 'profile_code', 'prefered_ex_state', 'exam_town', 'first_choices', 'programme_one', 'second_choices', 'programme_two', 'utme_sub_one', 'utme_sub_two', 'utme_sub_three', 'utme_sub_four', 'name_of_sec', 'exam_type', 'reg_mode', 'yr_of_exam', 'serial_no', 'pin_no', 'exam_no', 'num_of_sit', 'olevel_sub_one', 'grade1', 'olevel_sub_two', 'grade2', 'olevel_sub_three', 'grade3', 'olevel_sub_four', 'grade4', 'olevel_sub_five', 'grade5', 'olevel_sub_six', 'grade6', 'olevel_sub_sev', 'grade7', 'olevel_sub_eig', 'grade8', 'olevel_sub_nin', 'grade9']

    search_fields = ('last_name', 'first_name')


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(Account, AccountAdmin)
admin.site.register(AoneEducational, AoneAdminManager)
