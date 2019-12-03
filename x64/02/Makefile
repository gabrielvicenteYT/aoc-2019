.DEFAULT_GOAL := build/day02

build/%.o: %.asm
	mkdir -p build
	nasm -f elf64 $< -o $@

run: build/day02
	./build/day02