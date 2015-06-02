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

    === CPU Core Summary ===
    processor	: 7
    model name	: Intel(R) Core(TM) i7 CPU         860  @ 2.80GHz
    cpu MHz		: 2898.023
    siblings	: 8

    === Check and build stream ===
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

In general the following information is needed:

* Output from the stream-scaling command
* CPU information
* List of memory banks in the system, what size of RAM they have, and
  what technology/speed it runs at.

Common places you might assemble this info from include:

* /proc/cpuinfo
* lspci -v
* dmidecode

Since CPU performance data of this sort is very generic, many 
submissions are sent to help this project without wanting the
company or individual's name dislosed.  Accordingly, unless credit
for your submission is specifically requested, the source of reported
results will remain private.  So far all contributions have been
anonymous.

Preliminary Samples
-------------------

Here are some sample results from the program, showing how memory speeds
have marched forward as the industry moved from slower DDR2 to increasingly
fast DDR3.  They also demonstrate why AMD was able to limp along with slower
RAM for so long in their multi-socket configurations.  While no single core
gets great bandwidth, when the server is fully loaded the aggregate amount
can be impressive.

* T7200:  Intel Core2 T7200.  Dual core.  32K Data and Instruction L1 caches, 4096K L2 cache.
* E5420:  Intel Xeon E5420.  Quad core.  16K Data and Instruction L1 caches, 6144MB L2 cache.  8 X 4GB DDR2-667.
* 2 X E5405:  Dual Intel Xeon E5405.  Quad core.  32K Data and Instruction L1 caches, 6144K L2 cache.  8 X 4GB DDR2-667.
* 4 X 8347:  AMD Opteron 8347 HE.  Quad core, 4 sockets.  64K Data and Instruction L1 caches, 512K L2 cache, 2048K L3 cache.  32 X 2GB DDR2-667.
* E2180:  Intel Pentium E2180.  Dual core.  32K Data and Instruction L1 caches, 1024K L2 cache.  2 X 1GB DDR2-800.
* X2 4600+:  AMD Athlon 64 X2 4600+.  Dual core.  64K Data and Instruction L1 caches, 512K L2 cache.  4 X 2GB RAM.
* 2 X 280:  Amd Opteron 280.  Dual core, 2 sockets.  64K Data and Instruction L1 caches, 1024K L2 cache.  8 X 1GB DDR2-800.
* Q6600:  Intel Q6600.  Quad core.  32KB Data and Instruction L1 caches, 4096K L2 cache.  4 X 2GB RAM.
* 8 X 8431:  AMD Opteron 8431.  6 cores each, 8 sockets.  64K Data and Instruction L1 caches, 512K L2 cache, 5118K L3 cache.  256GB RAM.
* E5506:  Intel Xeon E5506 2.13GHz.  Quad core.  32K Data and Instruction L1 caches, 256K L2 cache, 4096K L3 cache.
* E5520:  Dual Intel Xeon E5520.  Quad core with Turbo and Hyper Threading for 8 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 8192K L3 cache.  18 X 4GB RAM.
* X4 955:  AMD Phenon II X4 955.  64K Data and Instruction L1 caches, 512K L2 cache, 6144K L3 cache.  4GB DDR3-1333.
* X6 1055T:  AMD Phenon II X6 1055T.  64K Data and Instruction L1 caches, 512K L2 cache, 6144K L3 cache.  8GB DDR3-1333.
* i7-860: Intel Core i7 860.  Quad core with Turbo and Hyper Threading for 8 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 8192K L3 cache.  4 X 2GB RAM.
* i7-870: Intel Core i7 870.  Quad core with Turbo and Hyper Threading for 8 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 8192K L3 cache.  2 X 2GB RAM.
* i7-870[2]: Intel Core i7 870, as above, except with 4 X 4GB RAM.
* 2 X E5620:  Dual Intel Xeon E5620.  Quad core with Turbo and Hyper Threading for 16 virtual cores.  32K Data and Instruction L1 cache, 256K L2 cache, 12288K L3 cache.  12 X 8GB DDR3/1333.
* 2 X X5560:  Dual Intel Xeon X5560. Quad core with Turbo and Hyper Threading for 8 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 8192K L3 cache.  6 X 2GB DDR3/1333.
* 4 x E7540:  Quad Intel Xeon E7540. Six cores with Turbo and Hyper Threading for 48 virtual cores, 32K Data and Instruction L1 caches, 256K L2 cache, 18432K L3 cache.  32 x 4096MB DDR3/1066.
* 4 x X7550:  Quad Intel Xeon X7550.  Eight cores with Turbo, Hyper Threading disabled for 32 total.  32K Data and Instruction L1 caches, 256K L2 cache, 18432K L3 cache.  32 X 4096 DDR3/1333.
* 4 X 6168:  Quad AMD Opteron 6168.  Twelve cores for 48 total, 64K Data and Instruction L1 caches, 512K L2 cache, 5118K L3 cache.  16 X 8192MB DDR3/133.
* 4 X 6172:  Quad AMD Opteron 6172.  Twelve cores for 48 total, 64K Data and Instruction L1 caches, 512K L2 cache, 5118K L3 cache.  32 X 4096MB DDR3/1333.
* 4x X7560:  Quad Intel X7560.  Eight cores with Turbo and Hyper Threading for 64 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 24576K L3 cache.  32 X 4096 DDR3/1066.
* X7560[2]:  Quad Intel X7560.  Eight cores with Turbo and Hyper Threading disabled, for 32 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 24576K L3 cache.  32 X 4096 DDR3/1066.
* 4 X 4850:  Quad Intel E7-4850.  Ten cores with Turbo and Hyper Threading for 80 virtual cores.  32K Data and Instruction L1 caches, 256K L2 cache, 24576K L3 cache.  64 X 8192MB DDR3/1333.

========= ===== ======= ========= ====== ===== ===== ===== ===== ===== ===== ===== =====  
Processor Cores Clock   Memory    1 Core 2     3     4     8     16    24    32    48
========= ===== ======= ========= ====== ===== ===== ===== ===== ===== ===== ===== =====  
T7200     2     2.0GHz  DDR2/667  2965   3084
E5420     4     2.5GHz  DDR2/667  3596   3992  4305  4365  4452
2 X E5405 8     2.0GHz  DDR2/667  3651   3830  4941  5774  5773
4 X 8347  16    1.9GHz  DDR2/667  2684   5212  7542  8760  9389  14590
E2180     2     2.0GHz  DDR2/800  2744   2784
X2 4600+  2     2.4GHz  DDR2/800  3657   4460
2 X 280   4     2.4GHz  DDR2/800  3035   3263  3130  6264
Q6600     4     2.4GHz  DDR2/800  4383   4537  4480  4390
8 X 8431  48    2.4GHz  DDR2/800  4038   7996  11918 13520 23658 22801 23688 24522 27214
E5506     4     2.13GHz DDR3/800  7826   9016  9273  9297
2 X E5520 8     2.27GHz DDR3/1066 7548   9841  9377  9754  12101 13176
X4 955    4     3.2GHz  DDR3/1333 6750   7150  7286  7258 
X6 1055T  6     3.2GHz  DDR3/1333 7207   8657  9873  9772  9932*
i7-860    8     2.8GHz  DDR3/1600 9664   13096 13959 14293 13231
i7-870    8     2.93GHz DDR3/1600 10022  12714 13698 13909 12787
i7-870[2] 8     2.93GHz DDR3/1600 9354   11935 13145 13853 12598
2 X E5620 16    2.4GHz  DDR3/1333 9514   16845 17960 22544 21744 19083
2 X X5560 16    2.8GHz  DDR3/1333 11658  18382 19918 24546 23407 29215
4 X E7540 48    2.0GHz  DDR3/1066 4992   9967  14926 18727 31685 35566 35488 35973 35284 
4 X X7550 32    2.0GHz  DDR3/1333 5236   10482 15723 20963 32557 35941 35874 35819
4 X 6168  48    1.90GHz DDR3/1333 5611   11148 15819 20943 34327 52206 67560 69517 65617
4 X 6172  48    2.1GHz  DDR3/1333 4958   9903  14493 19469 37613 51625 40611 47361 32301
4 X X7560 64    2.26GHz DDR3/1066 4356   7710  13028 14561 18702 19761 19938 20011 15964
X7560[2]  32    2.26GHz DDR3/1066 4345   8679  12970 16315 25293 27378 27368 28654
4 X 4850  80    2.0GHz  DDR3/1333 5932   11571 17404 16000 41932 72351 58657 71384 65395
========= ===== ======= ========= ====== ===== ===== ===== ===== ===== ===== ===== =====  

* The result for 6-core processors with 6 threads is shown in the 8-core column.  Only so much space to work with here...

Multiple runs
=============

Since significant run to run variation is often observed in stream
results, a set of tools to help average this data out are included.
The programs require the Ruby programming language be installed.
Using them looks like this, where we're using the server hostname
"grace" to label the files and averaging across 10 runs::

  ./multi-stream-scaling 10 grace
  ./multi-averager grace > stream.txt
  gnuplot stream-plot

A stream.png file will be produced with a graph showing the average
of the values from the multiple runs.  If you are interested in
analyzing the run to run variation, the stream.txt file also includes
the standard deviation of the results at each core count.

Todo
====

* Adding compatibility with more operating systems than Linux
  would be nice.  Some results have been submitted from FreeBSD that
  look correct, but the automatic cache validation code hasn't
  been validated on that OS.

* A results processor that took the verbose output shown
  and instead produced a compact version for easy comparison
  with other systems, similar to the CSV output mode of
  bonnie++, would make this program more useful.

* Some early cache size detection code has been written for OS X.
  But the program doesn't do anything useful there; it will just run
  normal STREAM many times.  The standard Apple compiler chain doesn't
  support OpenMP, and changing an OpenMP environment variable is the way
  core count is limited in this program.  You'll get this linker error::

  ld: library not found for -lgomp
 
Limitations
===========

On systems with many processors and large caches, most commonly AMD systems
with 24 or more cores, the results at high core counts will vary
significantly.  This is theorized to come from two causes:

* Thread scheduling will move the running stream processees between
  processors in a way that impacts results.

* Despite attempting to use a large enough data set to avoid it, some amount
  of processor caching will inflate results.

If the variation of results at high core counts is high, running the program
multiple times and considering the worst results seen at higher thread
counts is recommended.  Results listed above have included some work to try
and eliminate incorrect data from these processors.  That may not have been
entirely successful.  For example, the 4 X 6172 results show extremely high
results from 16 to 32 cores.  Determing whether those are accurate is still a
work in progress.

Bugs
====

On some systems, the amount of memory selected for the stream array
ends up exceeding how large of a block of RAM the operating system (or
in some cases the compiler) is willing to allocate at once.  This
seems a particular issue on 32-bit operating systems, but even 64-bit
ones are not immune.

If your system fails to compile stream with an error such as this::

  stream.c:(.text+0x34): relocation truncated to fit: R_X86_64_32S against `.bss'

stream-scaling will try to compile stream using the gcc "-mcmodel=large"
option after hitting this error.  That will let the program use larger data
structures.  If you are using a new enough version of the gcc compiler,
believed to be at least verison 4.4, the program will run normally after
that; you can ignore these "relocation truncated" warnings.

If you have both a large amount of cache--so a matching large block of memory
is needed--and an older version of gcc, the second compile attempt will also
fail, with the following error::

  stream.c:1: sorry, unimplemented: code model ‘large’ not supported yet

In that case, it is unlikely you will get accurate results from
stream-scaling.  You can try it anyway by manually decreasing the size of the
array until the program will compile and link.  Manual compile can be done like
this::

  gcc -O3 -DN=130000000 -fopenmp stream.c -o stream

And then reducing the ``-DN`` value until compilation is successful.
After that upper limit is determined, adjust the setting for
MAX_ARRAY_SIZE at the beginning of the stream-scaling program to reflect
it.  An upper limit on the stream array size of 130M as shown here
allocates approximately 3GB of memory for the test array, with 4GB being
the normal limit for 32-bit structures.

The fixes for this issue are new, and it is still possible a problem here
still exists.  If you have a gcc version >=4.4 but stream-scaling still won't
compile correctly, a problem report to the author would be appreciated.  It's
not clear yet why the exact cut-off value varies on some systems, or if there
are systems where the improved dynamic allocation logic may not be sufficient.

Documentation
=============

The documentation ``README.rst`` for the program is in ReST markup.  Tools
that operate on ReST can be used to make versions of it formatted
for other purposes, such as rst2html to make a HTML version.

Contact
=======

The project is hosted at http://github.com/gregs1104/stream-scaling

If you have any hints, changes or improvements, please contact:

 * Greg Smith greg.smith@crunchydatasolutions.com

Credits
=======

The sample results given in this file have benefitted from private
contributions all over the world.  Most submissions ask to remain
anonymous.

The multiple run averaging programs were originally contributed by
Ben Bleything <ben@bleything.net>

License
=======

stream-scaling is licensed under a standard 3-clause BSD license.

Copyright (c) 2010-2015, Gregory Smith
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
