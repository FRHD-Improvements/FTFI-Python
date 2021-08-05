# FTFI Spec

*The official spec for the FTFI (*F*ree rider *T*rack *F*ormat *I*mproved).*

## Basic
This is stuff that is already supported by the [editor](https://freeriderhd.com/create).

**NOTE: Support for teleports is coming soon, but not quite yet.**

1. Lines
Lines are started by either a `p` or a `s`, for `physics` or `scenery`. The following four numbers are the
start x/y pair and the destination x/y pair.
`p -40 50 100 50`

2. Boosts
Boosts are started by a `b`. The next three numbers are the x/y, as well as the rotation.
`b 90 -10 90`

3. Bombs
Bombs are started by a `k`. The next two numbers are the x/y.
`k 10 10`

4. Gravity
Gravity modifiers are started by a `g`. The next thee numbers are the x/y, as well as the rotation.
`g 90 10 10`

5. Checkpoints
Checkpoints are started by a `c`. The next two numbers are the x/y.
`c 100 100`

6. Slow Motion
SlowMos are started by a `m`. The next two numbers are the x/y.
`m -43 12`

7. Stars
Stars are started by a `t`. The next two numbers are the x/y.
`s 887 322`


## Extended
This is stuff that is not supported by the editor.

1. Images (two-shade)
Images with only two colors ((p || s) && null) are started by an `i`, and followed by the specification. The 
next letter is either `p` or `s`, which determines whether physical or scenery lines will be used. After the
specification, the absolute path to the image is included.
`is /Users/gabriel/Pictures/Space.png`

1. Images (three-shade)
Images with three colors (p && s && null) are started by a `` 

