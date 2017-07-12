.. _week-1-day-3:

======
第三日
======

.. num-section::

.. _chord:

和音
----

和音を入力するには、 ``<`` と ``>`` の中に音高を入力し、外に音長を記述する。

.. lily::
  :caption: 和音
  :name: chord-example

  {
    <c' e'>4 <e' c''> <c'' e'' g''>2
  }

相対オクターブ入力における音高は、和音中と、和音の外の（次の）音で基準が異なる。
和音中においては1つ前にある音高を基準にし、和音の **次の音符** は、 **直前の和音の最初** の音符の音高 が基準となる。

.. lily::
  :caption: 相対オクターブ入力における和音
  :name: chord-in-relative-octave

  \relative c' {
    e4 <g c e g> d <e a, g' c>
  }

1つ目の和音 ``<g c e g>`` においては、 最初の ``g`` はその前の音 ``e`` を基準にしており、
それぞれ ``c`` は ``g`` 、``e`` は ``c`` 、 ``g`` は ``e`` を基準にしている。
次の音 ``d`` は、前の音が和音であるから、和音の最初の音 ``g`` が基準となる。
最後の和音では、 ``e`` は ``d`` が基準であり、続く音は音の高低の順番にかかわらず、和音中の1つ前の音が基準となっていることを確認せよ。


.. num-section::

.. _chord-repeat:

和音の繰り返し (1)
------------------

同じ和音を繰り返すには、音名の代わりに ``q`` を入力する。オクターブ記号は許容されない。
``q`` は、間に単音や休符が存在しても、必ず最後に出現した和音と同じ音高の和音を生成する。

.. lily::
  :caption: 和音の繰り返し
  :name: chord-repeat-example

  \relative c' {
    <c e g>2 q4 <c f a>8 r f'4 r8 q r2
  }

音楽の最初で ``q`` を用いるとエラーとなる。


.. num-section::

.. _single-note-or-chord-repeat:

単音か和音の繰り返し
--------------------

音高を省略し音長のみを指定すると、最後に出現した単音あるいは和音と同じ音高が繰り返される。
休符は繰り返されない。

.. lily::
  :caption: 単音か和音の繰り返し
  :name: single-note-or-chord-repeat-example

  \relative c' {
    <c e g>2 4 <c f a>8 r f'4 r8 8 r2
  }

:ref:`chord-repeat` の例と比較せよ。

これを用いる際の注意は、前の音符の音長が指定されておらず、前の音符と数字がスペースで区切られているだけの場合、
数字がその音符の音長として解釈されてしまうことである。すなわち、 ``c 4`` は ``c c4`` ではなく ``c4`` と解釈される。
これはLilyPondの構文解析における仕様であり、このような場合においては、前の音符の音長を指定するか、数字のみの繰り返しを避ける必要がある。
なお、前の音符にスペース以外の何らかの文字が付加されていればこのような問題は起こらない。

音楽の最初で音高を省略すると ``c'`` が出力される。


.. num-section::

.. _tie-and-slur:

タイとスラー
------------

タイを描くには、タイを繋げる2つの音符のうち、最初の音符に ``~`` を付加する。

.. lily::
  :caption: タイ
  :name: tie-example

  \relative c' {
    c2~ c8 g'4 f8~ 8. e16~ 8 d8 c2
  }

和音にタイを付加する際、和音内の各音にタイ記号を付加することで繋ぐ音符を指定できるし、
``<`` ``>`` の外側に付加すれば可能な音全てがタイで繋がる。

.. lily::
  :caption: 和音のタイ
  :name: chord-tie-example

  \relative c' {
    <c e~ g>2 q <c f a>~ <c e g>
  }

タイ記号は音符の後にスペースを開けて ``c ~ c`` のようにも書くことができるが、この場合でも ``~`` は前者の音符と後者の音符を繋ぐ役割を果たしているわけではない。
``~`` はあくまでも前者の音符に属しており、「次の同じ音高の音符とタイを繋げよ」という情報に過ぎないのである。

スラーを描くには、最初の音符に ``(`` を付加し、最後の音符に ``)`` を付加する。

.. lily::
  :caption: スラー
  :name: slur-example

  \relative c' {
    c4( d e f)
  }

注意を要するのが、 ``(c4 d e f)`` のように括弧で音符を囲うようにしてはいけないということである。
スラーもタイのように「始まり」と「終わり」の情報を音符に付加しているだけであるということに留意せよ。

フレージングスラーという、もう一種類のスラーが存在する。構文は ``\(`` ``\)`` である。
スラーとフレージングスラーの違いは見た目にはわずかしか現れないが、大きな違いは、歌詞の自動割付においてスラーがメリスマを作成するのに対し、フレージングスラーは作成しないことである。
詳しいことや具体例は :ref:`TODO` で扱う。

スラーとフレージングスラーは同時に使用することができる。

.. lily::
  :caption: スラーとフレージングスラーの同時使用
  :name: simultaneous-use-of-slur-and-phrasing-slur

  \relative c' {
    c4\( e8( g) f4 e8( d\) c1)
  }

:ref:`spanner-id` で後述する ``\=`` コマンドを用いることで、スラーやフレージングスラーの片方を同時に複数使用することができる。

タイやスラーに限らず、音符の末尾に付けるタイプの記号（代表的なものにアーティキュレーションがあり、 :ref:`articulation` で扱う）は、
音符と記号との間にスペースを含んでも良く、また複数の記号を同じ音符に付加する場合の順番の制限も無い。


.. lily::
  :caption: 音符の末尾に付ける記号の複合
  :name: multiple-use-of-trailing-sign

  \relative c' {
    c8 ( \( d e f ) g4 ( ~ \) g16 f e d c1 )
  }

``c8`` には ``(`` と ``\(`` の二つ、 ``g4`` には ``(`` ``~`` ``\)`` の三つの記号が付加されているが、
これらの順番はどのようにしても良く、間のスペースが無くても構わない。


.. num-section::

.. _beam:

連桁
----

今までの例で見てきたように、連桁はLilyPondが拍子記号に合わせて自動で付加している。
しかしながら、休符を跨ぐ連桁が必要な場面や、特に声楽曲において拍の制約に縛られない連桁が必要な場面がある。
その場合、 ``[`` ``]`` で手動連桁を設定する。スラーと同様に、始まりと終わりの音符の末尾に付加する形で記述する。
連桁は休符に始端を設けることも可能である。

.. lily::
  :caption: 手動連桁
  :name: manual-beam

  \relative c' {
    c8[ r d e] r[ f e] d[
    e d c] b[] c2
  }

自動連桁をさせたくない場合、その音符の末尾に ``\noBeam`` を付加する。

.. lily::
  :caption: 自動連桁の局所的な無効化
  :name: no-beam-example

  \relative c' {
    c8 d e f
    c\noBeam d e f
    c d\noBeam e f
    c d e\noBeam f
  }

3拍目以降において、 ``\noBeam`` が付加された音符の連桁が解除されていることに注目せよ。

一定時間完全に連桁を無効にする方法については、 :ref:`disabling-and-enabling-automatic-beam` で扱う。


.. num-section::

.. _tuplet:

連符
----

連符を記述するには、 ``\tuplet`` の後に分数の形で音長の伸縮を与える。
例えば八分音符3つ分を2つ分の長さに縮めるのが三連符であるが、この場合の分数は ``3/2`` となる。
よく使われる分数としては、 ``3/2`` 、 ``6/4`` 、 ``5/4`` などがある。
最後に音楽表記をとる。


.. lily::
  :caption: 連符
  :name: tuplet-example

  \relative c' {
    \tuplet 3/2 { c4 d e } \tuplet 3/2 { f8 e d } \tuplet 6/4 { e16 f e d c b }
    \tuplet 7/4 { c16 d e f g a b } c2.
  }

分子の数字が連符に描かれる数字になっていることを確認せよ。

分数と音楽表記の間に数字で音長を指定することによって、連符の自動分割ができる。

.. lily::
  :caption: 連符の自動分割
  :name: tuplet-span-example

  \relative c' {
    \tuplet 3/2 { c8 d e } \tuplet 3/2 { f4 e8 } \tuplet 3/2 { d8 e d } c4
    \tuplet 3/2 { c8 d e f4 e8 d8 e d } c4
    \tuplet 3/2 4 { c8 d e f4 e8 d8 e d } c4
  }

一小節目が数字を指定せず、一つずつ連符を作ったものである。
二小節目は数字を指定しないまま一連の連符を一つの ``{`` ``}`` で囲んだものであり、全ての音符が一つの連符にまとまってしまっている。
三小節目は数字を指定することで、一小節目と同じ結果を得られている。

連符内の全ての音符が連桁で繋がっていない場合、自動的に角括弧が描かれる。

TODO: \tupletSpan http://lilypond.org/doc/v2.19/Documentation/notation/writing-rhythms.html#tuplets


.. num-section::

.. _barline-and-bar-check:

小節線と小節チェック
--------------------

LilyPondは拍子記号に合わせて小節線を自動で付加する。手動で小節線を追加する場合、 ``\bar`` の後に小節線の種類を ``"`` ``"`` で囲って指定する。
以下の例で使われている小節線の種類は一部で、全ての小節線は :ref:`bar-line-list` で確認することができる。

.. lily::
  :caption: 小節線
  :name: barline-example

  \relative c' {
    c1 \bar "|"
    c \bar "||"
    c \bar "."
    c \bar "|."
    c \bar ";"
    c \bar "!"
    c \bar ".|:"
    c \bar ":|."
    c \bar ":..:"
    c
  }

よく使われるものは 複縦線 ``||`` と 終止線 ``|.`` であろう。
繰り返しの小節線は :ref:`repeat` で扱う ``\repeat`` コマンドで描かれるのが普通であり、 ``\bar`` としては多くは用いられない。

小節線は小節の途中でも挿入できるが、小節番号は加算されない。

.. lily::
  :caption: 手動の小節線と小節番号
  :name: manual-barline-and-bar-number

  \relative c' {
    c8 d e f g a b c
    c, d e f g a b c
    c, d e f \bar "||" g a b c
    c, d e f g a b c \break
    c, d e f g a b c
    c, d e f g a b c
    c, d e f g a b c
    c, d e f g a b c
  }

三小節目の途中で二重線を挿入しているが、二段目の最初の小節番号が5であることに注目せよ。
``\break`` は強制的に改行するコマンドであり、 :ref:`breaking` で扱う。


.. _exercise-1-3:

練習問題
--------

以下のコード片に記述を追加し、各画像の通りの楽譜を出力せよ。

.. code-block:: lilypond

    \version "2.19.59"
    \relative c' {
      % ADD CODE HERE
    }

.. lily::
    :caption: 第一週第三日 練習問題(1)
    :name: w1d3-exercise1
    :without-code:

    \relative c'{
      c'4(  <g e c> c q)  |
      d(   <b g d> d q)  |
      <g, e'>8. <e c'>16~ q8 q~ q[ q <d b'> <f d'>] |
      <e c'>1 |  \bar "|."
    }

.. lily::
    :caption: 第一週第三日 練習問題(2)
    :name: w1d3-exercise1
    :without-code:

    \relative c'{
      \tuplet 3/2 { g'8 c, c }
      \tuplet 3/2 { g'4    c,8 }
      \tuplet 3/2 { g'8 c,16[ c] c8 } 
      \tuplet 6/4 { g'16 c, c d e f } |
      \tuplet 5/4 { g8\( a( g) a( g)\) } 
      g,8 g'~ \tuplet 5/4 { g16 f e d c } \bar "|." 
    }
