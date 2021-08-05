# FTFI Python

This is the old version of the Format-to-track tool. It has several problems, foremost of which is the fact that it uses a Python library to generate the track code
which is *really* slow. 


## What comes next?

I am currently working on a rewrite in a faster language (probably Rust or C). Since I have to rewrite an entire library in an entirely different language, it might take a while. Just hang in there.

Oh also, I might change the format to be a little more compact. We'll see.


## Contributing

Please don't. Just wait for the new version to come out, then contribute to that one!


## Use

Clone the repository, then run `code_generation.py` using python@3.5+. Edit `track_code.txt` to fit your needs (check out [spec.md](spec.md) for info on the current format)
