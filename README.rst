ansible-nginx
#############

An Ansible role to install Nginx.

Requirements
------------

Debian Wheezy or later.

Role Variables
--------------

None.

Dependencies
------------

`Common role <https://www.shore.co.il/cgit/ansible-common/>`_

Example Playbook
----------------
::

    - hosts: servers
      roles:
      - role: nginx

License
-------

This software is licnesed under the MIT licese (see the ``LICENSE.txt`` file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/cgit/.

TODO
----

- Implement.
- Server health.
- OCSP.
- Collectd metrics.
- Log to syslog.
- Assertions.
- Wait for server to come online.
