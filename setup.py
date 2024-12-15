from pathlib import Path

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

ROOT = Path(__file__).resolve().parent
setup(
    name='gaussianpro',
    ext_modules=[
        CUDAExtension('gaussianpro',
            sources=[
                'PatchMatch.cpp',
                'Propagation.cu',
                'pro.cpp'
            ],
            extra_compile_args={
                'cxx': ['-O3'],
                'nvcc': ['-O3', '-gencode=arch=compute_86,code=sm_86',
                ]
            },
            ),
    ],
    cmdclass={ 'build_ext' : BuildExtension }
)
