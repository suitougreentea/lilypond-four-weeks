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


.. num-section::

.. _key-signature:

調号
----


.. num-section::

.. _time-signature:

拍子記号
--------


.. num-section::

.. _rest-2:

休符 (2)
--------

\rest, multi-measure-rest http://lilypond.org/doc/v2.18/Documentation/notation/writing-rests.html#full-measure-rests


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
