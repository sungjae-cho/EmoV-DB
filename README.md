# EmoV-DB


# How to use
## Download link
Sorted version (recommended):
https://mega.nz/#F!KBp32apT!gLIgyWf9iQ-yqnWFUFuUHg

Not sorted version:
http://www.coe.neu.edu/Research/AClab/Speech%20Data/

## Forced alignments with gentle
"It is the process of taking the text transcription of an audio speech segment and determining where in time particular words occur in the speech segment." [source](http://www.voxforge.org/home/docs/faq/faq/what-is-forced-alignment)

It also allows to separate verbal and non-verbal vocalizations (laughs, yawns, etc.)

1. Go to https://github.com/lowerquality/gentle
2. Clone the repo
3. In Getting started, use the 3rd option: `./install.sh`
- OpenBLAS (`apt-get install libopenblas-dev libopenblas-base`)
- `sudo apt install gfortran`
- First, run `./install.sh`. Change the openfst url in `ext/kaldi/tools/Makefile`: Change `http://openfst.cs.nyu.edu/twiki/pub/FST/FstDownload/openfst-$(OPENFST_VERSION).tar.gz`
to `http://openfst.org/twiki/pub/FST/FstDownload/openfst-$(OPENFST_VERSION).tar.gz`. Then, run `./install.sh`.
4. Copy align_db.py in the repository
5. In align_db.py, change the "path" variable so that it corresponds to the path of EmoV-DB.
6. Launch command "python align_db.py". You'll probably have to install some packages to make it work
7. It should create a folder called "alignments" in the repo, with the same structure as the database, containing a json file for each sentence of the database.
  - I showed the following problem that infinitely listens signals from threads. Thus, I edited `return self._map_async(func, iterable, mapstar, chunksize).get()` as `return self._map_async(func, iterable, mapstar, chunksize).get(timeout=20)` in File `"/usr/lib/python3.6/multiprocessing/pool.py"`, line 266, in `map`. This stops listening signals from threads for 20 seconds.
```python
Traceback (most recent call last):
  File "align_db.py", line 116, in <module>
    align_db(data)
  File "align_db.py", line 93, in align_db
    result = aligner.transcribe(wavfile, progress_cb=on_progress, logging=logging)
  File "/data2/sungjaecho/Projects/gentle/gentle/forced_aligner.py", line 24, in transcribe
    words, duration = self.mtt.transcribe(wavfile, progress_cb=progress_cb)
  File "/data2/sungjaecho/Projects/gentle/gentle/transcriber.py", line 51, in transcribe
    pool.map(transcribe_chunk, range(n_chunks))
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 266, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 638, in get
    self.wait(timeout)
  File "/usr/lib/python3.6/multiprocessing/pool.py", line 635, in wait
    self._event.wait(timeout)
  File "/usr/lib/python3.6/threading.py", line 551, in wait
    signaled = self._cond.wait(timeout)
  File "/usr/lib/python3.6/threading.py", line 295, in wait
    waiter.acquire()
KeyboardInterrupt
```

8. The function "get_start_end_from_json(path)" allows you to extract start and end of the computed force alignment
9. you can play a file with function "play(path)"
10. you can play the part of the file in which there is speech according to the forced alignment with "play_start_end(path, start, end)"

# Overview of data

The Emotional Voices Database: Towards Controlling the Emotional Expressiveness in Voice Generation Systems

- This dataset is built for the purpose of emotional speech synthesis. The transcript were based on the CMU arctic database: http://www.festvox.org/cmu_arctic/cmuarctic.data.

- It includes recordings for four speakers- two males and two females.

- The emotional styles are neutral, sleepiness, anger, disgust and amused.

- Each audio file is recorded in 16bits .wav format

- Spk-Je (Female, English: Neutral(417 files), Amused(222 files), Angry(523 files), Sleepy(466 files), Disgust(189 files))
- Spk-Bea (Female, English: Neutral(373 files), Amused(309 files), Angry(317 files), Sleepy(520 files), Disgust(347 files))
- Spk-Sa (Male, English: Neutral(493 files), Amused(501 files), Angry(468 files), Sleepy(495 files), Disgust(497 files))
- Spk-Jsh (Male, English: Neutral(302 files), Amused(298 files), Sleepy(263 files))

- File naming (audio_folder): anger_1-28_0011.wav - 1) first word (emotion style), 1-28 - annotation doc file range, Last four digit is the sentence number.

- File naming (annotation_folder): anger_1-28.TextGrid - 1) first word (emotional style), 1-28- annotation doc range

# References
A description of the database here:
https://arxiv.org/pdf/1806.09514.pdf

Please reference this paper when using this database:

Bibtex:
```
@article{adigwe2018emotional,
  title={The emotional voices database: Towards controlling the emotion dimension in voice generation systems},
  author={Adigwe, Adaeze and Tits, No{\'e} and Haddad, Kevin El and Ostadabbas, Sarah and Dutoit, Thierry},
  journal={arXiv preprint arXiv:1806.09514},
  year={2018}
}
```
