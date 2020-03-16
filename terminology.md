# Parallel Programming (1st half): Terminology

atomic
:   A statement or instruction is (truly) atomic if it is executed by the CPU in a single, non-interruptible step.

abstractly atomic
:   A statement or instruction that, at a certain level of abstraction, appears to be executed atomically. E.g. from a caller's perspective, a method `synchronized append(x)` of a queue appears to append element `x` in one step, but from the queue's perspective, this might take several steps.

bad interleaving
:   An interleaving that yields a problematic or otherwise undesirable computation. E.g. an incorrect result, a deadlock or non-deterministic output.

busy waiting
:   Occurs when a thead busily (actively) waits, e.g. by spinning in a loop, for a condition to become true. In the opposite scenario, the thread sleeps (i.e. is blocked; in Java: `join()`, `wait()`) until the condition becomes true. Trade-off: busy waiting uses up CPU time, whereas blocking may cause additional context switches.

cache coherence protocols
:   Hardware protocols that ensure consistency across caches, typically by tracking which locations are cached, and synchronising them if necessary.

CISC, RISC
:   CISC (complex instruction set computer) and RISC (reduced instruction set computer) are two fundamental CPU architecture models. Classical RISC is easier to study, since simpler: e.g. RISC instructions can only work on registers, and reading/writing memory are separate instructions.

concurrency
:   Parallelism that requires reasoning about and managing shared resources. Often used interchangeably with parallelism.

context switch
:   Given a computation unit (CPU), a context switch denotes the action of switching the unit from one computation to another. Typically refers to switching between processes, but can also refer to switching between threads. Depending on the size of the context ("large" for a process, "small" for thread), a context switch might be computationally expensive, i.e. require comparably much CPU time.

critical section
:   A piece of code that, in order to guarantee correct program execution, may only be executed by one thread at a time.

data race
:   A program has a data race if, during any possible execution, a memory location could be written from one thread, while concurrently being read or written from another thread. Data race is often used interchangeably with race condition.

deadlock
:   Circular waiting/blocking (no instructions are executed/CPU time is used) between threads, so that the system (union of all threads) cannot make any progress anymore.

functional unit
:   A component of a CPU (or core) that performs a certain task, e.g. executing integer arithmetic operations. An execution unit is one such a functional unit, see also RISC.

instruction level parallelism
:   CPU-internal parallelisation of independent instructions, with the goal of improving performance by increasing utilisation of a CPU's functional units.

interleaving
:   Given multiple threads, each executing a sequence of instructions, an interleaving is a sequence of instructions obtained from merging the individual sequences. A sequentially consistent interleaving is one where the relative order of statements from one thread is preserved.

latency
:   An evaluation metric for pipelines. Latency measures the time a pipeline needs to process a given work item (e.g. a CPU instruction).

livelock
:   A situation in which all threads starve by infinitely often try to enter a critical section, but never succeeding. Similar to a deadlock, the system makes no real progress, although the threads execute statements/use CPU time.

liveness property
:   Property of a system: "something good eventually happens". Can only be violated in infinite time. Infinite loops and starvation are typical safety properties. Will be formally defined in Formal Methods using temporal logic.

locality
:   Has several meanings in the context of parallel programming:

  1. Locally reason about one thread at a time (also known as thread modularity). Simplifies correctness arguments.
  2. Data locality: related memory locations are accessed shortly after each other. Improves performance by optimal cache usage.
  3. Code locality: straight-line code increases opportunities for instruction level parallelism

lock
:   In general, a token/resource that can be acquired by at most one thread at a time. Locks are typically provided by a programming language to enforce mutual exclusion, by guarding/protecting a critical section. A lock can be acquired/locked by a thread, and is then held until it is released/unlocked. In Java, each object can be used as a lock (intrinsic/monitor lock), but the JDK also provides more complex locks.

lockout
:   Needlessly preventing a thread from entering a critical section.

mutual exclusion
:   Preventing more than one thread from being in a critical section, i.e. to execute a piece of code, at a given moment in time.

multiprocessing (multitasking)
:   Typically refers to parallelism on the operating system level, i.e. to processes running in parallel.

multithreading
:   Threads running in parallel.

parallelism
:   Performing computations simultaneously; either actually, if sufficient computations units (CPUs, cores, ...) are available, or virtually, via some form of alternation. Often used interchangeably with concurrency.

process
:   Independently running instance of a program/application, typically on the operation system level. Similar to a thread, but usually more heavy-weight (since a whole program) and encapsulated in memory.

process context
:   All state associated with a process, including CPU state (registers, program counter), program state (stack, heap, resource handles), and additional management information. A thread also has a context, but it is typically much smaller.

race condition
:   A program has a race condition if, during any possible execution with the same inputs, its observable behaviour (results, output, ...) may change if events happen in different order. Events here are typically scheduler interactions causing different interleavings, but could also be, e.g. changing network latency. Race condition is often used interchangeably with data race.

reentrancy
:   A lock is reentrant if it can be acquired (and released) multiple times by the same thread. If a lock is non-reentrant, trying to acquire it again might cause an exception or other problems.

safety property
:   Property of a system: "nothing bad ever happens". Can be violated in finite time. Exceptions, absence of deadlocks, and mutual exclusion are typical safety properties. Will be formally defined in Formal Methods using temporal logic.

scheduler
:   A management process, e.g. on the operating system level, that performs context switches. I.e. it interrupts/pauses/sends to sleep the currently running process (or thread), performs a context switch, and selects the next process (or thread) to run. Schedulers typically do not give guarantees when and how often they act, who gets selected next, etc.

shared resource
:   Any resource (memory location, input source, output sink, ...) shared by more than one thread.

starvation
:   A thread starves if it can never enter a/any critical section.

synchronisation
:   Some form of orchestration via threads. Typically, to prevent bad interleavings.

synchronized
:   Java keyword, enforcing mutual exclusion for a critical section via some object's intrinsic lock.

throughput
:   An evaluation metric for pipelines. Throughput measures the amount of work (e.g. CPU instructions) that can be done by a pipeline in a given period of time.

thread
:   In general, an independent (i.e. capable of running in parallel) unit of computation that executes a piece of code. The concept of threads exists on various levels: hardware (CPU), operating systems, programming languages. In Java, also an instance of the `Thread` class.

thread mapping
:   How a Java/JVM thread is related to an operating system thread. In native threading (most common), each JVM thread is mapped to a dedicated operating system thread. In green threading, the JVM maps several threads to a single operating system thread.

vectorisation
:   Using special machine code instructions to execute a single operation (e.g. plus) on a chunk of data (e.g. an array segment). Can significantly improve performance. Code can be vectorised automatically, by compilers, or manually, by using intrinsics libraries provided by hardware vendors.
