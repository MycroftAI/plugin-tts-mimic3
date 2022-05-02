#!/usr/bin/env bash
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
set -eo pipefail

# Directory of *this* script
this_dir="$( cd "$( dirname "$0" )" && pwd )"

module_name='mycroft_plugin_tts_mimic3'
src_dir="${this_dir}/${module_name}"

# Path to virtual environment
: "${venv:=${src_dir}/.venv}"

if [ -d "${venv}" ]; then
    # Activate virtual environment if available
    source "${venv}/bin/activate"
fi

# Format code
black "${src_dir}"
isort "${src_dir}"

# Check
flake8 "${src_dir}"
pylint "${src_dir}"
mypy "${src_dir}"

echo 'OK'
