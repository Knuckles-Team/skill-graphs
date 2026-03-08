##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Fcomplex&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Fcomplex "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/numeric/complex.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/numeric/complex.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/numeric/complex.html)
##### Views
  * [View](https://en.cppreference.com/w/c/numeric/complex.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/numeric/complex.html)
![ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.401293666;dc_trk_aid=593420487;dc_trk_cid=207494836;ord=177295381;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
# Complex number arithmetic
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [numeric](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[ C](https://en.cppreference.com/w/c.html "c")
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
---
[Language](https://en.cppreference.com/w/c/language.html "c/language")
[Headers](https://en.cppreference.com/w/c/header.html "c/header")
[Type support](https://en.cppreference.com/w/c/types.html "c/types")
[Program utilities](https://en.cppreference.com/w/c/program.html "c/program")
[Variadic function support](https://en.cppreference.com/w/c/variadic.html "c/variadic")
[Error handling](https://en.cppreference.com/w/c/error.html "c/error")
[Dynamic memory management](https://en.cppreference.com/w/c/memory.html "c/memory")
[Strings library](https://en.cppreference.com/w/c/string.html "c/string")
[Algorithms](https://en.cppreference.com/w/c/algorithm.html "c/algorithm")
[Numerics](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[Date and time utilities](https://en.cppreference.com/w/c/chrono.html "c/chrono")
[Input/output support](https://en.cppreference.com/w/c/io.html "c/io")
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
[ Numerics](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[Common mathematical functions](https://en.cppreference.com/w/c/numeric/math.html "c/numeric/math")
---
[Floating-point environment](https://en.cppreference.com/w/c/numeric/fenv.html "c/numeric/fenv") (C99)
[Pseudo-random number generation](https://en.cppreference.com/w/c/numeric/random.html "c/numeric/random")
**Complex number arithmetic** (C99)
[Type-generic math](https://en.cppreference.com/w/c/numeric/tgmath.html "c/numeric/tgmath") (C99)
[Bit manipulation](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation "c/numeric") (C23)
[Checked integer arithmetic](https://en.cppreference.com/w/c/numeric.html#Checked_integer_arithmetic "c/numeric") (C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/navbar_content&action=edit)
**Complex number arithmetic**
Types and the imaginary constant
---
|  [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html "c/numeric/complex/complex") (C99)
---
[_Complex_I](https://en.cppreference.com/w/c/numeric/complex/Complex_I.html "c/numeric/complex/Complex I") (C99)
[CMPLX](https://en.cppreference.com/w/c/numeric/complex/CMPLX.html "c/numeric/complex/CMPLX") (C11)
|  [imaginary](https://en.cppreference.com/w/c/numeric/complex/imaginary.html "c/numeric/complex/imaginary") (C99)
---
[_Imaginary_I](https://en.cppreference.com/w/c/numeric/complex/Imaginary_I.html "c/numeric/complex/Imaginary I") (C99)
[I](https://en.cppreference.com/w/c/numeric/complex/I.html "c/numeric/complex/I") (C99)
Manipulation
|  [cimag](https://en.cppreference.com/w/c/numeric/complex/cimag.html "c/numeric/complex/cimag") (C99)
---
[creal](https://en.cppreference.com/w/c/numeric/complex/creal.html "c/numeric/complex/creal") (C99)
[carg](https://en.cppreference.com/w/c/numeric/complex/carg.html "c/numeric/complex/carg") (C99)
|  [cabs](https://en.cppreference.com/w/c/numeric/complex/cabs.html "c/numeric/complex/cabs") (C99)
---
[conj](https://en.cppreference.com/w/c/numeric/complex/conj.html "c/numeric/complex/conj") (C99)
[cproj](https://en.cppreference.com/w/c/numeric/complex/cproj.html "c/numeric/complex/cproj") (C99)
Power and exponential functions
|  [cexp](https://en.cppreference.com/w/c/numeric/complex/cexp.html "c/numeric/complex/cexp") (C99)
---
[clog](https://en.cppreference.com/w/c/numeric/complex/clog.html "c/numeric/complex/clog") (C99)
|  [cpow](https://en.cppreference.com/w/c/numeric/complex/cpow.html "c/numeric/complex/cpow") (C99)
---
[csqrt](https://en.cppreference.com/w/c/numeric/complex/csqrt.html "c/numeric/complex/csqrt") (C99)
Trigonometric functions
|  [ccos](https://en.cppreference.com/w/c/numeric/complex/ccos.html "c/numeric/complex/ccos") (C99)
---
[csin](https://en.cppreference.com/w/c/numeric/complex/csin.html "c/numeric/complex/csin") (C99)
[ctan](https://en.cppreference.com/w/c/numeric/complex/ctan.html "c/numeric/complex/ctan") (C99)
|  [cacos](https://en.cppreference.com/w/c/numeric/complex/cacos.html "c/numeric/complex/cacos") (C99)
---
[casin](https://en.cppreference.com/w/c/numeric/complex/casin.html "c/numeric/complex/casin") (C99)
[catan](https://en.cppreference.com/w/c/numeric/complex/catan.html "c/numeric/complex/catan") (C99)
Hyperbolic functions
|  [ccosh](https://en.cppreference.com/w/c/numeric/complex/ccosh.html "c/numeric/complex/ccosh") (C99)
---
[csinh](https://en.cppreference.com/w/c/numeric/complex/csinh.html "c/numeric/complex/csinh") (C99)
[ctanh](https://en.cppreference.com/w/c/numeric/complex/ctanh.html "c/numeric/complex/ctanh") (C99)
|  [cacosh](https://en.cppreference.com/w/c/numeric/complex/cacosh.html "c/numeric/complex/cacosh") (C99)
---
[casinh](https://en.cppreference.com/w/c/numeric/complex/casinh.html "c/numeric/complex/casinh") (C99)
[catanh](https://en.cppreference.com/w/c/numeric/complex/catanh.html "c/numeric/complex/catanh") (C99)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/navbar_content&action=edit)
If the macro constant `__STDC_NO_COMPLEX__` is defined by the implementation, the complex types, the header [`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex") and all of the names listed here are not provided.  | (since C11)
---|---
The C programming language, as of C99, supports complex number math with the three built-in types double _Complex, float _Complex, and long double _Complex (see [`_Complex`](https://en.cppreference.com/w/c/keyword/_Complex.html "c/keyword/ Complex")). When the header [`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex") is included, the three complex number types are also accessible as double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html), float [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html), long double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html).
In addition to the complex types, the three imaginary types may be supported: double _Imaginary, float _Imaginary, and long double _Imaginary (see [`_Imaginary`](https://en.cppreference.com/w/c/keyword/_Imaginary.html "c/keyword/ Imaginary")). When the header [`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex") is included, the three imaginary types are also accessible as double [imaginary](https://en.cppreference.com/w/c/numeric/complex/imaginary.html), float [imaginary](https://en.cppreference.com/w/c/numeric/complex/imaginary.html), and long double [imaginary](https://en.cppreference.com/w/c/numeric/complex/imaginary.html).
Standard arithmetic operators +, -, *, / can be used with real, complex, and imaginary types in any combination.
A compiler that defines `__STDC_IEC_559_COMPLEX__` is recommended, but not required to support imaginary numbers. POSIX recommends checking if the macro [_Imaginary_I](https://en.cppreference.com/w/c/numeric/complex/Imaginary_I.html "c/numeric/complex/Imaginary I") is defined to identify imaginary number support.  |  (since C99)
(until C11)
---|---
Imaginary numbers are supported if `__STDC_IEC_559_COMPLEX__` or `__STDC_IEC_60559_COMPLEX__`(since C23) is defined.  | (since C11)
---
Defined in header `[`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex")`
|
## Contents
  * [1 Types](https://en.cppreference.com/w/c/numeric/complex.html#Types)
  * [2 The imaginary constant](https://en.cppreference.com/w/c/numeric/complex.html#The_imaginary_constant)
  * [3 Manipulation](https://en.cppreference.com/w/c/numeric/complex.html#Manipulation)
  * [4 Exponential functions](https://en.cppreference.com/w/c/numeric/complex.html#Exponential_functions)
  * [5 Power functions](https://en.cppreference.com/w/c/numeric/complex.html#Power_functions)
  * [6 Trigonometric functions](https://en.cppreference.com/w/c/numeric/complex.html#Trigonometric_functions)
  * [7 Hyperbolic functions](https://en.cppreference.com/w/c/numeric/complex.html#Hyperbolic_functions)
  * [8 Notes](https://en.cppreference.com/w/c/numeric/complex.html#Notes)
  * [9 Example](https://en.cppreference.com/w/c/numeric/complex.html#Example)
  * [10 References](https://en.cppreference.com/w/c/numeric/complex.html#References)
  * [11 See also](https://en.cppreference.com/w/c/numeric/complex.html#See_also)


---
#####  Types
[ imaginary](https://en.cppreference.com/w/c/numeric/complex/imaginary.html "c/numeric/complex/imaginary") (C99) |  imaginary type macro
(keyword macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_imaginary&action=edit)
[ complex](https://en.cppreference.com/w/c/numeric/complex/complex.html "c/numeric/complex/complex") (C99) |  complex type macro
(keyword macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_complex&action=edit)
#####  The imaginary constant
[ _Imaginary_I](https://en.cppreference.com/w/c/numeric/complex/Imaginary_I.html "c/numeric/complex/Imaginary I") (C99) |  the imaginary unit constant i
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_Imaginary_I&action=edit)
[ _Complex_I](https://en.cppreference.com/w/c/numeric/complex/Complex_I.html "c/numeric/complex/Complex I") (C99) |  the complex unit constant i
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_Complex_I&action=edit)
[ I](https://en.cppreference.com/w/c/numeric/complex/I.html "c/numeric/complex/I") (C99) |  the complex or imaginary unit constant i
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_I&action=edit)
#####  Manipulation
[ CMPLXCMPLXFCMPLXL](https://en.cppreference.com/w/c/numeric/complex/CMPLX.html "c/numeric/complex/CMPLX") (C11)(C11)(C11) |  constructs a complex number from real and imaginary parts
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_CMPLX&action=edit)
[ crealcrealfcreall](https://en.cppreference.com/w/c/numeric/complex/creal.html "c/numeric/complex/creal") (C99)(C99)(C99) |  computes the real part of a complex number
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_creal&action=edit)
[ cimagcimagfcimagl](https://en.cppreference.com/w/c/numeric/complex/cimag.html "c/numeric/complex/cimag") (C99)(C99)(C99) |  computes the imaginary part a complex number
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cimag&action=edit)
[ cabscabsfcabsl](https://en.cppreference.com/w/c/numeric/complex/cabs.html "c/numeric/complex/cabs") (C99)(C99)(C99) |  computes the magnitude of a complex number
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cabs&action=edit)
[ cargcargfcargl](https://en.cppreference.com/w/c/numeric/complex/carg.html "c/numeric/complex/carg") (C99)(C99)(C99) |  computes the phase angle of a complex number
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_carg&action=edit)
[ conjconjfconjl](https://en.cppreference.com/w/c/numeric/complex/conj.html "c/numeric/complex/conj") (C99)(C99)(C99) |  computes the complex conjugate
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_conj&action=edit)
[ cprojcprojfcprojl](https://en.cppreference.com/w/c/numeric/complex/cproj.html "c/numeric/complex/cproj") (C99)(C99)(C99) |  computes the projection on Riemann sphere
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cproj&action=edit)
#####  Exponential functions
[ cexpcexpfcexpl](https://en.cppreference.com/w/c/numeric/complex/cexp.html "c/numeric/complex/cexp") (C99)(C99)(C99) |  computes the complex base-e exponential
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cexp&action=edit)
[ clogclogfclogl](https://en.cppreference.com/w/c/numeric/complex/clog.html "c/numeric/complex/clog") (C99)(C99)(C99) |  computes the complex natural logarithm
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_clog&action=edit)
#####  Power functions
[ cpowcpowfcpowl](https://en.cppreference.com/w/c/numeric/complex/cpow.html "c/numeric/complex/cpow") (C99)(C99)(C99) |  computes the complex power function
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cpow&action=edit)
[ csqrtcsqrtfcsqrtl](https://en.cppreference.com/w/c/numeric/complex/csqrt.html "c/numeric/complex/csqrt") (C99)(C99)(C99) |  computes the complex square root
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_csqrt&action=edit)
#####  Trigonometric functions
[ csincsinfcsinl](https://en.cppreference.com/w/c/numeric/complex/csin.html "c/numeric/complex/csin") (C99)(C99)(C99) |  computes the complex sine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_csin&action=edit)
[ ccosccosfccosl](https://en.cppreference.com/w/c/numeric/complex/ccos.html "c/numeric/complex/ccos") (C99)(C99)(C99) |  computes the complex cosine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_ccos&action=edit)
[ ctanctanfctanl](https://en.cppreference.com/w/c/numeric/complex/ctan.html "c/numeric/complex/ctan") (C99)(C99)(C99) |  computes the complex tangent
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_ctan&action=edit)
[ casincasinfcasinl](https://en.cppreference.com/w/c/numeric/complex/casin.html "c/numeric/complex/casin") (C99)(C99)(C99) |  computes the complex arc sine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_casin&action=edit)
[ cacoscacosfcacosl](https://en.cppreference.com/w/c/numeric/complex/cacos.html "c/numeric/complex/cacos") (C99)(C99)(C99) |  computes the complex arc cosine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cacos&action=edit)
[ catancatanfcatanl](https://en.cppreference.com/w/c/numeric/complex/catan.html "c/numeric/complex/catan") (C99)(C99)(C99) |  computes the complex arc tangent
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_catan&action=edit)
#####  Hyperbolic functions
[ csinhcsinhfcsinhl](https://en.cppreference.com/w/c/numeric/complex/csinh.html "c/numeric/complex/csinh") (C99)(C99)(C99) |  computes the complex hyperbolic sine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_csinh&action=edit)
[ ccoshccoshfccoshl](https://en.cppreference.com/w/c/numeric/complex/ccosh.html "c/numeric/complex/ccosh") (C99)(C99)(C99) |  computes the complex hyperbolic cosine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_ccosh&action=edit)
[ ctanhctanhfctanhl](https://en.cppreference.com/w/c/numeric/complex/ctanh.html "c/numeric/complex/ctanh") (C99)(C99)(C99) |  computes the complex hyperbolic tangent
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_ctanh&action=edit)
[ casinhcasinhfcasinhl](https://en.cppreference.com/w/c/numeric/complex/casinh.html "c/numeric/complex/casinh") (C99)(C99)(C99) |  computes the complex arc hyperbolic sine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_casinh&action=edit)
[ cacoshcacoshfcacoshl](https://en.cppreference.com/w/c/numeric/complex/cacosh.html "c/numeric/complex/cacosh") (C99)(C99)(C99) |  computes the complex arc hyperbolic cosine
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_cacosh&action=edit)
[ catanhcatanhfcatanhl](https://en.cppreference.com/w/c/numeric/complex/catanh.html "c/numeric/complex/catanh") (C99)(C99)(C99) |  computes the complex arc hyperbolic tangent
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/complex/dsc_catanh&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=edit&section=1 "Edit section: Notes")] Notes
The following function names are potentially(since C23) reserved for future addition to [`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex") and are not available for use in the programs that include that header: cerf, cerfc, cexp2, cexpm1, clog10, clog1p, clog2, clgamma, ctgamma, csinpi, ccospi, ctanpi, casinpi, cacospi, catanpi, ccompoundn, cpown, cpowr, crootn, crsqrt, cexp10m1, cexp10, cexp2m1, clog10p1, clog2p1, clogp1(since C23), along with their -`f` and -`l` suffixed variants.
Although the C standard names the inverse hyperbolic with "complex arc hyperbolic sine" etc., the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct names are "complex inverse hyperbolic sine" etc. Some authors use "complex area hyperbolic sine" etc.
A complex or imaginary number is infinite if one of its parts is infinite, even if the other part is NaN.
A complex or imaginary number is finite if both parts are neither infinities nor NaNs.
A complex or imaginary number is a zero if both parts are positive or negative zeroes.
While MSVC does provide a structs, which are incompatible with standard C complex types and do not support the +, -, *, / operators.
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=edit&section=2 "Edit section: Example")] Example
Run this code
```
#include <complex.h>
#include <stdio.h>
#include <tgmath.h>
 
int main(void)
{
    double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) z1 = I * I;     // imaginary unit squared
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("I * I = %.1f%+.1fi\n", [creal](https://en.cppreference.com/w/c/numeric/complex/creal.html)(z1), [cimag](https://en.cppreference.com/w/c/numeric/complex/cimag.html)(z1));
 
    double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) z2 = [pow](https://en.cppreference.com/w/c/numeric/math/pow.html)(I, 2); // imaginary unit squared
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("pow(I, 2) = %.1f%+.1fi\n", [creal](https://en.cppreference.com/w/c/numeric/complex/creal.html)(z2), [cimag](https://en.cppreference.com/w/c/numeric/complex/cimag.html)(z2));
 
    double PI = [acos](https://en.cppreference.com/w/c/numeric/math/acos.html)(-1);
    double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) z3 = [exp](https://en.cppreference.com/w/c/numeric/math/exp.html)(I * PI); // Euler's formula
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("exp(I*PI) = %.1f%+.1fi\n", [creal](https://en.cppreference.com/w/c/numeric/complex/creal.html)(z3), [cimag](https://en.cppreference.com/w/c/numeric/complex/cimag.html)(z3));
 
    double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) z4 = 1 + 2 * I, z5 = 1 - 2 * I; // conjugates
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("(1+2i)*(1-2i) = %.1f%+.1fi\n", [creal](https://en.cppreference.com/w/c/numeric/complex/creal.html)(z4 * z5), [cimag](https://en.cppreference.com/w/c/numeric/complex/cimag.html)(z4 * z5));
}
```

Output:
```
I * I = -1.0+0.0i
pow(I, 2) = -1.0+0.0i
exp(I*PI) = -1.0+0.0i
(1+2i)*(1-2i) = 5.0+0.0i
```

###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=edit&section=3 "Edit section: References")] References
Extended content
---
  * C23 standard (ISO/IEC 9899:2024):


  * 6.10.8.3/1/2 `__STDC_NO_COMPLEX__` (p: TBD)


  * 6.10.8.3/1/2 `__STDC_IEC_559_COMPLEX__` (p: TBD)


  * 7.3 Complex arithmetic `<complex.h>` (p: TBD)


  * 7.25 Type-generic math `<tgmath.h>` (p: TBD)


  * 7.31.1 Complex arithmetic `<complex.h>` (p: TBD)


  * Annex G (normative) IEC 60559-compatible complex arithmetic (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 6.10.8.3/1/2 `__STDC_NO_COMPLEX__` (p: 128)


  * 6.10.8.3/1/2 `__STDC_IEC_559_COMPLEX__` (p: 128)


  * 7.3 Complex arithmetic `<complex.h>` (p: 136-144)


  * 7.25 Type-generic math `<tgmath.h>` (p: 272-273)


  * 7.31.1 Complex arithmetic `<complex.h>` (p: 391)


  * Annex G (normative) IEC 60559-compatible complex arithmetic (p: 469-479)


  * C11 standard (ISO/IEC 9899:2011):


  * 6.10.8.3/1/2 `__STDC_NO_COMPLEX__` (p: 177)


  * 6.10.8.3/1/2 `__STDC_IEC_559_COMPLEX__` (p: 177)


  * 7.3 Complex arithmetic `<complex.h>` (p: 188-199)


  * 7.25 Type-generic math `<tgmath.h>` (p: 373-375)


  * 7.31.1 Complex arithmetic `<complex.h>` (p: 455)


  * Annex G (normative) IEC 60559-compatible complex arithmetic (p: 532-545)


  * C99 standard (ISO/IEC 9899:1999):


  * 6.10.8/2 `__STDC_IEC_559_COMPLEX__` (p: 161)


  * 7.3 Complex arithmetic `<complex.h>` (p: 170-180)


  * 7.22 Type-generic math `<tgmath.h>` (p: 335-337)


  * 7.26.1 Complex arithmetic `<complex.h>` (p: 401)


  * Annex G (informative) IEC 60559-compatible complex arithmetic (p: 467-480)


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=edit&section=4 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/numeric/complex.html "cpp/numeric/complex") for Complex number arithmetic
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&oldid=180042](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&oldid=180042)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/numeric/complex.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/numeric/complex "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/numeric/complex "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&oldid=180042 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/numeric/complex&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Česky](http://cs.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Deutsch](http://de.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Español](http://es.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Français](http://fr.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Italiano](http://it.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [日本語](http://ja.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [한국어](http://ko.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Polski](http://pl.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Português](http://pt.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Русский](http://ru.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [Türkçe](http://tr.cppreference.com/w/c/numeric/complex "c/numeric/complex")
  * [中文](http://zh.cppreference.com/w/c/numeric/complex "c/numeric/complex")


  * This page was last modified on 1 February 2025, at 22:49.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
