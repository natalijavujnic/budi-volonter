from django.db import models
class Aktivnost(models.Model):
    idorg = models.OneToOneField('Korisnik', models.DO_NOTHING, db_column='idOrg', primary_key=True)  # Field name made lowercase. The composite primary key (idOrg, brAkt) found, that is not supported. The first column is selected.
    brakt = models.IntegerField(db_column='brAkt')  # Field name made lowercase.
    naziv = models.CharField(max_length=256)
    brmesta = models.IntegerField(db_column='brMesta')  # Field name made lowercase.
    datumod = models.DateField(db_column='datumOd')  # Field name made lowercase.
    datumdo = models.DateField(db_column='datumDo')  # Field name made lowercase.
    datumrok = models.DateField(db_column='datumRok')  # Field name made lowercase.
    mesto = models.CharField(max_length=256)
    drzava = models.ForeignKey('Lokacija', models.DO_NOTHING, db_column='drzava')
    kontinent = models.ForeignKey('Lokacija', models.DO_NOTHING, db_column='kontinent', to_field='kontinent', related_name='aktivnost_kontinent_set')

    class Meta:
        managed = False
        db_table = 'aktivnost'
        unique_together = (('idorg', 'brakt'),)


class Korisnik(models.Model):
    idkor = models.AutoField(db_column='idKor', primary_key=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=256)
    password = models.CharField(max_length=256)
    ime = models.CharField(max_length=256)
    prezime = models.CharField(max_length=256, blank=True, null=True)
    pib = models.IntegerField(unique=True, blank=True, null=True)
    telefon = models.CharField(unique=True, max_length=14, blank=True, null=True)
    tip = models.CharField(max_length=1)
    datumrodj = models.DateField(db_column='datumRodj', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'korisnik'


class Lokacija(models.Model):
    drzava = models.CharField(primary_key=True, max_length=256)  # The composite primary key (drzava, kontinent) found, that is not supported. The first column is selected.
    kontinent = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'lokacija'
        unique_together = (('drzava', 'kontinent'),)


class Oblast(models.Model):
    oblast = models.CharField(primary_key=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'oblast'


class Poruka(models.Model):
    idpre = models.OneToOneField('Prepiska', models.DO_NOTHING, db_column='idPre', primary_key=True)  # Field name made lowercase. The composite primary key (idPre, redBr) found, that is not supported. The first column is selected.
    redbr = models.CharField(db_column='redBr', max_length=45)  # Field name made lowercase.
    tekst = models.CharField(max_length=2000)
    time = models.DateTimeField()
    status = models.CharField(max_length=1)
    idsender = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='idSender')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'poruka'
        unique_together = (('idpre', 'redbr'),)


class Prepiska(models.Model):
    idpre = models.IntegerField(db_column='idPre', primary_key=True)  # Field name made lowercase.
    idkor1 = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='idKor1')  # Field name made lowercase.
    idkor2 = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='idKor2', related_name='prepiska_idkor2_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prepiska'


class Prijava(models.Model):
    idpri = models.IntegerField(db_column='idPri', primary_key=True)  # Field name made lowercase.
    idvol = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='idVol')  # Field name made lowercase.
    idorg = models.ForeignKey(Aktivnost, models.DO_NOTHING, db_column='idOrg')  # Field name made lowercase.
    brakt = models.ForeignKey(Aktivnost, models.DO_NOTHING, db_column='brAkt', to_field='brakt', related_name='prijava_brakt_set')  # Field name made lowercase.
    pismo = models.CharField(max_length=2000)
    rezime = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    preporukavol = models.CharField(db_column='preporukaVol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    preporukaorg = models.CharField(db_column='preporukaOrg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    komvol = models.CharField(db_column='komVol', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    komorg = models.CharField(db_column='komOrg', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prijava'


class Pripada(models.Model):
    idorg = models.OneToOneField(Aktivnost, models.DO_NOTHING, db_column='idOrg', primary_key=True)  # Field name made lowercase. The composite primary key (idOrg, brAkt, oblast) found, that is not supported. The first column is selected.
    brakt = models.ForeignKey(Aktivnost, models.DO_NOTHING, db_column='brAkt', to_field='brakt', related_name='pripada_brakt_set')  # Field name made lowercase.
    oblast = models.ForeignKey(Oblast, models.DO_NOTHING, db_column='oblast')

    class Meta:
        managed = False
        db_table = 'pripada'
        unique_together = (('idorg', 'brakt', 'oblast'),)


class Vestina(models.Model):
    idorg = models.OneToOneField(Aktivnost, models.DO_NOTHING, db_column='idOrg', primary_key=True)  # Field name made lowercase. The composite primary key (idOrg, brAkt, redBr) found, that is not supported. The first column is selected.
    brakt = models.ForeignKey(Aktivnost, models.DO_NOTHING, db_column='brAkt', to_field='brakt', related_name='vestina_brakt_set')  # Field name made lowercase.
    redbr = models.IntegerField(db_column='redBr')  # Field name made lowercase.
    opis = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'vestina'
        unique_together = (('idorg', 'brakt', 'redbr'),)


class ZanimaGa(models.Model):
    idkor = models.OneToOneField(Korisnik, models.DO_NOTHING, db_column='idKor', primary_key=True)  # Field name made lowercase. The composite primary key (idKor, oblast) found, that is not supported. The first column is selected.
    oblast = models.ForeignKey(Oblast, models.DO_NOTHING, db_column='oblast')
    class Meta:
        managed = False
        db_table = 'zanima_ga'
        unique_together = (('idkor', 'oblast'),)











