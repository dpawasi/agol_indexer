# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-21 04:54
from __future__ import unicode_literals

from django.db import migrations


def direct_relationship(apps, schema_editor):
    Webmap_Item = apps.get_model("webmap", "Webmap_Item")
    for webmap_item in Webmap_Item.objects.all():
        for webmap in webmap_item.webmap.all():
            for agol in webmap_item.agol.all():
                webmap.agols.add(agol)
            webmap.save()
        webmap_item.delete()


def indirect_relationship(apps, schema_editor):
    Webmap_Item = apps.get_model("webmap", "Webmap_Item")
    Webmap = apps.get_model("webmap", "Webmap")
    for webmap in Webmap.objects.all():
        webmap_item = Webmap_Item()
        webmap_item.name = "{} - AGOL Items".format(webmap.name)
        webmap_item.description = "Auto-generated entry to capture Webmap-AGOL_Item relationships"
        webmap_item.save()
        webmap_item.webmap.add(webmap)
        for agol in webmap.agols.all():
            webmap_item.agol.add(agol)
        webmap_item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('webmap', '0007_webmap_agols'),
    ]

    operations = [
        migrations.RunPython(direct_relationship, indirect_relationship),
    ]
