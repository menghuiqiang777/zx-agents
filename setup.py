from setuptools import setup, find_packages

setup(
    name='zx-agents',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 列出项目依赖的其他包
        # 例如: 'requests',
        'os'
        'logging'
        'openai'
        'asyncio'
        'agents'
        'typing'
        'mlflow'
    ],
    author='Meng',
    author_email='meng@zxtech.info',
    description='openai-agnets自定义配置',
    url='https://github.com/menghuiqiang777/zx-agents',
)