# Skyflow BYOC Platform Engineering Reference POC

A compact, tested control for deciding whether a multi-tenant or dedicated/BYOC environment is ready to provision, upgrade, and hand over. This is a personal demonstration project, not a representation of Skyflow systems or customers.

## Why this matters

Skyflow’s Platform Engineer role treats infrastructure automation as software. A customer environment must be reproducible and supportable in an account the platform team does not directly operate. This POC therefore turns environment readiness into a consistent, auditable decision rather than bespoke per-customer judgement.

`plan()` returns an approval/rejection with machine-readable reasons. The policy checks:

| Platform capability | Evidence required |
| --- | --- |
| Dedicated/BYOC ownership | Accountable customer and platform owners plus cloud-account isolation |
| Infrastructure as code | Terraform/OpenTofu configuration pinned to an immutable revision |
| GitOps fleet operation | Healthy ArgoCD/Helm reconciliation before handover |
| Secure-by-default access | Workload identity and network policy enforced |
| Stateful dependencies | Tested backup/restore for PostgreSQL, Aerospike, Kafka, or similar services |
| Upgrade safety | Verified cluster/service rollback |
| Observability and on-call | Metrics, logs, alerts, and a tested recovery runbook |

## Delivery flow

```text
Provision / upgrade request → BYOC readiness gate → GitOps reconciliation → handover
        ├─ immutable IaC + account isolation
        ├─ identity + network policy + audit controls
        └─ stateful recovery + observability + rollback
```

This pure Python policy layer can sit behind a GitOps workflow, internal Go/Python CLI, or provisioning API. A production implementation would have Terraform modules create the account topology, IAM, VPC, EKS/GKE, secrets, and observability integrations; CI would record plan/apply evidence; and ArgoCD/Helm would reconcile workload state.

## Run

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/environment.jsonl
```

The JSONL sample demonstrates a handover-ready environment and a rejected environment, with ownership, isolation, GitOps, security, stateful recovery, and upgrade evidence exposed as machine-readable reasons.

## Scope and candour

It focuses on the BYOC, Kubernetes, GitOps, secure platform automation, stateful services, and observability concerns in the role. AI tooling can assist diagnosis and documentation, while access-changing or production actions remain governed by tested automation, auditable evidence, and explicit policy.

[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
