# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from nnmware.apps.address.models import Institution
from nnmware.core.abstract import AbstractOrder, AbstractName, AbstractSkill, AbstractImg, GENDER_CHOICES
from nnmware.core.fields import std_text_field
from nnmware.core.utils import tuplify, current_year

EDUCATION_END = map(tuplify, range(current_year - 55, current_year + 1))

GROWTH = map(tuplify, range(50, 221))
WEIGHT = map(tuplify, range(1, 150))
CLOTHING_SIZE = map(tuplify, range(16, 74, 2))
SHOE_SIZE = map(tuplify, range(16, 49))
HEAD_SIZE = map(tuplify, range(34, 63))
AGE_SIZE = map(tuplify, range(1, 101))


class Education(AbstractImg):
    institution = models.ForeignKey(Institution, verbose_name=_('Institution'),
                                    related_name='edu', blank=True, null=True)
    education_end = models.IntegerField(verbose_name=_('End of education'), choices=EDUCATION_END,
                                        default=current_year)
    master_course = std_text_field(_('Master of course'))
    diploma_work = std_text_field(_('Diploma work'))
    diploma_role = std_text_field(_('Role'))
    specialty = std_text_field(_('Specialty'))
    prof_edu = models.BooleanField(_('Profile education'), default=False)
    nonprof_name = std_text_field(_('Non-profile course name'))

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")


class TypeAppearanceHuman(AbstractOrder):
    name = std_text_field(_('Type of appearance'))

    class Meta:
        verbose_name = _("Type of appearance")
        verbose_name_plural = _("Types of appearance")


class TypeNationalHuman(AbstractOrder):
    name = std_text_field(_('National Type'))

    class Meta:
        verbose_name = _("National Type")
        verbose_name_plural = _("National Types")


class TypeBodyHuman(AbstractOrder):
    name = std_text_field(_('Body Type'))

    class Meta:
        verbose_name = _("Body Type")
        verbose_name_plural = _("Body Types")


class TypeFeatureAppearanceHuman(AbstractOrder):
    name = std_text_field(_('Feature of appearance'))

    class Meta:
        verbose_name = _("Feature appearance type")
        verbose_name_plural = _("Feature appearances types")


class HairColor(AbstractOrder):
    name = std_text_field(_('Hair color'))

    class Meta:
        verbose_name = _("Hair color")
        verbose_name_plural = _("Hair colors")


class HairLength(AbstractOrder):
    name = std_text_field(_('Length of hair'))

    class Meta:
        verbose_name = _("Length of hair")
        verbose_name_plural = _("Length of hair")


class HairTexture(AbstractOrder):
    name = std_text_field(_('Texture of hair'))

    class Meta:
        verbose_name = _("Texture of hair")
        verbose_name_plural = _("Textures of hair")


class EyeColor(AbstractOrder):
    name = std_text_field(_('Eye color'))

    class Meta:
        verbose_name = _("Eye color")
        verbose_name_plural = _("Eyes colors")


class SkinColor(AbstractOrder):
    name = std_text_field(_('Skin color'))

    class Meta:
        verbose_name = _("Color of skin")
        verbose_name_plural = _("Colors of skin")


class ActorCategory(AbstractOrder):
    name = std_text_field(_('Category of actor'))

    class Meta:
        verbose_name = _("Category of actor")
        verbose_name_plural = _("Categories of actors")

    @property
    def get_random_img(self):
        all_actors = self.actor_set.order_by('?')
        for actor in all_actors:
            if actor.ava != settings.DEFAULT_AVATAR:
                return actor.ava
        return settings.DEFAULT_AVATAR


class TypeNational(AbstractOrder):
    name = std_text_field(_('Type on national sign'))

    class Meta:
        verbose_name = _("Type on national sign")
        verbose_name_plural = _("Types on national sign")


class TypeProfession(AbstractOrder):
    name = std_text_field(_('Type on profession'))

    class Meta:
        verbose_name = _("Type on profession")
        verbose_name_plural = _("Types on profession")


class TypeLifestyle(AbstractOrder):
    name = std_text_field(_('Type on lifestyle'))

    class Meta:
        verbose_name = _("Type on lifestyle")
        verbose_name_plural = _("Types on lifestyle")


class TypeBrightAppearance(AbstractOrder):
    name = std_text_field(_('Type on bright appearance'))

    class Meta:
        verbose_name = _("Type on bright appearance")
        verbose_name_plural = _("Types on bright appearance")


class TypeHistorical(AbstractOrder):
    name = std_text_field(_('Type in historical projects'))

    class Meta:
        verbose_name = _("Type in historical projects")
        verbose_name_plural = _("Types in historical projects")


class TypeSurvey(AbstractOrder):
    name = std_text_field(_('Type of survey'))

    class Meta:
        verbose_name = _("Type of survey")
        verbose_name_plural = _("Types of surveys")


class ReadinessScene(AbstractOrder):
    name = std_text_field(_('Readiness in scene'))

    class Meta:
        verbose_name = _("Readiness in scene")
        verbose_name_plural = _("Readiness in scenes")


class CreativeActivity(AbstractOrder):
    name = std_text_field(_('Creative activity'))

    class Meta:
        verbose_name = _("Creative activity")
        verbose_name_plural = _("Creative activities")


class AbstractHumanAppearance(models.Model):
    appearance = models.ManyToManyField(TypeAppearanceHuman, verbose_name=_('Type of Appearance'),
                                        related_name='appearance_human', blank=True, null=True)
    appearance_desc = std_text_field(_('Explain type of appearance'))
    national = models.ForeignKey(TypeNationalHuman, verbose_name=_('National Type'),
                                 related_name='national_human', blank=True, null=True)
    national_desc = std_text_field(_('Explain national'))
    body = models.ForeignKey(TypeBodyHuman, verbose_name=_('Body Type'),
                             related_name='body_human', blank=True, null=True)
    body_desc = std_text_field(_('Explain body'))
    feature_appearance = models.ManyToManyField(TypeFeatureAppearanceHuman, verbose_name=_('Feature appearance'),
                                                blank=True, null=True)
    another_feature = std_text_field(_('Text of Another feature of appearance'))
    growth = models.IntegerField(_('Growth'), choices=GROWTH, blank=True, null=True, default=None)
    weight = models.IntegerField(_('Weight'), choices=WEIGHT, blank=True, null=True, default=None)
    clothing_size = models.IntegerField(_('Clothing size'), choices=CLOTHING_SIZE, blank=True, null=True, default=None)
    shoe_size = models.IntegerField(_('Shoe size'), choices=SHOE_SIZE, blank=True, null=True, default=None)
    head_size = models.IntegerField(_('Head size'), choices=HEAD_SIZE, blank=True, null=True, default=None)
    hair_color = models.ForeignKey(HairColor, verbose_name=_('Hair color'),
                                   related_name='hair_color', blank=True, null=True)
    natural_hair_color = models.ForeignKey(HairColor, verbose_name=_('Natural hair color'),
                                   related_name='naturalhair_color', blank=True, null=True)
    have_wig = models.BooleanField(_('Have wig'), default=False)
    hair_length = models.ForeignKey(HairLength, verbose_name=_('Length of hair'),
                                    related_name='hair_length', blank=True, null=True)
    hair_texture = models.ForeignKey(HairTexture, verbose_name=_('Texture of hair'),
                                     related_name='hair_texture', blank=True, null=True)
    eye_color = models.ForeignKey(EyeColor, verbose_name=_('Eye color'),
                                  related_name='eye_color', blank=True, null=True)
    wear_glasses = models.BooleanField(_('Wear glasses'), default=False)
    wear_colour_lens = models.BooleanField(_('Wear colour lens'), default=False)
    have_glasses_collection = models.BooleanField(_('Have collection of glasses'), default=False)
    skin_color = models.ForeignKey(SkinColor, verbose_name=_('Color of skin'),
                                   related_name='color_skin', blank=True, null=True)
    piercing = std_text_field(_('Piercing'))
    tattoo = std_text_field(_('Tattoo'))
    feature_physique = std_text_field(_('Feature of physique'))
    feature_structure_body = std_text_field(_('Which feature of structure body'))
    nonstandard_growth = models.BooleanField(_('Non-standard growth'), default=False)
    pregnant = models.BooleanField(_('Pregnant'), default=False)
    similarity = std_text_field(_('Which person similarity'))
    twins = std_text_field(_('Have brother(sister) twins'))

    class Meta:
        verbose_name = _("Human appearance")
        verbose_name_plural = _("Human appearances")
        abstract = True

    @property
    def another_feature_split(self):
        result = self.another_feature.split(',')
        return map(lambda x: ' '.join(x.split()),result)

    @property
    def tattoo_split(self):
        result = self.tattoo.split(',')
        return map(lambda x: ' '.join(x.split()),result)

    @property
    def piercing_split(self):
        result = self.piercing.split(',')
        return map(lambda x: ' '.join(x.split()),result)


class LanguageSpeak(AbstractName):
    pass

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


LNG_SKILL_UNKNOWN = 0
LNG_SKILL_BASE = 1
LNG_SKILL_CONVERSATIONAL = 2

LNG_SKILL_CHOICES = (
    (LNG_SKILL_UNKNOWN, _("Unknown")),
    (LNG_SKILL_BASE, _("Base")),
    (LNG_SKILL_CONVERSATIONAL, _("Conversational")),
)


@python_2_unicode_compatible
class LanguageSkill(models.Model):
    speak = models.ForeignKey(LanguageSpeak, verbose_name=_('Language speak'),
                              related_name='language_skill', blank=True, null=True)
    level = models.IntegerField(_('Level'), choices=LNG_SKILL_CHOICES, blank=True, null=True, default=LNG_SKILL_UNKNOWN)

    class Meta:
        verbose_name = _("Language skill")
        verbose_name_plural = _("Language skills")

    def __str__(self):
        return "%s - %s" % (self.speak.name, self.get_level_display())


class TypeDance(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of dance")
        verbose_name_plural = _("Types of dances")


class DanceSkill(AbstractSkill):
    skill = models.ForeignKey(TypeDance, verbose_name=_('Dance type'),
                              related_name='dance_skill')

    class Meta:
        verbose_name = _("Dance skill")
        verbose_name_plural = _("Dance skills")


class TypeVocal(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of vocal")
        verbose_name_plural = _("Types of vocals")


class VocalSkill(AbstractSkill):
    skill = models.ForeignKey(TypeVocal, verbose_name=_('Vocal type'),
                              related_name='vocal_skill')

    class Meta:
        verbose_name = _("Vocal skill")
        verbose_name_plural = _("Vocal skills")


class TypeMusicInstrument(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of music instrument")
        verbose_name_plural = _("Types of music instruments")


class MusicSkill(AbstractSkill):
    skill = models.ForeignKey(TypeMusicInstrument, verbose_name=_('Music instrument type'),
                              related_name='music_skill')

    class Meta:
        verbose_name = _("Music skill")
        verbose_name_plural = _("Music skills")


class TypeDrive(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of driving")
        verbose_name_plural = _("Types of drivings")


class DriveSkill(AbstractSkill):
    skill = models.ForeignKey(TypeDrive, verbose_name=_('Type of driving'),
                              related_name='drive_skill')

    class Meta:
        verbose_name = _("Driving skill")
        verbose_name_plural = _("Driving skills")


class TypeSport(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of sport")
        verbose_name_plural = _("Types of sport")


class SportSkill(AbstractSkill):
    skill = models.ForeignKey(TypeSport, verbose_name=_('Type of sport'),
                              related_name='sport_skill')

    class Meta:
        verbose_name = _("Sport skill")
        verbose_name_plural = _("Sport skills")


class TypeSpecialSkill(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of special skill")
        verbose_name_plural = _("Types of special skill")


class SpecialSkill(AbstractSkill):
    skill = models.ForeignKey(TypeSpecialSkill, verbose_name=_('Type of special skill'),
                              related_name='special_skill')

    class Meta:
        verbose_name = _("Special skill")
        verbose_name_plural = _("Special skills")


class TypeOtherSkill(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of other skill")
        verbose_name_plural = _("Types of other skills")


class OtherSkill(AbstractSkill):
    skill = models.ForeignKey(TypeOtherSkill, verbose_name=_('Type of other skill'),
                              related_name='other_skill')

    class Meta:
        verbose_name = _("Other skill")
        verbose_name_plural = _("Other skills")


class AnimalType(AbstractName):
    pass

    class Meta:
        verbose_name = _("Animal type")
        verbose_name_plural = _("Animals types")


@python_2_unicode_compatible
class AnimalKind(AbstractImg):
    animal = models.ForeignKey(AnimalType, verbose_name=_('Animal'), related_name='kind')
    name = std_text_field(_('Name'))
    description = models.TextField(_("Description"), blank=True)
    name_en = std_text_field(_('English name'))

    class Meta:
        verbose_name = _("Animal kind")
        verbose_name_plural = _("Animals kinds")

    def __str__(self):
        return "%s :: %s" % (self.animal.name, self.name)


@python_2_unicode_compatible
class Animal(AbstractName):
    animal = models.ForeignKey(AnimalType, verbose_name=_('Animal'), related_name='animals')
    animalkind = models.ForeignKey(AnimalKind, verbose_name=_('Kind'), related_name='kind', blank=True, null=True)

    class Meta:
        verbose_name = _("Animal")
        verbose_name_plural = _("Animals")

    def __str__(self):
        return "%s :: %s" % (self.name, self.animal.name)


class TransportType(AbstractName):
    pass

    class Meta:
        verbose_name = _("Transport type")
        verbose_name_plural = _("Transport types")


@python_2_unicode_compatible
class TransportMark(AbstractImg):
    ttype = models.ForeignKey(TransportType, verbose_name=_('Transport'), related_name='tmarks')
    name = std_text_field(_('Name'))
    description = models.TextField(_("Description"), blank=True)
    name_en = std_text_field(_('English name'))

    class Meta:
        verbose_name = _("Transport mark")
        verbose_name_plural = _("Transport mark")

    def __str__(self):
        return "%s :: %s" % (self.ttype.name, self.name)


@python_2_unicode_compatible
class Vehicle(AbstractName):
    ttype = models.ForeignKey(TransportType, verbose_name=_('Transport'), related_name='t_vehicles')
    tmark = models.ForeignKey(TransportMark, verbose_name=_('Mark'), related_name='m_vehicles', blank=True, null=True)

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return "%s :: %s" % (self.name, self.ttype.name)


class SurveyObjectType(AbstractName):
    pass

    class Meta:
        verbose_name = _("Survey object type")
        verbose_name_plural = _("Survey object types")


@python_2_unicode_compatible
class SurveyObject(AbstractName):
    stype = models.ForeignKey(SurveyObjectType, verbose_name=_('Type'), related_name='t_s_o')

    class Meta:
        verbose_name = _("Survey object")
        verbose_name_plural = _("Survey objects")

    def __str__(self):
        return "%s :: %s" % (self.name, self.stype.name)


class SurveySuitType(AbstractName):
    overall = models.BooleanField(_('Overall'), default=False)

    class Meta:
        verbose_name = _("Survey suit type")
        verbose_name_plural = _("Survey suits types")


@python_2_unicode_compatible
class SurveySuit(AbstractName):
    stype = models.ForeignKey(SurveySuitType, verbose_name=_('Type'), related_name='t_s_o')

    class Meta:
        verbose_name = _("Survey suit")
        verbose_name_plural = _("Survey suits")

    def __str__(self):
        return "%s :: %s" % (self.name, self.stype.name)


class RequisiteType(AbstractName):
    pass

    class Meta:
        verbose_name = _("Requisite type")
        verbose_name_plural = _("Requisite types")


@python_2_unicode_compatible
class Requisite(AbstractName):
    rtype = models.ForeignKey(RequisiteType, verbose_name=_('Type'))

    class Meta:
        verbose_name = _("Requisite")
        verbose_name_plural = _("Requisites")

    def __str__(self):
        return "%s :: %s" % (self.name, self.rtype.name)


@python_2_unicode_compatible
class Child(AbstractName):
    birthdate = models.DateField(verbose_name=_('Date birth'), blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDER_CHOICES, blank=True)
    twins = models.BooleanField(_('Twins'), default=False)

    class Meta:
        verbose_name = _("Child")
        verbose_name_plural = _("Children")

    def __str__(self):
        return "%s :: %s" % (self.name, self.gender)


class AbstractPersonalData(models.Model):
    citizen_of_russia = models.BooleanField(_('Russia citizenship'), default=True)
    citizenship = models.CharField(max_length=30, verbose_name=_('Citizenship'), blank=True)
    foreign_passport = models.BooleanField(_('Foreign passport'), default=False)
    foreign_passport_expired = models.DateField(verbose_name=_('Foreign passport expired'), blank=True, null=True)
    inn = models.CharField(max_length=12, verbose_name=_('INN'), blank=True)
    insurance = models.CharField(max_length=12, verbose_name=_('Certificate of insurance'), blank=True)
    passport_series = models.CharField(max_length=40, verbose_name=_('Passport series'), blank=True)
    passport_num = models.CharField(max_length=40, verbose_name=_('Passport number'), blank=True)
    passport_issued = std_text_field(_('Passport issued'))
    passport_date = models.DateField(verbose_name=_('Date of passport issued'), blank=True, null=True)
    passport_registration = std_text_field(_('Passport registration'))

    class Meta:
        verbose_name = _("Personal Data")
        verbose_name_plural = _("Personal Data")
        abstract = True


class AbstractTypeActor(models.Model):
    type_national = models.ManyToManyField(TypeNational, verbose_name=_('Type of national sign'),
                                           blank=True, null=True)
    type_profession = models.ManyToManyField(TypeProfession, verbose_name=_('Type on profession'),
                                             blank=True, null=True)
    type_lifestyle = models.ManyToManyField(TypeLifestyle, verbose_name=_('Type on lifestyle'),
                                            blank=True, null=True)
    type_bright_appearance = models.ManyToManyField(TypeBrightAppearance,
                                                    verbose_name=_('Type on bright appearance'), blank=True, null=True)
    type_historical = models.ManyToManyField(TypeHistorical,
                                             verbose_name=_('Type in historical projects'), blank=True, null=True)

    class Meta:
        verbose_name = _("Type of actor")
        verbose_name_plural = _("Types of actors")
        abstract = True


VOICE_UNKNOWN = 0
VOICE_TENOR = 1
VOICE_BARITONE = 2
VOICE_MEZZO_SOPRANO = 3
VOICE_VIOLA = 4
VOICE_SOPRANO = 5
VOICE_BASS = 6

VOICE_CHOICES = (
    (VOICE_UNKNOWN, _("Unknown")),
    (VOICE_TENOR, _("Tenor")),
    (VOICE_BARITONE, _("Baritone")),
    (VOICE_MEZZO_SOPRANO, _("Mezzo soprano")),
    (VOICE_VIOLA, _("Viola")),
    (VOICE_SOPRANO, _("Soprano")),
    (VOICE_BASS, _("Bass")),
)


class HumanSkill(models.Model):
    language = models.ManyToManyField(LanguageSkill, verbose_name=_('Language skill'),
                                      blank=True, null=True, related_name='lng_skill')
    dance = models.ManyToManyField(DanceSkill, verbose_name=_('Dance skill'),
                                   blank=True, null=True, related_name='dnc_skill')
    drive = models.ManyToManyField(DriveSkill, verbose_name=_('Drive skill'),
                                   blank=True, null=True, related_name='drv_skill')
    other = models.ManyToManyField(OtherSkill, verbose_name=_('Other skill'),
                                   blank=True, null=True, related_name='oth_skill')
    music = models.ManyToManyField(MusicSkill, verbose_name=_('Music skill'),
                                   blank=True, null=True, related_name='msc_skill')
    vocal = models.ManyToManyField(VocalSkill, verbose_name=_('Vocal skill'),
                                   blank=True, null=True, related_name='vlc_skill')
    sport = models.ManyToManyField(SportSkill, verbose_name=_('Sport skill'),
                                   blank=True, null=True, related_name='spr_skill')
    special = models.ManyToManyField(SpecialSkill, verbose_name=_('Special skill'),
                                     blank=True, null=True, related_name='spc_skill')
    language_addon = std_text_field(_('Language addon text'))
    dance_addon = std_text_field(_('Dance addon text'))
    drive_addon = std_text_field(_('Drive skill addon text'))
    other_addon = std_text_field(_('Special skill addon text'))
    music_addon = std_text_field(_('Music addon text'))
    vocal_addon = std_text_field(_('Vocal addon text'))
    sport_addon = std_text_field(_('Sport addon text'))
    special_addon = std_text_field(_('Special skill addon text'))
    voice_tone = models.IntegerField(verbose_name=_('Voice tone'), choices=VOICE_CHOICES,
                                     blank=True, null=True, default=VOICE_UNKNOWN)
    spoken_dialect = std_text_field(_('Spoken dialect'))

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        abstract = True
