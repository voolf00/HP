# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table('doctor')

        # Deleting model 'Patient'
        db.delete_table('patient')

        # Adding model 'Who'
        db.create_table(u'medic_who', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_who', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'medic', ['Who'])

        # Adding model 'Profile'
        db.create_table('doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('secondName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('is_who', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medic.Who'])),
            ('diagnoz', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('vypisan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('model3d', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'medic', ['Profile'])


    def backwards(self, orm):
        # Adding model 'Doctor'
        db.create_table('doctor', (
            ('zvanie', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('secondName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('glav_doctore', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'medic', ['Doctor'])

        # Adding model 'Patient'
        db.create_table('patient', (
            ('diagnoz', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('model3d', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('vypisan', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('secondName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'medic', ['Patient'])

        # Deleting model 'Who'
        db.delete_table(u'medic_who')

        # Deleting model 'Profile'
        db.delete_table('doctor')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'medic.profile': {
            'Meta': {'object_name': 'Profile', 'db_table': "'doctor'"},
            'diagnoz': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_who': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['medic.Who']"}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'model3d': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'secondName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'vypisan': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'medic.who': {
            'Meta': {'object_name': 'Who'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_who': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['medic']