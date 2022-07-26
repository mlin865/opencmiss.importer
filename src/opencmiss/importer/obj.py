from opencmiss.importer.errors import OpenCMISSImportUnknownParameter

try:
    from opencmiss.importer.trimesh import import_data, import_data_into_region
except ImportError:
    pass


def identifier():
    return "OBJ"


def parameters(parameter_name=None):
    importer_parameters = {
        "version": "0.1.0",
        "id": identifier(),
        "title": "OBJ",
        "description":
            "Wavefront technologies 3D model information.",
        "input": {
            "mimetype": "model/obj",
        },
        "output": {
            "mimetype": "text/x.vnd.abi.exf+plain",
        }
    }

    if parameter_name is not None:
        if parameter_name in importer_parameters:
            return importer_parameters[parameter_name]
        else:
            raise OpenCMISSImportUnknownParameter(f"Importer '{identifier()}' does not have parameter: {parameter_name}")

    return importer_parameters


