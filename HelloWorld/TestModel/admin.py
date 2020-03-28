from django.contrib import admin
from TestModel.models import Test, Contact, Tags


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tags

class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')

    list_display = ('id', 'name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )

# fail, i do not learn inline, it may be influence list_display
# or maybe tags only have one attribute(except contact as fk)
# class TagsAdmin(admin.ModelAdmin):
#     fields = ('id', 'name', 'email')
#
#     list_display = ('name', 'contact')  # list
#     # search_fields = ('name',)
#     # fieldsets = (
#     #     ['Main', {
#     #         'fields': ('name',),
#     #     }],
#     #     ['Advance', {
#     #         'classes': ('collapse',),  # CSS
#     #         'fields': ('contact',),
#     #     }]
#     # )


class TestAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')

    list_display = ('id', 'name')  # list
    fields = ['id', 'name']


admin.site.register(Contact, ContactAdmin)
# admin.site.register(Tags, TagsAdmin)
admin.site.register(Test, TestAdmin)

