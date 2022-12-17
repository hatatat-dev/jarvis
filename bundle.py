#!/usr/bin/env python3

import argparse
import json
import xml.dom.minidom
import io

parser = argparse.ArgumentParser(description="Bundler for v5blocks file format")
parser.add_argument("--pack", action="store_true")
parser.add_argument("--unpack", action="store_true")
parser.add_argument("--parse-xml", action="store_true")
parser.add_argument("filename")

args = parser.parse_args()

if args.pack:
    with open(args.filename + ".workspace") as reader:
        if not args.parse_xml:
            workspace = reader.read().replace(">\n<", "><")
        else:
            out = io.StringIO()
            xml.dom.minidom.parseString(reader.read()).writexml(out)
            workspace = out.getvalue()
    
    with open(args.filename + ".cpp") as reader:
        cpp = reader.read()

    with open(args.filename + ".base") as reader:
        base = json.load(reader)

    result = (
        json.dumps(base, separators=(",", ":"))
        .replace('"rconfig"', '"workspace":' + json.dumps(workspace) + ',"rconfig"', 1)
        .replace('"target"', '"cpp":' + json.dumps(cpp) + ',"target"', 1)
    )

    with open(args.filename, "w") as writer:
        writer.write(result)

elif args.unpack:
    with open(args.filename) as reader:
        bundle = json.load(reader)
    
    workspace = bundle.pop("workspace")
    cpp = bundle.pop("cpp")

    with open(args.filename + ".workspace", "w") as writer:
        if not args.parse_xml:
            writer.write(workspace.replace("><", ">\n<"))
        else:
            writer.write(xml.dom.minidom.parseString(workspace).toprettyxml(indent="  "))
    
    with open(args.filename + ".cpp", "w") as writer:
        writer.write(cpp)

    with open(args.filename + ".base", "w") as writer:
        writer.write(json.dumps(bundle, indent=4) + "\n")

else:
    raise Exception("Please specify --pack or --unpack")
