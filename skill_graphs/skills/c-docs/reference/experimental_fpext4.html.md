##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fexperimental%2Ffpext4&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fexperimental%2Ffpext4 "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/experimental/fpext4.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/experimental/fpext4&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/experimental/fpext4.html)
##### Views
  * [View](https://en.cppreference.com/w/c/experimental/fpext4.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/experimental/fpext4.html)
# Floating-point extensions part 4: supplementary functions
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [experimental](https://en.cppreference.com/w/c/experimental.html "c/experimental")
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
[ Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[ Extensions for embedded processors](https://en.cppreference.com/mwiki/index.php?title=c/experimental/embedded&action=edit&redlink=1 "c/experimental/embedded \(page does not exist\)")
---
[ Dynamic memory extensions](https://en.cppreference.com/w/c/experimental/dynamic.html "c/experimental/dynamic")
[ Floating-point extensions part 1: Binary floating-point](https://en.cppreference.com/w/c/experimental/fpext1.html "c/experimental/fpext1")
**Floating-point extensions part 4: Supplementary functions**
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/navbar_content&action=edit)
**Floating-point extensions part 4: Supplementary functions**
[Template:c/experimental/fpext4/navbar content](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/navbar_content&action=edit&redlink=1 "Template:c/experimental/fpext4/navbar content \(page does not exist\)")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/navbar_content&action=edit)
Floating-point extensions for C - Part 4: Supplementary functions, ISO/IEC TS 18661-4:2015, defines the following new components for the C standard library, as recommended by ISO/IEC/IEEE 60559:2011 (the current revision of IEEE-754).
Supplemenatary mathematical functions listed below are merged into C2x standard.
|
## Contents
  * [1 Predefined feature test macros](https://en.cppreference.com/w/c/experimental/fpext4.html#Predefined_feature_test_macros)
  * [2 Supplementary mathematical functions](https://en.cppreference.com/w/c/experimental/fpext4.html#Supplementary_mathematical_functions)
  * [3 Reduction functions](https://en.cppreference.com/w/c/experimental/fpext4.html#Reduction_functions)
  * [4 Correctly-rounded version of functions](https://en.cppreference.com/w/c/experimental/fpext4.html#Correctly-rounded_version_of_functions)
  * [5 Complex version of functions](https://en.cppreference.com/w/c/experimental/fpext4.html#Complex_version_of_functions)
  * [6 Notes](https://en.cppreference.com/w/c/experimental/fpext4.html#Notes)


---
#####  Predefined feature test macros
__STDC_IEC_60559_FUNCS__ |  integer constant of type long and value 201506L
(macro constant)
#####  Supplementary mathematical functions
Defined in header `[`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math")`
[ exp2m1 exp2m1f exp2m1lexp2m1fN exp2m1fNxexp2m1dN exp2m1dNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/exp2m1&action=edit&redlink=1 "c/experimental/fpext4/exp2m1 \(page does not exist\)") (FP Ext 4 TS) |  compute 2x
-1
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_exp2m1&action=edit)
[ exp10 exp10f exp10lexp10fN exp10fNxexp10dN exp10dNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/exp10&action=edit&redlink=1 "c/experimental/fpext4/exp10 \(page does not exist\)") (FP Ext 4 TS) |  compute 10x

(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_exp10&action=edit)
[ exp10m1 exp10m1f exp10m1lexp10m1fN exp10m1fNxexp10m1dN exp10m1dNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/exp10m1&action=edit&redlink=1 "c/experimental/fpext4/exp10m1 \(page does not exist\)") (FP Ext 4 TS) |  compute 10x
-1
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_exp10m1&action=edit)
[ logp1 logp1f logp1llogp1fN logp1fNxlogp1dN logp1dNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/logp1&action=edit&redlink=1 "c/experimental/fpext4/logp1 \(page does not exist\)") (FP Ext 4 TS) |  compute ln(1+x) (same as [log1p](https://en.cppreference.com/w/c/numeric/math/log1p.html "c/numeric/math/log1p"))
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_logp1&action=edit)
[ log2p1 log2p1f log2p1llog2p1fN log2p1fNxlog2p1dN log2p1dNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/log2p1&action=edit&redlink=1 "c/experimental/fpext4/log2p1 \(page does not exist\)") (FP Ext 4 TS) |  compute log2(1+x)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_log2p1&action=edit)
[ log10p1 log10p1f log10p1llog10p1fN log10p1fNxlog10p1dN log10p1dNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/log10p1&action=edit&redlink=1 "c/experimental/fpext4/log10p1 \(page does not exist\)") (FP Ext 4 TS) |  compute log10(1+x)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_log10p1&action=edit)
[ rsqrt rsqrtf rsqrtlrsqrtfN rsqrtfNxrsqrtdN rsqrtdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/rsqrt&action=edit&redlink=1 "c/experimental/fpext4/rsqrt \(page does not exist\)") (FP Ext 4 TS) |  compute the inverse square root x-1/2

(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_rsqrt&action=edit)
[ compoundn compoundnf compoundnlcompoundnfN compoundnfNxcompoundndN compoundndNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/compoundn&action=edit&redlink=1 "c/experimental/fpext4/compoundn \(page does not exist\)") (FP Ext 4 TS) |  compute compound interest, (1+x)n

(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_compoundn&action=edit)
[ rootn rootnf rootnlrootnfN rootnfNxrootndN rootndNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/rootn&action=edit&redlink=1 "c/experimental/fpext4/rootn \(page does not exist\)") (FP Ext 4 TS) |  compute the nth root of x, x1/n

(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_rootn&action=edit)
[ pown pownf pownlpownfN pownfNxpowndN powndNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/pown&action=edit&redlink=1 "c/experimental/fpext4/pown \(page does not exist\)") (FP Ext 4 TS) |  compute x raised to the nth power, where n is integer
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_pown&action=edit)
[ powr powrf powrlpowrfN powrfNxpowrdN powrdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/powr&action=edit&redlink=1 "c/experimental/fpext4/powr \(page does not exist\)") (FP Ext 4 TS) |  compute x raised to the y power, xy

(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_powr&action=edit)
[ acospi acospif acospilacospifN acospifNxacospidN acospidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/acospi&action=edit&redlink=1 "c/experimental/fpext4/acospi \(page does not exist\)") (FP Ext 4 TS) |  compute arccos(x)/π (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_acospi&action=edit)
[ asinpi asinpif asinpilasinpifN asinpifNxasinpidN asinpidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/asinpi&action=edit&redlink=1 "c/experimental/fpext4/asinpi \(page does not exist\)") (FP Ext 4 TS) |  compute arcsin(x)/π (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_asinpi&action=edit)
[ atanpi atanpif atanpilatanpifN atanpifNxatanpidN atanpidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/atanpi&action=edit&redlink=1 "c/experimental/fpext4/atanpi \(page does not exist\)") (FP Ext 4 TS) |  compute arctan(x)/π (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_atanpi&action=edit)
[ atan2pi atan2pif atan2pilatan2pifN atan2pifNxatan2pidN atan2pidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/atan2pi&action=edit&redlink=1 "c/experimental/fpext4/atan2pi \(page does not exist\)") (FP Ext 4 TS) |  compute arctan(y/x)/π (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_atan2pi&action=edit)
[ cospi cospif cospilcospifN cospifNxcospidN cospidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/cospi&action=edit&redlink=1 "c/experimental/fpext4/cospi \(page does not exist\)") (FP Ext 4 TS) |  compute cos(πx) (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_cospi&action=edit)
[ sinpi sinpif sinpilsinpifN sinpifNxsinpidN sinpidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/sinpi&action=edit&redlink=1 "c/experimental/fpext4/sinpi \(page does not exist\)") (FP Ext 4 TS) |  compute sin(πx) (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_sinpi&action=edit)
[ tanpi tanpif tanpiltanpifN tanpifNxtanpidN tanpidNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/tanpi&action=edit&redlink=1 "c/experimental/fpext4/tanpi \(page does not exist\)") (FP Ext 4 TS) |  compute tan(πx) (measuring the angle in half-revolutions)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_tanpi&action=edit)
#####  Reduction functions
Defined in header `[`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math")`
[ reduc_sum reduc_sumf reduc_sumlreduc_sumfN reduc_sumfNxreduc_sumdN reduc_sumdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/reduc_sum&action=edit&redlink=1 "c/experimental/fpext4/reduc sum \(page does not exist\)") (FP Ext 4 TS) |  compute the sum of n members of an array
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_reduc_sum&action=edit)
[ reduc_sumabs reduc_sumabsf reduc_sumabslreduc_sumabsfN reduc_sumabsfNxreduc_sumabsdN reduc_sumabsdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/reduc_sumabs&action=edit&redlink=1 "c/experimental/fpext4/reduc sumabs \(page does not exist\)") (FP Ext 4 TS) |  compute the sum of the absolute values of n members of an array
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_reduc_sumabs&action=edit)
[ reduc_sumsq reduc_sumsqf reduc_sumsqlreduc_sumsqfN reduc_sumsqfNxreduc_sumsqdN reduc_sumsqdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/reduc_sumsq&action=edit&redlink=1 "c/experimental/fpext4/reduc sumsq \(page does not exist\)") (FP Ext 4 TS) |  compute the sum of squares of n members of an array
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_reduc_sumsq&action=edit)
[ reduc_sumprod reduc_sumprodf reduc_sumprodlreduc_sumprodfN reduc_sumprodfNxreduc_sumproddN reduc_sumproddNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/reduc_sumprod&action=edit&redlink=1 "c/experimental/fpext4/reduc sumprod \(page does not exist\)") (FP Ext 4 TS) |  compute the dot product between n members of two arrays
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_reduc_sumprod&action=edit)
[ scaled_prod scaled_prodf scaled_prodlscaled_prodfN scaled_prodfNxscaled_proddN scaled_proddNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/scaled_prod&action=edit&redlink=1 "c/experimental/fpext4/scaled prod \(page does not exist\)") (FP Ext 4 TS) |  compute the product of n members of an array as a scaled value and a scale factor
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_scaled_prod&action=edit)
[ scaled_prodsum scaled_prodsumf scaled_prodsumlscaled_prodsumfN scaled_prodsumfNxscaled_prodsumdN scaled_prodsumdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/scaled_prodsum&action=edit&redlink=1 "c/experimental/fpext4/scaled prodsum \(page does not exist\)") (FP Ext 4 TS) |  compute the dot product of n members of two arrays as a scaled value and a scale factor
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_scaled_prodsum&action=edit)
[ scaled_proddiff scaled_proddifff scaled_proddifflscaled_proddifffN scaled_proddifffNxscaled_proddiffdN scaled_proddiffdNx](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4/scaled_proddiff&action=edit&redlink=1 "c/experimental/fpext4/scaled proddiff \(page does not exist\)") (FP Ext 4 TS) |  compute the product of the differences between corresponding n members of two arrays as a scaled value and a scale factor
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/fpext4/dsc_scaled_proddiff&action=edit)
#####  Correctly-rounded version of functions
Defined in header `[`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math")`
crexp(optional) (FP Ext 4 TS) |  correctly-rounded version of [exp](https://en.cppreference.com/w/c/numeric/math/exp.html "c/numeric/math/exp")
(function)
crexpm1(optional) (FP Ext 4 TS) |  correctly-rounded version of [expm1](https://en.cppreference.com/w/c/numeric/math/expm1.html "c/numeric/math/expm1")
(function)
crexp2(optional) (FP Ext 4 TS) |  correctly-rounded version of [exp2](https://en.cppreference.com/w/c/numeric/math/exp2.html "c/numeric/math/exp2")
(function)
crexp2m1(optional) (FP Ext 4 TS) |  correctly-rounded version of exp2m1
(function)
crexp10(optional) (FP Ext 4 TS) |  correctly-rounded version of exp10
(function)
crexp10m1(optional) (FP Ext 4 TS) |  correctly-rounded version of exp10m1
(function)
crlog(optional) (FP Ext 4 TS) |  correctly-rounded version of [log](https://en.cppreference.com/w/c/numeric/math/log.html "c/numeric/math/log")
(function)
crlog2(optional) (FP Ext 4 TS) |  correctly-rounded version of log2
(function)
crlog10(optional) (FP Ext 4 TS) |  correctly-rounded version of [log10](https://en.cppreference.com/w/c/numeric/math/log10.html "c/numeric/math/log10")
(function)
crlog1p(optional) (FP Ext 4 TS) |  correctly-rounded version of [log1p](https://en.cppreference.com/w/c/numeric/math/log1p.html "c/numeric/math/log1p")
(function)
crlogp1(optional) (FP Ext 4 TS) |  correctly-rounded version of logp1
(function)
crlog2p1(optional) (FP Ext 4 TS) |  correctly-rounded version of log2p1
(function)
crlog10p1(optional) (FP Ext 4 TS) |  correctly-rounded version of log10p1
(function)
crrsqrt(optional) (FP Ext 4 TS) |  correctly-rounded version of rsqrt
(function)
crcompoundn(optional) (FP Ext 4 TS) |  correctly-rounded version of compoundn
(function)
crrootn(optional) (FP Ext 4 TS) |  correctly-rounded version of rootn
(function)
crpown(optional) (FP Ext 4 TS) |  correctly-rounded version of pown
(function)
crpow(optional) (FP Ext 4 TS) |  correctly-rounded version of [pow](https://en.cppreference.com/w/c/numeric/math/pow.html "c/numeric/math/pow")
(function)
crpowr(optional) (FP Ext 4 TS) |  correctly-rounded version of powr
(function)
crsin(optional) (FP Ext 4 TS) |  correctly-rounded version of [sin](https://en.cppreference.com/w/c/numeric/math/sin.html "c/numeric/math/sin")
(function)
crcos(optional) (FP Ext 4 TS) |  correctly-rounded version of [cos](https://en.cppreference.com/w/c/numeric/math/cos.html "c/numeric/math/cos")
(function)
crtan(optional) (FP Ext 4 TS) |  correctly-rounded version of [tan](https://en.cppreference.com/w/c/numeric/math/tan.html "c/numeric/math/tan")
(function)
crsinpi(optional) (FP Ext 4 TS) |  correctly-rounded version of sinpi
(function)
crcospi(optional) (FP Ext 4 TS) |  correctly-rounded version of cospi
(function)
crtanpi(optional) (FP Ext 4 TS) |  correctly-rounded version of tanpi
(function)
crasinpi(optional) (FP Ext 4 TS) |  correctly-rounded version of asinpi
(function)
cracospi(optional) (FP Ext 4 TS) |  correctly-rounded version of acospi
(function)
cracospi(optional) (FP Ext 4 TS) |  correctly-rounded version of acospi
(function)
cratanpi(optional) (FP Ext 4 TS) |  correctly-rounded version of atanpi
(function)
cratan2pi(optional) (FP Ext 4 TS) |  correctly-rounded version of atan2pi
(function)
crasin(optional) (FP Ext 4 TS) |  correctly-rounded version of [asin](https://en.cppreference.com/w/c/numeric/math/asin.html "c/numeric/math/asin")
(function)
cracos(optional) (FP Ext 4 TS) |  correctly-rounded version of [acos](https://en.cppreference.com/w/c/numeric/math/acos.html "c/numeric/math/acos")
(function)
cratan(optional) (FP Ext 4 TS) |  correctly-rounded version of [atan](https://en.cppreference.com/w/c/numeric/math/atan.html "c/numeric/math/atan")
(function)
cratan2(optional) (FP Ext 4 TS) |  correctly-rounded version of [atan2](https://en.cppreference.com/w/c/numeric/math/atan2.html "c/numeric/math/atan2")
(function)
crsinh(optional) (FP Ext 4 TS) |  correctly-rounded version of [sinh](https://en.cppreference.com/w/c/numeric/math/sinh.html "c/numeric/math/sinh")
(function)
crcosh(optional) (FP Ext 4 TS) |  correctly-rounded version of [cosh](https://en.cppreference.com/w/c/numeric/math/cosh.html "c/numeric/math/cosh")
(function)
crtanh(optional) (FP Ext 4 TS) |  correctly-rounded version of [tanh](https://en.cppreference.com/w/c/numeric/math/tanh.html "c/numeric/math/tanh")
(function)
crasinh(optional) (FP Ext 4 TS) |  correctly-rounded version of [asinh](https://en.cppreference.com/w/c/numeric/math/asinh.html "c/numeric/math/asinh")
(function)
cracosh(optional) (FP Ext 4 TS) |  correctly-rounded version of [acosh](https://en.cppreference.com/w/c/numeric/math/acosh.html "c/numeric/math/acosh")
(function)
cratanh(optional) (FP Ext 4 TS) |  correctly-rounded version of [atanh](https://en.cppreference.com/w/c/numeric/math/atanh.html "c/numeric/math/atanh")
(function)
crhypot(optional) (FP Ext 4 TS) |  correctly-rounded version of [hypot](https://en.cppreference.com/w/c/numeric/math/hypot.html "c/numeric/math/hypot")
(function)
#####  Complex version of functions
Defined in header `[`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex")`
cexp2m1(optional) (FP Ext 4 TS) |  complex number version of exp2m1
(function)
cexp10(optional) (FP Ext 4 TS) |  complex number version of exp10
(function)
cexp10m1(optional) (FP Ext 4 TS) |  complex number version of exp10m1
(function)
clogp1(optional) (FP Ext 4 TS) |  complex number version of logp1
(function)
clog2p1(optional) (FP Ext 4 TS) |  complex number version of log2p1
(function)
clog10p1(optional) (FP Ext 4 TS) |  complex number version of log10p1
(function)
crsqrt (optional) (FP Ext 4 TS) |  complex number version of rsqrt
(function)
ccompoundn (optional) (FP Ext 4 TS) |  complex number version of compoundn
(function)
crootn(optional) (FP Ext 4 TS) |  complex number version of rootn
(function)
cpown (optional) (FP Ext 4 TS) |  complex number version of pown
(function)
cpowr(optional) (FP Ext 4 TS) |  complex number version of powr
(function)
cacospi(optional) (FP Ext 4 TS) |  complex number version of acospi
(function)
casinpi(optional) (FP Ext 4 TS) |  complex number version of asinpi
(function)
catanpi(optional) (FP Ext 4 TS) |  complex number version of atanpi
(function)
ccospi(optional) (FP Ext 4 TS) |  complex number version of cospi
(function)
csinpi(optional) (FP Ext 4 TS) |  complex number version of sinpi
(function)
ctanpi(optional) (FP Ext 4 TS) |  complex number version of tanpi
(function)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&action=edit&section=1 "Edit section: Notes")] Notes
All functions added to the C library by this extension are only declared if a macro __STDC_WANT_IEC_60559_FUNCS_EXT__ is defined before math.h is included.
The decimal floating-point variants of every function are only defined if __STDC_WANT_IEC_60559_DFP_EXT__ is also defined before math.h is included.
The extended precision variants of every function are only defined if __STDC_WANT_IEC_60559_TYPES_EXT__ is defined before math.h is included.
The correctly-rounded versions of all functions (with the cr- prefix) are optional.
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&oldid=114957](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&oldid=114957)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/experimental/fpext4.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/experimental/fpext4 "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/experimental/fpext4 "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&oldid=114957 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/experimental/fpext4&action=info)


  * In other languages


  * [日本語](http://ja.cppreference.com/w/c/experimental/fpext4 "c/experimental/fpext4")
  * [中文](http://zh.cppreference.com/w/c/experimental/fpext4 "c/experimental/fpext4")


  * This page was last modified on 11 January 2020, at 05:03.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
