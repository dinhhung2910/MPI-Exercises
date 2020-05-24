# Vector addition using only one GPU thread
nvcc vector_add.cu -o vector_add
nvprof ./vector_add

# Parallelizing vector addition using multithread
nvcc vector_add_thread.cu -o vector_add_thread
nvprof ./vector_add_thread

# Adding more thread blocks
nvcc vector_add_grid.cu -o vector_add_grid
nvprof ./vector_add_grid
