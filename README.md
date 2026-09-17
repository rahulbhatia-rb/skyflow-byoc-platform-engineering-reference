# BYOC Platform Engineering Reference

This is a compact, tested application reference for Skyflow's India-remote Platform Engineer role. It makes a core BYOC operational decision explicit: a customer environment may only be provisioned when ownership, cloud/account isolation, immutable configuration, observability, and recovery evidence are present.

## Why this matters

BYOC changes the platform boundary: an environment must be reproducible and supportable in an account the product team does not directly operate. A provisioning workflow therefore needs repeatable guardrails rather than per-customer manual judgement.

`plan()` returns an auditable approval/rejection for an environment request. The policy checks:

- accountable customer and platform owners
- a unique cloud account boundary
- Terraform/OpenTofu configuration pinned to an immutable revision
- baseline metrics/logs/alerts before handover
- a tested recovery runbook

This pure Python policy layer can sit behind a GitOps workflow, internal CLI, or provisioning API. A production implementation would have Terraform modules create the account topology, IAM, VPC, EKS, secrets, and observability integrations; CI would record plan/apply evidence; and ArgoCD/Helm would reconcile workload state.

## Run

```bash
python3 -m unittest discover -s tests -v
```

## Scope and candour

This is a personal demonstration, not a claim of access to Skyflow systems or customers. It is informed by my AWS, RAG/GenAI deployment, infrastructure automation, and reliability work, and focuses on the BYOC, Kubernetes, GitOps, security, and observability concerns in the role.

[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
