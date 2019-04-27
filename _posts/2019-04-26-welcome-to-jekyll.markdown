---
layout: post
title:  "first post"
date:   2019-04-26 22:09:55 -0400
categories: jekyll update
---


A story of interesting primes...

(one day, the syntax will be highlighted) 
{% highlight J %}
NB. We define _xxx_ Prime as prime obtained by concatenation of nth Pascal Triangle row. 
NB. 
NB. Function to search for _xxx_ Primes. There first 3 are for n=1,8,29
NB. 11
NB. 18285670562881
NB. 1294063654237511187554750201560780429214510015005200300103459729051895935678639157755876077558760678639155189593534597290200300101001500542921451560780475020118755237513654406291
f =: 3 : '(0&,+,&0)^:y (1x)'
":@(1&p:)@".@,&'x'@(;@:(<@":"0)@f)"0 (>:i.30)
{% endhighlight %}

{% highlight J %}
require 'dll'
NB. INIT PARI JUST ONCE

ini_p =. '$PATH_TO_PARI/pari/2.9.3/lib/libpari-gmp.dylib pari_init n  ' cd ''
ini_p

NB. PARI FACTORIZATION BY MY WRAPPER
fac_p =:  >@(0&{@:('libutils.dylib is_prime i  *c'&cd@<@":))

m_prime =. 1294063654237511187554750201560780429214510015005200300103459729051895935678639157755876077558760678639155189593534597290200300101001500542921451560780475020118755237513654406291x

NB. echo 'Time Pari  ' , (": (6!:2) 'fac_p m_prime') , 's'
NB. echo 'Time J ' , (": (6!:2) '1 p: m_prime') , 's'

f =: 3 : '(0&,+,&0)^:y (1x)'
pari_mp =: 3 : '":@(fac_p)@".@,&(120}a.)@(;@:(<@":"0)@f)"0 y'
NB. We can leave it in string form
pari_mp =: 3 : '":@(fac_p)@(;@:(<@":"0)@f)"0 y'
J_mp =: 3 : '":@(1&p:)@".@,&(120}a.)@(;@:(<@":"0)@f)"0 y'
{% endhighlight %}

{% highlight C++ %}

//g++ -dynamiclib -o libutils.dylib wrap.cpp -L/usr/local/Cellar/pari/2.9.3/lib -lpari-gmp
#include "$PATH_TO_PARI/pari/2.9.3/include/pari/pari.h"
extern "C" {
bool is_prime(char *c){
    return isprime(strtoi(c));
  }
}
{% endhighlight %}


