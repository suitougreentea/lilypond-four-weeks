.. _week-1-day-1:

======
第一日
======

.. num-section::

.. _lilypond-official-page:

LilyPondの公式ページ
--------------------

日本語の公式ページは以下にある。

`LilyPond - みんなの楽譜作成 <http://lilypond.org/index.ja.html>`_ 

楽譜を記述するにあたって頻繁に参照するページは "マニュアル_" に集積されている。後述する「開発版」のマニュアルは、`コミュニティ/開発/マニュアル <http://lilypond.org/development.ja.html>`_ にある。

* `導入部 <http://lilypond.org/website/introduction.ja.html>`_ - 長所や実例の紹介
* `ダウンロード <http://lilypond.org/download.ja.html>`_
* マニュアル_

  * 導入部

    * **学習** - 入門者のためのチュートリアルと、簡単な調整方法が書かれている

  * 常用するマニュアル

    * **記譜法(リファレンス)** - 「学習」より細かく、求める楽譜を実現するための方法が書かれている
    * **Snippets(スニペット)** (英語のみ) - 項目ごとに1つのテーマについて、特殊な刻譜を行う方法や工夫が列挙されている

  * 常用外のマニュアル

    * **Internals(内部リファレンス)** (英語のみ) - LilyPond が内部的に行っている処理について書かれている。既存のコマンドで対処できない場合に参照する

* `コミュニティ <http://lilypond.org/community.ja.html>`_ - 開発版のマニュアルと、開発への貢献について

.. _マニュアル: http://lilypond.org/website/manuals.ja.html

.. num-section::

.. _downloading-and-installing-lilypond:

LilyPondのダウンロード・インストール
------------------------------------

公式ページでは、「**安定版**」としてバージョン 2.18.2 を、「**開発版**」としてバージョン 2.19.xx を配布している。このドキュメントではバージョン 2.19.59 以降を対象にしているため、「**開発版**」をインストールされたい。

#. `開発版の配布ページ <http://lilypond.org/development.ja.html>`_ から、実行中の OS に合ったファイルをダウンロードする
#. `安定版の配布ページ <http://lilypond.org/download.ja.html>`_ で、 OS ごとのインストールの手順を参照し、それを行う



.. num-section::

.. _launching-lilypond:

LilyPondの実行・楽譜のコンパイル
---------------------------------

Windowsと、Unix系での実行方法をそれぞれ記す。Windows では、エクスプローラから実行する方法、コマンドラインから実行する方法がある。

.. note::

    記述例の ``\version "z.yy.xx"`` は、LilyPond の文法変更に沿ってソースを変換するために必要で、ファイルの先頭に必ず書く。

Windows（エクスプローラから）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. テキストエディタで、以下の内容のファイルを "test.ly" としてデスクトップに保存する。

.. code-block:: lilypond

    \version "2.19.59"
    \relative { c' d e f g a b c }

2. デスクトップ上の "test.ly" を右クリックし、「**Generate PDF**」を選択する。または、 "test.ly" をダブルクリックする。

.. image:: ./img/day_1_generate_pdf.png

エラーがなければ、デスクトップに "test.pdf" が生成される。エラーがある場合、その詳細は "test.log" に記録される。


Windows 版では、LilyPond のインストール時にエディタ(LilyPad)がインストールされるが、メモ帳と同等の機能しかなく、特に使う必要はない。

Windows（コマンドラインから）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. テキストエディタで、以下の内容のファイルを "test.ly" として保存する

.. code-block:: lilypond

    \version "2.19.59"
    \relative { c' d e f g a b c }

2. スタートボタンを右クリックし、PowerShell を開く
3. 以下のコマンドで "test.ly" をコンパイルする

.. code-block:: bat

    chcp 437         # コンソール文字化けを防ぐ
    cd path¥to¥file  # (必要ならば) test.ly のあるディレクトリに行く
    lilypond test

エラーがなければ、同じフォルダに "test.pdf" ができる。


Unix 系 (Linux / FreeBSD / macOS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. テキストエディタで以下の内容の "test.ly" を作成する。

.. code-block:: lilypond

    \version "2.19.59"
    \relative { c' d e f g a b c }

2. 端末（ターミナル）を開き、 "test.ly" をコンパイルする。

.. code-block:: bash

    $ cd /path/to/file  # (必要ならば) test.ly のあるディレクトリに行く
    $ lilypond test

エラーがなければ、同じフォルダに "test.pdf" ができる。


.. num-section::

.. _frescobaldi-introduction:

Frescobaldi
-----------

`Frescobaldi <http://frescobaldi.org/>`_ は、LilyPond に特化された機能を持つエディタである。

代表的な機能に次のようなものがある。

- ソース→楽譜、楽譜→ソース 対応する箇所の表示・ジャンプ
- コードのハイライト表示
- コマンドの補完
- MIDI 再生
- ソースの移調

.. image:: ./img/day_1_frescobaldi.png
   :scale: 40%
   :align: center
