.. _week-1-day-5:

======
第五日
======

.. num-section::

.. _command:

コマンド
--------

これまで、 ``\relative`` などの ``\`` で始まる入力を何度か目にしたことがある。
これらを「コマンド」と呼び、LilyPondの入力において様々な役割を果たす。
コマンドの定義には揺れがあるが、 ``\`` で始まるものとすることで特に差し支えは無いだろう。

コマンドは単独で動作するものと、いくつかの「引数」を取るものとがある。

``\relative`` を例に取ると、基準ピッチと後に続く音楽表記がそれぞれ引数であり、
コマンドの名前と引数の間、引数と引数の間、コマンドの後を、空白か改行で区切る。[#command-space]_
``\bar`` は1つの ``"`` ``"`` で囲まれた文字列を引数として取るコマンドであり、
``\noBeam`` などは引数を取らないコマンドの例である。


.. num-section::

.. _clef:

音部記号
--------

音部記号を入力するには、 ``\clef`` コマンドを用いる。
``\clef`` コマンドは1つの文字列引数を取る。文字列は基本的に ``"`` ``"`` で囲むことで与えられる。

最初の音より前にこのコマンドが指定されれば、指定した音部記号の譜が生成され、
音楽の途中でこのコマンドが指定されれば、変更を示す小さい音部記号が描かれる。
何も指定せず音符を配置した場合、ト音記号として譜が生成される。

.. lily::
  :caption: 音部記号
  :name: clef-example

  \relative c' {
    \clef "treble" c1
    \clef "bass" c
    \clef "alto" c
  }

全ての音部記号のリストは :ref:`clef-list` を参照せよ。

文字列が数字や記号を含まず、かつ音名とも異なる場合、囲みの ``"`` ``"`` を省略することができる。
すなわち、 ``"foo"`` は ``foo`` と入力しても文字列として解釈されるが、
``"bar_1"`` や ``"g"`` は ``"`` ``"`` を省略することができない。

したがって、例えば ``\clef "treble"`` は通常 ``\clef treble`` のように表記される。

音部記号の名前の後ろに ``^`` と数字を付加することで、実音を数字の度数分下げるように表記することができ、
``_`` と数字を付加することで、実音を上げるように表記することができる。
これは、基本的に実音のオクターブ違いを表記するものであるため、通常数字には8や15を用いるが、
それ以外の度数の指定も可能である。
また、数字の前後に ``(`` ``)`` あるいは ``[`` ``]`` を付加することで括弧つきの表示にすることができる。

.. lily::
  :caption: 音部記号の実音移動
  :name: clef-real-pitch-shift-example

  \relative c' {
    \clef treble c1
    \clef "treble_8" c
    \clef "treble^(15)" c
  }

記号や数字を含む場合は ``"`` ``"`` を省略できないことを再度確認せよ。


.. num-section::

.. _key-signature:

調号
----

調号は ``\key`` コマンドで入力できる。
これは2つの引数を取り、1つ目は主音のピッチである。
2つ目はスケールを指定するリストであり、通常、既に用意されているコマンドを用いる。
通常のスケールには ``\major`` 、 ``\minor`` があり、
教会旋法として ``\ionian`` 、 ``\dorian`` 、 ``\phrygian`` 、 ``\lydian`` 、
``\mixolydian`` 、 ``\aeolian`` 、 ``\locrian`` が用意されている。

音部記号と同様に、最初の音符の前に指定するとその調号で譜が生成され、音楽の途中では転調を表す。
デフォルトは ``c \major`` である。

.. lily::
  :caption: 調号
  :name: key-signature-example

  \relative c' {
    \key d \major c1
    \key fis \minor c
    \key c \mixolydian c
  }

新たにスケールを定義することも可能である。 :ref:`creating-scale` で扱う。

ピッチのオクターブは無視される。


.. num-section::

.. _time-signature:

拍子記号
--------

拍子記号は ``\time`` コマンドで指定する。今回は引数が1つの場合を学ぼう。
拍子の分数を ``/`` で区切って指定する。 数字と ``/`` の間にスペースを入れてはいけない。

.. lily::
  :caption: 拍子記号
  :name: time-signature-example

  \relative c' {
    \time 3/4
    c8 c c c c c
    \time 6/8
    c c c c c c
    \time 4/4
    c c c c c c c c
    \time 2/2
    c c c c c c c c
  }

例にあるように、4/4拍子、2/2拍子の場合は通常、C記号が用いられる。
``\numericTimeSignature`` コマンドで分数記号を使用するように変更することができ、
``\defaultTimeSignature`` コマンドでC記号を用いるように設定を戻すことができる。


.. lily::
  :caption: 数字の拍子記号
  :name: numeric-time-signature

  \relative c' {
    \time 4/4 c1
    \time 2/2 c
    \numericTimeSignature
    \time 4/4 c
    \time 2/2 c
    \defaultTimeSignature
    \time 4/4 c
    \time 2/2 c
  }


自動連桁は拍子記号に基づいて行われるが、
引数を2つ指定することで、自動連桁の振る舞いを変更することができる。
:ref:`automatic-beam` で扱う。


.. num-section::

.. _rest-2:

休符 (2)
--------

\rest, \skip, multi-measure-rest http://lilypond.org/doc/v2.19/Documentation/notation/writing-rests.html


.. num-section::

.. _transpose:

トランスポーズ
--------------


.. num-section::

.. _ottava:

オッターヴァ
------------


.. num-section::

.. _grace:

装飾小音符
----------

.. rubric:: Footnotes

.. [#command-space]
  厳密には、後に続く文字の種類によって、空白を省略しても良い場合があるが、
  エラーを避けるため、また可読性のため、空白や改行を付加することを薦める。
