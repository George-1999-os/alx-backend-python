org_payload = {"login": "google"}

repos_payload = [
    {"name": "repo1", "license": {"key": "mit"}},
    {"name": "repo2", "license": {"key": "apache-2.0"}},
    {"name": "apache-2", "license": {"key": "apache-2.0"}},
]

expected_repos = ["repo1", "repo2", "apache-2"]
apache2_repos = ["repo2", "apache-2"]
