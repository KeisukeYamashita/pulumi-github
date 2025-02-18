# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['TeamRepository']


class TeamRepository(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource manages relationships between teams and repositories
        in your GitHub organization.

        Creating this resource grants a particular team permissions on a
        particular repository.

        The repository and the team must both belong to the same organization
        on GitHub. This resource does not actually *create* any repositories;
        to do that, see `Repository`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        # Add a repository to the team
        some_team = github.Team("someTeam", description="Some cool team")
        some_repo = github.Repository("someRepo")
        some_team_repo = github.TeamRepository("someTeamRepo",
            permission="pull",
            repository=some_repo.name,
            team_id=some_team.id)
        ```

        ## Import

        GitHub Team Repository can be imported using an ID made up of `teamid:repository`, e.g.

        ```sh
         $ pulumi import github:index/teamRepository:TeamRepository terraform_repo 1234567:terraform
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] permission: The permissions of team members regarding the repository.
               Must be one of `pull`, `triage`, `push`, `maintain`, or `admin`. Defaults to `pull`.
        :param pulumi.Input[str] repository: The repository to add to the team.
        :param pulumi.Input[str] team_id: The GitHub team id or the GitHub team slug
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

            __props__['permission'] = permission
            if repository is None and not opts.urn:
                raise TypeError("Missing required property 'repository'")
            __props__['repository'] = repository
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__['team_id'] = team_id
            __props__['etag'] = None
        super(TeamRepository, __self__).__init__(
            'github:index/teamRepository:TeamRepository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            etag: Optional[pulumi.Input[str]] = None,
            permission: Optional[pulumi.Input[str]] = None,
            repository: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'TeamRepository':
        """
        Get an existing TeamRepository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] permission: The permissions of team members regarding the repository.
               Must be one of `pull`, `triage`, `push`, `maintain`, or `admin`. Defaults to `pull`.
        :param pulumi.Input[str] repository: The repository to add to the team.
        :param pulumi.Input[str] team_id: The GitHub team id or the GitHub team slug
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["etag"] = etag
        __props__["permission"] = permission
        __props__["repository"] = repository
        __props__["team_id"] = team_id
        return TeamRepository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Output[Optional[str]]:
        """
        The permissions of team members regarding the repository.
        Must be one of `pull`, `triage`, `push`, `maintain`, or `admin`. Defaults to `pull`.
        """
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[str]:
        """
        The repository to add to the team.
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The GitHub team id or the GitHub team slug
        """
        return pulumi.get(self, "team_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

