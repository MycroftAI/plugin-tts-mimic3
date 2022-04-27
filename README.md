# Mimic 3 Text to Speech Plugin

Text to speech plugin for [Mycroft](https://mycroft.ai) using [Mimic 3](https://github.com/MycroftAI/mimic3).

[Available voices](https://github.com/MycroftAI/mimic3-voices)


## Dependencies

* Python 3.7 or higher
* [Mimic 3](https://github.com/MycroftAI/mimic3)
* [eSpeak-ng](https://github.com/espeak-ng/espeak-ng) (depending on the voice)


## Installation


### System Dependencies

Some voices depend on [eSpeak-ng](https://github.com/espeak-ng/espeak-ng), specifically `libespeak-ng.so`. For those voices, make sure that libespeak-ng is installed with:

``` sh
sudo apt-get install libespeak-ng1
```

On 32-bit ARM platforms (a.k.a. `armv7l` or `armhf`), you will also need some extra libraries:

``` sh
sudo apt-get install libatomic1 libgomp1 libatlas-base-dev
```


### Using pip

If you have Mycroft installed, you can install the plugin with:

``` sh
mycroft-pip install plugin-tts-mimic3[all]
```

otherwise, you can use `pip` directly:

``` sh
pip install plugin-tts-mimic3[all]
```

Language support can be selectively installed by replacing `all` with:

* `de` - German
* `es` - Spanish
* `fa` - Farsi
* `fr` - French
* `it` - Italian
* `nl` - Dutch
* `ru` - Russian
* `sw` - Kiswahili

Excluding `[..]` entirely will install support for English only.


### From Source

Clone the repository:

``` sh
git clone https://github.com/MycroftAI/plugin-tts-mimic3.git
```

Install in editable mode using `pip`:

``` sh
cd plugin-tts-mimic3/
pip install -e ./[all]
```


## Configuration

The plugin can be enabled in Mycroft with:

``` sh
mycroft-config set tts.module mimic3_tts_plug
```

Additional options can be set by running:

``` sh
mycroft-config edit user
```

and adding the following:

``` json
"tts": {
  "mimic3_tts_plug": {
    "<option>": <value>
  }
}
```

where options are:

* `voice` - [voice key](https://github.com/MycroftAI/mimic3/#voice-keys)
* `preloaded_voices` - list of voice keys to load at startup
* `length_scale` - speed of speaking (< 1 is faster, > 1 is slower)
* `noise_scale` - volatility of speaker
* `noise_w` - volatility of phoneme durations
