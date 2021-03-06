---
layout: base
title:  'Statistics of aux:aspect in UD_Chinese-GSDSimp'
udver: '2'
---

## Treebank Statistics: UD_Chinese-GSDSimp: Relations: `aux:aspect`

This relation is a language-specific subtype of <tt><a href="zh_gsdsimp-dep-aux.html">aux</a></tt>.
There are also 1 other language-specific subtypes of `aux`: <tt><a href="zh_gsdsimp-dep-aux-pass.html">aux:pass</a></tt>.

955 nodes (1%) are attached to their parents as `aux:aspect`.

951 instances of `aux:aspect` (100%) are left-to-right (parent precedes child).
Average distance between parent and child is 1.05340314136126.

The following 4 pairs of parts of speech are connected with `aux:aspect`: <tt><a href="zh_gsdsimp-pos-VERB.html">VERB</a></tt>-<tt><a href="zh_gsdsimp-pos-PART.html">PART</a></tt> (946; 99% instances), <tt><a href="zh_gsdsimp-pos-ADJ.html">ADJ</a></tt>-<tt><a href="zh_gsdsimp-pos-PART.html">PART</a></tt> (6; 1% instances), <tt><a href="zh_gsdsimp-pos-PART.html">PART</a></tt>-<tt><a href="zh_gsdsimp-pos-PART.html">PART</a></tt> (2; 0% instances), <tt><a href="zh_gsdsimp-pos-NOUN.html">NOUN</a></tt>-<tt><a href="zh_gsdsimp-pos-PART.html">PART</a></tt> (1; 0% instances).


~~~ conllu
# visual-style 16	bgColor:blue
# visual-style 16	fgColor:white
# visual-style 15	bgColor:blue
# visual-style 15	fgColor:white
# visual-style 15 16 aux:aspect	color:blue
1	动作	动作	NOUN	NN	_	3	nmod	_	SpaceAfter=No
2	冒险	冒险	NOUN	NN	_	3	nmod	_	SpaceAfter=No
3	游戏	游戏	NOUN	NN	_	12	nsubj	_	SpaceAfter=No
4	（	（	PUNCT	(	_	5	punct	_	SpaceAfter=No
5	A-AVG	A-AVG	X	FW	_	3	appos	_	SpaceAfter=No
6	）	）	PUNCT	)	_	5	punct	_	SpaceAfter=No
7	：	：	PUNCT	:	_	12	punct	_	SpaceAfter=No
8	是	是	AUX	VC	_	12	cop	_	SpaceAfter=No
9	冒险	冒险	NOUN	NN	_	10	nmod	_	SpaceAfter=No
10	游戏	游戏	NOUN	NN	_	12	nmod	_	SpaceAfter=No
11	的	的	PART	DEC	Case=Gen	10	case:dec	_	SpaceAfter=No
12	分支	分支	NOUN	NN	_	0	root	_	SpaceAfter=No
13	，	，	PUNCT	,	_	12	punct	_	SpaceAfter=No
14	它	它	PRON	PRP	Person=3	15	nsubj	_	SpaceAfter=No
15	融合	融合	VERB	VV	_	12	parataxis	_	SpaceAfter=No
16	了	了	PART	AS	Aspect=Perf	15	aux:aspect	_	SpaceAfter=No
17	动作	动作	NOUN	NN	_	18	nmod	_	SpaceAfter=No
18	游戏	游戏	NOUN	NN	_	21	nmod	_	SpaceAfter=No
19	的	的	PART	DEC	Case=Gen	18	case:dec	_	SpaceAfter=No
20	一些	一些	ADJ	JJ	_	21	amod	_	SpaceAfter=No
21	特征	特征	NOUN	NN	_	15	obj	_	SpaceAfter=No
22	。	。	PUNCT	.	_	12	punct	_	SpaceAfter=No

~~~


~~~ conllu
# visual-style 7	bgColor:blue
# visual-style 7	fgColor:white
# visual-style 8	bgColor:blue
# visual-style 8	fgColor:white
# visual-style 8 7 aux:aspect	color:blue
1	许多	许多	NUM	CD	NumType=Card	4	amod	_	SpaceAfter=No
2	国际	国际	NOUN	NN	_	4	nmod	_	SpaceAfter=No
3	国家	国家	NOUN	NN	_	4	nmod	_	SpaceAfter=No
4	组织	组织	NOUN	NN	_	8	nsubj	_	SpaceAfter=No
5	对此	对此	ADP	IN	_	8	case	_	SpaceAfter=No
6	表示	表示	AUX	VV	_	8	cop	_	SpaceAfter=No
7	了	了	PART	AS	Aspect=Perf	8	aux:aspect	_	SpaceAfter=No
8	不满	不满	ADJ	JJ	_	0	root	_	SpaceAfter=No
9	。	。	PUNCT	.	_	8	punct	_	SpaceAfter=No

~~~


~~~ conllu
# visual-style 16	bgColor:blue
# visual-style 16	fgColor:white
# visual-style 15	bgColor:blue
# visual-style 15	fgColor:white
# visual-style 15 16 aux:aspect	color:blue
1	这	这	DET	DT	_	2	det	_	SpaceAfter=No
2	个	个	NOUN	NNB	_	3	clf	_	SpaceAfter=No
3	原理	原理	NOUN	NN	_	5	nsubj	_	SpaceAfter=No
4	有时	有时	ADV	RB	_	5	advmod	_	SpaceAfter=No
5	叫做	叫做	VERB	VV	_	0	root	_	SpaceAfter=No
6	弗雷格	弗雷格	PROPN	NNP	_	7	nmod	_	SpaceAfter=No
7	原理	原理	NOUN	NN	_	5	obj	_	SpaceAfter=No
8	，	，	PUNCT	,	_	5	punct	_	SpaceAfter=No
9	因为	因为	ADP	IN	_	11	case	_	SpaceAfter=No
10	普遍	普遍	ADV	RB	_	11	advmod	_	SpaceAfter=No
11	认为	认为	VERB	VV	_	5	xcomp	_	SpaceAfter=No
12	弗雷格	弗雷格	PROPN	NNP	_	15	nsubj	_	SpaceAfter=No
13	首先	首先	ADV	RB	_	15	advmod	_	SpaceAfter=No
14	公式	公式	NOUN	NN	_	15	compound	_	SpaceAfter=No
15	化	化	PART	SFV	_	11	ccomp	_	SpaceAfter=No
16	了	了	PART	AS	Aspect=Perf	15	aux:aspect	_	SpaceAfter=No
17	它	它	PRON	PRP	Person=3	15	obj	_	SpaceAfter=No
18	。	。	PUNCT	.	_	5	punct	_	SpaceAfter=No

~~~


