.. _week-2-day-1:

======
第一日
======

.. num-section::

.. _context:

コンテキスト
------------

LilyPondの更なる利用のために、ここでコンテキストという概念について理解しておく必要がある。

LilyPondの楽譜表現は階層構造になっており、あるコンテキストが別のコンテキストを含むという形をとっている。
代表的なコンテキストは ``Score`` 、 ``Staff`` 、 ``Voice`` の3つであり、それぞれが出力される楽譜の「楽譜全体」、「譜（1パート分の五線譜）」「声部」に対応している。
``Score`` は1つまたは複数の ``Staff`` を含むことができ、 ``Staff`` は1つまたは複数の ``Voice`` を含むことができる。
以下の図は、コンテキストの階層構造を図示したものである。

TODO

コンテキストは :ref:`engraver` で扱うエングラーバというものをいくつか持ち、それぞれのエングラーバが実際に音楽記号を配置する。
例えば、 ``Voice`` コンテキストは ``Note_heads_engraver`` と呼ばれるエングラーバを持ち、このエングラーバは符頭を楽譜上に描く。
``Score`` コンテキストは ``Metronome_mark_engraver`` というエングラーバを持ち、楽譜全体で共有されるテンポ記号を描く。


.. num-section::

.. _creating-context:

コンテキストの生成
------------------

コンテキストは ``\new`` コマンドで生成する。 ``\new`` の後に、生成するコンテキストの種類を与え、必要であればコンテキストの固有名を ``=`` と文字列で指定する。
最後に音楽表記を与える。
ただし、 ``Score`` **コンテキストは** ``\new Score`` **によってではなく、** ``\score`` **によって生成する。**
``\score`` は ``{`` ``}`` で囲まれた音楽表記やいくつかの特殊なコマンドを取り、TODO
``\score`` は ``\book`` 以外のいかなる子要素になってはならない。TODO

.. lily::
  :caption: コンテキストの生成
  :name: creating-context-example

  \score {
    <<
      \new Staff {
        \new Voice {
          g'4
        }
      }
      \new Staff = "staff2" {
        \new Voice {
          c'4
        }
      }
    >>
  }

上の例では、 ``\score`` によって ``Score`` コンテキストを生成し、 ``<<`` ``>>`` で囲まれた2つの ``\new Staff`` により同時に2つの譜を作り出している。
後者の ``Staff`` には ``staff2`` という名前が付いており、ソースファイルの別の場所から参照することができる。


.. num-section::

.. _implicit-context-creation:

コンテキストの暗黙的作成
------------------------

第一週の種々の例で見てきたように、単純に音楽表記を ``{`` ``}`` で囲むことで楽譜を生成することができた。
これはLilyPondが内部的にコンテキストを自動生成しているためであり、TODO

.. lily::
  :caption: 単純な音楽表記
  :name: simple-music-example
  :without-image:

  {
    c'4 d' e' f'
  }

これは以下のように解釈される。

.. lily::
  :caption: 暗黙的に作成されるコンテキスト
  :name: implicit-context-creation-example
  :without-image:

  \book {
    \score {
      \new Staff {
        \new Voice {
          c'4 d' e' f'
        }
      }
      \layout { }
    }
    \paper { }
    \header { }
  }

音楽が ``\new Voice`` を省略して表記されるとき、暗黙的に ``Voice`` コンテキストが作成される。
この表記を囲んでいる ``Staff`` が存在しない時、暗黙的に ``Staff`` が作成される。
同様に、 ``\score`` 、 ``\layout`` 、 ``\book`` 、 ``\paper`` 、 ``\header`` が作成されている。

.. lily::
  :caption: Voice内でのStaff生成
  :name: creating-staff-in-voice
  :without-image:

  \score {
    \new Staff {
      \new Voice {
        \new Staff {
          c'4
        }
      }
    }
  }

上のコードのように、 ``Voice`` コンテキスト内で ``\new Staff`` を呼び出す時、 ``Voice`` は ``Staff`` を含むことができないから、
その外部にある ``Score`` コンテキストを探し、 ``Score`` の子コンテキストとして ``Staff`` が作成される。
（もちろん、 ``\score`` が存在していない時には暗黙的に作成される。）
結果的に、 ``Score`` 内には、 ``Score`` の直下にある ``Staff`` と、 ``Voice`` 内で宣言された ``Staff`` の二つが作成されるため、出力は以下のようになる。

.. lily::
  :name: creating-staff-in-voice-answer
  :without-code:

  \score {
    \new Staff {
      \new Voice {
        \new Staff {
          c'4
        }
      }
    }
  }

下段に新しく作成された ``Staff`` 内に暗黙的に ``Voice`` が作成され、そちらに音符が置かれていることに注意せよ。


.. num-section::

.. _polyphony-2:

多声表記 (2)
------------

:ref:`polyphony-1` で、以下のような表記について学習した。

.. lily::
  :caption: << \\\\ >> を用いた多声表記
  :name: polyphony-using-double-slash
  :without-image:

  << { g'4 a' b' c'' } \\ { e'4 f' g' a' } >>

これは ``\new Voice`` を用いた以下の表記と同等である。

.. lily::
  :caption: \\new Voice を用いた多声表記
  :name: polyphony-using-new-voice
  :without-image:

  <<
    \new Voice = "1" { \voiceOne g'4 a' b' c'' }
    \new Voice = "2" { \voiceTwo e'4 f' g' a' }
  >>

1つの譜の中で複数の声部を保持するために、 ``Staff`` コンテキスト内に複数の ``Voice`` コンテキストを持たせているというわけである。

TODO: \voices

TODO: スパナを繋げる

.. num-section::

.. _engraver:

エングラーバ
------------
