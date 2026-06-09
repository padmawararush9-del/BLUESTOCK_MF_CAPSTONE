"""
Master Pipeline Runner

Executes all project scripts in sequence.

Author: Arush Padmawar
"""

import subprocess

scripts = [
    "scripts/batch_nav_fetch.py",
    "scripts/live_nav_fetch.py",
    "scripts/recommender.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(
        ["python", script],
        check=True
    )
