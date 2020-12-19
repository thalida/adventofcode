# [Advent of Code](https://adventofcode.com/)

'twas once a year called 2020
a dumpster fire of a year
but then, lo and behold the 12th month came
and with it Advent of Code once again

I seek to do better than I did last year
But I accept I'll probably do worse

Yours in codetry,
thalida

**Current Day:** 18



```
                                ████████████
                        ████▓▓▓▓▓▓▒▒▓▓▒▒▒▒████▓▓▓▓██
                      ██▒▒▒▒▒▒▒▒▒▒▓▓▓▓████          ██
                    ▓▓▒▒▒▒▒▒▒▒▓▓▓▓████░░░░        ░░░░██
                    ██▒▒▒▒▒▒▓▓▓▓██          ░░░░░░░░░░██
                  ██▒▒▒▒▒▒▓▓▒▒██        ░░░░░░██████████████
                  ██▒▒▒▒▓▓▓▓██      ░░░░░░▓▓██░░░░░░░░░░░░░░██
                  ██▒▒▓▓▓▓██      ░░░░░░██░░░░              ░░██
                  ██▒▒▓▓▓▓██    ░░░░░░██░░                    ░░██
                  ██▒▒▓▓██      ░░░░██░░                  ████░░██
                  ██▒▒▓▓██    ░░░░▓▓░░                  ██  ▒▒▓▓░░▓▓
                  ██▒▒▓▓██░░  ░░██░░        ████        ██░░▒▒██░░██
                    ██▓▓██░░░░░░██░░      ██  ▒▒██    ████░░▒▒██░░██
                    ██▓▓██░░░░██░░        ██░░▒▒██  ██▒▒▒▒██████░░██
                      ██▓▓██░░██░░        ▓▓░░▒▒██  ██▒▒▒▒▒▒▒▒░░████                ████
                        ██▓▓██░░░░          ▓▓██      ██████████░░██            ████▒▒██
                        ██▓▓██░░░░░░                  ░░░░░░░░░░░░██          ██▒▒▒▒██
                        ██████░░░░░░░░        ░░░░░░░░░░░░░░░░░░██          ██▒▒██▓▓
                      ██    ░░██░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░██        ██▒▒██
                      ██    ░░████░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░▓▓░░████  ██▒▒▒▒▒▒██▓▓▓▓
                      ██░░░░░░██  ██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░██▒▒▒▒████▒▒▒▒▒▒██
                        ████▓▓      ██▓▓░░░░░░░░░░░░░░░░▓▓▒▒░░░░    ░░░░██▒▒██  ████████
        ██████                    ██░░░░████████████████░░░░            ░░██
        ██▒▒▒▒██                ██      ░░░░░░░░░░░░░░░░                  ░░██
          ████▒▒████          ██                          ████            ░░░░██
              ██▒▒▒▒████    ██                          ██▒▒▒▒██            ░░██
                ████▒▒▒▒██████████                      ██▓▓▓▓██            ░░░░██
                    ██▒▒▒▒▒▒▒▒▒▒▒▒████                    ████░░            ░░░░██
              ▓▓██▓▓▒▒████▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░                ░░░░              ░░░░██
            ██▒▒▒▒▒▒██    ████▒▒▒▒▒▒▒▒██░░                    ████        ░░░░░░░░██
          ██▒▒██████    ██    ████████░░░░                  ▓▓▓▓▓▓▓▓      ░░░░░░░░██
          ████          ██    ░░░░░░░░░░                    ██▓▓▓▓██    ░░░░░░░░░░██
              ████      ██                                    ▓▓██░░    ░░░░░░░░▓▓▓▓
              ██░░██  ██                                      ░░░░    ░░░░░░░░██▓▓██
              ██░░██  ██                                          ░░░░░░░░████▒▒▓▓██
                ████  ██░░                                  ░░░░░░░░░░████▓▓▓▓▓▓▓▓██
                      ██░░░░░░                    ░░░░░░░░░░░░░░░░████▒▒▒▒▒▒▓▓▓▓██
                      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓██▒▒▒▒▒▒▒▒▓▓▓▓▓▓██
                        ██████████░░░░░░░░░░░░░░░░██████████▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██
                        ██▒▒▒▒▒▒▒▒████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██
                          ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                          ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
    ▓▓░░    ▓▓▒▒▒▒▓▓▓▓    ▓▓██▓▓█▓▓▓▓▓▓▓█▓▓▓▓▓▓█▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓    ▓▓▓▓
  ██▓▓      ▓▓▒▒░░▒▒▓▓  ▓▓██▒▒████▓▓▓▓▓▓▓▓▓▒██▓▓▒▒▓▓░░▒▒▒▒▓▓▓▓▓▒▓▓▓▒▒░░▒▒▓▓▒▒██▓▓▓▓
  ▓▓▓▓██  ▓▓▒▒░░░░▒▒▓▓  ▓▓▓▓██▓▓▓▓▓▓▓▒▒▒▒▓▓▓█▓▓▒▒░░▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▒▓▓▒▒▓▓▒▒▒▒▓▓
  ▓▓▒▒▒▒▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓▒▒▒▒▓██▓▓▓▓▓▓░░▒▒▓▓▓█▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓▓▓░░▒▒▓▓
  ▒▒░░▒▒▓▓▓▓▒▒░░▒▒▓▓▓▓▒▒░░▒▒▓▓██▓▓▒▒░░▒▒▓▓▓▓▓▓▓░░░░▒▒▒▒░░░░▒▒██████▒▒░░▒▒██▓▓▓▓▒▒░░▒▒▓▓██
  ░░░░▒▒▓▓▒▒░░▒▒▓▓▓▓▓▓▒▒░░▒▒▓▓██▒▒░░░░▒▒▓▓▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒░░▒▒▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓▒▒░░░░▒▒▓▓▓▓
  ░░░░▒▒▓▓▒▒░░░░▓▓██▒▒░░░░▒▒▓▓██▒▒░░░░▒▒██▓▓▓▓▒▒░░▒▒▓▓▓▓▒▒░░░░▒▒▓▓▒▒░░░░██▓▓▓▓▒▒░░░░▒▒████
  ▒▒░░▒▒▓▓▓▓░░░░▒▒▓▓▒▒▒▒░░░░▒▒▓▓▓▓▒▒░░░░▒▒▓▓▓▓▒▒░░░░▒▒▓▓▒▒░░▒▒▓▓▓▓▓▓░░░░▒▒▓▓▓▓▓▓▒▒░░░░▒▒▓▓
  ▒▒░░▒▒▓▓▒▒▒▒░░▒▒██▒▒▒▒░░▒▒▒▒██▒▒▒▒░░░░░░▒▒▓▓▒▒░░░░▒▒▒▒░░░░▒▒████▒▒▒▒░░▒▒██▓▓▒▒▒▒░░░░░░▒▒
  ░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒
  ░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░
```





```
-----------------------------------------------------------------
This ASCII snowman and flames can be found at https://textart.sh/
-----------------------------------------------------------------
```
