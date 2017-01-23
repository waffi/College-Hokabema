# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-01-11 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghtelectroniccenter', '0007_auto_20170106_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alamat',
            fields=[
                ('id_alamat', models.IntegerField(db_column='ID_ALAMAT', primary_key=True, serialize=False)),
                ('id_pelanggan', models.IntegerField(db_column='ID_PELANGGAN')),
                ('latitude', models.FloatField(blank=True, db_column='LATITUDE', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='LONGITUDE', null=True)),
                ('jalan', models.CharField(blank=True, db_column='JALAN', max_length=20, null=True)),
                ('rt', models.IntegerField(blank=True, db_column='RT', null=True)),
                ('rw', models.IntegerField(blank=True, db_column='RW', null=True)),
                ('no_rumah', models.IntegerField(blank=True, db_column='NO_RUMAH', null=True)),
                ('kecamatan', models.CharField(blank=True, db_column='KECAMATAN', max_length=20, null=True)),
                ('desa_kelurahan', models.CharField(blank=True, db_column='DESA_KELURAHAN', max_length=20, null=True)),
                ('provinsi', models.CharField(blank=True, db_column='PROVINSI', max_length=20, null=True)),
                ('kota_kabupaten', models.CharField(blank=True, db_column='KOTA_KABUPATEN', max_length=20, null=True)),
                ('kode_pos', models.CharField(blank=True, db_column='KODE_POS', max_length=6, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'alamat',
            },
        ),
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id_berita', models.IntegerField(db_column='ID_BERITA', primary_key=True, serialize=False)),
                ('deskripsi', models.TextField(blank=True, db_column='DESKRIPSI', null=True)),
                ('gambar', models.TextField(blank=True, db_column='GAMBAR', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'berita',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id_cart', models.IntegerField(db_column='ID_CART', primary_key=True, serialize=False)),
                ('id_pelanggan', models.IntegerField(db_column='ID_PELANGGAN')),
                ('id_alamat', models.IntegerField(db_column='ID_ALAMAT')),
                ('tanggal', models.DateTimeField(blank=True, db_column='TANGGAL', null=True)),
                ('status_telah_dipesan', models.SmallIntegerField(blank=True, db_column='STATUS_TELAH_DIPESAN', null=True)),
                ('status_verifikasi', models.SmallIntegerField(blank=True, db_column='STATUS_VERIFIKASI', null=True)),
                ('status_pembayaran', models.SmallIntegerField(blank=True, db_column='STATUS_PEMBAYARAN', null=True)),
                ('status_pengiriman', models.SmallIntegerField(blank=True, db_column='STATUS_PENGIRIMAN', null=True)),
                ('total_keseluruhan', models.FloatField(blank=True, db_column='TOTAL_KESELURUHAN', null=True)),
                ('pajak', models.FloatField(blank=True, db_column='PAJAK', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Kandungan',
            fields=[
                ('id_kandungan', models.IntegerField(db_column='ID_KANDUNGAN', primary_key=True, serialize=False)),
                ('nama_kandungan', models.CharField(blank=True, db_column='NAMA_KANDUNGAN', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'kandungan',
            },
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.IntegerField(db_column='ID_KATEGORI', primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(blank=True, db_column='NAMA_KATEGORI', max_length=10, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'kategori',
            },
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id_komentar', models.IntegerField(db_column='ID_KOMENTAR', primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=20, null=True)),
                ('deskripsi_komentar', models.CharField(blank=True, db_column='DESKRIPSI_KOMENTAR', max_length=200, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'komentar',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.IntegerField(db_column='ID_MENU', primary_key=True, serialize=False)),
                ('id_kategori', models.IntegerField(db_column='ID_KATEGORI')),
                ('nama_menu', models.CharField(blank=True, db_column='NAMA_MENU', max_length=20, null=True)),
                ('deskripsi_menu', models.CharField(blank=True, db_column='DESKRIPSI_MENU', max_length=200, null=True)),
                ('stok_menu', models.IntegerField(blank=True, db_column='STOK_MENU', null=True)),
                ('gambar_menu', models.TextField(blank=True, db_column='GAMBAR_MENU', null=True)),
                ('harga_menu', models.FloatField(blank=True, db_column='HARGA_MENU', null=True)),
                ('discount', models.FloatField(blank=True, db_column='DISCOUNT', null=True)),
                ('kalori', models.FloatField(blank=True, db_column='KALORI', null=True)),
                ('protein', models.FloatField(blank=True, db_column='PROTEIN', null=True)),
                ('natrium', models.FloatField(blank=True, db_column='NATRIUM', null=True)),
                ('lemak', models.FloatField(blank=True, db_column='LEMAK', null=True)),
                ('karbohidrat', models.FloatField(blank=True, db_column='KARBOHIDRAT', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Menuhaskandungan',
            fields=[
                ('id_kandungan', models.IntegerField(db_column='ID_KANDUNGAN', primary_key=True, serialize=False)),
                ('id_menu', models.IntegerField(db_column='ID_MENU')),
            ],
            options={
                'managed': False,
                'db_table': 'menuhaskandungan',
            },
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id_outlet', models.IntegerField(db_column='ID_OUTLET', primary_key=True, serialize=False)),
                ('waktu_buka', models.TimeField(blank=True, db_column='WAKTU_BUKA', null=True)),
                ('waktu_tutup', models.TimeField(blank=True, db_column='WAKTU_TUTUP', null=True)),
                ('latitude_outlet', models.FloatField(blank=True, db_column='LATITUDE_OUTLET', null=True)),
                ('longitude_outlet', models.FloatField(blank=True, db_column='LONGITUDE_OUTLET', null=True)),
                ('jalan', models.CharField(blank=True, db_column='JALAN', max_length=20, null=True)),
                ('rt', models.IntegerField(blank=True, db_column='RT', null=True)),
                ('rw', models.IntegerField(blank=True, db_column='RW', null=True)),
                ('no_rumah', models.IntegerField(blank=True, db_column='NO_RUMAH', null=True)),
                ('kecamatan', models.CharField(blank=True, db_column='KECAMATAN', max_length=20, null=True)),
                ('desa_kelurahan', models.CharField(blank=True, db_column='DESA_KELURAHAN', max_length=20, null=True)),
                ('provinsi', models.CharField(blank=True, db_column='PROVINSI', max_length=20, null=True)),
                ('kota_kabupaten', models.CharField(blank=True, db_column='KOTA_KABUPATEN', max_length=20, null=True)),
                ('kode_pos', models.CharField(blank=True, db_column='KODE_POS', max_length=6, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'outlet',
            },
        ),
        migrations.CreateModel(
            name='Outlethassevis',
            fields=[
                ('id_servis', models.IntegerField(db_column='ID_SERVIS', primary_key=True, serialize=False)),
                ('id_outlet', models.IntegerField(db_column='ID_OUTLET')),
            ],
            options={
                'managed': False,
                'db_table': 'outlethassevis',
            },
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id_pelanggan', models.IntegerField(db_column='ID_PELANGGAN', primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, db_column='USER_NAME', max_length=10, null=True)),
                ('password', models.CharField(blank=True, db_column='PASSWORD', max_length=6, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=20, null=True)),
                ('nomor_hp', models.CharField(blank=True, db_column='NOMOR_HP', max_length=12, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'pelanggan',
            },
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id_menu', models.IntegerField(db_column='ID_MENU', primary_key=True, serialize=False)),
                ('id_cart', models.IntegerField(db_column='ID_CART')),
                ('jumlah_pesanan', models.FloatField(blank=True, db_column='JUMLAH_PESANAN', null=True)),
                ('total_harga', models.FloatField(blank=True, db_column='TOTAL_HARGA', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'pesanan',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id_menu', models.IntegerField(db_column='ID_MENU', primary_key=True, serialize=False)),
                ('id_pelanggan', models.IntegerField(db_column='ID_PELANGGAN')),
                ('nilai', models.IntegerField(blank=True, db_column='NILAI', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'rating',
            },
        ),
        migrations.CreateModel(
            name='Servis',
            fields=[
                ('id_servis', models.IntegerField(db_column='ID_SERVIS', primary_key=True, serialize=False)),
                ('nama_servis', models.CharField(blank=True, db_column='NAMA_SERVIS', max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'servis',
            },
        ),
    ]