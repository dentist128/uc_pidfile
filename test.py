# -*- coding: utf-8 -*-
# uc_pidfile - A set of classes and functions for managing pidfile.
# It is part of the Unicon project.
# https://unicon.10k.me
#
# Copyright © 2020 Eduard S. Markelov.
# All rights reserved.
# Author: Eduard S. Markelov <markeloveduard@gmail.com>
#
# This program is Free Software; you can redistribute it and/or modify it under
# the terms of version three of the GNU Affero General Public License as
# published by the Free Software Foundation and included in the file LICENSE.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""
Set of the tests for package.
"""
import os
import unittest
import uc_pidfile as pid


class TestSimplePid(unittest.TestCase):
    """
    Set of the tests for package.
    """
    def __init__(self, *args, **kwargs):
        self.testfilename = "/tmp/test.pid"
        super(TestSimplePid, self).__init__(*args, **kwargs)

    def test_process_exists(self):
        """
        Checks if the function returns True for current process id.
        """
        self.assertTrue(pid.process_exists(os.getpid()))

    def test_process_not_exists(self):
        """
        Checks if the function returns False for non existent process id.
        """
        with open("/proc/sys/kernel/pid_max") as handle:
            max__pid = int(handle.readline().strip())
        self.assertTrue(not pid.process_exists(max__pid + 1))

    def test_read_pid_no_file(self):
        """
        Checks if the function returns None if pidfile not exists.
        """
        self.assertIsNone(pid.read_pid("/tmp/never_exists_file_012821"))

    def test_read_pid(self):
        """
        Checks if the function returns valid process id.
        """
        with open(self.testfilename, "w") as handle:
            handle.write("123")

        ppid = pid.read_pid(self.testfilename)

        self.assertEqual(123, ppid)

        os.remove(self.testfilename)

    def test_read_pid_not_found(self):
        """
        Checks if the function returns None if pidfile not exists.
        """
        self.assertIsNone(pid.read_pid("/hallapullala.test`"))


    def test_validate_not(self):
        """
        Checks if the function returns False if the contents of the pidfile are not integer.
        """
        with open(self.testfilename, "w") as handle:
            handle.write("1ggdw1312")

        ppid = pid.validate_pidfile(self.testfilename)
        self.assertFalse(ppid)

        os.remove(self.testfilename)

    def test_pid(self):
        """
        Checks if the pidfile was created and pid written are valid.
        """
        pid.PidFile(self.testfilename)
        self.assertEqual(os.getpid(), pid.read_pid(self.testfilename))


if __name__ == "__main__":
    unittest.main(verbosity=2)
