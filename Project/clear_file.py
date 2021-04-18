import json


class clear_file:
    def write_json(self, data, filename='output.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def clear_output_file(self):
        with open("output.json") as json_file:
            data = json.load(json_file)

            data['scores'] = []
        self.write_json(data)
