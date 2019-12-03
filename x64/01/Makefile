.DEFAULT_GOAL := build/day01

build/%.o: %.asm
	mkdir -p build
	nasm -f elf64 $< -o $@

run: build/day01
	./build/day01