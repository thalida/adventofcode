# Day 10: Pipe Maze


## Part 1
You use the hang glider to ride the hot air from Desert Island all the way up
to the floating metal island. This island is surprisingly cold and there
definitely aren't any thermals to glide on, so you leave your hang glider
behind.

You wander around for a while, but you don't find any people or animals.
However, you do occasionally find signposts labeled "[Hot
Springs](https://en.wikipedia.org/wiki/Hot_spring)" pointing in a seemingly
consistent direction; maybe you can find someone at the hot springs and ask
them where the desert-machine parts are made.

The landscape here is alien; even the flowers and trees are made of metal. As
you stop to admire some metal grass, you notice something metallic scurry away
in your peripheral vision and jump into a big pipe! It didn't look like any
animal you've ever seen; if you want a better look, you'll need to get ahead
of it.

Scanning the area, you discover that the entire field you're standing on is
densely packed with pipes; it was hard to tell at first because they're the
same metallic silver color as the "ground". You make a quick sketch of all of
the surface pipes you can see (your puzzle input).

The pipes are arranged in a two-dimensional grid of _tiles_ :

  * `|` is a _vertical pipe_ connecting north and south.
  * `-` is a _horizontal pipe_ connecting east and west.
  * `L` is a _90-degree bend_ connecting north and east.
  * `J` is a _90-degree bend_ connecting north and west.
  * `7` is a _90-degree bend_ connecting south and west.
  * `F` is a _90-degree bend_ connecting south and east.
  * `.` is _ground_ ; there is no pipe in this tile.
  * `S` is the _starting position_ of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

Based on the acoustics of the animal's scurrying, you're confident the pipe
that contains the animal is _one large, continuous loop_.

For example, here is a square loop of pipe:

    
    
    .....
    .F-7.
    .|.|.
    .L-J.
    .....
    

If the animal had entered this loop in the northwest corner, the sketch would
instead look like this:

    
    
    .....
    . _S_ -7.
    .|.|.
    .L-J.
    .....
    

In the above diagram, the `S` tile is still a 90-degree `F` bend: you can tell
because of how the adjacent pipes connect to it.

Unfortunately, there are also many pipes that _aren't connected to the loop_!
This sketch shows the same loop as above:

    
    
    -L|F7
    7S-7|
    L|7||
    -L-J|
    L|-JF
    

In the above diagram, you can still figure out which pipes form the main loop:
they're the ones connected to `S`, pipes those pipes connect to, pipes _those_
pipes connect to, and so on. Every pipe in the main loop connects to its two
neighbors (including `S`, which will have exactly two pipes connecting to it,
and which is assumed to connect back to those two pipes).

Here is a sketch that contains a slightly more complex main loop:

    
    
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    

Here's the same example sketch with the extra, non-main-loop pipe tiles also
shown:

    
    
    7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ
    

If you want to _get out ahead of the animal_ , you should find the tile in the
loop that is _farthest_ from the starting position. Because the animal is in
the pipe, it doesn't make sense to measure this by direct distance. Instead,
you need to find the tile that would take the longest number of steps _along
the loop_ to reach from the starting point - regardless of which way around
the loop the animal went.

In the first example with the square loop:

    
    
    .....
    .S-7.
    .|.|.
    .L-J.
    .....
    

You can count the distance each tile in the loop is from the starting point
like this:

    
    
    .....
    .012.
    .1.3.
    .23 _4_.
    .....
    

In this example, the farthest point from the start is _`4`_ steps away.

Here's the more complex loop again:

    
    
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    

Here are the distances for each tile on that loop:

    
    
    ..45.
    .236.
    01.7 _8_
    14567
    23...
    

Find the single giant loop starting at `S`. _How many steps along the loop
does it take to get from the starting position to the point farthest from the
starting position?_




## Part 2


You quickly reach the farthest point of the loop, but the animal never
emerges. Maybe its nest is _within the area enclosed by the loop_?

To determine whether it's even worth taking the time to search for such a
nest, you should calculate how many tiles are contained within the loop. For
example:

    
    
    ...........
    .S-------7.
    .|F-----7|.
    .||.....||.
    .||.....||.
    .|L-7.F-J|.
    .|..|.|..|.
    .L--J.L--J.
    ...........
    

The above loop encloses merely _four tiles_ \- the two pairs of `.` in the
southwest and southeast (marked `I` below). The middle `.` tiles (marked `O`
below) are _not_ in the loop. Here is the same loop again with those regions
marked:

    
    
    ...........
    .S-------7.
    .|F-----7|.
    .|| _OOOOO_ ||.
    .|| _OOOOO_ ||.
    .|L-7 _O_ F-J|.
    .| _II_ | _O_ | _II_ |.
    .L--J _O_ L--J.
    ..... _O_.....
    

In fact, there doesn't even need to be a full tile path to the outside for
tiles to count as outside the loop - squeezing between pipes is also allowed!
Here, `I` is still within the loop and `O` is still outside the loop:

    
    
    ..........
    .S------7.
    .|F----7|.
    .|| _OOOO_ ||.
    .|| _OOOO_ ||.
    .|L-7F-J|.
    .| _II_ || _II_ |.
    .L--JL--J.
    ..........
    

In both of the above examples, _`4`_ tiles are enclosed by the loop.

Here's a larger example:

    
    
    .F----7F7F7F7F-7....
    .|F--7||||||||FJ....
    .||.FJ||||||||L7....
    FJL7L7LJLJ||LJ.L-7..
    L--J.L7...LJS7F-7L7.
    ....F-J..F7FJ|L7L7L7
    ....L7.F7||L7|.L7L7|
    .....|FJLJ|FJ|F7|.LJ
    ....FJL-7.||.||||...
    ....L---J.LJ.LJLJ...
    

The above sketch has many random bits of ground, some of which are in the loop
(`I`) and some of which are outside it (`O`):

    
    
    _O_ F----7F7F7F7F-7 _OOOO_
    _O_ |F--7||||||||FJ _OOOO_
    _O_ || _O_ FJ||||||||L7 _OOOO_
    FJL7L7LJLJ||LJ _I_ L-7 _OO_
    L--J _O_ L7 _III_ LJS7F-7L7 _O_
    _OOOO_ F-J _II_ F7FJ|L7L7L7
    _OOOO_ L7 _I_ F7||L7| _I_ L7L7|
    _OOOOO_ |FJLJ|FJ|F7| _O_ LJ
    _OOOO_ FJL-7 _O_ || _O_ |||| _OOO_
    _OOOO_ L---J _O_ LJ _O_ LJLJ _OOO_
    

In this larger example, _`8`_ tiles are enclosed by the loop.

Any tile that isn't part of the main loop can count as being enclosed by the
loop. Here's another example with many bits of junk pipe lying around that
aren't connected to the main loop at all:

    
    
    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJ7F7FJ-
    L---JF-JLJ.||-FJLJJ7
    |F|F-JF---7F7-L7L|7|
    |FFJF7L7F-JF7|JL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L
    

Here are just the tiles that are _enclosed by the loop_ marked with `I`:

    
    
    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJ _I_ F7FJ-
    L---JF-JLJ _IIII_ FJLJJ7
    |F|F-JF---7 _III_ L7L|7|
    |FFJF7L7F-JF7 _II_ L---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L
    

In this last example, _`10`_ tiles are enclosed by the loop.

Figure out whether you have time to search for the nest by calculating the
area within the loop. _How many tiles are enclosed by the loop?_

