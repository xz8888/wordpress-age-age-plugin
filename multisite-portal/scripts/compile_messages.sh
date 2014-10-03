#!/bin/sh
echo "starting compiling messages"

SITE=uk
export SITE
python ../isobar/manage.py compilemessages

SITE=isobar
export SITE
python ../isobar/manage.py compilemessages

SITE=us
export SITE
python ../isobar/manage.py compilemessages

SITE=us2
export SITE
python ../isobar/manage.py compilemessages


SITE=ca
export SITE
python ../isobar/manage.py compilemessages

SITE=au
export SITE
python ../isobar/manage.py compilemessages

SITE=br
export SITE
python ../isobar/manage.py compilemessages

SITE=ch
export SITE
python ../isobar/manage.py compilemessages

SITE=jp
export SITE
python ../isobar/manage.py compilemessages

SITE=no
export SITE
python ../isobar/manage.py compilemessages

SITE=br2
export SITE
python ../isobar/manage.py compilemessages

SITE=de
export SITE
python ../isobar/manage.py compilemessages

SITE=dk
export SITE
python ../isobar/manage.py compilemessages

SITE=du
export SITE
python ../isobar/manage.py compilemessages

SITE=fr
export SITE
python ../isobar/manage.py compilemessages

SITE=hk
export SITE
python ../isobar/manage.py compilemessages

SITE=hu
export SITE
python ../isobar/manage.py compilemessages

SITE=ind
export SITE
python ../isobar/manage.py compilemessages

SITE=it
export SITE
python ../isobar/manage.py compilemessages

SITE=ko
export SITE
python ../isobar/manage.py compilemessages

SITE=ma
export SITE
python ../isobar/manage.py compilemessages

SITE=my
export SITE
python ../isobar/manage.py compilemessages

SITE=pt
export SITE
python ../isobar/manage.py compilemessages

SITE=se
export SITE
python ../isobar/manage.py compilemessages

SITE=th
export SITE
python ../isobar/manage.py compilemessages

SITE=tw
export SITE
python ../isobar/manage.py compilemessages
