import os
import logging

from gabbi.suite import GabbiSuite
from nose.plugins import Plugin
from unittest.loader import defaultTestLoader

# The module that build_tests comes from.
from gabbi import driver

log = logging.getLogger(__name__)


class Nabbit(Plugin):
    extension = None
    suiteClass = GabbiSuite

    def options(self, parser, env):
        """Register commmand line options.
        """
        Plugin.options(self, parser, env)

    def configure(self, options, config):
        """Configure plugin.
        """
        Plugin.configure(self, options, config)

    def prepareTestLoader(self, loader):
        """Capture loader's suiteClass.

        This is used to create test suites from doctest files.

        """
        self.suiteClass = loader.suiteClass

    def loadTestsFromModule(self, module):
        """Load Gabbits from the Module
        """
        TESTS_DIR = 'gabbits'

        test_dir = os.path.join(os.path.dirname(module.__file__), TESTS_DIR)
        tests = driver.build_tests(test_dir, defaultTestLoader,
                                   host='localhost', port=8000)
        yield tests
