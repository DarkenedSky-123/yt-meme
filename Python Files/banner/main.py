import subprocess

subprocess.run(["python", "banner/banner.py"], check=True)
subprocess.run(["python", "banner/update_banner.py"], check=True)
