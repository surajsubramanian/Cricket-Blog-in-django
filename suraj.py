# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PointsTable(models.Model):
    index = models.TextField(primary_key=True)
    mat = models.BigIntegerField(db_column='Mat', blank=True, null=True)  # Field name made lowercase.
    won = models.BigIntegerField(db_column='Won', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    tied = models.BigIntegerField(db_column='Tied', blank=True, null=True)  # Field name made lowercase.
    nr = models.BigIntegerField(db_column='NR', blank=True, null=True)  # Field name made lowercase.
    pts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Points_table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IplMatch(models.Model):
    match_id = models.IntegerField(primary_key=True)
    match_date = models.DateTimeField(blank=True, null=True)
    team_name_id = models.IntegerField(blank=True, null=True)
    opponent_team_id = models.IntegerField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    venue_name = models.TextField(blank=True, null=True)
    toss_winner_id = models.IntegerField(blank=True, null=True)
    toss_decision = models.TextField(blank=True, null=True)
    is_superover = models.IntegerField(blank=True, null=True)
    is_result = models.IntegerField(blank=True, null=True)
    is_duckworthlewis = models.IntegerField(blank=True, null=True)
    win_type = models.TextField(blank=True, null=True)
    won_by = models.TextField(blank=True, null=True)
    match_winner_id = models.IntegerField(blank=True, null=True)
    man_of_the_match_id = models.IntegerField(blank=True, null=True)
    first_umpire_id = models.IntegerField(blank=True, null=True)
    second_umpire_id = models.IntegerField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)
    host_country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipl_match'


class PlayerIpl(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.TextField()
    dob = models.DateTimeField(blank=True, null=True)
    batting_hand = models.TextField(blank=True, null=True)
    bowling_skill = models.TextField(blank=True, null=True)
    country = models.TextField()
    is_umpire = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_ipl'


class PlayerMatch(models.Model):
    match_id = models.IntegerField()
    player_id = models.IntegerField()
    team_id = models.IntegerField()
    is_keeper = models.IntegerField()
    is_captain = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_match'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    season_year = models.IntegerField(blank=True, null=True)
    orange_cap_id = models.IntegerField(blank=True, null=True)
    purple_cap_id = models.IntegerField(db_column='purple_cap_Id', blank=True, null=True)  # Field name made lowercase.
    man_of_the_series_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class TableName(models.Model):
    index = models.TextField(blank=True, null=True)
    mat = models.BigIntegerField(db_column='Mat', blank=True, null=True)  # Field name made lowercase.
    won = models.BigIntegerField(db_column='Won', blank=True, null=True)  # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    tied = models.BigIntegerField(db_column='Tied', blank=True, null=True)  # Field name made lowercase.
    nr = models.BigIntegerField(db_column='NR', blank=True, null=True)  # Field name made lowercase.
    pts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_name'


class TeamIpl(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.TextField(blank=True, null=True)
    team_short_code = models.TextField(blank=True, null=True)
    team_logo = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_ipl'


class UsersProfile(models.Model):
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'users_profile'
