---
layout: base
title:  'Statistics of NumType in UD_Portuguese-Bosque'
udver: '2'
---

## Treebank Statistics: UD_Portuguese-Bosque: Features: `NumType`

This feature is universal.
It occurs with 6 different values: `Card`, `Frac`, `Mult`, `Ord`, `Range`, `Sets`.

5416 tokens (2%) have a non-empty value of `NumType`.
966 types (4%) occur at least once with a non-empty value of `NumType`.
910 lemmas (5%) occur at least once with a non-empty value of `NumType`.
The feature is used with 5 part-of-speech tags: <tt><a href="pt_bosque-pos-NUM.html">NUM</a></tt> (4621; 2% instances), <tt><a href="pt_bosque-pos-ADJ.html">ADJ</a></tt> (790; 0% instances), <tt><a href="pt_bosque-pos-NOUN.html">NOUN</a></tt> (3; 0% instances), <tt><a href="pt_bosque-pos-DET.html">DET</a></tt> (1; 0% instances), <tt><a href="pt_bosque-pos-PROPN.html">PROPN</a></tt> (1; 0% instances).

### `NUM`

4621 <tt><a href="pt_bosque-pos-NUM.html">NUM</a></tt> tokens (100% of all `NUM` tokens) have a non-empty value of `NumType`.

`NUM` tokens may have the following values of `NumType`:

* `Card` (4472; 97% of non-empty `NumType`): <em>um, dois, três, milhões, mil, uma, duas, quatro, cinco, 15</em>
* `Frac` (6; 0% of non-empty `NumType`): <em>meia, meio</em>
* `Mult` (132; 3% of non-empty `NumType`): <em>cento</em>
* `Ord` (8; 0% of non-empty `NumType`): <em>1º, 2º, quinta, 1., 2., 4ª, I, XVII</em>
* `Range` (2; 0% of non-empty `NumType`): <em>07.00-09.00, 10.00-12.00</em>
* `Sets` (1; 0% of non-empty `NumType`): <em>dúzia</em>
* `EMPTY` (16): <em>milhões, 2, milhares, 14, 185/60, 3, 5, 94, II, Um</em>

<table>
  <tr><th>Paradigm <i>meio</i></th><th><tt>Card</tt></th><th><tt>Frac</tt></th></tr>
  <tr><td><tt></tt></td><td><em>meio, meia</em></td><td><em>meio</em></td></tr>
</table>

`NumType` seems to be **lexical feature** of `NUM`. 100% lemmas (830) occur only with one value of `NumType`.

### `ADJ`

790 <tt><a href="pt_bosque-pos-ADJ.html">ADJ</a></tt> tokens (7% of all `ADJ` tokens) have a non-empty value of `NumType`.

The most frequent other feature values with which `ADJ` and `NumType` co-occurred: <tt><a href="pt_bosque-feat-Number.html">Number</a></tt><tt>=Sing</tt> (666; 84%), <tt><a href="pt_bosque-feat-Gender.html">Gender</a></tt><tt>=Masc</tt> (465; 59%).

`ADJ` tokens may have the following values of `NumType`:

* `Ord` (790; 100% of non-empty `NumType`): <em>primeiro, primeira, último, última, segundo, últimos, segunda, primeiros, terceiro, terceira</em>
* `EMPTY` (10548): <em>maior, grande, novo, nova, mesmo, grandes, nacional, melhor, passado, mesma</em>

`NumType` seems to be **lexical feature** of `ADJ`. 100% lemmas (79) occur only with one value of `NumType`.

### `NOUN`

3 <tt><a href="pt_bosque-pos-NOUN.html">NOUN</a></tt> tokens (0% of all `NOUN` tokens) have a non-empty value of `NumType`.

The most frequent other feature values with which `NOUN` and `NumType` co-occurred: <tt><a href="pt_bosque-feat-Gender.html">Gender</a></tt><tt>=Masc</tt> (3; 100%), <tt><a href="pt_bosque-feat-Number.html">Number</a></tt><tt>=Sing</tt> (3; 100%).

`NOUN` tokens may have the following values of `NumType`:

* `Ord` (3; 100% of non-empty `NumType`): <em>quarto, primeiro</em>
* `EMPTY` (41318): <em>anos, presidente, ano, dia, país, pessoas, estado, parte, tempo, contos</em>

### `DET`

1 <tt><a href="pt_bosque-pos-DET.html">DET</a></tt> tokens (0% of all `DET` tokens) have a non-empty value of `NumType`.

The most frequent other feature values with which `DET` and `NumType` co-occurred: <tt><a href="pt_bosque-feat-Definite.html">Definite</a></tt><tt>=EMPTY</tt> (1; 100%), <tt><a href="pt_bosque-feat-Gender.html">Gender</a></tt><tt>=EMPTY</tt> (1; 100%), <tt><a href="pt_bosque-feat-Number.html">Number</a></tt><tt>=EMPTY</tt> (1; 100%), <tt><a href="pt_bosque-feat-PronType.html">PronType</a></tt><tt>=EMPTY</tt> (1; 100%).

`DET` tokens may have the following values of `NumType`:

* `Card` (1; 100% of non-empty `NumType`): <em>uma</em>
* `EMPTY` (34868): <em>o, a, os, as, um, uma, sua, seu, este, esta</em>

### `PROPN`

1 <tt><a href="pt_bosque-pos-PROPN.html">PROPN</a></tt> tokens (0% of all `PROPN` tokens) have a non-empty value of `NumType`.

The most frequent other feature values with which `PROPN` and `NumType` co-occurred: <tt><a href="pt_bosque-feat-Gender.html">Gender</a></tt><tt>=EMPTY</tt> (1; 100%), <tt><a href="pt_bosque-feat-Number.html">Number</a></tt><tt>=EMPTY</tt> (1; 100%).

`PROPN` tokens may have the following values of `NumType`:

* `Ord` (1; 100% of non-empty `NumType`): <em>IX</em>
* `EMPTY` (18903): <em>Paulo, São, Portugal, Brasil, José, Porto, Governo, Lisboa, Nacional, João</em>

## Relations with Agreement in `NumType`

The 10 most frequent relations where parent and child node agree in `NumType`:
<tt>NUM --[<tt><a href="pt_bosque-dep-flat.html">flat</a></tt>]--> NUM</tt> (443; 98%),
<tt>NUM --[<tt><a href="pt_bosque-dep-conj.html">conj</a></tt>]--> NUM</tt> (112; 100%),
<tt>NUM --[<tt><a href="pt_bosque-dep-nmod.html">nmod</a></tt>]--> NUM</tt> (51; 100%),
<tt>ADJ --[<tt><a href="pt_bosque-dep-conj.html">conj</a></tt>]--> ADJ</tt> (17; 89%),
<tt>NUM --[<tt><a href="pt_bosque-dep-appos.html">appos</a></tt>]--> NUM</tt> (10; 91%),
<tt>NUM --[<tt><a href="pt_bosque-dep-nummod.html">nummod</a></tt>]--> NUM</tt> (8; 89%),
<tt>NUM --[<tt><a href="pt_bosque-dep-fixed.html">fixed</a></tt>]--> NUM</tt> (4; 100%),
<tt>NUM --[<tt><a href="pt_bosque-dep-parataxis.html">parataxis</a></tt>]--> NUM</tt> (3; 100%),
<tt>ADJ --[<tt><a href="pt_bosque-dep-amod.html">amod</a></tt>]--> ADJ</tt> (2; 100%),
<tt>ADJ --[<tt><a href="pt_bosque-dep-nmod.html">nmod</a></tt>]--> ADJ</tt> (1; 100%).

