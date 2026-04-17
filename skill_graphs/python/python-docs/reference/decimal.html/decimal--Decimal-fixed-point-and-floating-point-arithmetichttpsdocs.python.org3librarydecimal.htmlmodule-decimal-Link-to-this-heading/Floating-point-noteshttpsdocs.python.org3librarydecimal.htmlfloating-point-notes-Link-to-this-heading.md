## Floating-point notes[¶](https://docs.python.org/3/library/decimal.html#floating-point-notes "Link to this heading")
### Mitigating round-off error with increased precision[¶](https://docs.python.org/3/library/decimal.html#mitigating-round-off-error-with-increased-precision "Link to this heading")
The use of decimal floating point eliminates decimal representation error (making it possible to represent `0.1` exactly); however, some operations can still incur round-off error when non-zero digits exceed the fixed precision.
The effects of round-off error can be amplified by the addition or subtraction of nearly offsetting quantities resulting in loss of significance. Knuth provides two instructive examples where rounded floating-point arithmetic with insufficient precision causes the breakdown of the associative and distributive properties of addition:
Copy```
