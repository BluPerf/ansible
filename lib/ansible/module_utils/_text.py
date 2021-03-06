# Copyright (c), Toshio Kuratomi <tkuratomi@ansible.com> 2016
# Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)

"""
.. warn:: Use ansible.module_utils.common.text.converters instead.
"""

# Backwards compat for people still calling it from this package
from ansible.module_utils.common.text.converters import to_bytes, to_native, to_text
