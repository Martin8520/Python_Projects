import numpy as np


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.randn(1, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.random.randn(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward_propagate(self, inputs):
        hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)

        output_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        predicted_output = self.sigmoid(output_input)

        return predicted_output, hidden_output

    def backward_propagate(self, inputs, targets, predicted_output, hidden_output, learning_rate):
        # Compute output layer error
        output_error = targets - predicted_output
        output_delta = output_error * self.sigmoid_derivative(predicted_output)

        # Compute hidden layer error
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(hidden_output)

        # Update weights and biases
        self.weights_hidden_output += learning_rate * np.dot(hidden_output.T, output_delta)
        self.bias_output += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
        self.weights_input_hidden += learning_rate * np.dot(inputs.T, hidden_delta)
        self.bias_hidden += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

    def train(self, inputs, targets, learning_rate, epochs):
        for epoch in range(epochs):
            predicted_output, hidden_output = self.forward_propagate(inputs)

            self.backward_propagate(inputs, targets, predicted_output, hidden_output, learning_rate)

            mse = np.mean(np.square(targets - predicted_output))
            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Mean Squared Error: {mse}')


input_size = 2
hidden_size = 3
output_size = 1

network = NeuralNetwork(input_size, hidden_size, output_size)

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

learning_rate = 0.1
epochs = 1000
network.train(inputs, targets, learning_rate, epochs)
