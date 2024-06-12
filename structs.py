import numpy as np


class Results:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.importances: list = []
        self.accuracies: list = []
        self.precisions: list = []
        self.recalls: list = []
        self.f1_scores: list = []
        self.conf_matrices: list = []

    def calculate(self, method: str, key: str) -> float:
        method_dict = {"mean": np.mean, "median": np.median}
        return method_dict[method](getattr(self, key))

    def calculate_dictionary(self, method: str) -> dict:

        attributes = [
            "importances",
            "accuracies",
            "precisions",
            "recalls",
            "f1_scores",
            "conf_matrices",
        ]

        output_dictionary = {}
        for attribute in attributes:
            output_dictionary[attribute] = self.calculate(method, attribute)

        return output_dictionary
