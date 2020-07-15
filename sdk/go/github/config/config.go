// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

// Authenticate without a token. When `anonymous`is true, the provider will not be able to access resourcesthat require
// authentication.
//
// Deprecated: For versions later than 3.0.0, absence of a token enables this mode
func GetAnonymous(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "github:anonymous")
}

// The GitHub Base API URL
func GetBaseUrl(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "github:baseUrl")
	if err == nil {
		return v
	}
	return getEnvOrDefault("https://api.github.com/", nil, "GITHUB_BASE_URL").(string)
}

// Deprecated: For versions later than 3.0.0, absence of an organization enables this mode
func GetIndividual(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "github:individual")
}

// Whether server should be accessed without verifying the TLS certificate.
func GetInsecure(ctx *pulumi.Context) bool {
	return config.GetBool(ctx, "github:insecure")
}

// The GitHub organization name to manage. If `individual` is false, `organization` is required.
func GetOrganization(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "github:organization")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "GITHUB_ORGANIZATION").(string)
}

// The OAuth token used to connect to GitHub. If `anonymous` is false, `token` is required.
func GetToken(ctx *pulumi.Context) string {
	v, err := config.Try(ctx, "github:token")
	if err == nil {
		return v
	}
	return getEnvOrDefault("", nil, "GITHUB_TOKEN").(string)
}
