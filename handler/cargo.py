from .base import BaseHandler

class CargoHandler(BaseHandler):
    attributes = [
        ["cargoName", "text", "Cargo Name"],
        ["cargoSpec", "text", "Cargo Specification"],
        ["producerID", "text", "Producer ID"],
    ]

    data = [
        ["1", "123", "123", "123"],
        ["2", "233", "233", "233"],
    ]

    def get(self):
        self.render("cargo.html", attributes=self.attributes, data = self.data)

    def post(self):
        # Get data here, and transfer data to database.
        post_data = []
        for item in self.attributes:
            data = self.get_argument(item[0])
            post_data.append([item[0], data])
        self.write(str(post_data))