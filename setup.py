from setuptools import setup, find_packages

setup(
    name='zx-agents',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        # 这里需要注意，os、logging、asyncio、typing 是 Python 标准库，无需安装
        'openai',
        'agents',
        'mlflow'
    ],
    author='Meng',
    author_email='meng@zxtech.info',
    description='openai-agnets自定义配置',
    url='https://github.com/menghuiqiang777/zx-agents',
)