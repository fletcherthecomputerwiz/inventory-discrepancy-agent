import sys

print("Python Version: ",  sys.version.split()[0])
print("Running From: ",  sys.executable)
print("Inside a Venv: ",  hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
print("The folder venv was built from is ",  getattr(sys, 'real_prefix', None) or getattr(sys, 'base_prefix', None))
