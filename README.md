# Unicoder 1.0.0 #

Unicoder is a utility for converting UTF-8 character codes, such as U+0024 ($) or U+20AC (€), into sequences of bytes presented as hexadecimal strings.

Unicoder's output is in the form of Squirrel string assignments that are ready to be cut and pasted into Squirrel code. For example:

```squirrel
/Users/smitty > ./unicoder.py U+20AC U+24 U+0939 U+0025 U+10348

local unicodeString="\xE2\x82\xAC";
local unicodeString="\x24";
local unicodeString="\xE0\xA4\xB9";
local unicodeString="\x25";
local unicodeString="\xF0\x90\x8D\x88";
```

As you can see from the example above, just call the script with one or more UTF-8 codes separated by spaces.

**Note** Unicode contains more than 137,000 characters so at this time there is no way to derive a hex string from a character, only that character's UTF-8 code.

## Release Notes ##

- 1.0.0 *5 June 2019*
    - Initial release.

## Licence And Copyright ##

This software is copyright &copy; 2019, Tony Smith (@smittytone).

The UTF-8 character codes and encoding scheme is copyright &copy; [The Unicode Consortium](https://www.unicode.org).