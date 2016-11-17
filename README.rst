Nginx
#####

Install Nginx with common minimal configuration. Just package installation,
create configuration directories and copy templates (if any). Configuration
templates can be placed inside :code:`templates/nginx/conf.d/` and server
templates inside :code:`templates/nginx/sites-enabled/` either inside the role
or relative to the playbook. OCSP, XSS and other such headers are not always
possible and therefore out of the scope of this role and left up to the user.

Requirements
------------

See :code:`meta/main.yml`, :code:`tests/requirements.yml` and assertions at
the top of :code:`tasks/main.yml`.

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

Testing requires Virtualbox and Vagrant and Python 2.7. Install the Python
dependencies, add pre-commit hooks by running:

.. code:: shell

    pip install -r tests/requirements.txt
    pre-commit install

To run the full test suite:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule test --platform all
    pre-commit run --all-files

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
