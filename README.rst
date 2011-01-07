Introduction
============

``stream-scaling`` automates running the STREAM memory bandwidth
test on Linux systems.  It detects the number of CPUs and
how large each of their caches are.  The program then
downloads STREAM, compiles it, and runs it with an array
size large enough to not fit into cache.  The number
of threads is varied from 1 to the total number of
cores in the server, so that you can see how memory speed
scales as cores involved increase.

Installation/Usage
==================

Just run stream-scaling::

  ./stream-scaling

And it should do the rest.  Note that a stream.c and stream
binary will be left behind afterwards.

Note that the program is only expected to work on systems
using gcc 4.2 or later, as the OpenMP libraries are required.

Sample result
=============

This sample is from an Intel i7 860 processor, featuring 4 real cores with
Hyper Threading for a total of 8 virtual cores.  It also features the Turbo feature
to accelerate running with low core counts.  Memory is 4 X 2GB DDR-1600::

    $ ./stream-scaling 
    === CPU cache information ===
    CPU /sys/devices/system/cpu/cpu0 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu0 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu0 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu0 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu1 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu1 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu1 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu1 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu2 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu2 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu2 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu2 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu3 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu3 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu3 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu3 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu4 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu4 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu4 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu4 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu5 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu5 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu5 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu5 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu6 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu6 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu6 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu6 Level 3 Cache: 8192K (Unified)
    CPU /sys/devices/system/cpu/cpu7 Level 1 Cache: 32K (Data)
    CPU /sys/devices/system/cpu/cpu7 Level 1 Cache: 32K (Instruction)
    CPU /sys/devices/system/cpu/cpu7 Level 2 Cache: 256K (Unified)
    CPU /sys/devices/system/cpu/cpu7 Level 3 Cache: 8192K (Unified)
    Total CPU system cache: 69468160 bytes
    Suggested minimum array elements needed: 31576436
    Array elements used: 31576436

    === Check and possibly build stream ===
    --2010-09-19 21:41:46--  http://www.cs.virginia.edu/stream/FTP/Code/stream.c
    Resolving www.cs.virginia.edu... 128.143.137.29
    Connecting to www.cs.virginia.edu|128.143.137.29|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 11918 (12K) [text/plain]
    Saving to: `stream.c'

    100%[======================================>] 11,918      --.-K/s   in 0.03s   

    2010-09-19 21:41:46 (373 KB/s) - `stream.c' saved [11918/11918]


    === Testing up to 8 cores ===

    -------------------------------------------------------------
    STREAM version $Revision: 5.9 $
    -------------------------------------------------------------
    This system uses 8 bytes per DOUBLE PRECISION word.
    -------------------------------------------------------------
    Array size = 31576436, Offset = 0
    Total memory required = 722.7 MB.
    Each test is run 10 times, but only
    the *best* time for each is used.
    -------------------------------------------------------------
    Number of Threads requested = 1
    -------------------------------------------------------------
    Printing one line per active thread....
    -------------------------------------------------------------
    Your clock granularity/precision appears to be 1 microseconds.
    Each test below will take on the order of 38888 microseconds.
       (= 38888 clock ticks)
    Increase the size of the arrays if this shows that
    you are not getting at least 20 clock ticks per test.
    -------------------------------------------------------------
    WARNING -- The above is only a rough guideline.
    For best results, please be sure you know the
    precision of your system timer.
    -------------------------------------------------------------
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Copy:        9663.6238       0.0524       0.0523       0.0527
    Scale:       9315.7724       0.0545       0.0542       0.0558
    Add:        10429.7390       0.0729       0.0727       0.0732
    Triad:      10108.3413       0.0753       0.0750       0.0758
    -------------------------------------------------------------
    Solution Validates
    -------------------------------------------------------------

    Number of Threads requested = 2
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      13095.9151       0.0579       0.0579       0.0580

    Number of Threads requested = 3
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      13958.5017       0.0545       0.0543       0.0547

    Number of Threads requested = 4
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      14293.3696       0.0532       0.0530       0.0537

    Number of Threads requested = 5
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      13663.0608       0.0563       0.0555       0.0571

    Number of Threads requested = 6
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      13757.0249       0.0559       0.0551       0.0567

    Number of Threads requested = 7
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      13463.7445       0.0564       0.0563       0.0566

    Number of Threads requested = 8
    Function      Rate (MB/s)   Avg time     Min time     Max time
    Triad:      13230.8312       0.0575       0.0573       0.0583

Like many of the post-Nehalem Intel processors, this system gets
quite good memory bandwidth even when running a single thread,
with the Turbo feature helping a bit too.  And it's almost reached
saturation of all available bandwidth with only two threads active,
which is good for a system with this many cores; they don't all
have to be doing something to take advantage of all the memory
on this server.

Results database
================

Eventually it's hoped that this program can help build a database
of per-core scaling information for STREAM similar to the the
core STREAM project maintains for peak throughput.  Guidelines
for submission to such a project are still being worked on.
Please contact the author if you have any ideas for helping organize
this work.

Preliminary Samples
-------------------

Here are some sample results from the program, showing how memory speeds
have marched forward as the industry moved from slower DDR2 to increasingly
fast DDR3.  They also demonstrate why AMD was able to limp along with slower
RAM for so long in their multi-socket configurations.  While no single core
gets great bandwidth, when the server is fully loaded the aggregate amount
can be impressive.

* T7200:  Intel Core2 T7200.  Dual core.  32K Data and Instruction L1 caches, 4096K L2 cache.
* 4 X 8347:  AMD Opteron 8347 HE.  Quad core, 4 sockets.  64K Data and Instruction L1 caches, 512K L2 cache, 2048K L3 cache.  32 X 2GB DDR2-667.
* X2 4600+:  AMD Athlon 64 X2 4600+.  Dual core.  64K Data and Instruction L1 caches, 512K L2 cache.  4 X 2GB RAM.
* 2 X 280:  Amd Opteron 280.  Dual core, 2 sockets.  64K Data and Instruction L1 caches, 1024K L2 cache.  8 X 1GB DDR2-800.
* Q6600:  Intel Q6600.  Quad core.  32KB Data and Instruction L1 caches, 4096K L2 cache.  4 X 2GB RAM.
* 8 X 8431:  AMD Opteron 8431.  6 cores each, 8 sockets.  64K Data and Instruction L1 caches, 512K L2 cache, 5118K L3 cache.  256GB RAM.
* E5506:  Intel Xeon E5506 2.13GHz.  Quad core.  32K Data and Instruction L1 caches, 256K L2 cache, 4096K L3 cache.
* X4 955:  AMD Phenon II X4 955.  64K Data and Instruction L1 caches, 512K L2 cache, 6144K L3 cache.  4GB DDR3-1333.
* X6 1055T:  AMD Phenon II X6 1055T.  64K Data and Instruction L1 caches, 512K L2 cache, 6144K L3 cache.  8GB DDR3-1333.
* i860: Intel Core i7 860.  Quad core with Turbo and Hyper Threading for 8 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 8192K L3 cache.  4 X 2GB RAM.

========= ===== ====== ========= ====== ===== ===== ===== ===== ===== ===== ===== =====  
Processor Cores Clock  Memory    1 Core 2     3     4     8     16    24    32    48
========= ===== ====== ========= ====== ===== ===== ===== ===== ===== ===== ===== =====  
T7200     2     2.0GHz DDR2/667  2965   3084
4 X 8347  16    1.9GHz DDR2/667  2684   5212  7542  8760  9389  14590
X2 4600+  2     2.4GHz DDR2/800  3657   4460
2 X 280   4     2.4GHz DDR2/800  3035   3263  3130  6264
Q6600     4     2.4GHz DDR2/800  4383   4537  4480  4390
8 X 8431  48    2.4GHz DDR2/800  4038   7996  11918 13520 23658 22801 23688 24522 27214
E5506     4     2.1GHz DDR3/800  7826   9016  9273  9297
X4 955    4     3.2GHz DDR3/1333 6750   7150  7286  7258 
X6 1055T  6     3.2GHz DDR3/1333 7207   8657  9873  9772  9932*
i860      8     2.8GHz DDR3/1600 9664   13096 13959 14293 13231
========= ===== ====== ========= ====== ===== ===== ===== ===== ===== ===== ===== =====  

* The result for 6-core processors with 6 threads is shown in the 8-core column.  Only so much space to work with here...

Todo
====

* Adding compatibility with more operating systems than Linux
  would be nice.

* A results processor that took the verbose output shown
  and instead produced a compact version for easy comparison
  with other systems, similar to the CSV output mode of
  bonnie++, would make this program more useful.

Bugs
====

There aren't any known bugs, just limitations.

Documentation
=============

The documentation README.rst for the program is in ReST markup.  Tools
that operate on ReST can be used to make versions of it formatted
for other purposes, such as rst2html to make a HTML version.

Contact
=======

The project is hosted at http://github.com/gregs1104/stream-scaling

If you have any hints, changes or improvements, please contact:

 * Greg Smith greg@2ndQuadrant.com

License
=======

stream-scaling is licensed under a standard 3-clause BSD license.

Copyright (c) 2010, Gregory Smith
All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are 
met:

  * Redistributions of source code must retain the above copyright 
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright 
    notice, this list of conditions and the following disclaimer in 
    the documentation and/or other materials provided with the 
    distribution.
  * Neither the name of the author nor the names of contributors may 
    be used to endorse or promote products derived from this 
    software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS 
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

