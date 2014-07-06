# -*- coding: utf-8 -*-

import csv
import logging
import tablib   #La versi[on para Python3 de tablib 0.10.0 presenta errores al instalarse con pio
from datetime import datetime
from django.db.models import Model
from django.db.models.fields.files import FieldFile
from unicodedata import normalize
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import Context, Template
from django.conf import settings
from django.core.urlresolvers import reverse
from setuptools.compat import unicode


#Exportar a Excel
def export_as_excel(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % str(opts).replace('.', '_')
    try:
        field_names = modeladmin.model.get_csv_fields()
        v_field_names = field_names
    except:
        field_names = [field.name for field in opts.fields]
        v_field_names = [getattr(field, 'verbose_name') or field.name for field in opts.fields]
    v_field_names = map(lambda x: x.encode('utf-8') if x != 'ID' else 'Id', v_field_names)


    ax = []
    headers = v_field_names

    data = []

    data = tablib.Dataset(*data, headers=headers)
    for obj in queryset:
        acc = []
        for field in field_names:
            try:
                uf = getattr(obj, field)()
            except TypeError:
                try:
                    uf = getattr(obj, field)
                except:
                    uf = ' Error obteniendo el dato!'
            if uf is None:
                uf = ''
            elif isinstance(uf, datetime):
                uf = str(uf) #cambie todas las referencias de unicode por str pues tengo python3
            elif isinstance(uf, Model):
                uf = str(uf)
            elif isinstance(uf, FieldFile):
                uf = uf.url
            acc.append(uf)
        data.append(acc)
    response.write(data.xls)
    return response

export_as_excel.short_description = "Exportar como Excel"

#Exportar a CSV
def export_as_csv_action(description="Export selected objects as CSV file",
						 fields=None, exclude=None, header=True):
	"""
	This function returns an export csv action
	'fields' and 'exclude' work like in django ModelForm
	'header' is whether or not to output the column names as the first row
	"""

	from itertools import chain

	def export_as_csv(modeladmin, request, queryset):
		"""
		Generic csv export admin action.
		based on http://djangosnippets.org/snippets/2369/
		"""
		opts = modeladmin.model._meta
		field_names = set([field.name for field in opts.fields])
		many_to_many_field_names = set([many_to_many_field.name for many_to_many_field in opts.many_to_many])
		if fields:
			fieldset = set(fields)
			field_names = field_names & fieldset
		elif exclude:
			excludeset = set(exclude)
			field_names = field_names - excludeset

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

		writer = csv.writer(response)
		if header:
			writer.writerow(list(chain(field_names, many_to_many_field_names)))
		for obj in queryset:
			row = []
			for field in field_names:
				row.append(unicode(getattr(obj, field)))
			for field in many_to_many_field_names:
				row.append(unicode(getattr(obj, field).all()))

			writer.writerow(row)
		return response
	export_as_csv.short_description = description
	return export_as_csv

export_as_csv_action.short_description = "Exportar como CSV"