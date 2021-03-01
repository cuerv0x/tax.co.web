from   datetime import datetime # for datetime.datetime.now
import os
import subprocess

from   django.core.files.storage import FileSystemStorage
from   django.http import HttpResponseRedirect
from   django.shortcuts import render
from   django.urls import reverse

from   run_make.forms import TaxConfigForm
import run_make.views.lib as lib



# PITFALL: These paths are simpler than one would expect because
# Django treats as root every DocumentRoot folder
# configured in apache2.conf. Name collisions must be hell.
rate_tables = {
      "/marginal_rates/most.csv" : "El impuesto para la mayoría de las categorías de ingreso:",
      "/marginal_rates/dividend.csv" : "El impuesto para los dividendos:",
      "/marginal_rates/ocasional_high.csv" : "El impuesto más alto para los ingresos ocasionales:",
      "/marginal_rates/ocasional_low.csv" : "El impuesto más bajo para los ingresos ocasionales:",
      "/vat-by-coicop.csv" : "El IVA, asignado por código COICOP:",
      "/vat-by-capitulo-c.csv" : "El IVA, asignado por código 'capitulo c'. (La mayoría de las compras en la ENPH son identificados por el COICOP, pero algunos usan este sistema alternativo.)" }

def ingest_full_spec ( request ):
  """ For commentary and simpler illustrations, see the functions
      ingest_json() and upload_multiple() in examples.py.
  """

  log = open ( "/mnt/web/logs/log_outer.txt", "a" )
  log . write ( "Here, it writes to the filesystem.\n" )
  log . write ( request . method + "\n" )
  log . close ()

  if request . method == 'POST':
    advanced_specs_form = TaxConfigForm ( request . POST )

    if advanced_specs_form . is_valid ():

      log = open ( "/mnt/web/logs/log_inner.txt", "a" )
      log . write ( "But this doesn't get written." )
      # This is what I'd like to write.
      #log . write( "\n".join(
      #    [ "user email: " + user_email,
      #      "user hash: " + user_hash,
      #      "user path: " + user_path ] ) )
      log . close ()

      user_email = advanced_specs_form . cleaned_data [ "user_email" ]
#      user_hash = lib.hash_from_str ( user_email )
#      user_path = os.path.join (
#          '/mnt/tax/users/',
#          user_hash )
#
#      lib.write_form_to_maybe_new_user_folder (
#          user_path,
#          advanced_specs_form )

#      return HttpResponseRedirect (
#        reverse (
#          'run_make:thank-for-spec',
#          kwargs = { "user_email" : user_email } ) )

  else: return render (
      request,
      'run_make/ingest_full_spec.html',
      { 'advanced_specs_form' : TaxConfigForm (),
        "rate_tables"         : rate_tables
       } )
