// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// This resource allows you to create and manage columns for GitHub projects.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-github/sdk/v2/go/github"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project, err := github.NewOrganizationProject(ctx, "project", &github.OrganizationProjectArgs{
// 			Body: pulumi.String("This is an organization project."),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = github.NewProjectColumn(ctx, "column", &github.ProjectColumnArgs{
// 			ProjectId: project.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ProjectColumn struct {
	pulumi.CustomResourceState

	ColumnId pulumi.IntOutput    `pulumi:"columnId"`
	Etag     pulumi.StringOutput `pulumi:"etag"`
	// The name of the column.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of an existing project that the column will be created in.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewProjectColumn registers a new resource with the given unique name, arguments, and options.
func NewProjectColumn(ctx *pulumi.Context,
	name string, args *ProjectColumnArgs, opts ...pulumi.ResourceOption) (*ProjectColumn, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &ProjectColumnArgs{}
	}
	var resource ProjectColumn
	err := ctx.RegisterResource("github:index/projectColumn:ProjectColumn", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProjectColumn gets an existing ProjectColumn resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProjectColumn(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectColumnState, opts ...pulumi.ResourceOption) (*ProjectColumn, error) {
	var resource ProjectColumn
	err := ctx.ReadResource("github:index/projectColumn:ProjectColumn", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ProjectColumn resources.
type projectColumnState struct {
	ColumnId *int    `pulumi:"columnId"`
	Etag     *string `pulumi:"etag"`
	// The name of the column.
	Name *string `pulumi:"name"`
	// The ID of an existing project that the column will be created in.
	ProjectId *string `pulumi:"projectId"`
}

type ProjectColumnState struct {
	ColumnId pulumi.IntPtrInput
	Etag     pulumi.StringPtrInput
	// The name of the column.
	Name pulumi.StringPtrInput
	// The ID of an existing project that the column will be created in.
	ProjectId pulumi.StringPtrInput
}

func (ProjectColumnState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectColumnState)(nil)).Elem()
}

type projectColumnArgs struct {
	// The name of the column.
	Name *string `pulumi:"name"`
	// The ID of an existing project that the column will be created in.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a ProjectColumn resource.
type ProjectColumnArgs struct {
	// The name of the column.
	Name pulumi.StringPtrInput
	// The ID of an existing project that the column will be created in.
	ProjectId pulumi.StringInput
}

func (ProjectColumnArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectColumnArgs)(nil)).Elem()
}
