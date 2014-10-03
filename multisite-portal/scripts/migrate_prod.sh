#!/bin/sh
echo "starting production migration script"

export SITE=uk
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=isobar
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=us
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=us2
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/initial_data.json;
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=contacts
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/initial_data.json;
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ca
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=au
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=br
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=ch
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=jp
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;
export SITE=no
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=br2
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=de
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=dk
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=du
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=fr
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=hk
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ind
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=it
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ko
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ma
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=my
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;



export SITE=pt
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=se
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=th
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=tw
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=ukm
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ru
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=hu
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=nl
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.about --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.work --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.common --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.people --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate apps.news --fake 0001;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


<<COMMENT1
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/initial_data.json;
COMMENT1
