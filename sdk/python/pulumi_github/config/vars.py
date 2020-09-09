# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'base_url',
    'insecure',
    'organization',
    'owner',
    'token',
]

__config__ = pulumi.Config('github')

base_url = __config__.get('baseUrl') or (_utilities.get_env('GITHUB_BASE_URL') or 'https://api.github.com/')
"""
The GitHub Base API URL
"""

insecure = __config__.get('insecure')
"""
Enable `insecure` mode for testing purposes
"""

organization = __config__.get('organization') or _utilities.get_env('GITHUB_ORGANIZATION')
"""
The GitHub organization name to manage. Use this field instead of `owner` when managing organization accounts.
"""

owner = __config__.get('owner')
"""
The GitHub owner name to manage. Use this field instead of `organization` when managing individual accounts.
"""

token = __config__.get('token') or _utilities.get_env('GITHUB_TOKEN')
"""
The OAuth token used to connect to GitHub. `anonymous` mode is enabled if `token` is not configured.
"""

