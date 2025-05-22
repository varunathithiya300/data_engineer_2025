# Interview question from micro1

def editText(input_text, operations):
    transformation_history = [input_text]
    redo_history = []

    for op in operations:
        if op == "undo":
            if len(transformation_history) > 1:
                redo_history.append(transformation_history.pop())
        elif op == "redo":
            if redo_history:
                transformation_history.append(redo_history.pop())

        else:
            text_to_operate = transformation_history[-1]
            op_result = text_to_operate[:op[0]] + op[2] + text_to_operate[op[1]+1:]
            transformation_history.append(op_result)
            print(transformation_history)

editText("data engineer", [(0, 4, "A"), (1, 6, "BB"), "undo", (3, 8, "CC")])