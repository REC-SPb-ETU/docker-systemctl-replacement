import unittest
from files.docker.systemctl import checkstatus


class TestCheckStatus(unittest.TestCase):
    def setUp(self):
        self.checkstatus = checkstatus

    def test_simple_case(self):
        self.assertEqual(self.checkstatus("/bin/true"), (True, "/bin/true"))

    def test_case_with_arguments(self):
        self.assertEqual(self.checkstatus("/usr/sbin/cron -f $EXTRA_OPTS"), (True, "/usr/sbin/cron -f $EXTRA_OPTS"))

    def test_case_with_prefix_at(self):
        self.assertEqual(self.checkstatus("@/usr/bin/pg_ctlcluster postgresql@%i --skip-systemctl-redirect %i start"),
                         (True, "/usr/bin/pg_ctlcluster --skip-systemctl-redirect %i start"))

    def test_case_with_prefix_hyphen(self):
        self.assertEqual(self.checkstatus("-/bin/plymouth update-root-fs --read-write"),
                         (False, "/bin/plymouth update-root-fs --read-write"))


if __name__ == "__main__":
    unittest.main()
