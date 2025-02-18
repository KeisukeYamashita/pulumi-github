# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetIpRangesResult',
    'AwaitableGetIpRangesResult',
    'get_ip_ranges',
]

@pulumi.output_type
class GetIpRangesResult:
    """
    A collection of values returned by getIpRanges.
    """
    def __init__(__self__, gits=None, hooks=None, id=None, importers=None, pages=None):
        if gits and not isinstance(gits, list):
            raise TypeError("Expected argument 'gits' to be a list")
        pulumi.set(__self__, "gits", gits)
        if hooks and not isinstance(hooks, list):
            raise TypeError("Expected argument 'hooks' to be a list")
        pulumi.set(__self__, "hooks", hooks)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if importers and not isinstance(importers, list):
            raise TypeError("Expected argument 'importers' to be a list")
        pulumi.set(__self__, "importers", importers)
        if pages and not isinstance(pages, list):
            raise TypeError("Expected argument 'pages' to be a list")
        pulumi.set(__self__, "pages", pages)

    @property
    @pulumi.getter
    def gits(self) -> Sequence[str]:
        """
        An Array of IP addresses in CIDR format specifying the Git servers.
        """
        return pulumi.get(self, "gits")

    @property
    @pulumi.getter
    def hooks(self) -> Sequence[str]:
        """
        An Array of IP addresses in CIDR format specifying the addresses that incoming service hooks will originate from.
        """
        return pulumi.get(self, "hooks")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def importers(self) -> Sequence[str]:
        """
        An Array of IP addresses in CIDR format specifying the A records for GitHub Importer.
        """
        return pulumi.get(self, "importers")

    @property
    @pulumi.getter
    def pages(self) -> Sequence[str]:
        """
        An Array of IP addresses in CIDR format specifying the A records for GitHub Pages.
        """
        return pulumi.get(self, "pages")


class AwaitableGetIpRangesResult(GetIpRangesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpRangesResult(
            gits=self.gits,
            hooks=self.hooks,
            id=self.id,
            importers=self.importers,
            pages=self.pages)


def get_ip_ranges(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpRangesResult:
    """
    Use this data source to retrieve information about GitHub's IP addresses.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_github as github

    test = github.get_ip_ranges()
    ```
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('github:index/getIpRanges:getIpRanges', __args__, opts=opts, typ=GetIpRangesResult).value

    return AwaitableGetIpRangesResult(
        gits=__ret__.gits,
        hooks=__ret__.hooks,
        id=__ret__.id,
        importers=__ret__.importers,
        pages=__ret__.pages)
