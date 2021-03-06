# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from honeybee.radiance.command.ra_bmp import ra_bmp
from honeybee.radiance.parameters.ra_bmp import ra_bmp_parameters
import os


class RaBmpTestCase(unittest.TestCase):
    """Test for (honeybee/radiance/command/ra_bmp.py)."""

    # test prep
    def setUp(self):
        ra_bmp_para = ra_bmp_parameters()
        ra_bmp_para.exposure = '-3'

        self.ra_bmp = ra_bmp()
        self.ra_bmp.input_hdr_file = 'assets/sample.hdr'
        self.ra_bmp.ra_bmp_parameters = ra_bmp_para
        self.ra_bmp.output_bmp_file = 'assets/sample.bmp'

    def tearDown(self):
        # cleanup
        os.remove('assets/sample.bmp')

    def test_default_values(self):
        # Two tests will be conducted:
        #   First one checks if ra_bmp created the file correctly.
        #   Second one checks if the file size is greater than zero.
        self.ra_bmp.execute()
        self.assertTrue(os.path.exists('assets/sample.bmp'),
                        'The file that should have been created by ra_bmp was not'
                        'found.')

        file_size = os.stat('assets/sample.bmp').st_size

        self.assertGreater(file_size, 10,
                           'The size of the file created by ra_bmp does not appear to'
                           ' be correct')


if __name__ == "__main__":
    unittest.main()
