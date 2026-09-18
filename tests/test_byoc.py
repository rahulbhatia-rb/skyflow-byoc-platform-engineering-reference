import unittest

from src.byoc import Environment, plan


class Tests(unittest.TestCase):
    def valid(self, **changes):
        values = dict(customer_owner="customer", platform_owner="platform", cloud_account_id="123456789012", config_revision="sha256:abc", observability_ready=True, recovery_runbook_tested=True, gitops_sync_healthy=True, workload_identity_enabled=True, network_policy_enforced=True, stateful_backup_tested=True, upgrade_rollback_verified=True)
        values.update(changes)
        return Environment(**values)

    def test_approves_ready_environment(self):
        self.assertTrue(plan(self.valid())[0])

    def test_requires_immutable_config(self):
        self.assertIn("configuration must be pinned to an immutable revision", plan(self.valid(config_revision="main"))[1])

    def test_requires_secure_and_safe_fleet_operations(self):
        approved, reasons = plan(self.valid(gitops_sync_healthy=False, workload_identity_enabled=False, stateful_backup_tested=False, upgrade_rollback_verified=False))
        self.assertFalse(approved)
        self.assertIn("GitOps reconciliation must be healthy before handover", reasons)
        self.assertIn("cluster or service upgrade rollback must be verified", reasons)
