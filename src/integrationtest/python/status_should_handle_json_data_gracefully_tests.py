#   YADT - an Augmented Deployment Tool
#   Copyright (C) 2010-2014  Immobilien Scout GmbH
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'Arne Hilmann, Marcel Wolf'

import unittest
import integrationtest_support

import yadt_status_answer


class Test (integrationtest_support.IntegrationTestSupport):

    def test(self):
        self.write_target_file('it01.domain')

        with self.fixture() as when:
            when.calling('ssh').at_least_with_arguments('it01.domain').and_input('/usr/bin/yadt-status') \
                .then_write(yadt_status_answer.stdout('it01.domain', template=yadt_status_answer.STATUS_JSON_TEMPLATE))

        actual_return_code = self.execute_command('yadtshell status')

        self.assertEqual(0, actual_return_code)

        with self.verify() as complete_verify:
            with complete_verify.filter_by_argument('it01.domain') as verify:
                verify.called('ssh').at_least_with_arguments(
                    'it01.domain').and_input('/usr/bin/yadt-status')

            complete_verify.finished()

if __name__ == '__main__':
    unittest.main()
