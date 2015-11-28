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
