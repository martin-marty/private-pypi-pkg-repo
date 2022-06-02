'''
Created on 2 Jun 2022

@author: martin
'''
from django.test.runner import DiscoverRunner


class Runner(DiscoverRunner):
    def __init__(
            self,
            pattern=None,
            top_level=None,
            verbosity=1,
            interactive=True,
            failfast=False,
            keepdb=False,
            reverse=False,
            debug_mode=False,
            debug_sql=False,
            parallel=0,
            tags=None,
            exclude_tags=None,
            test_name_patterns=None,
            pdb=False,
            buffer=False,
            enable_faulthandler=True,
            timing=False,
            shuffle=False,
            logger=None, **
            kwargs):
        if not debug_mode:
            debug_mode = True
        DiscoverRunner.__init__(self, pattern=pattern, top_level=top_level, verbosity=verbosity, interactive=interactive, failfast=failfast, keepdb=keepdb, reverse=reverse, debug_mode=debug_mode, debug_sql=debug_sql,
                                parallel=parallel, tags=tags, exclude_tags=exclude_tags, test_name_patterns=test_name_patterns, pdb=pdb, buffer=buffer, enable_faulthandler=enable_faulthandler, timing=timing, shuffle=shuffle, logger=logger, **kwargs)

    def teardown_test_environment(self, **kwargs):
        DiscoverRunner.teardown_test_environment(self, **kwargs)
