# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table(u'pmi_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comienzo_pro', self.gf('django.db.models.fields.DateTimeField')()),
            ('final_pro', self.gf('django.db.models.fields.DateTimeField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'pmi', ['Proyecto'])

        # Adding model 'Tarea'
        db.create_table(u'pmi_tarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comienzo', self.gf('django.db.models.fields.DateTimeField')()),
            ('final', self.gf('django.db.models.fields.DateTimeField')()),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pmi.Proyecto'])),
        ))
        db.send_create_signal(u'pmi', ['Tarea'])


    def backwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table(u'pmi_proyecto')

        # Deleting model 'Tarea'
        db.delete_table(u'pmi_tarea')


    models = {
        u'pmi.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'comienzo_pro': ('django.db.models.fields.DateTimeField', [], {}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'final_pro': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pmi.tarea': {
            'Meta': {'object_name': 'Tarea'},
            'comienzo': ('django.db.models.fields.DateTimeField', [], {}),
            'final': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pmi.Proyecto']"})
        }
    }

    complete_apps = ['pmi']