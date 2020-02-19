# Generated by Django 2.2.8 on 2019-12-07 17:37

import app.ex_fields.fields
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180716_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(editable=False, max_length=20, verbose_name='版本号')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '版本',
                'verbose_name_plural': '版本',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, '待审核'), (1, '未通过'), (2, '通过')], default=0, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='config',
            name='v2_config',
            field=app.ex_fields.fields.ConfigFieldV2(blank=True, null=True, verbose_name='v2版配置'),
        ),
        migrations.AddField(
            model_name='config',
            name='v2_real_config',
            field=jsonfield.fields.JSONField(blank=True, editable=False, null=True, verbose_name='解析后的config'),
        ),
        migrations.AddField(
            model_name='config',
            name='v2_schema',
            field=models.TextField(blank=True, null=True, verbose_name='json-editor配置'),
        ),
        migrations.AddField(
            model_name='config',
            name='v2_script',
            field=models.TextField(default='', verbose_name='js代码'),
        ),
        migrations.AlterField(
            model_name='config',
            name='config',
            field=app.ex_fields.fields.ConfigField(null=True, verbose_name='v1版配置'),
        ),
        migrations.AlterField(
            model_name='config',
            name='last_config',
            field=app.ex_fields.fields.ConfigField(blank=True, null=True, verbose_name='v1版旧配置'),
        ),
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='配置名称'),
        ),
    ]
