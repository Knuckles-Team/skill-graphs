## Contents
  * [1 Types](https://en.cppreference.com/w/c/numeric/math.html#Types)
  * [2 Constants](https://en.cppreference.com/w/c/numeric/math.html#Constants)
    * [2.1 Classification](https://en.cppreference.com/w/c/numeric/math.html#Classification)
  * [3 Functions](https://en.cppreference.com/w/c/numeric/math.html#Functions)
    * [3.1 Basic operations](https://en.cppreference.com/w/c/numeric/math.html#Basic_operations)
    * [3.2 Exponential functions](https://en.cppreference.com/w/c/numeric/math.html#Exponential_functions)
    * [3.3 Power functions](https://en.cppreference.com/w/c/numeric/math.html#Power_functions)
    * [3.4 Trigonometric functions](https://en.cppreference.com/w/c/numeric/math.html#Trigonometric_functions)
    * [3.5 Hyperbolic functions](https://en.cppreference.com/w/c/numeric/math.html#Hyperbolic_functions)
    * [3.6 Error and gamma functions](https://en.cppreference.com/w/c/numeric/math.html#Error_and_gamma_functions)
    * [3.7 Nearest integer floating-point operations](https://en.cppreference.com/w/c/numeric/math.html#Nearest_integer_floating-point_operations)
    * [3.8 Floating-point manipulation functions](https://en.cppreference.com/w/c/numeric/math.html#Floating-point_manipulation_functions)
    * [3.9 Classification and comparison](https://en.cppreference.com/w/c/numeric/math.html#Classification_and_comparison)
  * [4 References](https://en.cppreference.com/w/c/numeric/math.html#References)
  * [5 See also](https://en.cppreference.com/w/c/numeric/math.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&action=edit&section=1 "Edit section: Types")] Types
Defined in header `[`<stdlib.h>`](https://en.cppreference.com/w/c/header/stdlib.html "c/header/stdlib")`
---
[ div_t](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") |  structure type, return of the [div](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") function
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_div_t&action=edit)
[ ldiv_t](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") |  structure type, return of the [ldiv](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") function
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_ldiv_t&action=edit)
[ lldiv_t](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") (C99) |  structure type, return of the lldiv function
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_lldiv_t&action=edit)
Defined in header `[`<inttypes.h>`](https://en.cppreference.com/w/c/header/inttypes.html "c/header/inttypes")`
[ imaxdiv_t](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") (C99) |  structure type, return of the imaxdiv function
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_imaxdiv_t&action=edit)
Defined in header `[`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math")`
[ float_t](https://en.cppreference.com/w/c/numeric/math/float_t.html "c/numeric/math/float t") (C99) |  most efficient floating-point type at least as wide as float
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_float_t&action=edit)
[ double_t](https://en.cppreference.com/w/c/numeric/math/float_t.html "c/numeric/math/float t") (C99) |  most efficient floating-point type at least as wide as double
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_double_t&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&action=edit&section=2 "Edit section: Constants")] Constants
Defined in header `[`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math")`
---
[ HUGE_VALFHUGE_VALHUGE_VALL](https://en.cppreference.com/w/c/numeric/math/HUGE_VALL.html "c/numeric/math/HUGE VAL") (C99)(C99) |  indicates value too big to be representable (infinity) by float, double and long double respectively
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_HUGE_VAL&action=edit)
[ INFINITY](https://en.cppreference.com/w/c/numeric/math/INFINITY.html "c/numeric/math/INFINITY") (C99) |  evaluates to positive infinity or the value guaranteed to overflow a float
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_INFINITY&action=edit)
[ NAN](https://en.cppreference.com/w/c/numeric/math/NAN.html "c/numeric/math/NAN") (C99) |  evaluates to a quiet NaN of type float
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_NAN&action=edit)
[ FP_FAST_FMAFFP_FAST_FMAFP_FAST_FMAL](https://en.cppreference.com/w/c/numeric/math/fma.html "c/numeric/math/fma") (C99)(C99)(C99) |  indicates that the fma function generally executes about as fast as, or faster than, a multiply and an add of double operands
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_FP_FAST_FMA&action=edit)
[ FP_ILOGB0FP_ILOGBNAN](https://en.cppreference.com/w/c/numeric/math/ilogb.html "c/numeric/math/ilogb") (C99)(C99) |  evaluates to [ilogb](https://en.cppreference.com/w/c/numeric/math/ilogb.html)(x) if x is zero or NaN, respectively
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_FP_ILOGB0&action=edit)
[ math_errhandlingMATH_ERRNOMATH_ERREXCEPT](https://en.cppreference.com/w/c/numeric/math/math_errhandling.html "c/numeric/math/math errhandling") (C99)(C99)(C99) |  defines the error handling mechanism used by the common mathematical functions
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_math_errhandling&action=edit)
#####  Classification
[ FP_NORMALFP_SUBNORMALFP_ZEROFP_INFINITEFP_NAN](https://en.cppreference.com/w/c/numeric/math/FP_categories.html "c/numeric/math/FP categories") (C99)(C99)(C99)(C99)(C99) |  indicates a floating-point category
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_FP_categories&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&action=edit&section=3 "Edit section: Functions")] Functions
Defined in header `[`<stdlib.h>`](https://en.cppreference.com/w/c/header/stdlib.html "c/header/stdlib")`
---
[ abslabsllabs](https://en.cppreference.com/w/c/numeric/math/abs.html "c/numeric/math/abs") (C99) |  computes absolute value of an integral value (\\(\small{|x|}\\)|x|)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_abs&action=edit)
[ divldivlldiv](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") (C99) |  computes quotient and remainder of integer division
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_div&action=edit)
Defined in header `[`<inttypes.h>`](https://en.cppreference.com/w/c/header/inttypes.html "c/header/inttypes")`
[ imaxabs](https://en.cppreference.com/w/c/numeric/math/abs.html "c/numeric/math/abs") (C99) |  computes absolute value of an integral value (\\(\small{|x|}\\)|x|)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_imaxabs&action=edit)
[ imaxdiv](https://en.cppreference.com/w/c/numeric/math/div.html "c/numeric/math/div") (C99) |  computes quotient and remainder of integer division
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_imaxdiv&action=edit)
Defined in header `[`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math")`
#####  Basic operations
[ fabsfabsffabsl](https://en.cppreference.com/w/c/numeric/math/fabs.html "c/numeric/math/fabs") (C99)(C99) |  computes absolute value of a floating-point value (\\(\small{|x|}\\)|x|)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fabs&action=edit)
[ fmodfmodffmodl](https://en.cppreference.com/w/c/numeric/math/fmod.html "c/numeric/math/fmod") (C99)(C99) |  computes remainder of the floating-point division operation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fmod&action=edit)
[ remainderremainderfremainderl](https://en.cppreference.com/w/c/numeric/math/remainder.html "c/numeric/math/remainder") (C99)(C99)(C99) |  computes signed remainder of the floating-point division operation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_remainder&action=edit)
[ remquoremquofremquol](https://en.cppreference.com/w/c/numeric/math/remquo.html "c/numeric/math/remquo") (C99)(C99)(C99) |  computes signed remainder as well as the three last bits of the division operation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_remquo&action=edit)
[ fmafmaffmal](https://en.cppreference.com/w/c/numeric/math/fma.html "c/numeric/math/fma") (C99)(C99)(C99) |  computes fused multiply-add operation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fma&action=edit)
[ fmaxfmaxffmaxl](https://en.cppreference.com/w/c/numeric/math/fmax.html "c/numeric/math/fmax") (C99)(C99)(C99) |  determines larger of two floating-point values
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fmax&action=edit)
[ fminfminffminl](https://en.cppreference.com/w/c/numeric/math/fmin.html "c/numeric/math/fmin") (C99)(C99)(C99) |  determines smaller of two floating-point values
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fmin&action=edit)
[ fdimfdimffdiml](https://en.cppreference.com/w/c/numeric/math/fdim.html "c/numeric/math/fdim") (C99)(C99)(C99) |  determines positive difference of two floating-point values (\\({\small\max{(0, x-y)} }\\)max(0, x-y))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fdim&action=edit)
[ nannanfnanl](https://en.cppreference.com/w/c/numeric/math/nan.html "c/numeric/math/nan") (C99)(C99)(C99) |  returns a NaN (not-a-number)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fnan&action=edit)
#####  Exponential functions
[ expexpfexpl](https://en.cppreference.com/w/c/numeric/math/exp.html "c/numeric/math/exp") (C99)(C99) |  computes _e_ raised to the given power (\\({\small e^x}\\)ex)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_exp&action=edit)
[ exp2exp2fexp2l](https://en.cppreference.com/w/c/numeric/math/exp2.html "c/numeric/math/exp2") (C99)(C99)(C99) |  computes _2_ raised to the given power (\\({\small 2^x}\\)2x)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_exp2&action=edit)
[ expm1expm1fexpm1l](https://en.cppreference.com/w/c/numeric/math/expm1.html "c/numeric/math/expm1") (C99)(C99)(C99) |  computes _e_ raised to the given power, minus one (\\({\small e^x-1}\\)ex-1)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_expm1&action=edit)
[ loglogflogl](https://en.cppreference.com/w/c/numeric/math/log.html "c/numeric/math/log") (C99)(C99) |  computes natural (base-_e_) logarithm (\\({\small \ln{x} }\\)ln(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_log&action=edit)
[ log10log10flog10l](https://en.cppreference.com/w/c/numeric/math/log10.html "c/numeric/math/log10") (C99)(C99) |  computes common (base-_10_) logarithm (\\({\small \log_{10}{x} }\\)log10(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_log10&action=edit)
[ log2log2flog2l](https://en.cppreference.com/w/c/numeric/math/log2.html "c/numeric/math/log2") (C99)(C99)(C99) |  computes base-2 logarithm (\\({\small \log_{2}{x} }\\)log2(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_log2&action=edit)
[ log1plog1pflog1pl](https://en.cppreference.com/w/c/numeric/math/log1p.html "c/numeric/math/log1p") (C99)(C99)(C99) |  computes natural (base-_e_) logarithm of 1 plus the given number (\\({\small \ln{(1+x)} }\\)ln(1+x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_log1p&action=edit)
#####  Power functions
[ powpowfpowl](https://en.cppreference.com/w/c/numeric/math/pow.html "c/numeric/math/pow") (C99)(C99) |  computes a number raised to the given power (\\(\small{x^y}\\)xy)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_pow&action=edit)
[ sqrtsqrtfsqrtl](https://en.cppreference.com/w/c/numeric/math/sqrt.html "c/numeric/math/sqrt") (C99)(C99) |  computes square root (\\(\small{\sqrt{x} }\\)√x)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_sqrt&action=edit)
[ cbrtcbrtfcbrtl](https://en.cppreference.com/w/c/numeric/math/cbrt.html "c/numeric/math/cbrt") (C99)(C99)(C99) |  computes cube root (\\(\small{\sqrt[3]{x} }\\)3√x)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_cbrt&action=edit)
[ hypothypotfhypotl](https://en.cppreference.com/w/c/numeric/math/hypot.html "c/numeric/math/hypot") (C99)(C99)(C99) |  computes square root of the sum of the squares of two given numbers (\\(\scriptsize{\sqrt{x^2+y^2} }\\)√x2
+y2
)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_hypot&action=edit)
#####  Trigonometric functions
[ sinsinfsinl](https://en.cppreference.com/w/c/numeric/math/sin.html "c/numeric/math/sin") (C99)(C99) |  computes sine (\\({\small\sin{x} }\\)sin(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_sin&action=edit)
[ coscosfcosl](https://en.cppreference.com/w/c/numeric/math/cos.html "c/numeric/math/cos") (C99)(C99) |  computes cosine (\\({\small\cos{x} }\\)cos(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_cos&action=edit)
[ tantanftanl](https://en.cppreference.com/w/c/numeric/math/tan.html "c/numeric/math/tan") (C99)(C99) |  computes tangent (\\({\small\tan{x} }\\)tan(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_tan&action=edit)
[ asinasinfasinl](https://en.cppreference.com/w/c/numeric/math/asin.html "c/numeric/math/asin") (C99)(C99) |  computes arc sine (\\({\small\arcsin{x} }\\)arcsin(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_asin&action=edit)
[ acosacosfacosl](https://en.cppreference.com/w/c/numeric/math/acos.html "c/numeric/math/acos") (C99)(C99) |  computes arc cosine (\\({\small\arccos{x} }\\)arccos(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_acos&action=edit)
[ atanatanfatanl](https://en.cppreference.com/w/c/numeric/math/atan.html "c/numeric/math/atan") (C99)(C99) |  computes arc tangent (\\({\small\arctan{x} }\\)arctan(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_atan&action=edit)
[ atan2atan2fatan2l](https://en.cppreference.com/w/c/numeric/math/atan2.html "c/numeric/math/atan2") (C99)(C99) |  computes arc tangent, using signs to determine quadrants
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_atan2&action=edit)
#####  Hyperbolic functions
[ sinhsinhfsinhl](https://en.cppreference.com/w/c/numeric/math/sinh.html "c/numeric/math/sinh") (C99)(C99) |  computes hyperbolic sine (\\({\small\sinh{x} }\\)sinh(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_sinh&action=edit)
[ coshcoshfcoshl](https://en.cppreference.com/w/c/numeric/math/cosh.html "c/numeric/math/cosh") (C99)(C99) |  computes hyperbolic cosine (\\({\small\cosh{x} }\\)cosh(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_cosh&action=edit)
[ tanhtanhftanhl](https://en.cppreference.com/w/c/numeric/math/tanh.html "c/numeric/math/tanh") (C99)(C99) |  computes hyperbolic tangent (\\({\small\tanh{x} }\\)tanh(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_tanh&action=edit)
[ asinhasinhfasinhl](https://en.cppreference.com/w/c/numeric/math/asinh.html "c/numeric/math/asinh") (C99)(C99)(C99) |  computes inverse hyperbolic sine (\\({\small\operatorname{arsinh}{x} }\\)arsinh(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_asinh&action=edit)
[ acoshacoshfacoshl](https://en.cppreference.com/w/c/numeric/math/acosh.html "c/numeric/math/acosh") (C99)(C99)(C99) |  computes inverse hyperbolic cosine (\\({\small\operatorname{arcosh}{x} }\\)arcosh(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_acosh&action=edit)
[ atanhatanhfatanhl](https://en.cppreference.com/w/c/numeric/math/atanh.html "c/numeric/math/atanh") (C99)(C99)(C99) |  computes inverse hyperbolic tangent (\\({\small\operatorname{artanh}{x} }\\)artanh(x))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_atanh&action=edit)
#####  Error and gamma functions
[ erferfferfl](https://en.cppreference.com/w/c/numeric/math/erf.html "c/numeric/math/erf") (C99)(C99)(C99) |  computes error function
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_erf&action=edit)
[ erfcerfcferfcl](https://en.cppreference.com/w/c/numeric/math/erfc.html "c/numeric/math/erfc") (C99)(C99)(C99) |  computes complementary error function
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_erfc&action=edit)
[ tgammatgammaftgammal](https://en.cppreference.com/w/c/numeric/math/tgamma.html "c/numeric/math/tgamma") (C99)(C99)(C99) |  computes gamma function
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_tgamma&action=edit)
[ lgammalgammaflgammal](https://en.cppreference.com/w/c/numeric/math/lgamma.html "c/numeric/math/lgamma") (C99)(C99)(C99) |  computes natural (base-_e_) logarithm of the gamma function
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_lgamma&action=edit)
#####  Nearest integer floating-point operations
[ ceilceilfceill](https://en.cppreference.com/w/c/numeric/math/ceil.html "c/numeric/math/ceil") (C99)(C99) |  computes smallest integer not less than the given value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_ceil&action=edit)
[ floorfloorffloorl](https://en.cppreference.com/w/c/numeric/math/floor.html "c/numeric/math/floor") (C99)(C99) |  computes largest integer not greater than the given value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_floor&action=edit)
[ trunctruncftruncl](https://en.cppreference.com/w/c/numeric/math/trunc.html "c/numeric/math/trunc") (C99)(C99)(C99) |  rounds to nearest integer not greater in magnitude than the given value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_trunc&action=edit)
[ roundroundfroundllroundlroundflroundlllroundllroundfllroundl](https://en.cppreference.com/w/c/numeric/math/round.html "c/numeric/math/round") (C99)(C99)(C99)(C99)(C99)(C99)(C99)(C99)(C99) |  rounds to nearest integer, rounding away from zero in halfway cases
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_round&action=edit)
[ nearbyintnearbyintfnearbyintl](https://en.cppreference.com/w/c/numeric/math/nearbyint.html "c/numeric/math/nearbyint") (C99)(C99)(C99) |  rounds to an integer using current rounding mode
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_nearbyint&action=edit)
[ rintrintfrintllrintlrintflrintlllrintllrintfllrintl](https://en.cppreference.com/w/c/numeric/math/rint.html "c/numeric/math/rint") (C99)(C99)(C99)(C99)(C99)(C99)(C99)(C99)(C99) |  rounds to an integer using current rounding mode with
exception if the result differs
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_rint&action=edit)
#####  Floating-point manipulation functions
[ frexpfrexpffrexpl](https://en.cppreference.com/w/c/numeric/math/frexp.html "c/numeric/math/frexp") (C99)(C99) |  breaks a number into significand and a power of 2
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_frexp&action=edit)
[ ldexpldexpfldexpl](https://en.cppreference.com/w/c/numeric/math/ldexp.html "c/numeric/math/ldexp") (C99)(C99) |  multiplies a number by 2 raised to a power
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_ldexp&action=edit)
[ modfmodffmodfl](https://en.cppreference.com/w/c/numeric/math/modf.html "c/numeric/math/modf") (C99)(C99) |  breaks a number into integer and fractional parts
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_modf&action=edit)
[ scalbnscalbnfscalbnlscalblnscalblnfscalblnl](https://en.cppreference.com/w/c/numeric/math/scalbn.html "c/numeric/math/scalbn") (C99)(C99)(C99)(C99)(C99)(C99) |  computes efficiently a number times [FLT_RADIX](https://en.cppreference.com/w/c/types/limits.html "c/types/limits") raised to a power
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_scalbn&action=edit)
[ ilogbilogbfilogbl](https://en.cppreference.com/w/c/numeric/math/ilogb.html "c/numeric/math/ilogb") (C99)(C99)(C99) |  extracts exponent of the given number
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_ilogb&action=edit)
[ logblogbflogbl](https://en.cppreference.com/w/c/numeric/math/logb.html "c/numeric/math/logb") (C99)(C99)(C99) |  extracts exponent of the given number
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_logb&action=edit)
[ nextafternextafterfnextafterlnexttowardnexttowardfnexttowardl](https://en.cppreference.com/w/c/numeric/math/nexttoward.html "c/numeric/math/nextafter") (C99)(C99)(C99)(C99)(C99)(C99) |  determines next representable floating-point value towards the given value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_nextafter&action=edit)
[ copysigncopysignfcopysignl](https://en.cppreference.com/w/c/numeric/math/copysign.html "c/numeric/math/copysign") (C99)(C99)(C99) |  produces a value with the magnitude of a given value and the sign of another given value
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_copysign&action=edit)
#####  Classification and comparison
[ fpclassify](https://en.cppreference.com/w/c/numeric/math/fpclassify.html "c/numeric/math/fpclassify") (C99) |  classifies the given floating-point value
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_fpclassify&action=edit)
[ isfinite](https://en.cppreference.com/w/c/numeric/math/isfinite.html "c/numeric/math/isfinite") (C99) |  checks if the given number has finite value
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isfinite&action=edit)
[ isinf](https://en.cppreference.com/w/c/numeric/math/isinf.html "c/numeric/math/isinf") (C99) |  checks if the given number is infinite
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isinf&action=edit)
[ isnan](https://en.cppreference.com/w/c/numeric/math/isnan.html "c/numeric/math/isnan") (C99) |  checks if the given number is NaN
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isnan&action=edit)
[ isnormal](https://en.cppreference.com/w/c/numeric/math/isnormal.html "c/numeric/math/isnormal") (C99) |  checks if the given number is normal
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isnormal&action=edit)
[ signbit](https://en.cppreference.com/w/c/numeric/math/signbit.html "c/numeric/math/signbit") (C99) |  checks if the given number is negative
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_signbit&action=edit)
[ isgreater](https://en.cppreference.com/w/c/numeric/math/isgreater.html "c/numeric/math/isgreater") (C99) |  checks if the first floating-point argument is greater than the second
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isgreater&action=edit)
[ isgreaterequal](https://en.cppreference.com/w/c/numeric/math/isgreaterequal.html "c/numeric/math/isgreaterequal") (C99) |  checks if the first floating-point argument is greater or equal than the second
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isgreaterequal&action=edit)
[ isless](https://en.cppreference.com/w/c/numeric/math/isless.html "c/numeric/math/isless") (C99) |  checks if the first floating-point argument is less than the second
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isless&action=edit)
[ islessequal](https://en.cppreference.com/w/c/numeric/math/islessequal.html "c/numeric/math/islessequal") (C99) |  checks if the first floating-point argument is less or equal than the second
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_islessequal&action=edit)
[ islessgreater](https://en.cppreference.com/w/c/numeric/math/islessgreater.html "c/numeric/math/islessgreater") (C99) |  checks if the first floating-point argument is less or greater than the second
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_islessgreater&action=edit)
[ isunordered](https://en.cppreference.com/w/c/numeric/math/isunordered.html "c/numeric/math/isunordered") (C99) |  checks if two floating-point values are unordered
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/math/dsc_isunordered&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&action=edit&section=4 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.8 Format conversion of integer types <inttypes.h> (p: TBD)


  * 7.12 Mathematics <math.h> (p: TBD)


  * 7.22 General utilities <stdlib.h> (p: TBD)


  * 7.31.5 Format conversion of integer types <inttypes.h> (p: TBD)


  * 7.31.12 General utilities <stdlib.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.8 Format conversion of integer types <inttypes.h> (p: 158-160)


  * 7.12 Mathematics <math.h> (p: 169-190)


  * 7.22 General utilities <stdlib.h> (p: 248-262)


  * 7.31.5 Format conversion of integer types <inttypes.h> (p: 332)


  * 7.31.12 General utilities <stdlib.h> (p: 333)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.8 Format conversion of integer types <inttypes.h> (p: 217-220)


  * 7.12 Mathematics <math.h> (p: 231-261)


  * 7.22 General utilities <stdlib.h> (p: 340-360)


  * 7.31.5 Format conversion of integer types <inttypes.h> (p: 455)


  * 7.31.12 General utilities <stdlib.h> (p: 456)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.8 Format conversion of integer types <inttypes.h> (p: 198-201)


  * 7.12 Mathematics <math.h> (p: 212-242)


  * 7.20 General utilities <stdlib.h> (p: 306-324)


  * 7.26.4 Format conversion of integer types <inttypes.h> (p: 401)


  * 7.26.10 General utilities <stdlib.h> (p: 402)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.5 MATHEMATICS <math.h>


  * 4.10 GENERAL UTILITIES <stdlib.h>


  * 4.13.4 Mathematics <math.h>


  * 7.13.7 General utilities <stdlib.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&action=edit&section=5 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/numeric/math.html "cpp/numeric/math") for Common mathematical functions
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&oldid=180095](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&oldid=180095)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/numeric/math.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/numeric/math "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/numeric/math "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&oldid=180095 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/numeric/math&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Česky](http://cs.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Deutsch](http://de.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Español](http://es.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Français](http://fr.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Italiano](http://it.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [日本語](http://ja.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [한국어](http://ko.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Polski](http://pl.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Português](http://pt.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Русский](http://ru.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [Türkçe](http://tr.cppreference.com/w/c/numeric/math "c/numeric/math")
  * [中文](http://zh.cppreference.com/w/c/numeric/math "c/numeric/math")


  * This page was last modified on 3 February 2025, at 16:32.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
