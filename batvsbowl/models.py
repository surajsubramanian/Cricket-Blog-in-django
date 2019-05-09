from django.db import models


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


class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    season_year = models.IntegerField(blank=True, null=True)
    orange_cap_id = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    purple_cap_id = models.IntegerField(
        db_column='purple_cap_Id', blank=True, null=True)
    man_of_the_series_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class TeamIpl(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.TextField(blank=True, null=True)
    team_short_code = models.TextField(blank=True, null=True)
    team_logo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_ipl'
