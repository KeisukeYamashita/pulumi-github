// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package github

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// This resource allows you to create and manage cards for GitHub projects.
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
// 		column, err := github.NewProjectColumn(ctx, "column", &github.ProjectColumnArgs{
// 			ProjectId: project.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = github.NewProjectCard(ctx, "card", &github.ProjectCardArgs{
// 			ColumnId: column.ColumnId,
// 			Note:     pulumi.String("## Unaccepted 👇"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// A GitHub Project Card can be imported using its [Card ID](https://developer.github.com/v3/projects/cards/#get-a-project-card)
//
// ```sh
//  $ pulumi import github:index/projectCard:ProjectCard card 01234567
// ```
type ProjectCard struct {
	pulumi.CustomResourceState

	CardId pulumi.IntOutput `pulumi:"cardId"`
	// The ID of the card.
	ColumnId pulumi.StringOutput `pulumi:"columnId"`
	Etag     pulumi.StringOutput `pulumi:"etag"`
	// The note contents of the card. Markdown supported.
	Note pulumi.StringOutput `pulumi:"note"`
}

// NewProjectCard registers a new resource with the given unique name, arguments, and options.
func NewProjectCard(ctx *pulumi.Context,
	name string, args *ProjectCardArgs, opts ...pulumi.ResourceOption) (*ProjectCard, error) {
	if args == nil || args.ColumnId == nil {
		return nil, errors.New("missing required argument 'ColumnId'")
	}
	if args == nil || args.Note == nil {
		return nil, errors.New("missing required argument 'Note'")
	}
	if args == nil {
		args = &ProjectCardArgs{}
	}
	var resource ProjectCard
	err := ctx.RegisterResource("github:index/projectCard:ProjectCard", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProjectCard gets an existing ProjectCard resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProjectCard(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectCardState, opts ...pulumi.ResourceOption) (*ProjectCard, error) {
	var resource ProjectCard
	err := ctx.ReadResource("github:index/projectCard:ProjectCard", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ProjectCard resources.
type projectCardState struct {
	CardId *int `pulumi:"cardId"`
	// The ID of the card.
	ColumnId *string `pulumi:"columnId"`
	Etag     *string `pulumi:"etag"`
	// The note contents of the card. Markdown supported.
	Note *string `pulumi:"note"`
}

type ProjectCardState struct {
	CardId pulumi.IntPtrInput
	// The ID of the card.
	ColumnId pulumi.StringPtrInput
	Etag     pulumi.StringPtrInput
	// The note contents of the card. Markdown supported.
	Note pulumi.StringPtrInput
}

func (ProjectCardState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectCardState)(nil)).Elem()
}

type projectCardArgs struct {
	// The ID of the card.
	ColumnId string `pulumi:"columnId"`
	// The note contents of the card. Markdown supported.
	Note string `pulumi:"note"`
}

// The set of arguments for constructing a ProjectCard resource.
type ProjectCardArgs struct {
	// The ID of the card.
	ColumnId pulumi.StringInput
	// The note contents of the card. Markdown supported.
	Note pulumi.StringInput
}

func (ProjectCardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectCardArgs)(nil)).Elem()
}

type ProjectCardInput interface {
	pulumi.Input

	ToProjectCardOutput() ProjectCardOutput
	ToProjectCardOutputWithContext(ctx context.Context) ProjectCardOutput
}

func (ProjectCard) ElementType() reflect.Type {
	return reflect.TypeOf((*ProjectCard)(nil)).Elem()
}

func (i ProjectCard) ToProjectCardOutput() ProjectCardOutput {
	return i.ToProjectCardOutputWithContext(context.Background())
}

func (i ProjectCard) ToProjectCardOutputWithContext(ctx context.Context) ProjectCardOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectCardOutput)
}

type ProjectCardOutput struct {
	*pulumi.OutputState
}

func (ProjectCardOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProjectCardOutput)(nil)).Elem()
}

func (o ProjectCardOutput) ToProjectCardOutput() ProjectCardOutput {
	return o
}

func (o ProjectCardOutput) ToProjectCardOutputWithContext(ctx context.Context) ProjectCardOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ProjectCardOutput{})
}
