from setuptools import setup, find_packages

setup(
  name = 'alphafold2-pytorch',
  packages = find_packages(),
  version = '0.0.5',
  license='MIT',
  description = 'AlphaFold2 - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/alphafold2',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'protein folding'
  ],
  install_requires=[
    'einops>=0.3',
    'numpy',
    'torch>=1.6',
    'mdtraj>=1.8'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
