import sys
from typing import List


class GenerateAst:
    @classmethod
    def run(cls, *args: str):
        if len(args) != 1:
            print("Usage: generate_ast <output directort>")
            sys.exit(64)
        output_dir = args[0]
        cls.define_ast(
            output_dir,
            "Expr",
            [
                "Binary   -> left: Expr, operator: Token, right: Expr",
                "Grouping -> expression: Expr",
                "Literal  -> value: object",
                "Unary    -> operator: Token, right: Expr",
            ],
        )

    @classmethod
    def define_ast(cls, output_dir: str, base_name: str, types: List[str]):
        path = f"{output_dir}/{base_name.lower()}.py"

        lines = list()  # type: List[str]
        lines.append(
            "# NOTE: This file is generated by `generate_ast.py` automatically, do not modify it manually\n\n"
        )
        lines.append("from typing import TYPE_CHECKING\n\n")
        lines.append("from .token import Token\n\n")
        lines.append("if TYPE_CHECKING:\n")
        lines.append("    from .ast_printer import AstPrinter\n")
        lines.append("else:\n")
        lines.append("    AstPrinter = None\n\n\n")
        lines.append(f"class {base_name}:\n")
        # Annotations
        for type in types:
            class_name = type.split("->")[0].strip()
            lines.append(f'    {class_name}: "{class_name}"\n')

        cls.define_visitor(lines, base_name, types)

        lines.append("\n\n")
        for type in types:
            class_name, fields = type.split("->")
            class_name, fields = class_name.strip(), fields.strip()
            cls.define_type(lines, base_name, class_name, fields)

        for type in types:
            class_name = type.split("->")[0].strip()
            lines.append(f'setattr({base_name}, "{class_name}", {class_name})\n')

        with open(path, "w") as f:
            f.writelines(lines)

        lines.clear()
        del lines

    @classmethod
    def define_type(cls, lines: List[str], base_name: str, class_name: str, fields: str):
        lines.append(f"class {class_name}({base_name}):\n")
        # Constructor.
        lines.append(f"    def __init__(self, {fields}):\n")
        # Fields.
        _fields = fields.split(", ")
        for field in _fields:
            name = field.split(": ")[0]
            lines.append(f"        self.{name} = {name}\n")

        lines.append("\n")
        lines.append(f"    def accept(self, visitor: AstPrinter) -> str:\n")
        lines.append(f"        return visitor.visit_{class_name.lower()}_expr(self)\n")

        lines.append("\n\n")

    @classmethod
    def define_visitor(cls, lines: List[str], base_name: str, types: List[str]):
        lines.append("\n")
        lines.append("    def accept(self, visitor: AstPrinter) -> str:\n")
        lines.append("        raise NotImplementedError\n")


if __name__ == "__main__":
    GenerateAst.run("./src/veda/")
