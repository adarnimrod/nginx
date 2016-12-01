Nginx
#####

.. image:: https://travis-ci.org/adarnimrod/nginx.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/nginx

Install Nginx with common minimal configuration. Just package installation,
create configuration directories and copy templates (if any). Configuration
templates can be placed inside :code:`templates/nginx/conf.d/` and server
templates inside :code:`templates/nginx/sites-enabled/` either inside the role
or relative to the playbook. OCSP, XSS and other such headers are not always
possible and therefore out of the scope of this role and left up to the user.

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7 and either Docker or Vagrant and Virtualbox.
Install the Python dependencies, dependent roles and roles required for
testing:

.. code:: shell

    pip install -r tests/requirements.txt
    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule dependency

To run the full test suite:

.. code:: shell

    pre-commit run --all-files
    molecule test --platform all

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
