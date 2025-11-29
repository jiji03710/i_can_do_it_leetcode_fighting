# 2D Parallel Sandpile Implementation

This project implements a two-dimensional parallel version
of the sandpile model using MPI. The global grid is decomposed into a 2D process grid, each process updates its local region and
exchanges halo data with its neighbours.

At the current stage, the implementation is a simple version that assumes the global grid can be evenly divided among processes. Both dimensions of the process grid must divide the global size L without remainder, satisfying:
```bash
L mod dims[0] = 0
L mod dims[1] = 0
```
If this condition is not met, the program will terminate with an error, for example: 
```bash
sandpile: ERROR
    cannot decompose global grid L=512 into a 3 x 2 process grid. 
    L must be divisible by dims[0] and dims[1].
    Suggested valid process counts include: 1,2,4,8,16,...
```
---
## 1. How to Run the Program

A complete SLURM script is provided (run_sandpile.slurm).

This SLURM script handles node allocation and compilation automatically, so users only need to modify a small number of variables to set the initial sandpile status.

With the default input settings, if users directly submit the script using:

```bash
sbatch run_sandpile.slurm
```
It will run the program with L = 512, TOTAL_PROCS = 16, and OFFSET = 256.


Moreover, users can customise the run by modifying only three variables at the top of the script, which are:
```bash
TOTAL_PROCS // total number of process
L           // global grid size 
OFFSET      // initial sandpile offset
```
Changing these values allows users to specify the total number of MPI processes, the global size, and the initial sandpile offset. The script will automatically adjust node allocation and recompile the program accordingly.

For example, if the user sets TOTAL_PROCS=256, the script will automatically request 2 nodes, each running 128 tasks. 

Moreover, users should also ensure that the chosen OFFSET value does not exceed the global size L. Otherwise the program will terminate with an error. For instance, using an offset of 1024 for a grid of size 128 will produce an output such as:
```bash
sandpile: ERROR, offset (1024) out of range [0, 128)
```

## 2.Project Structure
The project structure is as follows:
```bash
project/
|
+-- compare/ # Image output comparison for correctness verification
|   +-- compare_ppm.c # compares two PPM images pixel-by-pixel
|   +-- compare_ppm # Compiled executable
|   +-- ori-512-256-sand.ppm # Example baseline image
|   +-- sand.ppm # Example parallel output image
|
+-- includes/ # Header files 
|   +-- arraymalloc.h  # array allocation/ initialization/ free
|   +-- check.h  # Input checks
|   +-- exchange.h  # Halo exchange 
|   +-- loop.h  # Main simulation loop
|   +-- output.h # PPM output 
|   +-- sandpile.h  # Global definitions & parameters
|   +-- topology.h  # MPI topology setup /clean
|
+-- obj/ # Object files generated during compilation
|
+-- src/ # Core implementation of 2-D sandpile
|   +-- arraymalloc.c # array allocation/ initialization/ free
|   +-- check.c # Input checks such as L divisibility, offset range..
|   +-- exchange.c # exchange implementation using MPI type vector
|   +-- loop.c  # Main simulation loop
|   +-- output.c  # gather information and PPM output 
|   +-- sandio.c  # PPM output
|   +-- sandpile.c  # Main program 
|   +-- topology.c  # topology setup /clean
|
+-- Makefile 
+-- run_sandpile.slurm  # SLURM script (build + execution)
+-- sandpile_11710994.out # Example output (e.g. 256 procs, L=2048)
+-- README.md                   
```
### 2.1 Main Functionalities
The main functionalities such as domain decomposition, halo exchange, simulation loop, I/O and so on are implemented entirely within the includes/ and src/ directories. The obj/ folder stores intermediate object files created during compilation. The output file from a typical simulation (e.g., 256 processes, L=2048) is also included as an example.

### 2.2 Image Comparison Module (compare/)

To verify that the 2-D parallel implementation produces the same final image (sand.ppm) as the baseline serial version, the project includes a simple comparison module located in the compare/ directory. It checks two PPM images pixel by pixel to ensure correctness.

You can compile the comparison tool with:

```bash
cc -o compare_ppm compare_ppm.c
```
The program requires two filenames as input, for example:
```bash
./compare_ppm sand_baseline.ppm sand_2D.ppm
```
If the two images match exactly, the output will be:
```bash
The two images are identical.
```
Otherwise, it will report:
```bash
The two images are different.
```
