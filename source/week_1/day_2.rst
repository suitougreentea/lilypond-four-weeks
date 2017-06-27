.. _week-1-day-2:

======
第二日
======

.. num-section::

.. _note-names:

音名
----

デフォルトでは、以下が基本の音名である。

.. rst-class:: indented

  ===== ===== ===== =====
  ド    ``c`` ソ    ``g``
  レ    ``d`` ラ    ``a``
  ミ    ``e`` シ    ``b``
  ファ  ``f``
  ===== ===== ===== =====

ドのシャープなどの派生音は、音名の末尾に ``is`` （シャープ）または ``es`` （フラット）を付ける。
``isis`` でダブルシャープ、 ``eses`` でダブルフラットを表現する。

.. rst-class:: indented

  ``cis`` → ドのシャープ, ``ges`` → ソのフラット, ``bisis`` → シのダブルシャープ

また、以下の音名に限り別表記がある。

.. rst-class:: indented

  ``ees`` = ``es`` , ``eeses`` = ``eses`` , ``aes`` = ``as`` , ``aeses`` = ``ases``

コマンドを付加することで、他の言語での音名表記が可能であるが、本ドキュメントでは省略する。TODO: http://lilypond.org/doc/v2.18/Documentation/notation/writing-pitches#note-names-in-other-languages http://git.savannah.gnu.org/gitweb/?p=lilypond.git;a=blob;f=scm/define-note-names.scm

音符と音符との間は1つ以上のスペースか改行で区切らなければならない。
すなわち、ドとレを続けて表記する際、 ``cd`` とは書くことができないということである。

注意しなければならないのが、音名は調号や臨時記号のいかんに関わらず実際に演奏される音名で記述されなければならないことである。
例えば、次の出力は全て同じ音名の入力 ``g' fis' aes' bes'`` から得られる。臨時記号はLilyPondが自動的に付加する。
オクターブ記号 ``'`` については :ref:`absolute-octave` で、調号については :ref:`key-signature` で学ぶ。

.. lily::
  :without-code:
  :caption: ハ長調
  :name: same-pitch-in-c-major

  {
    \key c \major
    g' fis' aes' bes'
  }

.. lily::
  :without-code:
  :caption: ト長調
  :name: same-pitch-in-g-major

  {
    \key g \major
    g' fis' aes' bes'
  }

.. lily::
  :without-code:
  :caption: 変二長調
  :name: same-pitch-in-des-major

  {
    \key des \major
    g' fis' aes' bes'
  }


.. num-section::

.. _absolute-octave:

絶対オクターブ入力
------------------

LilyPondには2つのオクターブ入力方法がある。絶対オクターブ入力と、相対オクターブ入力である。

何も指定しない時、LilyPondは絶対オクターブ入力を用いる。
絶対オクターブ入力では、 ``c`` 〜 ``b`` はヘ音記号譜表でいう第二間〜上第一間に対応する。
これより高いピッチを指定するには、 ``c'`` のように音名のすぐ後に ``'`` を付加する。
``c'`` 〜 ``b`` はト音記号譜表の下第一線〜第三線に対応する。
低いピッチは、 ``c,`` のように ``,`` を付加する。
``'`` や ``,`` を複数付けることで更に高いピッチや低いピッチを指定することができる。

以下の例では、ピッチの見やすさのため ``\clef`` コマンドで音部記号を変更しているが、これについては :ref:`clef` で扱う。
なお、例で見るように、音楽表記は ``{`` ``}`` で囲む必要がある。

.. lily::
  :caption: 絶対オクターブ入力
  :name: absolute-octave-example

  {
    \clef bass
    c, b, c b
    \clef treble
    c' b' c'' b''
  }


.. num-section::

.. _relative-octave:

相対オクターブ入力
------------------

音符を ``\relative`` コマンドで囲うと、中にある音符では相対オクターブ入力が用いられる。
相対オクターブ入力では、ある音符のオクターブはその前の音符のピッチによって決定される。
具体的には、 ``'`` や ``,`` が付いていない場合、前の音符との音程の間隔が一番近いオクターブが（すなわち、四度以内のものが）選ばれる。
``'`` や ``,`` が付いている場合、上記のピッチに対して相対的にオクターブが移動する。

``\relative`` コマンドを使用するには、まず ``\relative`` の後にスペース、続けて最初の音符の基準となるピッチを絶対オクターブで入力する。
最後に、相対オクターブとして解釈する音符列を ``{`` と ``}`` で挟む。括弧の前後もスペースまたは改行で区切る。

.. lily::
  :caption: 相対オクターブ入力
  :name: relative-octave-example

  \relative c'' { e b g' e, }

この例では、 ``c''`` （すなわち、ト音記号譜表第三間のド）が基準ピッチであり、
最初の音符 ``e`` は基準ピッチの ``c''`` に近いものが選ばれるから、第四間のミ（絶対オクターブでいうところの ``e''`` ）となる。
次の音符 ``b`` は ``e`` との関係で配置される。下のシが選ばれているが、上のシよりも間隔が狭いことを確認してほしい。
``g'`` は、 ``b`` により近い下側のソの1オクターブ上、 ``e,`` は ``g'`` により近い下側のミの更に1オクターブ下となる。

基準ピッチは省略可能であり、省略された場合は最初の音符が絶対オクターブとして解釈される。
（基準ピッチが ``f`` になっているのと同じことである。）
しかし、基準ピッチは常に明記することを推奨している。

.. lily::
  :caption: 基準ピッチを指定しない場合
  :name: relative-octave-example-without-startpitch

  \relative { e' g b, e' }

上の例では、最初のピッチ ``e'`` が絶対オクターブとして扱われ、それ以降の音符は前の音を基準にしてオクターブが決定されている。

.. note::

    相対オクターブの決定に、 ``-is``, ``-es`` などの派生は **関与せず** 、基本となる（ピアノの白鍵の）音高のみ考慮される。
    つまり、 ``{ cis ges }`` の ``ges`` のオクターブは、 ``{ c g }`` と同様に決定される。

基準ピッチは、 ``c`` の任意のオクターブを用いるのが慣例である。


.. num-section::

.. _note-length:

音長
----

音名のすぐ後に数字を記入することで音長を指定する。
指定可能な音長は2のべき乗（1, 2, 4, 8, 16, …）であり、それぞれ全音符、二分音符、四分音符…に対応する。

倍全音符（ブレーべ、全音符の2倍長）は数字の代わりに ``\breve`` 、四倍全音符（ロンガ）は ``\longa`` を記入する。
八倍長（マキシマ）は ``\maxima`` で得られるが、通常では符頭が用意されていないため休符でしか用いない。
休符は :ref:`rest-1` で扱う。

付点は数字の後に ``.`` を付加する。付点は複数付けることができる。

音長が指定されていない音符は、その前の音符の音長を引き継ぐ。付点を用いる時は数字を省略できない。

.. lily::
  :caption: 音長の指定例
  :name: note-length-example

  \relative c' { c2 c4 c c16 c c c c2. c4.. c16 c8. c16 c8 c c1 }


.. num-section::

.. _rest-1:

休符 (1)
--------

通常の休符は音名の部分を ``r`` に置き換えることで入力できる。

.. lily::
  :caption: 休符
  :name: rest-example

  \relative c' { c2 r4 r c16 c c r c2. c4.. r16 r8. c16 c8 r c1 }

小節の中央に書かれる全休符は、 ``r1`` の代わりに大文字の ``R1`` を用いる。
``R`` は、指定された音長にかかわらず、小節の中央に全休符記号を描く。
そのため、例えば3/4拍子の小節に対して全休符を書きたい場合、以下のように ``R2.`` を用いる。

.. lily::
  :caption: 小節にわたる全休符
  :name: whole-rest-example

  \relative c' {
    \time 3/4
    c4 d e R2. a b c
  }

拍子記号コマンド ``\time`` については :ref:`time-signature` で扱う。

LilyPondはもう一種類、空白休符と呼ばれる特殊な休符が存在する。
空白休符は何の記号も出力しないが、演奏しない時間を作り出すものである。

.. lily::
  :caption: 空白休符
  :name: skip-rest-example

  \relative c' { c4 c s c c c8. c16 s2 }

空白休符は、声部が1つの譜ではほとんど用いられないが、複数の声部を持つ場合に用いることがある。
複数声部については :ref:`week-1-day-4` で扱うため、下の例は眺めるだけでよい。

.. lily::
  :caption: 空白休符（多声部の例）
  :name: skip-rest-polyphony-example

  \relative c'' {
    << { s4  c s bes } \\
       { c,4 e g e   } >>
  }

.. num-section::

.. _comment:

コメント
--------

LilyPondのソースファイルには、出力結果に全く関与しないコメントを挿入することができる。

単一行コメントは、 ``%`` で始まり、行末までがコメントとなる。

.. lily::
  :caption: 単一行コメント
  :name: single-line-comment
  :without-image:

  {
    c4 d e f % これがコメント
  }

複数行コメントは、 ``%{`` ``%}`` で囲まれた範囲が対象となる。

.. lily::
  :caption: 複数行コメント
  :name: multi-line-comment
  :without-image:

  {
    c4 d e f
    %{
      これが複数行コメント。
      長いコメントを書くことができる。
    %}
  }

複数行コメントは入れ子構造にすることはできず、最初に出現した ``%}`` でコメントは終了する。

:ref:`scheme-syntax` で扱うが、Schemeコード中でのコメントはこれと異なり、単一行が ``'`` 、複数行が ``#!`` ``!#`` である。


.. _exercise-1-2:

練習問題
--------

以下のコード片に記述を追加し、画像のような楽譜を出力せよ。

.. code-block:: lilypond

    \version "2.19.59"
    \relative c' {
      % ADD CODE HERE
    }

.. lily::
    :caption: 第一週第二日 練習問題
    :name: practice_week1_day1
    :without-code:

    \relative c' {
      c4. g'8 c16 es fis bes, d,8. g,16
      c4.. r16 r2
    }