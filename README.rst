Nginx
#####

Install Nginx with common minimal configuration. Just package installation,
create configuration directories and copy templates (if any). Configuration
templates can be placed inside :code:`templates/nginx.conf.d/` and server
templates inside :code:`templates/nginx.sites-enabled/` either inside the role
or relative to the playbook.

Requirements
------------

- `Ansible 2.0 or later <https://www.ansible.com/>`_.
- `OpenBSD <http://www.openbsd.org/>`_ or `Debian <http://www.debian.org/>`_
  (OpenBSD 5.9 and Debian Jessie are tested, other versions or derivatives
  should also work).

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

To install the dependencies:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD)

To run the full test suite:

.. code:: shell

    molecule test

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

TODO
----

- dhparams.
- Status and/or metrics (http_status and http_stub_status modules).
- Rate limit (http_limit_req and http_limit_conn modules).
