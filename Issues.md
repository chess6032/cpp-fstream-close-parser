# Known Issues & Limitations

Right now, the parser just checks for the *presence* of `std::fstream::close` for 
every declared `std::fstream`. This has many limitations:


* Doesn't distinguish between fstream object and fstream parameter in a function.
* Doesn't distinguish whether a `.close()` statement is commented-out or not.
* Doesn't take scoping into account. e.g., if two fstreams are declared with the same
name, only one would need to be closed to pass.
* Doesn't distinguish between code and string literals. `std::cout << "infile.close()\n"`
would pass.
* Doesn't check an fstream is closed throughout all branches in an if/else tree.
* Doesn't take into account whether a filestream gets closed inside a function.
It should be valid to pass an fstream into a function that calls `.close()` on it.
* Does not take into account references or pointers to an fstream object. If an 
fstream object is declared, it should be valid for a reference/pointer to that
fstream to call `close()`.
* Doesn't take into account fstreams that aren't opened. If an fstream
is never opened (e.g., the student declared but forgot to use it), then
a `close()` statement shouldn't be required for that fstream.
* Doesn't check that `.close()` would ever actually run. It should no be valid
for `.close()` to only be called in code that never runs (e.g., an `if` 
statement whose condition is never true).

Also, it's suboptimal. It re-checks the entire file for every fstream.
This class's assignments are small enough that it's probably not a
problem, but it's still worth noting.

Other limitations:

* The current Regex pattern for finding filestream declarations
doesn't match filestreams that are members of a class or struct.
* The current Regex pattern for finding filestream declarations
doesn't match multi-line definitions.
* The current method for finding filestream declarations is
not compatible with templates or typedef aliases.