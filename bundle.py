import argparse
import json
import xml.dom.minidom

parser = argparse.ArgumentParser(description="Bundler for v5blocks file format")
parser.add_argument("--pack", action="store_true")
parser.add_argument("--unpack", action="store_true")
parser.add_argument("filename")

args = parser.parse_args()

if args.pack:
    raise NotImplementedError("--pack not implemented")
elif args.unpack:
    with open(args.filename) as reader:
        bundle = json.load(reader)
    
    workspace = bundle.pop("workspace")
    cpp = bundle.pop("cpp")

    with open(args.filename + ".workspace", "w") as writer:
        writer.write(xml.dom.minidom.parseString(workspace).toprettyxml(indent="  "))
    
    with open(args.filename + ".cpp", "w") as writer:
        writer.write(cpp)

    with open(args.filename + ".base", "w") as writer:
        writer.write(json.dumps(bundle, indent=4) + "\n")

else:
    raise Exception("Please specify --pack or --unpack")

        