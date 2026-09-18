from dataclasses import dataclass

@dataclass(frozen=True)
class Environment:
    customer_owner: str
    platform_owner: str
    cloud_account_id: str
    config_revision: str
    observability_ready: bool
    recovery_runbook_tested: bool
    gitops_sync_healthy: bool
    workload_identity_enabled: bool
    network_policy_enforced: bool
    stateful_backup_tested: bool
    upgrade_rollback_verified: bool

def plan(env: Environment) -> tuple[bool, tuple[str, ...]]:
    reasons=[]
    if not env.customer_owner.strip() or not env.platform_owner.strip(): reasons.append("customer and platform ownership are required")
    if len(env.cloud_account_id) < 8: reasons.append("a distinct cloud account boundary is required")
    if not env.config_revision.startswith("sha256:"): reasons.append("configuration must be pinned to an immutable revision")
    if not env.observability_ready: reasons.append("metrics, logs, and alerts must be ready before handover")
    if not env.recovery_runbook_tested: reasons.append("a recovery runbook must be tested")
    if not env.gitops_sync_healthy: reasons.append("GitOps reconciliation must be healthy before handover")
    if not env.workload_identity_enabled: reasons.append("workload identity must be enabled for secure-by-default access")
    if not env.network_policy_enforced: reasons.append("network policy must be enforced for tenant isolation")
    if not env.stateful_backup_tested: reasons.append("stateful service backup and restore must be tested")
    if not env.upgrade_rollback_verified: reasons.append("cluster or service upgrade rollback must be verified")
    return (not reasons, tuple(reasons))
