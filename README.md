# register-machine-encodings

This tool will find the register machine encodings of natural numbers, lists, register machine instructions and register machine programs.

Use the tool by:

  python encoding.py <OPTION> <NUMBER>

  where

    OPTION is from:

        'p' -> program

        'l' -> list

        'b' -> body

        'd' -> double arrow encoding

        's' -> single arrow encoding

    NUMBER is the natural number to decode.

  Note:

    <<x, y>> = 2<sup>x</sup> (2y+ 1)

    <x, y> = 2<sup>x</sup> (2y+ 1) - 1

    [x<sub>1</sub>, x<sub>2</sub>, . . . , x<sub>n</sub>] = [x<sub>1</sub> :: ([x<sub>2</sub> :: (... [x<sub>n</sub> :: [] ...))

    encode([x<sub>1</sub>, x<sub>2</sub>, . . . , x<sub>n</sub>]) = <<x<sub>1</sub>, <<x<sub>2</sub>, ... <<x<sub>n</sub>,0>> ... >> >>

    encode(R+<sub>i</sub> -> L<sub>j</sub>) = <<2i, j>>

    encode(R-<sub>i</sub> -> L<sub>j</sub>, L<sub>k</sub>) = <<2i + 1, <j, k> >>

    encode(HALT) = 0

    encode(program) = encode([encode(body<sub>1</sub>), encode(body<sub>2</sub>), ..., encode(body<sub>n</sub>)])
