# Mimic 3 Text to Speech Plugin

Text to speech plugin for [Mycroft](https://mycroft.ai) using [Mimic 3](https://github.com/MycroftAI/mimic3).

* [Available voices](https://github.com/MycroftAI/mimic3-voices)
* [Documentation](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mimic-tts/coming-soon-mimic-3)


## Installation

Install the necessary system packages:

``` sh
sudo apt-get install libespeak-ng1
```

On 32-bit ARM platforms (a.k.a. `armv7l` or `armhf`), you will also need some extra libraries:

``` sh
sudo apt-get install libatomic1 libgomp1 libatlas-base-dev
```

Then, ensure that you're using the latest `pip`:

```sh
mycroft-pip install --upgrade pip
```

Next, install the TTS plugin in Mycroft:

```sh
mycroft-pip install mycroft-plugin-tts-mimic3[all]
```

Removing `[all]` will install support for English only.

Additional language support can be selectively installed by replacing `all` with a two-character language code, such as `de` (German) or `fr` (French).
See [`setup.py`](https://github.com/MycroftAI/mimic3/blob/master/setup.py) for an up-to-date list of language codes.

Enable the plugin in your [mycroft.conf](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/customizations/mycroft-conf) file:

``` sh
mycroft-config set tts.module mimic3_tts_plug
```

or you can manually add the following to `mycroft.conf` with `mycroft-config edit user`:

``` json
"tts": {
  "module": "mimic3_tts_plug"
}
```


## Plugin Options

Additional settings can be configured in `mycroft.conf`:

``` json
"tts": {
  "module": "mimic3_tts_plug",
  "mimic3_tts_plug": {
      "voice": "en_US/cmu-arctic_low",  // default voice
      "speaker": "fem",  // default speaker
      "length_scale": 1.0,  // speaking rate
      "noise_scale": 0.667,  // speaking variablility
      "noise_w": 1.0  // phoneme duration variablility
  }
}
```
