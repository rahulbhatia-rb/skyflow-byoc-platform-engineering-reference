from dataclasses import dataclass

@dataclass(frozen=True)
class Environment:
    customer_owner: str
    platform_owner: str
    cloud_account_id: str
    config_revision: str
    observability_ready: bool
    recovery_runbook_tested: bool

def plan(env: Environment) -> tuple[bool, tuple[str, ...]]:
    reasons=[]
    if not env.customer_owner.strip() or not env.platform_owner.strip(): reasons.append("customer and platform ownership are required")
    if len(env.cloud_account_id) < 8: reasons.append("a distinct cloud account boundary is required")
    if not env.config_revision.startswith("sha256:"): reasons.append("configuration must be pinned to an immutable revision")
    if not env.observability_ready: reasons.append("metrics, logs, and alerts must be ready before handover")
    if not env.recovery_runbook_tested: reasons.append("a recovery runbook must be tested")
    return (not reasons, tuple(reasons))
