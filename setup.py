#!/usr/bin/env python3
# Copyright 2022 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import defaultdict
from pathlib import Path

import setuptools
from setuptools import setup

this_dir = Path(__file__).parent
module_dir = this_dir / "mycroft_plugin_tts_mimic3"

# -----------------------------------------------------------------------------

# Load README in as long description
long_description: str = ""
readme_path = this_dir / "README.md"
if readme_path.is_file():
    long_description = readme_path.read_text(encoding="utf-8")

requirements = []
requirements_path = this_dir / "requirements.txt"
if requirements_path.is_file():
    with open(requirements_path, "r", encoding="utf-8") as requirements_file:
        requirements = requirements_file.read().splitlines()

version_path = module_dir / "VERSION"
with open(version_path, "r", encoding="utf-8") as version_file:
    version = version_file.read().strip()

# -----------------------------------------------------------------------------

# dependency => [tags]
extras = {}

# Create language-specific extras
for lang in [
    "de",
    "es",
    "fa",
    "fr",
    "it",
    "nl",
    "ru",
    "sw",
]:
    extras[f"mycroft-mimic3-tts[{lang}]"] = [lang]

# Add "all" tag
for tags in extras.values():
    tags.append("all")

# Invert for setup
extras_require = defaultdict(list)
for dep, tags in extras.items():
    for tag in tags:
        extras_require[tag].append(dep)

# -----------------------------------------------------------------------------

PLUGIN_ENTRY_POINT = "mimic3_tts_plug = mycroft_plugin_tts_mimic3:Mimic3TTSPlugin"
setup(
    name="mycroft_plugin_tts_mimic3",
    version=version,
    description="Text to speech plugin for Mycroft using Mimic3",
    url="http://github.com/MycroftAI/plugin-tts-mimic3",
    author="Michael Hansen",
    author_email="michael.hansen@mycroft.ai",
    license="Apache-2.0",
    packages=setuptools.find_packages(),
    package_data={"mycroft_plugin_tts_mimic3": ["VERSION", "py.typed"]},
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="mycroft plugin tts mimic mimic3",
    entry_points={"mycroft.plugin.tts": PLUGIN_ENTRY_POINT},
)
