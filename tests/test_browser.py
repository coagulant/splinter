# -*- coding: utf-8 -*-

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from __future__ import with_statement

import unittest
import warnings

from splinter.exceptions import DriverNotFoundError

from fake_webapp import EXAMPLE_APP


class BrowserTest(unittest.TestCase):

    def browser_can_change_user_agent(self, webdriver):
        from splinter import Browser
        browser = Browser(driver_name=webdriver, user_agent="iphone")
        browser.visit(EXAMPLE_APP + "useragent")
        result = 'iphone' in browser.html
        browser.quit()

        return result

    def test_brower_can_still_be_imported_from_splinters_browser_module(self):
        from splinter.browser import Browser

    def test_should_raise_an_exception_when_browser_driver_is_not_found(self):
        with self.assertRaises(DriverNotFoundError):
            from splinter import Browser
            Browser('unknown-driver')

    def test_firefox_should_be_able_to_change_user_agent(self):
        self.assertTrue(self.browser_can_change_user_agent('firefox'))

    def test_chrome_should_be_able_to_change_user_agent(self):
        self.assertTrue(self.browser_can_change_user_agent('chrome'))

    def test_zope_testbrowser_should_be_able_to_change_user_agent(self):
        self.assertTrue(self.browser_can_change_user_agent('zope.testbrowser'))

    def test_should_support_with_statement(self):
        for browser in ('firefox', 'chrome', 'zope.testbrowser'):
            from splinter import Browser
            with Browser(browser) as internet:
                pass
