#!/bin/sh
echo "starting production migration script"

export SITE=uk
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;
python26 /var/www/deploy/isobar/current/isobar/apps/social/cron.py

export SITE=isobar
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;
python26 /var/www/deploy/isobar/current/isobar/apps/social/cron.py

export SITE=us
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=us2
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate common --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate work --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate about --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate people --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate news --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate video_promo --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate aboutisobar --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate contactisobar --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate workisobar --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate labsisobar --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate homeisobar --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate careerisobar --noinput;

python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/initial_data.json;
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/sites.json;
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/user.json;

export SITE=contacts
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate contactisobar --noinput;

python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/initial_data.json;
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/sites.json;
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/user.json;

export SITE=ca
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=au
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=br
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=ch
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=jp
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=no
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=br2
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=de
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=dk
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=du
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=fr
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=hk
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ind
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=it
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ko
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=ma
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=my
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;



export SITE=pt
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=se
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=th
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=tw
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=ukm
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=ru
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;


export SITE=hu
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=nl
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;

export SITE=sg
echo $SITE
python26 /var/www/deploy/isobar/current/isobar/manage.py syncdb --noinput;
python26 /var/www/deploy/isobar/current/isobar/manage.py migrate --all --noinput;



<<COMMENT1
//initialize 
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/initial_data.json;

//reset site table --> site value at CMS side
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/sites.json;

//reset admin
python26 /var/www/deploy/isobar/current/isobar/manage.py loaddata /var/www/deploy/isobar/current/isobar/user.json;


