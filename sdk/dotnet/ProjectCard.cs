// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Github
{
    /// <summary>
    /// This resource allows you to create and manage cards for GitHub projects.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Github = Pulumi.Github;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var project = new Github.OrganizationProject("project", new Github.OrganizationProjectArgs
    ///         {
    ///             Body = "This is an organization project.",
    ///         });
    ///         var column = new Github.ProjectColumn("column", new Github.ProjectColumnArgs
    ///         {
    ///             ProjectId = project.Id,
    ///         });
    ///         var card = new Github.ProjectCard("card", new Github.ProjectCardArgs
    ///         {
    ///             ColumnId = column.ColumnId,
    ///             Note = "## Unaccepted 👇",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class ProjectCard : Pulumi.CustomResource
    {
        [Output("cardId")]
        public Output<int> CardId { get; private set; } = null!;

        /// <summary>
        /// The ID of the card.
        /// </summary>
        [Output("columnId")]
        public Output<string> ColumnId { get; private set; } = null!;

        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// The note contents of the card. Markdown supported.
        /// </summary>
        [Output("note")]
        public Output<string> Note { get; private set; } = null!;


        /// <summary>
        /// Create a ProjectCard resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProjectCard(string name, ProjectCardArgs args, CustomResourceOptions? options = null)
            : base("github:index/projectCard:ProjectCard", name, args ?? new ProjectCardArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ProjectCard(string name, Input<string> id, ProjectCardState? state = null, CustomResourceOptions? options = null)
            : base("github:index/projectCard:ProjectCard", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ProjectCard resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProjectCard Get(string name, Input<string> id, ProjectCardState? state = null, CustomResourceOptions? options = null)
        {
            return new ProjectCard(name, id, state, options);
        }
    }

    public sealed class ProjectCardArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the card.
        /// </summary>
        [Input("columnId", required: true)]
        public Input<string> ColumnId { get; set; } = null!;

        /// <summary>
        /// The note contents of the card. Markdown supported.
        /// </summary>
        [Input("note", required: true)]
        public Input<string> Note { get; set; } = null!;

        public ProjectCardArgs()
        {
        }
    }

    public sealed class ProjectCardState : Pulumi.ResourceArgs
    {
        [Input("cardId")]
        public Input<int>? CardId { get; set; }

        /// <summary>
        /// The ID of the card.
        /// </summary>
        [Input("columnId")]
        public Input<string>? ColumnId { get; set; }

        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// The note contents of the card. Markdown supported.
        /// </summary>
        [Input("note")]
        public Input<string>? Note { get; set; }

        public ProjectCardState()
        {
        }
    }
}
