with open('data.txt') as f:
    data = f.read()

width = 25
height = 6

layers = [data[i:i + width * height] for i in range(0, len(data), width * height)]

least_zeros = min(layers, key=lambda layer: layer.count('0'))

print(least_zeros.count('1') * least_zeros.count('2'))

image = [next(layer[i] for layer in layers if layer[i] != '2') for i in range(width * height)]

for i in range(0, width * height, width):
    print(' '.join(image[i:i + width]).translate(' #' * 25))
