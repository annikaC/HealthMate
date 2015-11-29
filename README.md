# healthmate

This is the repository for the Healthmate website.

## Prerequisites
Vagrant
VirtualBox
Ansible

## Installation

In the root of this project, run `vagrant up`

After the script has finished provisioning the box, run `vagrant ssh`

## Project Setup

When logged into the box, run `workon healthmate`

Then run `./manage.py migrate` to setup the database

To create a user, run `./manage.py createsuperuser`

To run the test server: `invoke runserver`

Navigate to localhost:8000 in your browser to see the site!

## Translation

All translations are stored in the locale files.

Run `./manage.py compilemessages` to compile translation files.

Use the language switcher to see other languages

## Todo

* Some parts of the site are untranslated and needs the correct template tags. 
* Form translation
* Text download for services around you
