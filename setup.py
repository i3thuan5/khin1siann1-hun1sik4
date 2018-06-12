from setuptools import setup, find_packages
from os.path import os

版本 = '1.0.0'

def 揣工具包(頭='.'):
    'setup的find_packages無支援windows中文檔案'
    工具包 = []
    for 目錄, _, 檔案 in os.walk(頭):
        if '__init__.py' in 檔案:
            工具包.append(目錄.replace('/', '.'))
    return 工具包

setup(
    name='khin1siann1_hun1sik4',
    version=版本,
#     packages = 揣工具包('輕聲分析'),
    packages = find_packages(exclude=["試驗"]),
    install_requires=['tai5-uan5_gian5-gi2_kang1-ku7'],
    include_package_data=True,
    author='意傳科技',
    author_email='a8568730@gmail.com',
    description='計算詞頻時的輕聲分析工具',
    long_description='按照詞彙分級網站的詞頻書寫，判斷一句內底輕聲詞的斷詞',
    license="MIT",
    url='https://github.com/i3thuan5/khin1siann1-hun1sik4/',
    download_url='https://github.com/i3thuan5/khin1siann1-hun1sik4/archive/master.zip',
    project_urls={
        "Bug Tracker": "https://github.com/i3thuan5/khin1siann1-hun1sik4/issues/",
        "Documentation": "https://github.com/i3thuan5/khin1siann1-hun1sik4",
        "Source Code": "https://github.com/i3thuan5/khin1siann1-hun1sik4",
    },
    keywords=[
        '臺灣', '臺語', '自然語言', '語料庫', '斷詞', '輕聲詞',
        'Taiwan', 'Taiwanese', 'Natural Language', 'Corpus',
        'Word Segmentation',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: Unix',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
)
