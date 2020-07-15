[![Generic badge](https://www.code-inspector.com/project/7200/status/svg)](https://www.code-inspector.com/project/7200/status/svg)
[![Generic badge](https://www.code-inspector.com/project/7200/score/svg)](https://www.code-inspector.com/project/7200/score/svg)

# Language_Detection
Neural network to detect languages

Just type any word 20 letters or less and the network will tll you whether it is Italian or English!
## Network Structure
The Neural Network has 520 binary input neurons, with 26 neurons for each character, and enough for 20 characters. For example, the letter 'a' would give this input to the first 26 neurons [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], and so forth. The next layers of the network are dense layers with 520, 260, and 100 neurons, ReLU activation functions, and a bias neuron. The final layer is a dense connected layer with a sigmoidal activation function, with a final output that is somewhere between 1 (100% chance of the respective word being English) and 0 (100% chance of the word being italian)*.



*Disclaimer: I later realised there is a problem with having a single output neuron, that being that any word that is neither english nor italian would give unusual results. The bias in each layer should fix this, but I need to explore it further
