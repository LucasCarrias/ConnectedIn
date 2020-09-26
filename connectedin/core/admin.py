from django.contrib import admin
from .models import UserAccount,\
                    Profile,\
                    Post,\
                    Comment,\
                    Reaction,\
                    PostReaction,\
                    Invitation


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    exclude = ('password', 'groups', 'user_permissions', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('contacts',)
    list_display = ('name', 'user',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('profile', 'body', 'created', 'updated')
    readonly_fields = ('created', 'updated',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(PostReaction)
class PostReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    pass