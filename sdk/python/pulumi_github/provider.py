# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = ['Provider']


class Provider(pulumi.ProviderResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anonymous: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 individual: Optional[pulumi.Input[bool]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The provider type for the github package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] anonymous: Authenticate without a token. When `anonymous`is true, the provider will not be able to access resourcesthat require
               authentication.
        :param pulumi.Input[str] base_url: The GitHub Base API URL
        :param pulumi.Input[bool] insecure: Whether server should be accessed without verifying the TLS certificate.
        :param pulumi.Input[str] organization: The GitHub organization name to manage. If `individual` is false, `organization` is required.
        :param pulumi.Input[str] token: The OAuth token used to connect to GitHub. If `anonymous` is false, `token` is required.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if anonymous is not None:
                warnings.warn("For versions later than 3.0.0, absence of a token enables this mode", DeprecationWarning)
                pulumi.log.warn("anonymous is deprecated: For versions later than 3.0.0, absence of a token enables this mode")
            __props__['anonymous'] = pulumi.Output.from_input(anonymous).apply(json.dumps) if anonymous is not None else None
            if base_url is None:
                base_url = (_utilities.get_env('GITHUB_BASE_URL') or 'https://api.github.com/')
            __props__['base_url'] = base_url
            if individual is not None:
                warnings.warn("For versions later than 3.0.0, absence of an organization enables this mode", DeprecationWarning)
                pulumi.log.warn("individual is deprecated: For versions later than 3.0.0, absence of an organization enables this mode")
            __props__['individual'] = pulumi.Output.from_input(individual).apply(json.dumps) if individual is not None else None
            __props__['insecure'] = pulumi.Output.from_input(insecure).apply(json.dumps) if insecure is not None else None
            if organization is None:
                organization = _utilities.get_env('GITHUB_ORGANIZATION')
            __props__['organization'] = organization
            if token is None:
                token = _utilities.get_env('GITHUB_TOKEN')
            __props__['token'] = token
        super(Provider, __self__).__init__(
            'github',
            resource_name,
            __props__,
            opts)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

