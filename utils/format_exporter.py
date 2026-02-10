import json

class FormatExporter:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return json.dumps(self.data)

    def to_csv(self):
        import csv
        from io import StringIO
        output = StringIO()
        writer = csv.writer(output)
        if isinstance(self.data, list) and len(self.data) > 0:
            writer.writerow(self.data[0].keys())  # Write header
            for row in self.data:
                writer.writerow(row.values())
        return output.getvalue()

    def to_xml(self):
        from xml.etree.ElementTree import Element, SubElement, tostring
        import xml.dom.minidom as minidom
        root = Element('data')
        for item in self.data:
            entry = SubElement(root, 'entry')
            for key, value in item.items():
                subelem = SubElement(entry, key)
                subelem.text = str(value)
        xml_str = tostring(root, 'utf-8')
        return minidom.parseString(xml_str).toprettyxml(indent='  ')

# Example Usage:
# export_data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
# exporter = FormatExporter(export_data)
# print(exporter.to_json())
# print(exporter.to_csv())
# print(exporter.to_xml())
