.DEFAULT_GOAL := build/day01

build/%.o: %.asm
	mkdir build
	nasm -f elf64 $< -o $@

run: build/day01
	./build/day01