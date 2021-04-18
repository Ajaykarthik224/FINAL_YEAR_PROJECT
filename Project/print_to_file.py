import json


class print_to_file:
    def __init__(self, algorithm, prediction, accuracy):
        super().__init__()
        self.algorithm = algorithm
        self.prediction = prediction
        self.accuracy = accuracy

    def write_json(self, data, filename='output.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def print_output_file(self):
        with open("output.json") as json_file:
            data = json.load(json_file)

            scores_to_be_written = {
                "algorithm": self.algorithm,
                "prediction": self.prediction,
                "accuracy": self.accuracy
            }

            data['scores'].append(scores_to_be_written)
        self.write_json(data)
