class print_to_file:
    def __init__(self, algorithm, prediction, accuracy):
        super().__init__()
        self.algorithm = algorithm
        self.prediction = prediction
        self.accuracy = accuracy
        self.file_name = "OutputFile.txt"

    def print_output_file(self):
        file_object = open(self.file_name, "a")
        file_object.writelines(
            f"Algorithm: {self.algorithm}: Prediction: {self.prediction} with an accuracy of {self.accuracy}%!\n\n")
        file_object.close()
