import sys, unittest
sys.path.append("src")
from byoc import Environment, plan
class Tests(unittest.TestCase):
 def valid(self, **x):
  d=dict(customer_owner="customer",platform_owner="platform",cloud_account_id="123456789012",config_revision="sha256:abc",observability_ready=True,recovery_runbook_tested=True);d.update(x);return Environment(**d)
 def test_approves_ready_environment(self): self.assertTrue(plan(self.valid())[0])
 def test_requires_immutable_config(self): self.assertIn("configuration must be pinned to an immutable revision",plan(self.valid(config_revision="main"))[1])
 def test_requires_operational_readiness(self): self.assertFalse(plan(self.valid(observability_ready=False,recovery_runbook_tested=False))[0])
if __name__=="__main__": unittest.main()
