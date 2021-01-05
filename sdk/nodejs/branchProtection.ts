// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Protects a GitHub branch.
 *
 * This resource allows you to configure branch protection for repositories in your organization. When applied, the branch will be protected from forced pushes and deletion. Additional constraints, such as required status checks or restrictions on users, teams, and apps, can also be configured.
 *
 * ## Import
 *
 * GitHub Branch Protection can be imported using an ID made up of `repository:pattern`, e.g.
 *
 * ```sh
 *  $ pulumi import github:index/branchProtection:BranchProtection terraform terraform:main
 * ```
 */
export class BranchProtection extends pulumi.CustomResource {
    /**
     * Get an existing BranchProtection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BranchProtectionState, opts?: pulumi.CustomResourceOptions): BranchProtection {
        return new BranchProtection(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'github:index/branchProtection:BranchProtection';

    /**
     * Returns true if the given object is an instance of BranchProtection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BranchProtection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BranchProtection.__pulumiType;
    }

    /**
     * Boolean, setting this to `true` enforces status checks for repository administrators.
     */
    public readonly enforceAdmins!: pulumi.Output<boolean | undefined>;
    /**
     * Identifies the protection rule pattern.
     */
    public readonly pattern!: pulumi.Output<string>;
    /**
     * The list of actor IDs that may push to the branch.
     */
    public readonly pushRestrictions!: pulumi.Output<string[] | undefined>;
    /**
     * The name or node ID of the repository associated with this branch protection rule.
     */
    public readonly repositoryId!: pulumi.Output<string>;
    /**
     * Boolean, setting this to `true` requires all commits to be signed with GPG.
     */
    public readonly requireSignedCommits!: pulumi.Output<boolean | undefined>;
    /**
     * Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
     */
    public readonly requiredPullRequestReviews!: pulumi.Output<outputs.BranchProtectionRequiredPullRequestReview[] | undefined>;
    /**
     * Enforce restrictions for required status checks. See Required Status Checks below for details.
     */
    public readonly requiredStatusChecks!: pulumi.Output<outputs.BranchProtectionRequiredStatusCheck[] | undefined>;

    /**
     * Create a BranchProtection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BranchProtectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BranchProtectionArgs | BranchProtectionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as BranchProtectionState | undefined;
            inputs["enforceAdmins"] = state ? state.enforceAdmins : undefined;
            inputs["pattern"] = state ? state.pattern : undefined;
            inputs["pushRestrictions"] = state ? state.pushRestrictions : undefined;
            inputs["repositoryId"] = state ? state.repositoryId : undefined;
            inputs["requireSignedCommits"] = state ? state.requireSignedCommits : undefined;
            inputs["requiredPullRequestReviews"] = state ? state.requiredPullRequestReviews : undefined;
            inputs["requiredStatusChecks"] = state ? state.requiredStatusChecks : undefined;
        } else {
            const args = argsOrState as BranchProtectionArgs | undefined;
            if (!args || args.pattern === undefined) {
                throw new Error("Missing required property 'pattern'");
            }
            if (!args || args.repositoryId === undefined) {
                throw new Error("Missing required property 'repositoryId'");
            }
            inputs["enforceAdmins"] = args ? args.enforceAdmins : undefined;
            inputs["pattern"] = args ? args.pattern : undefined;
            inputs["pushRestrictions"] = args ? args.pushRestrictions : undefined;
            inputs["repositoryId"] = args ? args.repositoryId : undefined;
            inputs["requireSignedCommits"] = args ? args.requireSignedCommits : undefined;
            inputs["requiredPullRequestReviews"] = args ? args.requiredPullRequestReviews : undefined;
            inputs["requiredStatusChecks"] = args ? args.requiredStatusChecks : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(BranchProtection.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BranchProtection resources.
 */
export interface BranchProtectionState {
    /**
     * Boolean, setting this to `true` enforces status checks for repository administrators.
     */
    readonly enforceAdmins?: pulumi.Input<boolean>;
    /**
     * Identifies the protection rule pattern.
     */
    readonly pattern?: pulumi.Input<string>;
    /**
     * The list of actor IDs that may push to the branch.
     */
    readonly pushRestrictions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name or node ID of the repository associated with this branch protection rule.
     */
    readonly repositoryId?: pulumi.Input<string>;
    /**
     * Boolean, setting this to `true` requires all commits to be signed with GPG.
     */
    readonly requireSignedCommits?: pulumi.Input<boolean>;
    /**
     * Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
     */
    readonly requiredPullRequestReviews?: pulumi.Input<pulumi.Input<inputs.BranchProtectionRequiredPullRequestReview>[]>;
    /**
     * Enforce restrictions for required status checks. See Required Status Checks below for details.
     */
    readonly requiredStatusChecks?: pulumi.Input<pulumi.Input<inputs.BranchProtectionRequiredStatusCheck>[]>;
}

/**
 * The set of arguments for constructing a BranchProtection resource.
 */
export interface BranchProtectionArgs {
    /**
     * Boolean, setting this to `true` enforces status checks for repository administrators.
     */
    readonly enforceAdmins?: pulumi.Input<boolean>;
    /**
     * Identifies the protection rule pattern.
     */
    readonly pattern: pulumi.Input<string>;
    /**
     * The list of actor IDs that may push to the branch.
     */
    readonly pushRestrictions?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name or node ID of the repository associated with this branch protection rule.
     */
    readonly repositoryId: pulumi.Input<string>;
    /**
     * Boolean, setting this to `true` requires all commits to be signed with GPG.
     */
    readonly requireSignedCommits?: pulumi.Input<boolean>;
    /**
     * Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.
     */
    readonly requiredPullRequestReviews?: pulumi.Input<pulumi.Input<inputs.BranchProtectionRequiredPullRequestReview>[]>;
    /**
     * Enforce restrictions for required status checks. See Required Status Checks below for details.
     */
    readonly requiredStatusChecks?: pulumi.Input<pulumi.Input<inputs.BranchProtectionRequiredStatusCheck>[]>;
}
