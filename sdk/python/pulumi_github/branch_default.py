# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['BranchDefault']


class BranchDefault(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a GitHub branch default resource.

        This resource allows you to set the default branch for a given repository.

        Note that use of this resource is incompatible with the `default_branch` option of the `Repository` resource.  Using both will result in plans always showing a diff.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.Repository("example",
            description="My awesome codebase",
            auto_init=True)
        development = github.Branch("development",
            repository=example.name,
            branch="development")
        default = github.BranchDefault("default",
            repository=example.name,
            branch=development.branch)
        ```

        ## Import

        GitHub Branch Defaults can be imported using an ID made up of `repository`, e.g.

        ```sh
         $ pulumi import github:index/branchDefault:BranchDefault branch_default my-repo
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The branch (e.g. `main`)
        :param pulumi.Input[str] repository: The GitHub repository
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

            if branch is None and not opts.urn:
                raise TypeError("Missing required property 'branch'")
            __props__['branch'] = branch
            if repository is None and not opts.urn:
                raise TypeError("Missing required property 'repository'")
            __props__['repository'] = repository
        super(BranchDefault, __self__).__init__(
            'github:index/branchDefault:BranchDefault',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            branch: Optional[pulumi.Input[str]] = None,
            repository: Optional[pulumi.Input[str]] = None) -> 'BranchDefault':
        """
        Get an existing BranchDefault resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The branch (e.g. `main`)
        :param pulumi.Input[str] repository: The GitHub repository
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["branch"] = branch
        __props__["repository"] = repository
        return BranchDefault(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[str]:
        """
        The branch (e.g. `main`)
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[str]:
        """
        The GitHub repository
        """
        return pulumi.get(self, "repository")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

