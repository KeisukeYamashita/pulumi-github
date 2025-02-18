# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['TeamSyncGroupMapping']


class TeamSyncGroupMapping(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TeamSyncGroupMappingGroupArgs']]]]] = None,
                 team_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource allows you to create and manage Identity Provider (IdP) group connections within your GitHub teams.
        You must have team synchronization enabled for organizations owned by enterprise accounts.

        To learn more about team synchronization between IdPs and GitHub, please refer to:
        https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/synchronizing-teams-between-your-identity-provider-and-github

        ## Import

        GitHub Team Sync Group Mappings can be imported using the GitHub team `slug` e.g.

        ```sh
         $ pulumi import github:index/teamSyncGroupMapping:TeamSyncGroupMapping example some_team
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TeamSyncGroupMappingGroupArgs']]]] groups: An Array of GitHub Identity Provider Groups (or empty []).  Each `group` block consists of the fields documented below.
               ___
        :param pulumi.Input[str] team_slug: Slug of the team
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

            __props__['groups'] = groups
            if team_slug is None and not opts.urn:
                raise TypeError("Missing required property 'team_slug'")
            __props__['team_slug'] = team_slug
            __props__['etag'] = None
        super(TeamSyncGroupMapping, __self__).__init__(
            'github:index/teamSyncGroupMapping:TeamSyncGroupMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            etag: Optional[pulumi.Input[str]] = None,
            groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TeamSyncGroupMappingGroupArgs']]]]] = None,
            team_slug: Optional[pulumi.Input[str]] = None) -> 'TeamSyncGroupMapping':
        """
        Get an existing TeamSyncGroupMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TeamSyncGroupMappingGroupArgs']]]] groups: An Array of GitHub Identity Provider Groups (or empty []).  Each `group` block consists of the fields documented below.
               ___
        :param pulumi.Input[str] team_slug: Slug of the team
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["etag"] = etag
        __props__["groups"] = groups
        __props__["team_slug"] = team_slug
        return TeamSyncGroupMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Optional[Sequence['outputs.TeamSyncGroupMappingGroup']]]:
        """
        An Array of GitHub Identity Provider Groups (or empty []).  Each `group` block consists of the fields documented below.
        ___
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="teamSlug")
    def team_slug(self) -> pulumi.Output[str]:
        """
        Slug of the team
        """
        return pulumi.get(self, "team_slug")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

