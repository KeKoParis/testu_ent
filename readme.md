docker run --rm -i blep/testu01_gw -s < test_1.dat

docker run --rm -i blep/testu01_gw -s -r < test_1.dat

testu01_gateway reads number from stdin and forwards them to TestU01
selected battery of tests.

Each generated 32 bits number must be serialized to stdin as 4 bytes.

Makes sure to run tests twice: once with and once without --reverse-bits.
            
Options:
--name: set the name of the random number generator (used in final report).
-s, --small-crush  : run SmallCrunch tests.
-c, --crush        : run Crunch tests (the default battery of test).
-b, --big-crush    : run BigCrunch tests.
-r, --reverse-bits : reverse bits of the decoded 32 bits integer (bit 0 is 
                     swapped with bit 31, bit 1 with bit 30...).
-h, --help         : show this help text.