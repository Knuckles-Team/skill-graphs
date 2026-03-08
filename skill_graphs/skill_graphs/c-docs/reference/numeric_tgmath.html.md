##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Ftgmath&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Ftgmath "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/numeric/tgmath.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/numeric/tgmath.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/numeric/tgmath.html)
##### Views
  * [View](https://en.cppreference.com/w/c/numeric/tgmath.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/numeric/tgmath.html)
# Type-generic math (since C99)
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
[Complex number arithmetic](https://en.cppreference.com/w/c/numeric/complex.html "c/numeric/complex") (C99)
**Type-generic math** (C99)
[Bit manipulation](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation "c/numeric") (C23)
[Checked integer arithmetic](https://en.cppreference.com/w/c/numeric.html#Checked_integer_arithmetic "c/numeric") (C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/navbar_content&action=edit)
The header [`<tgmath.h>`](https://en.cppreference.com/w/c/header/tgmath.html "c/header/tgmath") includes the headers [`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math") and [`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex") and defines several [type-generic macros](https://en.cppreference.com/w/c/language/generic.html "c/language/generic") that determine which real or, when applicable, complex function to call based on the types of the arguments.
For each macro, the parameters whose corresponding real type in the unsuffixed [`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math") function is double are known as _generic parameters_ (for example, both parameters of [pow](https://en.cppreference.com/w/c/numeric/math/pow.html "c/numeric/math/pow") are generic parameters, but only the first parameter of [scalbn](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn") is a generic parameter).
When a [`<tgmath.h>`](https://en.cppreference.com/w/c/header/tgmath.html "c/header/tgmath")'s macro is used the types of the arguments passed to the generic parameters determine which function is selected by the macro as described below. If the types of the arguments are not [compatible](https://en.cppreference.com/w/c/language/compatible_type.html#Compatible_types "c/language/type") with the parameter types of the selected function, the behavior is undefined (e.g. if a complex argument is passed into a real-only [`<tgmath.h>`](https://en.cppreference.com/w/c/header/tgmath.html "c/header/tgmath")'s macro: float [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) fc; [ceil](https://en.cppreference.com/w/c/numeric/math/ceil.html)(fc); or double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) dc; double d; [fmax](https://en.cppreference.com/w/c/numeric/math/fmax.html)(dc, d); are examples of undefined behavior).
Note: type-generic macros were implemented in implementation-defined manner in C99, but C11 keyword [`_Generic`](https://en.cppreference.com/w/c/keyword/_Generic.html "c/keyword/ Generic") makes it possible to implement these macros in portable manner.
## Contents
  * [1 Complex/real type-generic macros](https://en.cppreference.com/w/c/numeric/tgmath.html#Complex.2Freal_type-generic_macros)
  * [2 Real-only functions](https://en.cppreference.com/w/c/numeric/tgmath.html#Real-only_functions)
  * [3 Complex-only functions](https://en.cppreference.com/w/c/numeric/tgmath.html#Complex-only_functions)
  * [4 Example](https://en.cppreference.com/w/c/numeric/tgmath.html#Example)
  * [5 References](https://en.cppreference.com/w/c/numeric/tgmath.html#References)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=edit&section=1 "Edit section: Complex/real type-generic macros")] Complex/real type-generic macros
For all functions that have both real and complex counterparts, a type-generic macro `XXX` exists, which calls either of:
  * real function:


  * float variant `XXXf`
  * double variant `XXX`
  * long double variant `XXXl`


  * complex function:


  * float variant `cXXXf`
  * double variant `cXXX`
  * long double variant `cXXXl`


An exception to the above rule is the `fabs` macro (see the table below).
The function to call is determined as follows:
  * If any of the arguments for the generic parameters is imaginary, the behavior is specified on each function reference page individually (in particular, `sin`, `cos`, `tan`, `cosh`, `sinh`, `tanh`, `asin`, `atan`, `asinh`, and `atanh` call _real_ functions, the return types of `sin`, `tan`, `sinh`, `tanh`, `asin`, `atan`, `asinh`, and `atanh` are imaginary, and the return types of `cos` and `cosh` are real).
  * If any of the arguments for the generic parameters is complex, then the complex function is called, otherwise the real function is called.
  * If any of the arguments for the generic parameters is long double, then the long double variant is called. Otherwise, if any of the parameters is double or integer, then the double variant is called. Otherwise, float variant is called.


The type-generic macros are as follows:
Type-generic
macro  | Real function
variants  | Complex function
variants
---|---|---
|  float |  double |  long double |  float |  double |  long double
fabs  |  [`fabsf`](https://en.cppreference.com/w/c/numeric/math/fabs.html "c/numeric/math/fabs") |  [`fabs`](https://en.cppreference.com/w/c/numeric/math/fabs.html "c/numeric/math/fabs") |  [`fabsl`](https://en.cppreference.com/w/c/numeric/math/fabs.html "c/numeric/math/fabs") |  [`cabsf`](https://en.cppreference.com/w/c/numeric/complex/cabs.html "c/numeric/complex/cabs") |  [`cabs`](https://en.cppreference.com/w/c/numeric/complex/cabs.html "c/numeric/complex/cabs") |  [`cabsl`](https://en.cppreference.com/w/c/numeric/complex/cabs.html "c/numeric/complex/cabs")
exp  |  [`expf`](https://en.cppreference.com/w/c/numeric/math/exp.html "c/numeric/math/exp") |  [`exp`](https://en.cppreference.com/w/c/numeric/math/exp.html "c/numeric/math/exp") |  [`expl`](https://en.cppreference.com/w/c/numeric/math/exp.html "c/numeric/math/exp") |  [`cexpf`](https://en.cppreference.com/w/c/numeric/complex/cexp.html "c/numeric/complex/cexp") |  [`cexp`](https://en.cppreference.com/w/c/numeric/complex/cexp.html "c/numeric/complex/cexp") |  [`cexpl`](https://en.cppreference.com/w/c/numeric/complex/cexp.html "c/numeric/complex/cexp")
log  |  [`logf`](https://en.cppreference.com/w/c/numeric/math/log.html "c/numeric/math/log") |  [`log`](https://en.cppreference.com/w/c/numeric/math/log.html "c/numeric/math/log") |  [`logl`](https://en.cppreference.com/w/c/numeric/math/log.html "c/numeric/math/log") |  [`clogf`](https://en.cppreference.com/w/c/numeric/complex/clog.html "c/numeric/complex/clog") |  [`clog`](https://en.cppreference.com/w/c/numeric/complex/clog.html "c/numeric/complex/clog") |  [`clogl`](https://en.cppreference.com/w/c/numeric/complex/clog.html "c/numeric/complex/clog")
pow  |  [`powf`](https://en.cppreference.com/w/c/numeric/math/pow.html "c/numeric/math/pow") |  [`pow`](https://en.cppreference.com/w/c/numeric/math/pow.html "c/numeric/math/pow") |  [`powl`](https://en.cppreference.com/w/c/numeric/math/pow.html "c/numeric/math/pow") |  [`cpowf`](https://en.cppreference.com/w/c/numeric/complex/cpow.html "c/numeric/complex/cpow") |  [`cpow`](https://en.cppreference.com/w/c/numeric/complex/cpow.html "c/numeric/complex/cpow") |  [`cpowl`](https://en.cppreference.com/w/c/numeric/complex/cpow.html "c/numeric/complex/cpow")
sqrt  |  [`sqrtf`](https://en.cppreference.com/w/c/numeric/math/sqrt.html "c/numeric/math/sqrt") |  [`sqrt`](https://en.cppreference.com/w/c/numeric/math/sqrt.html "c/numeric/math/sqrt") |  [`sqrtl`](https://en.cppreference.com/w/c/numeric/math/sqrt.html "c/numeric/math/sqrt") |  [`csqrtf`](https://en.cppreference.com/w/c/numeric/complex/csqrt.html "c/numeric/complex/csqrt") |  [`csqrt`](https://en.cppreference.com/w/c/numeric/complex/csqrt.html "c/numeric/complex/csqrt") |  [`csqrtl`](https://en.cppreference.com/w/c/numeric/complex/csqrt.html "c/numeric/complex/csqrt")
sin  |  [`sinf`](https://en.cppreference.com/w/c/numeric/math/sin.html "c/numeric/math/sin") |  [`sin`](https://en.cppreference.com/w/c/numeric/math/sin.html "c/numeric/math/sin") |  [`sinl`](https://en.cppreference.com/w/c/numeric/math/sin.html "c/numeric/math/sin") |  [`csinf`](https://en.cppreference.com/w/c/numeric/complex/csin.html "c/numeric/complex/csin") |  [`csin`](https://en.cppreference.com/w/c/numeric/complex/csin.html "c/numeric/complex/csin") |  [`csinl`](https://en.cppreference.com/w/c/numeric/complex/csin.html "c/numeric/complex/csin")
cos  |  [`cosf`](https://en.cppreference.com/w/c/numeric/math/cos.html "c/numeric/math/cos") |  [`cos`](https://en.cppreference.com/w/c/numeric/math/cos.html "c/numeric/math/cos") |  [`cosl`](https://en.cppreference.com/w/c/numeric/math/cos.html "c/numeric/math/cos") |  [`ccosf`](https://en.cppreference.com/w/c/numeric/complex/ccos.html "c/numeric/complex/ccos") |  [`ccos`](https://en.cppreference.com/w/c/numeric/complex/ccos.html "c/numeric/complex/ccos") |  [`ccosl`](https://en.cppreference.com/w/c/numeric/complex/ccos.html "c/numeric/complex/ccos")
tan  |  [`tanf`](https://en.cppreference.com/w/c/numeric/math/tan.html "c/numeric/math/tan") |  [`tan`](https://en.cppreference.com/w/c/numeric/math/tan.html "c/numeric/math/tan") |  [`tanl`](https://en.cppreference.com/w/c/numeric/math/tan.html "c/numeric/math/tan") |  [`ctanf`](https://en.cppreference.com/w/c/numeric/complex/ctan.html "c/numeric/complex/ctan") |  [`ctan`](https://en.cppreference.com/w/c/numeric/complex/ctan.html "c/numeric/complex/ctan") |  [`ctanl`](https://en.cppreference.com/w/c/numeric/complex/ctan.html "c/numeric/complex/ctan")
asin  |  [`asinf`](https://en.cppreference.com/w/c/numeric/math/asin.html "c/numeric/math/asin") |  [`asin`](https://en.cppreference.com/w/c/numeric/math/asin.html "c/numeric/math/asin") |  [`asinl`](https://en.cppreference.com/w/c/numeric/math/asin.html "c/numeric/math/asin") |  [`casinf`](https://en.cppreference.com/w/c/numeric/complex/casin.html "c/numeric/complex/casin") |  [`casin`](https://en.cppreference.com/w/c/numeric/complex/casin.html "c/numeric/complex/casin") |  [`casinl`](https://en.cppreference.com/w/c/numeric/complex/casin.html "c/numeric/complex/casin")
acos  |  [`acosf`](https://en.cppreference.com/w/c/numeric/math/acos.html "c/numeric/math/acos") |  [`acos`](https://en.cppreference.com/w/c/numeric/math/acos.html "c/numeric/math/acos") |  [`acosl`](https://en.cppreference.com/w/c/numeric/math/acos.html "c/numeric/math/acos") |  [`cacosf`](https://en.cppreference.com/w/c/numeric/complex/cacos.html "c/numeric/complex/cacos") |  [`cacos`](https://en.cppreference.com/w/c/numeric/complex/cacos.html "c/numeric/complex/cacos") |  [`cacosl`](https://en.cppreference.com/w/c/numeric/complex/cacos.html "c/numeric/complex/cacos")
atan  |  [`atanf`](https://en.cppreference.com/w/c/numeric/math/atan.html "c/numeric/math/atan") |  [`atan`](https://en.cppreference.com/w/c/numeric/math/atan.html "c/numeric/math/atan") |  [`atanl`](https://en.cppreference.com/w/c/numeric/math/atan.html "c/numeric/math/atan") |  [`catanf`](https://en.cppreference.com/w/c/numeric/complex/catan.html "c/numeric/complex/catan") |  [`catan`](https://en.cppreference.com/w/c/numeric/complex/catan.html "c/numeric/complex/catan") |  [`catanl`](https://en.cppreference.com/w/c/numeric/complex/catan.html "c/numeric/complex/catan")
sinh  |  [`sinhf`](https://en.cppreference.com/w/c/numeric/math/sinh.html "c/numeric/math/sinh") |  [`sinh`](https://en.cppreference.com/w/c/numeric/math/sinh.html "c/numeric/math/sinh") |  [`sinhl`](https://en.cppreference.com/w/c/numeric/math/sinh.html "c/numeric/math/sinh") |  [`csinhf`](https://en.cppreference.com/w/c/numeric/complex/csinh.html "c/numeric/complex/csinh") |  [`csinh`](https://en.cppreference.com/w/c/numeric/complex/csinh.html "c/numeric/complex/csinh") |  [`csinhl`](https://en.cppreference.com/w/c/numeric/complex/csinh.html "c/numeric/complex/csinh")
cosh  |  [`coshf`](https://en.cppreference.com/w/c/numeric/math/cosh.html "c/numeric/math/cosh") |  [`cosh`](https://en.cppreference.com/w/c/numeric/math/cosh.html "c/numeric/math/cosh") |  [`coshl`](https://en.cppreference.com/w/c/numeric/math/cosh.html "c/numeric/math/cosh") |  [`ccoshf`](https://en.cppreference.com/w/c/numeric/complex/ccosh.html "c/numeric/complex/ccosh") |  [`ccosh`](https://en.cppreference.com/w/c/numeric/complex/ccosh.html "c/numeric/complex/ccosh") |  [`ccoshl`](https://en.cppreference.com/w/c/numeric/complex/ccosh.html "c/numeric/complex/ccosh")
tanh  |  [`tanhf`](https://en.cppreference.com/w/c/numeric/math/tanh.html "c/numeric/math/tanh") |  [`tanh`](https://en.cppreference.com/w/c/numeric/math/tanh.html "c/numeric/math/tanh") |  [`tanhl`](https://en.cppreference.com/w/c/numeric/math/tanh.html "c/numeric/math/tanh") |  [`ctanhf`](https://en.cppreference.com/w/c/numeric/complex/ctanh.html "c/numeric/complex/ctanh") |  [`ctanh`](https://en.cppreference.com/w/c/numeric/complex/ctanh.html "c/numeric/complex/ctanh") |  [`ctanhl`](https://en.cppreference.com/w/c/numeric/complex/ctanh.html "c/numeric/complex/ctanh")
asinh  |  [`asinhf`](https://en.cppreference.com/w/c/numeric/math/asinh.html "c/numeric/math/asinh") |  [`asinh`](https://en.cppreference.com/w/c/numeric/math/asinh.html "c/numeric/math/asinh") |  [`asinhl`](https://en.cppreference.com/w/c/numeric/math/asinh.html "c/numeric/math/asinh") |  [`casinhf`](https://en.cppreference.com/w/c/numeric/complex/casinh.html "c/numeric/complex/casinh") |  [`casinh`](https://en.cppreference.com/w/c/numeric/complex/casinh.html "c/numeric/complex/casinh") |  [`casinhl`](https://en.cppreference.com/w/c/numeric/complex/casinh.html "c/numeric/complex/casinh")
acosh  |  [`acoshf`](https://en.cppreference.com/w/c/numeric/math/acosh.html "c/numeric/math/acosh") |  [`acosh`](https://en.cppreference.com/w/c/numeric/math/acosh.html "c/numeric/math/acosh") |  [`acoshl`](https://en.cppreference.com/w/c/numeric/math/acosh.html "c/numeric/math/acosh") |  [`cacoshf`](https://en.cppreference.com/w/c/numeric/complex/cacosh.html "c/numeric/complex/cacosh") |  [`cacosh`](https://en.cppreference.com/w/c/numeric/complex/cacosh.html "c/numeric/complex/cacosh") |  [`cacoshl`](https://en.cppreference.com/w/c/numeric/complex/cacosh.html "c/numeric/complex/cacosh")
atanh  |  [`atanhf`](https://en.cppreference.com/w/c/numeric/math/atanh.html "c/numeric/math/atanh") |  [`atanh`](https://en.cppreference.com/w/c/numeric/math/atanh.html "c/numeric/math/atanh") |  [`atanhl`](https://en.cppreference.com/w/c/numeric/math/atanh.html "c/numeric/math/atanh") |  [`catanhf`](https://en.cppreference.com/w/c/numeric/complex/catanh.html "c/numeric/complex/catanh") |  [`catanh`](https://en.cppreference.com/w/c/numeric/complex/catanh.html "c/numeric/complex/catanh") |  [`catanhl`](https://en.cppreference.com/w/c/numeric/complex/catanh.html "c/numeric/complex/catanh")
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=edit&section=2 "Edit section: Real-only functions")] Real-only functions
For all functions that do not have complex counterparts, with the exception of `modf`, a type-generic macro `XXX` exists, which calls either of the variants of a real function:
  * float variant `XXXf`
  * double variant `XXX`
  * long double variant `XXXl`


The function to call is determined as follows:
  * If any of the arguments for the generic parameters is long double, then the long double variant is called. Otherwise, if any of the arguments for the generic parameters is double, then the double variant is called. Otherwise, float variant is called.

Type-generic
macro  | Real function
variants
---|---
|  float |  double |  long double
atan2  |  [`atan2f`](https://en.cppreference.com/w/c/numeric/math/atan2.html "c/numeric/math/atan2") |  [`atan2`](https://en.cppreference.com/w/c/numeric/math/atan2.html "c/numeric/math/atan2") |  [`atan2l`](https://en.cppreference.com/w/c/numeric/math/atan2.html "c/numeric/math/atan2")
cbrt  |  [`cbrtf`](https://en.cppreference.com/w/c/numeric/math/cbrt.html "c/numeric/math/cbrt") |  [`cbrt`](https://en.cppreference.com/w/c/numeric/math/cbrt.html "c/numeric/math/cbrt") |  [`cbrtl`](https://en.cppreference.com/w/c/numeric/math/cbrt.html "c/numeric/math/cbrt")
ceil  |  [`ceilf`](https://en.cppreference.com/w/c/numeric/math/ceil.html "c/numeric/math/ceil") |  [`ceil`](https://en.cppreference.com/w/c/numeric/math/ceil.html "c/numeric/math/ceil") |  [`ceill`](https://en.cppreference.com/w/c/numeric/math/ceil.html "c/numeric/math/ceil")
copysign  |  [`copysignf`](https://en.cppreference.com/w/c/numeric/math/copysign.html "c/numeric/math/copysign") |  [`copysign`](https://en.cppreference.com/w/c/numeric/math/copysign.html "c/numeric/math/copysign") |  [`copysignl`](https://en.cppreference.com/w/c/numeric/math/copysign.html "c/numeric/math/copysign")
erf  |  [`erff`](https://en.cppreference.com/w/c/numeric/math/erf.html "c/numeric/math/erf") |  [`erf`](https://en.cppreference.com/w/c/numeric/math/erf.html "c/numeric/math/erf") |  [`erfl`](https://en.cppreference.com/w/c/numeric/math/erf.html "c/numeric/math/erf")
erfc  |  [`erfcf`](https://en.cppreference.com/w/c/numeric/math/erfc.html "c/numeric/math/erfc") |  [`erfc`](https://en.cppreference.com/w/c/numeric/math/erfc.html "c/numeric/math/erfc") |  [`erfcl`](https://en.cppreference.com/w/c/numeric/math/erfc.html "c/numeric/math/erfc")
exp2  |  [`exp2f`](https://en.cppreference.com/w/c/numeric/math/exp2.html "c/numeric/math/exp2") |  [`exp2`](https://en.cppreference.com/w/c/numeric/math/exp2.html "c/numeric/math/exp2") |  [`exp2l`](https://en.cppreference.com/w/c/numeric/math/exp2.html "c/numeric/math/exp2")
expm1  |  [`expm1f`](https://en.cppreference.com/w/c/numeric/math/expm1.html "c/numeric/math/expm1") |  [`expm1`](https://en.cppreference.com/w/c/numeric/math/expm1.html "c/numeric/math/expm1") |  [`expm1l`](https://en.cppreference.com/w/c/numeric/math/expm1.html "c/numeric/math/expm1")
fdim  |  [`fdimf`](https://en.cppreference.com/w/c/numeric/math/fdim.html "c/numeric/math/fdim") |  [`fdim`](https://en.cppreference.com/w/c/numeric/math/fdim.html "c/numeric/math/fdim") |  [`fdiml`](https://en.cppreference.com/w/c/numeric/math/fdim.html "c/numeric/math/fdim")
floor  |  [`floorf`](https://en.cppreference.com/w/c/numeric/math/floor.html "c/numeric/math/floor") |  [`floor`](https://en.cppreference.com/w/c/numeric/math/floor.html "c/numeric/math/floor") |  [`floorl`](https://en.cppreference.com/w/c/numeric/math/floor.html "c/numeric/math/floor")
fma  |  [`fmaf`](https://en.cppreference.com/w/c/numeric/math/fma.html "c/numeric/math/fma") |  [`fma`](https://en.cppreference.com/w/c/numeric/math/fma.html "c/numeric/math/fma") |  [`fmal`](https://en.cppreference.com/w/c/numeric/math/fma.html "c/numeric/math/fma")
fmax  |  [`fmaxf`](https://en.cppreference.com/w/c/numeric/math/fmax.html "c/numeric/math/fmax") |  [`fmax`](https://en.cppreference.com/w/c/numeric/math/fmax.html "c/numeric/math/fmax") |  [`fmaxl`](https://en.cppreference.com/w/c/numeric/math/fmax.html "c/numeric/math/fmax")
fmin  |  [`fminf`](https://en.cppreference.com/w/c/numeric/math/fmin.html "c/numeric/math/fmin") |  [`fmin`](https://en.cppreference.com/w/c/numeric/math/fmin.html "c/numeric/math/fmin") |  [`fminl`](https://en.cppreference.com/w/c/numeric/math/fmin.html "c/numeric/math/fmin")
fmod  |  [`fmodf`](https://en.cppreference.com/w/c/numeric/math/fmod.html "c/numeric/math/fmod") |  [`fmod`](https://en.cppreference.com/w/c/numeric/math/fmod.html "c/numeric/math/fmod") |  [`fmodl`](https://en.cppreference.com/w/c/numeric/math/fmod.html "c/numeric/math/fmod")
frexp  |  [`frexpf`](https://en.cppreference.com/w/c/numeric/math/frexp.html "c/numeric/math/frexp") |  [`frexp`](https://en.cppreference.com/w/c/numeric/math/frexp.html "c/numeric/math/frexp") |  [`frexpl`](https://en.cppreference.com/w/c/numeric/math/frexp.html "c/numeric/math/frexp")
hypot  |  [`hypotf`](https://en.cppreference.com/w/c/numeric/math/hypot.html "c/numeric/math/hypot") |  [`hypot`](https://en.cppreference.com/w/c/numeric/math/hypot.html "c/numeric/math/hypot") |  [`hypotl`](https://en.cppreference.com/w/c/numeric/math/hypot.html "c/numeric/math/hypot")
ilogb  |  [`ilogbf`](https://en.cppreference.com/w/c/numeric/math/ilogb.html "c/numeric/math/ilogb") |  [`ilogb`](https://en.cppreference.com/w/c/numeric/math/ilogb.html "c/numeric/math/ilogb") |  [`ilogbl`](https://en.cppreference.com/w/c/numeric/math/ilogb.html "c/numeric/math/ilogb")
ldexp  |  [`ldexpf`](https://en.cppreference.com/w/c/numeric/math/ldexp.html "c/numeric/math/ldexp") |  [`ldexp`](https://en.cppreference.com/w/c/numeric/math/ldexp.html "c/numeric/math/ldexp") |  [`ldexpl`](https://en.cppreference.com/w/c/numeric/math/ldexp.html "c/numeric/math/ldexp")
lgamma  |  [`lgammaf`](https://en.cppreference.com/w/c/numeric/math/lgamma.html "c/numeric/math/lgamma") |  [`lgamma`](https://en.cppreference.com/w/c/numeric/math/lgamma.html "c/numeric/math/lgamma") |  [`lgammal`](https://en.cppreference.com/w/c/numeric/math/lgamma.html "c/numeric/math/lgamma")
llrint  |  [`llrintf`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") |  [`llrint`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") |  [`llrintl`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint")
llround  |  [`llroundf`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") |  [`llround`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") |  [`llroundl`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round")
log10  |  [`log10f`](https://en.cppreference.com/w/c/numeric/math/log10.html "c/numeric/math/log10") |  [`log10`](https://en.cppreference.com/w/c/numeric/math/log10.html "c/numeric/math/log10") |  [`log10l`](https://en.cppreference.com/w/c/numeric/math/log10.html "c/numeric/math/log10")
log1p  |  [`log1pf`](https://en.cppreference.com/w/c/numeric/math/log1p.html "c/numeric/math/log1p") |  [`log1p`](https://en.cppreference.com/w/c/numeric/math/log1p.html "c/numeric/math/log1p") |  [`log1pl`](https://en.cppreference.com/w/c/numeric/math/log1p.html "c/numeric/math/log1p")
log2  |  [`log2f`](https://en.cppreference.com/w/c/numeric/math/log2.html "c/numeric/math/log2") |  [`log2`](https://en.cppreference.com/w/c/numeric/math/log2.html "c/numeric/math/log2") |  [`log2l`](https://en.cppreference.com/w/c/numeric/math/log2.html "c/numeric/math/log2")
logb  |  [`logbf`](https://en.cppreference.com/w/c/numeric/math/logb.html "c/numeric/math/logb") |  [`logb`](https://en.cppreference.com/w/c/numeric/math/logb.html "c/numeric/math/logb") |  [`logbl`](https://en.cppreference.com/w/c/numeric/math/logb.html "c/numeric/math/logb")
lrint  |  [`lrintf`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") |  [`lrint`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") |  [`lrintl`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint")
lround  |  [`lroundf`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") |  [`lround`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") |  [`lroundl`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round")
nearbyint  |  [`nearbyintf`](https://en.cppreference.com/w/c/numeric/math/nearbyint.html "c/numeric/math/nearbyint") |  [`nearbyint`](https://en.cppreference.com/w/c/numeric/math/nearbyint.html "c/numeric/math/nearbyint") |  [`nearbyintl`](https://en.cppreference.com/w/c/numeric/math/nearbyint.html "c/numeric/math/nearbyint")
nextafter  |  [`nextafterf`](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter") |  [`nextafter`](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter") |  [`nextafterl`](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter")
nexttoward  |  [`nexttowardf`](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter") |  [`nexttoward`](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter") |  [`nexttowardl`](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter")
remainder  |  [`remainderf`](https://en.cppreference.com/w/c/numeric/math/remainder.html "c/numeric/math/remainder") |  [`remainder`](https://en.cppreference.com/w/c/numeric/math/remainder.html "c/numeric/math/remainder") |  [`remainderl`](https://en.cppreference.com/w/c/numeric/math/remainder.html "c/numeric/math/remainder")
remquo  |  [`remquof`](https://en.cppreference.com/w/c/numeric/math/remquo.html "c/numeric/math/remquo") |  [`remquo`](https://en.cppreference.com/w/c/numeric/math/remquo.html "c/numeric/math/remquo") |  [`remquol`](https://en.cppreference.com/w/c/numeric/math/remquo.html "c/numeric/math/remquo")
rint  |  [`rintf`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") |  [`rint`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") |  [`rintl`](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint")
round  |  [`roundf`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") |  [`round`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") |  [`roundl`](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round")
scalbln  |  [`scalblnf`](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn") |  [`scalbln`](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn") |  [`scalblnl`](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn")
scalbn  |  [`scalbnf`](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn") |  [`scalbn`](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn") |  [`scalbnl`](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn")
tgamma  |  [`tgammaf`](https://en.cppreference.com/w/c/numeric/math/tgamma.html "c/numeric/math/tgamma") |  [`tgamma`](https://en.cppreference.com/w/c/numeric/math/tgamma.html "c/numeric/math/tgamma") |  [`tgammal`](https://en.cppreference.com/w/c/numeric/math/tgamma.html "c/numeric/math/tgamma")
trunc  |  [`truncf`](https://en.cppreference.com/w/c/numeric/math/trunc.html "c/numeric/math/trunc") |  [`trunc`](https://en.cppreference.com/w/c/numeric/math/trunc.html "c/numeric/math/trunc") |  [`truncl`](https://en.cppreference.com/w/c/numeric/math/trunc.html "c/numeric/math/trunc")
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=edit&section=3 "Edit section: Complex-only functions")] Complex-only functions
For all complex number functions that do not have real counterparts, a type-generic macro `cXXX` exists, which calls either of the variants of a complex function:
  * float [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) variant `cXXXf`
  * double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) variant `cXXX`
  * long double [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) variant `cXXXl`


The function to call is determined as follows:
  * If any of the arguments for the generic parameters is real, complex, or imaginary, then the appropriate complex function is called.

Type-generic
macro  | Complex function
variants
---|---
|  float |  double |  long double
carg  |  [`cargf`](https://en.cppreference.com/w/c/numeric/complex/carg.html "c/numeric/complex/carg") |  [`carg`](https://en.cppreference.com/w/c/numeric/complex/carg.html "c/numeric/complex/carg") |  [`cargl`](https://en.cppreference.com/w/c/numeric/complex/carg.html "c/numeric/complex/carg")
conj  |  [`conjf`](https://en.cppreference.com/w/c/numeric/complex/conj.html "c/numeric/complex/conj") |  [`conj`](https://en.cppreference.com/w/c/numeric/complex/conj.html "c/numeric/complex/conj") |  [`conjl`](https://en.cppreference.com/w/c/numeric/complex/conj.html "c/numeric/complex/conj")
creal  |  [`crealf`](https://en.cppreference.com/w/c/numeric/complex/creal.html "c/numeric/complex/creal") |  [`creal`](https://en.cppreference.com/w/c/numeric/complex/creal.html "c/numeric/complex/creal") |  [`creall`](https://en.cppreference.com/w/c/numeric/complex/creal.html "c/numeric/complex/creal")
cimag  |  [`cimagf`](https://en.cppreference.com/w/c/numeric/complex/cimag.html "c/numeric/complex/cimag") |  [`cimag`](https://en.cppreference.com/w/c/numeric/complex/cimag.html "c/numeric/complex/cimag") |  [`cimagl`](https://en.cppreference.com/w/c/numeric/complex/cimag.html "c/numeric/complex/cimag")
cproj  |  [`cprojf`](https://en.cppreference.com/w/c/numeric/complex/cproj.html "c/numeric/complex/cproj") |  [`cproj`](https://en.cppreference.com/w/c/numeric/complex/cproj.html "c/numeric/complex/cproj") |  [`cprojl`](https://en.cppreference.com/w/c/numeric/complex/cproj.html "c/numeric/complex/cproj")
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=edit&section=4 "Edit section: Example")] Example
Run this code
```
#include <stdio.h>
#include <tgmath.h>
 
int main(void)
{
    int i = 2;
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("sqrt(2) = %f\n", [sqrt](https://en.cppreference.com/w/c/numeric/math/sqrt.html)(i)); // argument type is int, calls sqrt
 
    float f = 0.5;
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("sin(0.5f) = %f\n", [sin](https://en.cppreference.com/w/c/numeric/math/sin.html)(f)); // argument type is float, calls sinf
 
    float [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) dc = 1 + 0.5*I;
    float [complex](https://en.cppreference.com/w/c/numeric/complex/complex.html) z = [sqrt](https://en.cppreference.com/w/c/numeric/math/sqrt.html)(dc); // argument type is float complex, calls csqrtf
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("sqrt(1 + 0.5i) = %f+%fi\n",
           [creal](https://en.cppreference.com/w/c/numeric/complex/creal.html)(z),  // argument type is float complex, calls crealf
           [cimag](https://en.cppreference.com/w/c/numeric/complex/cimag.html)(z)); // argument type is float complex, calls cimagf
}
```

Output:
```
sqrt(2) = 1.414214
sin(0.5f) = 0.479426
sqrt(1 + 0.5i) = 1.029086+0.242934i
```

###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=edit&section=5 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.25 Type-generic math <tgmath.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.25 Type-generic math <tgmath.h> (p: 272-273)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.25 Type-generic math <tgmath.h> (p: 373-375)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.22 Type-generic math <tgmath.h> (p: 335-337)


Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&oldid=180676](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&oldid=180676)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/numeric/tgmath.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/numeric/tgmath "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/numeric/tgmath "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&oldid=180676 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/numeric/tgmath&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Česky](http://cs.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Deutsch](http://de.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Español](http://es.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Français](http://fr.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Italiano](http://it.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [日本語](http://ja.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [한국어](http://ko.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Polski](http://pl.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Português](http://pt.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Русский](http://ru.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [Türkçe](http://tr.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")
  * [中文](http://zh.cppreference.com/w/c/numeric/tgmath "c/numeric/tgmath")


  * This page was last modified on 14 February 2025, at 20:41.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
