from django.db import models

class Alimento(models.Model):
    codigomex2 = models.IntegerField(primary_key=True)
    nombre_del_alimento = models.CharField(max_length=255)
    energ_kcal = models.FloatField()
    carbohydrt = models.FloatField()
    lipid_tot = models.FloatField()
    protein = models.FloatField()
    fiber_td = models.FloatField()
    calcium = models.FloatField()
    iron = models.FloatField()
    ironhem = models.FloatField()
    ironnohem = models.FloatField()
    zinc = models.FloatField()
    vit_c = models.FloatField()
    thiamin = models.FloatField()
    riboflavin = models.FloatField()
    niacin = models.FloatField()
    panto_acid = models.FloatField()
    vit_b6 = models.FloatField()
    folic_acid = models.FloatField()
    food_folate = models.FloatField()
    folate_dfe = models.FloatField()
    vit_b12 = models.FloatField()
    vit_a_rae = models.FloatField()
    vit_e = models.FloatField()
    vit_d_iu = models.FloatField()
    vit_k = models.FloatField()
    fa_sat = models.FloatField()
    fa_mono = models.FloatField()
    fa_poly = models.FloatField()
    chole = models.IntegerField()


class Alimento1(models.Model):
    id = models.IntegerField(primary_key=True)
    codigomex2 = models.IntegerField()
    nombre_del_alimento = models.CharField(max_length=255)
    energ_kcal = models.FloatField()
    carbohydrt = models.FloatField()
    lipid_tot = models.FloatField()
    protein = models.FloatField()
    fiber_td = models.FloatField()
    calcium = models.FloatField()
    iron = models.FloatField()
    ironhem = models.FloatField()
    ironnohem = models.FloatField()
    zinc = models.FloatField()
    vit_c = models.FloatField()
    thiamin = models.FloatField()
    riboflavin = models.FloatField()
    niacin = models.FloatField()
    panto_acid = models.FloatField()
    vit_b6 = models.FloatField()
    folic_acid = models.FloatField()
    food_folate = models.FloatField()
    folate_dfe = models.FloatField()
    vit_b12 = models.FloatField()
    vit_a_rae = models.FloatField()
    vit_e = models.FloatField()
    vit_d_iu = models.FloatField()
    vit_k = models.FloatField()
    fa_sat = models.FloatField()
    fa_mono = models.FloatField()
    fa_poly = models.FloatField()
    chole = models.FloatField()

class Alimento2(models.Model):
    id = models.IntegerField(primary_key=True)
    codigomex2 = models.IntegerField()
    nombre_del_alimento = models.CharField(max_length=255)
    energ_kcal = models.FloatField()
    carbohydrt = models.FloatField()
    lipid_tot = models.FloatField()
    protein = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.id
