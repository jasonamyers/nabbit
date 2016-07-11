import os
import logging
from pkg_resources import resource_filename

from gabbi.suite import GabbiSuite
from nose.plugins import Plugin
from wsgiref.simple_server import make_server, demo_app
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
        print self.__dict__
        print module

        test_dir = os.path.join(os.path.dirname(module.__file__), TESTS_DIR)
        print test_dir
        tests = driver.build_tests(test_dir, defaultTestLoader,
                                   intercept=demo_app({}, 'stuff'),
                                   # fixture_module=fixtures
                                  )
        yield tests

