#!/usr/bin/python
import sys
import os
import shutil
import string
from random import choice
from boto.cloudfront import CloudFrontConnection
from boto.cloudfront.origin import CustomOrigin
from django.core import management
os.environ['SITE'] = 'isobar'
import settings


ROOT_PATH = settings.ROOT_PATH
	
def create_site_dir(market_code):
	site_path = "%s/sites/%s" % (ROOT_PATH, market_code)

	if os.path.exists(site_path):
		sys.stderr.write("Site path exists: %s\n" % site_path)
		sys.exit(1)

	os.makedirs(site_path)

	return site_path

def update_settings_file(site_path, languages, market_code, agency_name, cloudfront_id):
	f = open("%s/settings.py" % site_path, 'r')
	contents = f.read()

	db_password = generate_password()
	language_codes = ''
	for language in languages:
		language_codes += "    ('%s', '%s'),\n" % (
				language['code'],
				language['name']
		)

	contents = contents.replace('<country_code>', market_code)
	contents = contents.replace('<agency_name>', agency_name)
	contents = contents.replace('<db_password>', db_password)
	contents = contents.replace('<language_codes>', language_codes)
	contents = contents.replace('<primary_language_code>', languages[0]['code'])
	contents = contents.replace('<cloudfront_id>', cloudfront_id)

	f = open("%s/settings.py" % site_path, 'w')
	f.write(contents)

def update_apache_config_file(market_code):
	f = open("%s/../config/%s.conf" % (ROOT_PATH, market_code), 'r')
	contents = f.read()

	contents = contents.replace('<country_code>', market_code)

	f = open("%s/../config/%s.conf" % (ROOT_PATH, market_code), 'w')
	f.write(contents)

def link_apache_config(market_code):
	f = open("%s/../config/vhost.conf" % ROOT_PATH, 'a')
	f.write("\nInclude /var/www/deploy/isobar/current/config/%s.conf" \
		% market_code)

def copy_base_assets(site_path):
	for file in ['__init__.py', 'settings.py', 'urls.py']:
		shutil.copy(
			"%s/sites/template/%s" % (ROOT_PATH, file),
			"%s/%s" % (site_path, file)
		)

	shutil.copy(
		"%s/../config/template.conf" % ROOT_PATH,
		"%s/../config/%s.conf" % (ROOT_PATH, market_code)
	)

def create_localisation_files(site_path, languages):
	os.makedirs("%s/locale" % ROOT_PATH)

	for language in languages:	
		management.call_command('makemessages',
							locale=language['code'],
							ignore_patterns=['*apps\\filebrowser*','*apps\\multilingual*','*apps\\tinymce*','*apps\\rosetta*','*apps\\isobar*'],
							verbosity=0)

	shutil.move(
		"%s/locale" % settings.ROOT_PATH,
		"%s/locale" % site_path
	)

def get_languages():
	number_languages = raw_input('Enter number of languages: ')
	try:
		number_languages = int(number_languages)
	except ValueError:
		sys.stderr.write("Invalid number entered.\n")
		sys.exit(1)

	languages = []
	for i in range(0, number_languages):
		language_code = raw_input('Enter language code %s (e.g. "en"): ' % str(i+1))
		language_name = raw_input('Enter language description %s (e.g. "English"): ' % str(i+1))

		languages.append({
			'code': language_code,
			'name': language_name,
		})

	return languages

def create_cloudfront_distro(market_code):
	origin_domain = "%s.origin.isobar.com" % market_code
	distro_comment = "%s Isobar production" % market_code

	c = CloudFrontConnection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
	origin = CustomOrigin(origin_domain, origin_protocol_policy='http-only')
	distro = c.create_distribution(origin=origin, enabled=True, comment=distro_comment)

	return distro

def generate_password():
	return ''.join([choice(string.letters + string.digits) \
		for i in range(9)])

if __name__ == "__main__":
	market_code = raw_input('Enter market code (e.g. "us", "uk" or "de") to create: ')
	languages = get_languages()
	agency_name = raw_input('Enter agency name (e.g. "glue Isobar"): ')

	site_path = create_site_dir(market_code)
	copy_base_assets(site_path)
	cloudfront_distro = create_cloudfront_distro(market_code)
	update_settings_file(site_path, languages, market_code, agency_name, cloudfront_distro.id)
	update_apache_config_file(market_code)
	link_apache_config(market_code)
	create_localisation_files(site_path, languages)

	print "\n\nCNAME: %s\n" % cloudfront_distro.domain_name