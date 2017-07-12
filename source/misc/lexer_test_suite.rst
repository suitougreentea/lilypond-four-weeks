.. code-block:: lilypond

  \version "2.19.59"
  \relative { cis' des eisis feses g a b c }

.. code-block:: lilypond

  \relative c' {
    c\accent c->
    d\tenuto d--        |
    e\staccato e-.
    f\staccatissimo f-! |
    g\marcato g-^
    a\portato a-_       |
    b\stopped b-+
  }

.. code-block:: lilypond

  \relative c' {
    c4^~ c c_~ c |
    c8^( d e f) c_( d e f) |
    c8^[ d e f] c_[ d e f] |
    c4^\accent c_\accent c^> c_> |
    c2^\f c_\p |
    c8^\< d e f\! c_\< d e f\! |
  }

.. code-block:: lilypond

  %{
    comment
    %{
      cannot be nested
      }
    %}
    outside
  %}

.. code-block:: lilypond

  {
    c4^\markup "String%{String%}String"
  }

.. code-block:: lilypond

  \relative c' {
    <c e~ g>2 q <c f a>~ <c e g>
  }

  \relative c'' {
    << { c8 d e f g2 } \\ << { e,2 d } { g f } >> \\ <g g'>1 >>
  }
